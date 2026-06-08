#!/usr/bin/env python3

import warnings
warnings.filterwarnings('ignore')

import os
import sys
import json
import time
import logging
import argparse
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder, PolynomialFeatures
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score, roc_curve
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neural_network import MLPClassifier
import xgboost as xgb
import ast

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('aligned_xgb_baseline.log', mode='a')
    ],
    force=True
)
logger = logging.getLogger(__name__)

# GAT-aligned sample sizes
GAT_ALIGNED_SAMPLES = {
    'arbitrage': 100000,    # 100K to match GAT
    'sandwich': 100000,     # 100K to match GAT  
    'liquidation': 30000    # 30K to match GAT (not 100K)
}

logger.info("=" * 100)
logger.info("ALIGNED XGB BASELINE - MATCHING GAT CONFIGURATION")
logger.info("=" * 100)
logger.info(f"Sample sizes: Arbitrage={GAT_ALIGNED_SAMPLES['arbitrage']:,}, "
           f"Sandwich={GAT_ALIGNED_SAMPLES['sandwich']:,}, "
           f"Liquidation={GAT_ALIGNED_SAMPLES['liquidation']:,}")
logger.info(f"Total scale: {sum(GAT_ALIGNED_SAMPLES.values()):,} transactions")
logger.info("=" * 100)

def load_aligned_mev_data(mev_type, max_samples):
    logger.info(f"Loading {mev_type} data (target: {max_samples:,} samples)...")
    
    data_path = f"../large/{mev_type}_results.csv"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data not found: {data_path}")
    
    # Load in chunks for memory efficiency
    chunk_size = 50000
    chunks = []
    total_loaded = 0
    
    for chunk in pd.read_csv(data_path, chunksize=chunk_size):
        chunks.append(chunk)
        total_loaded += len(chunk)
        if total_loaded >= max_samples:
            break
        if len(chunks) % 10 == 0:
            logger.info(f"  Loaded {total_loaded:,} rows...")
    
    df = pd.concat(chunks, ignore_index=True)
    if len(df) > max_samples:
        df = df.sample(n=max_samples, random_state=42).reset_index(drop=True)
    
    df['mev_type'] = mev_type
    logger.info(f"Final {mev_type} dataset: {len(df):,} samples")
    return df

def extract_comprehensive_features(df):
    logger.info("Extracting comprehensive features...")
    
    features = []
    feature_names = []
    
    # Basic transaction features
    basic_features = ['block_number', 'profit_eth', 'profit_usd']
    for feat in basic_features:
        if feat in df.columns:
            features.append(df[feat].fillna(0).values.reshape(-1, 1))
            feature_names.append(feat)
    
    # Gas features (extract from transaction if needed)
    if 'gas_used' not in df.columns and 'transaction' in df.columns:
        logger.info("Extracting gas information from transaction JSON...")
        def extract_gas_info(tx_str):
            if pd.isna(tx_str):
                return 21000, 20e9
            try:
                tx_dict = ast.literal_eval(str(tx_str))
                gas_used = int(tx_dict.get('gas', 21000))
                gas_price = int(tx_dict.get('gasPrice', 20e9))
                return gas_used, gas_price
            except:
                return 21000, 20e9
        
        gas_info = df['transaction'].apply(extract_gas_info)
        df['gas_used'] = [x[0] for x in gas_info]
        df['gas_price'] = [x[1] for x in gas_info]
    
    # Gas features
    if 'gas_used' in df.columns:
        features.append(df['gas_used'].fillna(21000).values.reshape(-1, 1))
        feature_names.append('gas_used')
    
    if 'gas_price' in df.columns:
        features.append(df['gas_price'].fillna(20e9).values.reshape(-1, 1))
        feature_names.append('gas_price')
    
    # Transaction complexity features
    if 'transaction' in df.columns:
        # Transaction length as complexity indicator
        tx_length = df['transaction'].astype(str).str.len().fillna(0)
        features.append(tx_length.values.reshape(-1, 1))
        feature_names.append('transaction_complexity')
    
    # MEV type encoding
    mev_encoder = LabelEncoder()
    mev_encoded = mev_encoder.fit_transform(df['mev_type'])
    features.append(mev_encoded.reshape(-1, 1))
    feature_names.append('mev_type_encoded')
    
    # Block-based features
    if 'block_number' in df.columns:
        # Block position within dataset
        block_norm = (df['block_number'] - df['block_number'].min()) / (df['block_number'].max() - df['block_number'].min() + 1)
        features.append(block_norm.values.reshape(-1, 1))
        feature_names.append('block_position')
    
    # Profit-based features  
    if 'profit_eth' in df.columns:
        profit_log = np.log1p(np.abs(df['profit_eth'].fillna(0)))
        features.append(profit_log.values.reshape(-1, 1))
        feature_names.append('profit_log')
        
        profit_binary = (df['profit_eth'].fillna(0) > 0).astype(int)
        features.append(profit_binary.values.reshape(-1, 1))
        feature_names.append('is_profitable')
    
    # Combine all features
    if features:
        X = np.hstack(features)
    else:
        raise ValueError("No features could be extracted")
    
    logger.info(f"Extracted {len(feature_names)} features: {feature_names}")
    logger.info(f"Feature matrix shape: {X.shape}")
    
    return X, feature_names

def train_aligned_xgb_model(X, y):
    logger.info("Training XGB ensemble model...")
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # XGBoost classifier
    xgb_model = xgb.XGBClassifier(
        n_estimators=200,
        max_depth=8,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric='mlogloss'
    )
    
    # Random Forest for ensemble
    rf_model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    
    # Neural Network
    nn_model = MLPClassifier(
        hidden_layer_sizes=(128, 64),
        max_iter=500,
        random_state=42
    )
    
    # Create ensemble
    ensemble = VotingClassifier(
        estimators=[
            ('xgb', xgb_model),
            ('rf', rf_model),
            ('nn', nn_model)
        ],
        voting='soft'
    )
    
    # Train ensemble
    logger.info("Training ensemble...")
    ensemble.fit(X_scaled, y)
    
    # Calibrate probabilities
    logger.info("Calibrating probabilities...")
    calibrated_model = CalibratedClassifierCV(ensemble, method='isotonic', cv=3)
    calibrated_model.fit(X_scaled, y)
    
    return calibrated_model, scaler

def run_aligned_xgb_experiment():
    logger.info("STARTING ALIGNED XGB BASELINE EXPERIMENT")
    logger.info("=" * 80)
    logger.info("Configuration matching GAT large-scale setup:")
    for mev_type, samples in GAT_ALIGNED_SAMPLES.items():
        logger.info(f"  {mev_type.capitalize()}: {samples:,} transactions")
    logger.info(f"  Total: {sum(GAT_ALIGNED_SAMPLES.values()):,} transactions")
    logger.info("=" * 80)
    
    start_time = time.time()
    
    # Load data with GAT-aligned sample sizes
    logger.info("Phase 1: Loading aligned MEV datasets...")
    all_dfs = []
    
    for mev_type, max_samples in GAT_ALIGNED_SAMPLES.items():
        try:
            df = load_aligned_mev_data(mev_type, max_samples)
            all_dfs.append(df)
        except Exception as e:
            logger.warning(f"Failed to load {mev_type}: {e}")
    
    if not all_dfs:
        raise ValueError("No data loaded!")
    
    combined_df = pd.concat(all_dfs, ignore_index=True)
    logger.info(f"Combined dataset: {len(combined_df):,} transactions")
    
    # Extract features
    logger.info("Phase 2: Feature extraction...")
    X, feature_names = extract_comprehensive_features(combined_df)
    
    # Prepare labels (multi-class)
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(combined_df['mev_type'])
    
    logger.info(f"Dataset: {X.shape[0]:,} samples, {X.shape[1]} features")
    logger.info(f"Classes: {list(label_encoder.classes_)}")
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    logger.info(f"Train set: {len(X_train):,} samples")
    logger.info(f"Test set: {len(X_test):,} samples")
    
    # Train model
    logger.info("Phase 3: Model training...")
    model, scaler = train_aligned_xgb_model(X_train, y_train)
    
    # Test model
    logger.info("Phase 4: Model evaluation...")
    X_test_scaled = scaler.transform(X_test)
    
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
    
    # Multi-class ROC AUC
    try:
        auc = roc_auc_score(y_test, y_pred_proba, multi_class='ovr', average='weighted')
    except:
        auc = 0.0
    
    total_time = time.time() - start_time
    
    # Results
    results = {
        'experiment_type': 'aligned_xgb_baseline',
        'total_samples': len(combined_df),
        'sample_breakdown': GAT_ALIGNED_SAMPLES,
        'test_samples': len(X_test),
        'accuracy': float(accuracy),
        'precision': float(precision),
        'recall': float(recall),
        'f1_score': float(f1),
        'roc_auc': float(auc),
        'execution_time': total_time,
        'feature_names': feature_names,
        'classes': list(label_encoder.classes_)
    }
    
    # Save results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results_file = f"aligned_xgb_results_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    logger.info("=" * 80)
    logger.info("ALIGNED XGB BASELINE RESULTS")
    logger.info("=" * 80)
    logger.info(f"Total Samples: {len(combined_df):,}")
    logger.info(f"Test Samples: {len(X_test):,}")
    logger.info(f"Accuracy: {accuracy:.3f}")
    logger.info(f"Precision: {precision:.3f}")
    logger.info(f"Recall: {recall:.3f}")
    logger.info(f"F1-Score: {f1:.3f}")
    logger.info(f"ROC AUC: {auc:.3f}")
    logger.info(f"Runtime: {total_time/60:.1f} minutes")
    logger.info(f"Results: {results_file}")
    logger.info("=" * 80)
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Aligned XGB Baseline - Matching GAT Configuration')
    parser.add_argument('--run', action='store_true', help='Run the aligned XGB experiment')
    
    args = parser.parse_args()
    
    if args.run:
        try:
            results = run_aligned_xgb_experiment()
            logger.info("Aligned XGB baseline completed successfully!")
        except Exception as e:
            logger.error(f"Experiment failed: {e}")
            raise
    else:
        logger.info("Aligned XGB Baseline Configuration:")
        logger.info(f"  Arbitrage: {GAT_ALIGNED_SAMPLES['arbitrage']:,} transactions")
        logger.info(f"  Sandwich: {GAT_ALIGNED_SAMPLES['sandwich']:,} transactions")
        logger.info(f"  Liquidation: {GAT_ALIGNED_SAMPLES['liquidation']:,} transactions")
        logger.info(f"  Total: {sum(GAT_ALIGNED_SAMPLES.values()):,} transactions")
        logger.info("")
        logger.info("To run: python aligned_xgb_baseline.py --run")

if __name__ == "__main__":
    main()