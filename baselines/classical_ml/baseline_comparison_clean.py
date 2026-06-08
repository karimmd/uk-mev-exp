#!/usr/bin/env python3

# Suppress warnings
import warnings
warnings.filterwarnings('ignore', message='.*torch-scatter.*')
warnings.filterwarnings('ignore')

import os
import sys
import json
import logging
import argparse
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

# ML libraries
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import xgboost as xgb

# Deep learning libraries
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

# GNN libraries (optional, graceful fallback if not available)
try:
    from torch_geometric.nn import GCNConv, GATv2Conv, SAGEConv
    from torch_geometric.nn import global_mean_pool, global_max_pool
    from torch_geometric.data import Data, DataLoader as GeoDataLoader
    GNN_AVAILABLE = True
except ImportError:
    GNN_AVAILABLE = False

# Setup logging
def setup_logging(mev_type: str) -> logging.Logger:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/baseline_clean_{mev_type}_{timestamp}.log"
    
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

class MEVFeatureExtractor:
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_names = [
            'profit_eth', 'cost_eth', 'gain_eth', 'gas_used', 'block_number',
            'num_swaps', 'profit_ratio', 'cost_ratio', 'gas_efficiency',
            'block_recency', 'profit_magnitude', 'cost_magnitude', 'gain_magnitude',
            'transaction_complexity', 'profitability_score'
        ]
    
    def extract_features(self, data: List[Dict]) -> np.ndarray:
        features = []
        
        for transaction in data:
            # Basic financial metrics
            profit_eth = float(transaction.get('profit_eth', 0))
            cost_eth = float(transaction.get('cost_eth', 0))
            gain_eth = float(transaction.get('gain_eth', 0))
            gas_used = float(transaction.get('gas_used', 0))
            block_number = float(transaction.get('block_number', 0))
            num_swaps = float(transaction.get('num_swaps', 0))
            
            # Derived features
            profit_ratio = profit_eth / max(cost_eth, 1e-10)
            cost_ratio = cost_eth / max(gain_eth, 1e-10) 
            gas_efficiency = profit_eth / max(gas_used, 1e-10)
            block_recency = 20000000 - block_number  # Approximate recency
            
            # Magnitude features (log-scaled)
            profit_magnitude = np.log1p(abs(profit_eth))
            cost_magnitude = np.log1p(abs(cost_eth))
            gain_magnitude = np.log1p(abs(gain_eth))
            
            # Complexity and profitability
            transaction_complexity = num_swaps * np.log1p(gas_used)
            profitability_score = profit_eth / max(cost_eth + gas_used * 1e-9, 1e-10)
            
            features.append([
                profit_eth, cost_eth, gain_eth, gas_used, block_number, num_swaps,
                profit_ratio, cost_ratio, gas_efficiency, block_recency,
                profit_magnitude, cost_magnitude, gain_magnitude,
                transaction_complexity, profitability_score
            ])
        
        return np.array(features)
    
    def fit_transform(self, data: List[Dict]) -> np.ndarray:
        features = self.extract_features(data)
        return self.scaler.fit_transform(features)
    
    def transform(self, data: List[Dict]) -> np.ndarray:
        features = self.extract_features(data)
        return self.scaler.transform(features)

class AutoEncoder(nn.Module):
    
    def __init__(self, input_dim: int, hidden_dims: List[int] = [128, 64, 32]):
        super(AutoEncoder, self).__init__()
        
        # Encoder
        encoder_layers = []
        prev_dim = input_dim
        for dim in hidden_dims:
            encoder_layers.extend([
                nn.Linear(prev_dim, dim),
                nn.ReLU(),
                nn.Dropout(0.2)
            ])
            prev_dim = dim
        self.encoder = nn.Sequential(*encoder_layers)
        
        # Decoder
        decoder_layers = []
        dims_reversed = hidden_dims[::-1] + [input_dim]
        for i in range(len(dims_reversed) - 1):
            decoder_layers.extend([
                nn.Linear(dims_reversed[i], dims_reversed[i + 1]),
                nn.ReLU() if i < len(dims_reversed) - 2 else nn.Sigmoid()
            ])
        self.decoder = nn.Sequential(*decoder_layers)
        
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded, encoded

# GNN Models (only if torch_geometric is available)
if GNN_AVAILABLE:
    class MeconGNN(nn.Module):
        
        def __init__(self, input_features: int, hidden_channels: int = 64):
            super().__init__()
            self.conv1 = GCNConv(input_features, hidden_channels)
            self.conv2 = GCNConv(hidden_channels, hidden_channels)
            self.conv3 = GCNConv(hidden_channels, hidden_channels//2)
            
            # Reconstruction head for anomaly detection
            self.reconstruction = nn.Linear(hidden_channels//2, input_features)
            
            # Anomaly scoring
            self.anomaly_score = nn.Sequential(
                nn.Linear(hidden_channels//2, 32),
                nn.ReLU(),
                nn.Linear(32, 1),
                nn.Sigmoid()
            )
        
        def forward(self, x, edge_index, batch):
            # GNN layers
            x = F.relu(self.conv1(x, edge_index))
            x = F.relu(self.conv2(x, edge_index))
            x = self.conv3(x, edge_index)
            
            # Global pooling
            graph_repr = global_mean_pool(x, batch)
            
            # Outputs
            reconstruction = self.reconstruction(graph_repr)
            anomaly_score = self.anomaly_score(graph_repr)
            
            return anomaly_score, reconstruction

    class ArbiNetGNN(nn.Module):
        
        def __init__(self, input_features: int, hidden_channels: int = 128):
            super().__init__()
            self.conv1 = GATv2Conv(input_features, hidden_channels, heads=4, dropout=0.2)
            self.conv2 = GATv2Conv(hidden_channels * 4, hidden_channels, heads=2, dropout=0.2)
            self.conv3 = GATv2Conv(hidden_channels * 2, hidden_channels, heads=1, dropout=0.2)
            
            # Final layers
            self.anomaly_score = nn.Sequential(
                nn.Linear(hidden_channels * 2, 64),  # *2 for mean + max pooling
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(64, 1),
                nn.Sigmoid()
            )
        
        def forward(self, x, edge_index, batch):
            # GAT layers
            x = F.elu(self.conv1(x, edge_index))
            x = F.elu(self.conv2(x, edge_index))
            x = self.conv3(x, edge_index)
            
            # Dual pooling (ArbiNet style)
            mean_pool = global_mean_pool(x, batch)
            max_pool = global_max_pool(x, batch)
            graph_repr = torch.cat([mean_pool, max_pool], dim=1)
            
            return self.anomaly_score(graph_repr)

class BaselineComparison:
    
    def __init__(self, data_dir: str = "..", device: str = "cuda"):
        self.data_dir = Path(data_dir)
        self.device = device if torch.cuda.is_available() else "cpu"
        self.feature_extractor = MEVFeatureExtractor()
        self.results = {}
        
        # Setup logger
        self.logger = logging.getLogger(__name__)
        
    def load_raw_data(self, mev_type: str, max_samples: int = 5000) -> List[Dict]:
        raw_data_path = self.data_dir / "large" / f"{mev_type}_results.csv"
        
        if not raw_data_path.exists():
            self.logger.error(f"Raw data file not found: {raw_data_path}")
            return []
        
        self.logger.info(f"Loading raw data from: {raw_data_path}")
        
        try:
            df = pd.read_csv(raw_data_path)
            self.logger.info(f"Loaded {len(df)} raw transactions")
            
            # Sample for processing efficiency
            if len(df) > max_samples:
                df = df.sample(n=max_samples, random_state=42)
                self.logger.info(f"Sampled {max_samples} transactions for analysis")
            
            data = []
            for _, row in df.iterrows():
                transaction_data = {
                    'transaction_id': row.get('transaction_id', ''),
                    'mev_type': mev_type,
                    'profit_eth': float(row.get('profit_eth', 0)),
                    'cost_eth': float(row.get('cost_eth', 0)),
                    'gain_eth': float(row.get('gain_eth', 0)),
                    'gas_used': float(row.get('gas_used', 0)) if 'gas_used' in row else 0,
                    'block_number': int(row.get('block_number', 0)) if 'block_number' in row else 0,
                    'num_swaps': int(row.get('num_swaps', 0)) if 'num_swaps' in row else 0,
                    'description': row.get('description', ''),
                }
                data.append(transaction_data)
            
            self.logger.info(f"Processed {len(data)} transactions for baseline comparison")
            return data
            
        except Exception as e:
            self.logger.error(f"Error loading raw data: {str(e)}")
            return []
    
    def run_isolation_forest(self, X_train: np.ndarray, X_test: np.ndarray) -> Dict[str, Any]:
        self.logger.info("Running Isolation Forest...")
        
        iso_forest = IsolationForest(
            n_estimators=100,
            contamination='auto',
            random_state=42,
            n_jobs=-1
        )
        
        iso_forest.fit(X_train)
        predictions = iso_forest.predict(X_test)
        predictions = (predictions == -1).astype(int)
        anomaly_scores = iso_forest.decision_function(X_test)
        
        return {
            'method': 'Isolation Forest',
            'anomaly_detection_rate': (predictions.sum() / len(predictions)) * 100,
            'anomalies_detected': int(predictions.sum()),
            'total_samples': len(predictions),
            'anomaly_scores_mean': float(np.mean(anomaly_scores)),
            'anomaly_scores_std': float(np.std(anomaly_scores))
        }
    
    def run_one_class_svm(self, X_train: np.ndarray, X_test: np.ndarray) -> Dict[str, Any]:
        self.logger.info("Running One-Class SVM...")
        
        oc_svm = OneClassSVM(kernel='rbf', gamma='scale', nu=0.1)
        oc_svm.fit(X_train)
        
        predictions = oc_svm.predict(X_test)
        predictions = (predictions == -1).astype(int)
        decision_scores = oc_svm.decision_function(X_test)
        
        return {
            'method': 'One-Class SVM',
            'anomaly_detection_rate': (predictions.sum() / len(predictions)) * 100,
            'anomalies_detected': int(predictions.sum()),
            'total_samples': len(predictions),
            'decision_scores_mean': float(np.mean(decision_scores)),
            'decision_scores_std': float(np.std(decision_scores))
        }
    
    def run_xgboost_outlier(self, X_train: np.ndarray, X_test: np.ndarray) -> Dict[str, Any]:
        self.logger.info("Running XGBoost (Outlier-based)...")
        
        # Use Isolation Forest to create training labels
        iso_forest = IsolationForest(contamination=0.1, random_state=42)
        outlier_labels = iso_forest.fit_predict(X_train)
        outlier_labels = (outlier_labels == -1).astype(int)
        
        # Train XGBoost on these patterns
        xgb_model = xgb.XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            random_state=42,
            eval_metric='logloss'
        )
        
        xgb_model.fit(X_train, outlier_labels)
        predictions = xgb_model.predict(X_test)
        probabilities = xgb_model.predict_proba(X_test)
        
        return {
            'method': 'XGBoost (Outlier-based)',
            'anomaly_detection_rate': (predictions.sum() / len(predictions)) * 100,
            'anomalies_detected': int(predictions.sum()),
            'total_samples': len(predictions),
            'confidence_scores_mean': float(np.mean(np.max(probabilities, axis=1)))
        }
    
    def run_random_forest_outlier(self, X_train: np.ndarray, X_test: np.ndarray) -> Dict[str, Any]:
        self.logger.info("Running Random Forest (Outlier-based)...")
        
        # Use Isolation Forest to create training labels
        iso_forest = IsolationForest(contamination=0.15, random_state=42)
        outlier_labels = iso_forest.fit_predict(X_train)
        outlier_labels = (outlier_labels == -1).astype(int)
        
        # Train Random Forest on these patterns
        rf_model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        
        rf_model.fit(X_train, outlier_labels)
        predictions = rf_model.predict(X_test)
        probabilities = rf_model.predict_proba(X_test)
        
        return {
            'method': 'Random Forest (Outlier-based)',
            'anomaly_detection_rate': (predictions.sum() / len(predictions)) * 100,
            'anomalies_detected': int(predictions.sum()),
            'total_samples': len(predictions),
            'confidence_scores_mean': float(np.mean(np.max(probabilities, axis=1))),
            'feature_importance_mean': float(np.mean(rf_model.feature_importances_))
        }
    
    def run_autoencoder(self, X_train: np.ndarray, X_test: np.ndarray) -> Dict[str, Any]:
        self.logger.info("Running Autoencoder...")
        
        # Convert to tensors
        X_train_tensor = torch.FloatTensor(X_train).to(self.device)
        X_test_tensor = torch.FloatTensor(X_test).to(self.device)
        
        # Create and train autoencoder
        autoencoder = AutoEncoder(input_dim=X_train.shape[1]).to(self.device)
        optimizer = optim.Adam(autoencoder.parameters(), lr=0.001)
        criterion = nn.MSELoss()
        
        autoencoder.train()
        for epoch in range(50):  # Reduced epochs for speed
            optimizer.zero_grad()
            reconstructed, _ = autoencoder(X_train_tensor)
            loss = criterion(reconstructed, X_train_tensor)
            loss.backward()
            optimizer.step()
            
            if (epoch + 1) % 20 == 0:
                self.logger.info(f"Autoencoder Epoch {epoch + 1}/50, Loss: {loss.item():.4f}")
        
        # Evaluation
        autoencoder.eval()
        with torch.no_grad():
            reconstructed_test, _ = autoencoder(X_test_tensor)
            reconstruction_errors = torch.mean((X_test_tensor - reconstructed_test) ** 2, dim=1)
            
            # Top 10% as anomalies
            threshold = torch.quantile(reconstruction_errors, 0.9)
            predictions = (reconstruction_errors > threshold).int().cpu().numpy()
        
        return {
            'method': 'Autoencoder',
            'anomaly_detection_rate': (predictions.sum() / len(predictions)) * 100,
            'anomalies_detected': int(predictions.sum()),
            'total_samples': len(predictions),
            'reconstruction_error_mean': float(torch.mean(reconstruction_errors).cpu()),
            'threshold': float(threshold.cpu())
        }
    
    def create_simple_graph(self, data: List[Dict], max_nodes: int = 50) -> Optional[Data]:
        if not GNN_AVAILABLE:
            return None
            
        # Limit nodes for memory efficiency
        sample_data = data[:max_nodes]
        
        # Extract features
        node_features = []
        for tx in sample_data:
            features = [
                float(tx.get('profit_eth', 0)),
                float(tx.get('cost_eth', 0)),
                float(tx.get('gas_used', 0)),
                float(tx.get('num_swaps', 0)),
                float(tx.get('block_number', 0)) % 1000  # Normalized
            ]
            node_features.append(features)
        
        # Create sequential edges (simple chain graph)
        edge_indices = []
        for i in range(len(sample_data) - 1):
            edge_indices.append([i, i + 1])
            edge_indices.append([i + 1, i])
        
        if not edge_indices:
            edge_indices = [[0, 0]]  # Self-loop for single node
        
        x = torch.FloatTensor(node_features)
        edge_index = torch.LongTensor(edge_indices).t().contiguous()
        
        return Data(x=x, edge_index=edge_index)
    
    def run_mecon_gnn(self, train_data: List[Dict], test_data: List[Dict]) -> Dict[str, Any]:
        if not GNN_AVAILABLE:
            return {
                'method': 'Mecon GNN',
                'error': 'torch_geometric not available'
            }
        
        self.logger.info("Running Mecon GNN...")
        
        try:
            # Create model
            model = MeconGNN(input_features=5, hidden_channels=32).to(self.device)
            optimizer = optim.Adam(model.parameters(), lr=0.001)
            
            # Training
            model.train()
            for epoch in range(30):
                # Create training graph
                train_graph = self.create_simple_graph(train_data, max_nodes=30)
                if train_graph is None:
                    continue
                    
                train_graph = train_graph.to(self.device)
                batch = torch.zeros(train_graph.x.size(0), dtype=torch.long).to(self.device)
                
                optimizer.zero_grad()
                anomaly_scores, reconstruction = model(train_graph.x, train_graph.edge_index, batch)
                
                # Unsupervised loss: encourage diversity in anomaly scores
                loss = torch.var(anomaly_scores) * -1 + torch.mean(anomaly_scores ** 2) * 0.1
                
                if not torch.isnan(loss):
                    loss.backward()
                    optimizer.step()
                
                if (epoch + 1) % 10 == 0:
                    self.logger.info(f"Mecon GNN Epoch {epoch + 1}/30, Loss: {loss.item():.4f}")
            
            # Evaluation
            model.eval()
            with torch.no_grad():
                test_graph = self.create_simple_graph(test_data, max_nodes=30)
                if test_graph is None:
                    return {'method': 'Mecon GNN', 'error': 'Failed to create test graph'}
                    
                test_graph = test_graph.to(self.device)
                batch = torch.zeros(test_graph.x.size(0), dtype=torch.long).to(self.device)
                
                anomaly_scores, _ = model(test_graph.x, test_graph.edge_index, batch)
                
                # Top 10% as anomalies
                threshold = torch.quantile(anomaly_scores.flatten(), 0.9)
                predictions = (anomaly_scores.flatten() > threshold).int().cpu().numpy()
            
            return {
                'method': 'Mecon GNN',
                'anomaly_detection_rate': (predictions.sum() / len(predictions)) * 100,
                'anomalies_detected': int(predictions.sum()),
                'total_samples': len(predictions),
                'anomaly_scores_mean': float(torch.mean(anomaly_scores).cpu())
            }
            
        except Exception as e:
            self.logger.error(f"Error in Mecon GNN: {str(e)}")
            return {'method': 'Mecon GNN', 'error': str(e)}
    
    def run_arbinet_gnn(self, train_data: List[Dict], test_data: List[Dict]) -> Dict[str, Any]:
        if not GNN_AVAILABLE:
            return {
                'method': 'ArbiNet GNN',
                'error': 'torch_geometric not available'
            }
        
        self.logger.info("Running ArbiNet GNN...")
        
        try:
            # Create model
            model = ArbiNetGNN(input_features=5, hidden_channels=64).to(self.device)
            optimizer = optim.Adam(model.parameters(), lr=0.001)
            
            # Training
            model.train()
            for epoch in range(30):
                # Create training graph
                train_graph = self.create_simple_graph(train_data, max_nodes=25)
                if train_graph is None:
                    continue
                    
                train_graph = train_graph.to(self.device)
                batch = torch.zeros(train_graph.x.size(0), dtype=torch.long).to(self.device)
                
                optimizer.zero_grad()
                anomaly_scores = model(train_graph.x, train_graph.edge_index, batch)
                
                # Unsupervised loss
                loss = torch.var(anomaly_scores) * -1 + torch.mean(anomaly_scores ** 2) * 0.1
                
                if not torch.isnan(loss):
                    loss.backward()
                    optimizer.step()
                
                if (epoch + 1) % 10 == 0:
                    self.logger.info(f"ArbiNet GNN Epoch {epoch + 1}/30, Loss: {loss.item():.4f}")
            
            # Evaluation
            model.eval()
            with torch.no_grad():
                test_graph = self.create_simple_graph(test_data, max_nodes=25)
                if test_graph is None:
                    return {'method': 'ArbiNet GNN', 'error': 'Failed to create test graph'}
                    
                test_graph = test_graph.to(self.device)
                batch = torch.zeros(test_graph.x.size(0), dtype=torch.long).to(self.device)
                
                anomaly_scores = model(test_graph.x, test_graph.edge_index, batch)
                
                # Top 10% as anomalies
                threshold = torch.quantile(anomaly_scores.flatten(), 0.9)
                predictions = (anomaly_scores.flatten() > threshold).int().cpu().numpy()
            
            return {
                'method': 'ArbiNet GNN',
                'anomaly_detection_rate': (predictions.sum() / len(predictions)) * 100,
                'anomalies_detected': int(predictions.sum()),
                'total_samples': len(predictions),
                'anomaly_scores_mean': float(torch.mean(anomaly_scores).cpu())
            }
            
        except Exception as e:
            self.logger.error(f"Error in ArbiNet GNN: {str(e)}")
            return {'method': 'ArbiNet GNN', 'error': str(e)}
    
    def run_all_baselines(self, mev_type: str, max_samples: int = 5000, include_gnn: bool = True) -> Dict[str, Any]:
        self.logger.info(f"Starting baseline comparison for {mev_type.upper()}...")
        
        # Load raw data
        data = self.load_raw_data(mev_type, max_samples)
        if len(data) == 0:
            return {'error': 'No data loaded'}
        
        # Extract features for traditional ML methods
        X = self.feature_extractor.fit_transform(data)
        X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)
        
        self.logger.info(f"Data split: {X_train.shape[0]} train, {X_test.shape[0]} test samples")
        
        results = {}
        
        # Traditional ML baselines
        traditional_methods = [
            ('Isolation Forest', self.run_isolation_forest),
            ('One-Class SVM', self.run_one_class_svm),
            ('XGBoost', self.run_xgboost_outlier),
            ('Random Forest', self.run_random_forest_outlier),
            ('Autoencoder', self.run_autoencoder)
        ]
        
        for name, method in traditional_methods:
            try:
                self.logger.info(f"Running {name}...")
                result = method(X_train, X_test)
                results[name] = result
                
                self.logger.info(f"{name} Results:")
                self.logger.info(f"  Anomaly Detection Rate: {result['anomaly_detection_rate']:.3f}%")
                self.logger.info(f"  Anomalies Detected: {result['anomalies_detected']}")
                
            except Exception as e:
                self.logger.error(f"Error running {name}: {str(e)}")
                results[name] = {'method': name, 'error': str(e)}
        
        # GNN baselines
        if include_gnn and GNN_AVAILABLE:
            # Split data for GNN training
            train_size = int(0.8 * len(data))
            train_data = data[:train_size]
            test_data = data[train_size:]
            
            gnn_methods = [
                ('Mecon GNN', self.run_mecon_gnn),
                ('ArbiNet GNN', self.run_arbinet_gnn)
            ]
            
            for name, method in gnn_methods:
                try:
                    result = method(train_data, test_data)
                    results[name] = result
                    
                    if 'error' not in result:
                        self.logger.info(f"{name} Results:")
                        self.logger.info(f"  Anomaly Detection Rate: {result['anomaly_detection_rate']:.3f}%")
                        self.logger.info(f"  Anomalies Detected: {result['anomalies_detected']}")
                    else:
                        self.logger.warning(f"{name} failed: {result['error']}")
                        
                except Exception as e:
                    self.logger.error(f"Error running {name}: {str(e)}")
                    results[name] = {'method': name, 'error': str(e)}
        
        elif include_gnn and not GNN_AVAILABLE:
            self.logger.warning("GNN baselines requested but torch_geometric not available")
            results['Mecon GNN'] = {'method': 'Mecon GNN', 'error': 'torch_geometric not available'}
            results['ArbiNet GNN'] = {'method': 'ArbiNet GNN', 'error': 'torch_geometric not available'}
        
        return results
    
    def save_results(self, results: Dict[str, Any], mev_type: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"results/baseline_comparison_{mev_type}_{timestamp}.json"
        
        # Create results directory if it doesn't exist
        os.makedirs("results", exist_ok=True)
        
        # Add metadata
        output_data = {
            'metadata': {
                'mev_type': mev_type,
                'timestamp': timestamp,
                'device_used': self.device,
                'gnn_available': GNN_AVAILABLE
            },
            'results': results
        }
        
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        self.logger.info(f"Results saved to: {output_file}")
        return output_file

def main():
    parser = argparse.ArgumentParser(description='Clean MEV Baseline Comparison')
    parser.add_argument('--mev_type', type=str, choices=['arbitrage', 'sandwich', 'liquidation'], 
                       default='arbitrage', help='MEV type to analyze')
    parser.add_argument('--max_samples', type=int, default=5000, 
                       help='Maximum samples to process')
    parser.add_argument('--no_gnn', action='store_true', 
                       help='Skip GNN baselines')
    parser.add_argument('--data_dir', type=str, default='..',
                       help='Data directory path')
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.mev_type)
    
    logger.info("=" * 80)
    logger.info("CLEAN MEV BASELINE COMPARISON STARTED")
    logger.info("=" * 80)
    logger.info(f"MEV Type: {args.mev_type.upper()}")
    logger.info(f"Max Samples: {args.max_samples}")
    logger.info(f"GNN Available: {GNN_AVAILABLE}")
    logger.info(f"Device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
    logger.info("=" * 80)
    
    # Run comparison
    comparator = BaselineComparison(data_dir=args.data_dir)
    results = comparator.run_all_baselines(
        mev_type=args.mev_type,
        max_samples=args.max_samples,
        include_gnn=not args.no_gnn
    )
    
    # Save results
    output_file = comparator.save_results(results, args.mev_type)
    
    # Summary
    logger.info("\n" + "=" * 80)
    logger.info("BASELINE COMPARISON SUMMARY")
    logger.info("=" * 80)
    
    for method, result in results.items():
        if 'error' in result:
            logger.info(f"{method}: ERROR - {result['error']}")
        else:
            rate = result.get('anomaly_detection_rate', 0)
            count = result.get('anomalies_detected', 0)
            logger.info(f"{method}: {rate:.1f}% detection rate ({count} anomalies)")
    
    logger.info(f"\nResults saved to: {output_file}")
    logger.info("Baseline comparison completed successfully!")

if __name__ == "__main__":
    main()