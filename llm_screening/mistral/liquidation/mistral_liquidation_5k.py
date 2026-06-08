#!/usr/bin/env python3

import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import logging
import json
import os
import sys
from datetime import datetime, timedelta
import time
import traceback
import psutil
import gc
import numpy as np
from collections import defaultdict
import hashlib
import re

class EnhancedLiquidationDeployment:
    def __init__(self):
        self.model_path = "<PROJECT_ROOT>/Part-2_Unknown_Mev/huggingface_cache/models--mistralai--Mistral-7B-Instruct-v0.1/snapshots/2dcff66eac0c01dc50e4c41eea959968232187fe"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = None
        self.model = None
        
        # Configuration for enhanced liquidation analysis
        self.target_transactions = 5000  # Start with 5K for validation
        self.batch_size = 50
        self.checkpoint_interval = 1000
        self.max_retries = 3
        self.retry_delay = 5
        
        # Dataset path
        self.liquidation_path = '<PROJECT_ROOT>/large/liquidation_results.csv'
        
        # Initialize logging
        self.setup_logging()
        
        # Rich analysis caches
        self.protocol_analysis_cache = {}
        self.liquidator_behavior_cache = {}
        self.token_analysis_cache = {}
        
    def setup_logging(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create logs directory
        log_dir = "enhanced_liquidation_logs"
        os.makedirs(log_dir, exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"{log_dir}/enhanced_liquidation_{timestamp}.log"),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.results_file = f"enhanced_liquidation_results_{timestamp}.csv"
        
        self.logger.info("Enhanced Liquidation Deployment Initialized")
        
    def load_model(self):
        self.logger.info("Loading Mistral model...")
        start_time = time.time()
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, use_fast=False)
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                torch_dtype=torch.float16,
                device_map="auto",
                trust_remote_code=True
            )
            
            load_time = time.time() - start_time
            self.logger.info(f"Model loaded successfully in {load_time:.1f}s")
            
        except Exception as e:
            self.logger.error(f"Failed to load model: {e}")
            raise

    def analyze_protocol_patterns(self, df):
        protocol_stats = {}
        
        for protocol in df['protocol_name'].unique():
            if pd.isna(protocol):
                continue
                
            protocol_data = df[df['protocol_name'] == protocol]
            
            # Safe calculation with proper data type handling
            avg_profit = 0
            median_profit = 0
            profit_variance = 0
            if 'profit_eth' in protocol_data.columns:
                profit_clean = pd.to_numeric(protocol_data['profit_eth'], errors='coerce')
                avg_profit = profit_clean.mean() if not profit_clean.isna().all() else 0
                median_profit = profit_clean.median() if not profit_clean.isna().all() else 0
                profit_variance = profit_clean.var() if not profit_clean.isna().all() else 0
            
            # Safe flash_loan rate calculation
            flash_loan_rate = 0
            if 'flash_loan' in protocol_data.columns:
                flash_loan_clean = protocol_data['flash_loan'].apply(
                    lambda x: 1 if str(x).lower() in ['true', '1', 'yes', True] else 0
                )
                flash_loan_rate = flash_loan_clean.mean()
            
            # Safe flashbots rate calculation
            flashbots_rate = 0
            if 'flashbots_bundle' in protocol_data.columns:
                flashbots_clean = protocol_data['flashbots_bundle'].apply(
                    lambda x: 1 if str(x).lower() in ['true', '1', 'yes', True] else 0
                )
                flashbots_rate = flashbots_clean.mean()
            
            # Calculate protocol statistics
            stats = {
                'transaction_count': len(protocol_data),
                'avg_profit': avg_profit,
                'median_profit': median_profit,
                'profit_variance': profit_variance,
                'unique_liquidators': protocol_data['liquidator'].nunique() if 'liquidator' in protocol_data.columns else 0,
                'unique_tokens': protocol_data['debt_token_name'].nunique() if 'debt_token_name' in protocol_data.columns else 0,
                'flash_loan_rate': flash_loan_rate,
                'flashbots_rate': flashbots_rate
            }
            
            protocol_stats[protocol] = stats
            
        return protocol_stats

    def analyze_liquidator_behavior(self, df):
        liquidator_stats = {}
        
        for liquidator in df['liquidator'].unique():
            if pd.isna(liquidator):
                continue
                
            liquidator_data = df[df['liquidator'] == liquidator]
            
            # Safe profit calculations
            profit_clean = pd.to_numeric(liquidator_data['profit_eth'], errors='coerce')
            avg_profit = profit_clean.mean() if not profit_clean.isna().all() else 0
            profit_std = profit_clean.std() if not profit_clean.isna().all() else 0
            profit_consistency = 1 - (profit_std / avg_profit) if avg_profit > 0 else 0
            success_rate = (profit_clean > 0).mean() if not profit_clean.isna().all() else 0
            
            # Safe flash_loan usage calculation
            flash_loan_usage = 0
            if 'flash_loan' in liquidator_data.columns:
                flash_loan_clean = liquidator_data['flash_loan'].apply(
                    lambda x: 1 if str(x).lower() in ['true', '1', 'yes', True] else 0
                )
                flash_loan_usage = flash_loan_clean.mean()
            
            # Safe flashbots usage calculation
            flashbots_usage = 0
            if 'flashbots_bundle' in liquidator_data.columns:
                flashbots_clean = liquidator_data['flashbots_bundle'].apply(
                    lambda x: 1 if str(x).lower() in ['true', '1', 'yes', True] else 0
                )
                flashbots_usage = flashbots_clean.mean()
            
            # Calculate liquidator behavioral metrics
            stats = {
                'total_liquidations': len(liquidator_data),
                'protocols_used': liquidator_data['protocol_name'].nunique(),
                'avg_profit_per_liquidation': avg_profit,
                'profit_consistency': profit_consistency,
                'success_rate': success_rate,
                'flash_loan_usage': flash_loan_usage,
                'flashbots_usage': flashbots_usage,
                'unique_tokens_targeted': liquidator_data['debt_token_name'].nunique(),
                'time_span_analysis': self.calculate_time_span(liquidator_data)
            }
            
            liquidator_stats[liquidator] = stats
            
        return liquidator_stats

    def calculate_time_span(self, data):
        if 'block_timestamp' in data.columns and len(data) > 1:
            timestamps = pd.to_datetime(data['block_timestamp'], errors='coerce')
            valid_timestamps = timestamps.dropna()
            
            if len(valid_timestamps) > 1:
                time_span = (valid_timestamps.max() - valid_timestamps.min()).total_seconds()
                avg_interval = time_span / len(valid_timestamps) if len(valid_timestamps) > 0 else 0
                return {
                    'total_time_span_hours': time_span / 3600,
                    'avg_interval_minutes': avg_interval / 60,
                    'activity_frequency': len(valid_timestamps) / (time_span / 3600) if time_span > 0 else 0
                }
        
        return {'total_time_span_hours': 0, 'avg_interval_minutes': 0, 'activity_frequency': 0}

    def analyze_token_liquidation_patterns(self, df):
        token_stats = {}
        
        for token in df['debt_token_name'].unique():
            if pd.isna(token):
                continue
                
            token_data = df[df['debt_token_name'] == token]
            
            # Safe profit calculations
            profit_clean = pd.to_numeric(token_data['profit_eth'], errors='coerce')
            avg_profit = profit_clean.mean() if not profit_clean.isna().all() else 0
            profit_volatility = profit_clean.std() if not profit_clean.isna().all() else 0
            
            # Safe cost calculations
            avg_cost = 0
            profit_efficiency = 0
            if 'cost_eth' in token_data.columns:
                cost_clean = pd.to_numeric(token_data['cost_eth'], errors='coerce')
                avg_cost = cost_clean.mean() if not cost_clean.isna().all() else 0
                
                # Calculate profit efficiency safely
                if not cost_clean.isna().all() and not profit_clean.isna().all():
                    valid_indices = ~(cost_clean.isna() | profit_clean.isna() | (cost_clean == 0))
                    if valid_indices.any():
                        efficiency_ratio = profit_clean[valid_indices] / cost_clean[valid_indices]
                        profit_efficiency = efficiency_ratio.mean()
            
            # Calculate token liquidation characteristics
            stats = {
                'liquidation_frequency': len(token_data),
                'avg_liquidation_profit': avg_profit,
                'profit_volatility': profit_volatility,
                'protocols_involved': token_data['protocol_name'].nunique(),
                'unique_liquidators': token_data['liquidator'].nunique(),
                'market_dominance': len(token_data) / len(df),
                'avg_liquidation_cost': avg_cost,
                'profit_efficiency': profit_efficiency
            }
            
            token_stats[token] = stats
            
        return token_stats

    def calculate_advanced_metrics(self, transaction_data, protocol_stats, liquidator_stats, token_stats):
        metrics = {}
        
        # Protocol context
        protocol = transaction_data.get('protocol_name', 'Unknown')
        if protocol in protocol_stats:
            p_stats = protocol_stats[protocol]
            metrics['protocol_profit_percentile'] = self.calculate_percentile(
                transaction_data.get('profit_eth', 0), p_stats['avg_profit'], p_stats['profit_variance']
            )
            metrics['protocol_complexity_score'] = (
                p_stats['unique_liquidators'] * 0.3 +
                p_stats['unique_tokens'] * 0.3 +
                p_stats['flash_loan_rate'] * 0.2 +
                p_stats['flashbots_rate'] * 0.2
            )
        
        # Liquidator context
        liquidator = transaction_data.get('liquidator', 'Unknown')
        if liquidator in liquidator_stats:
            l_stats = liquidator_stats[liquidator]
            metrics['liquidator_experience_score'] = min(l_stats['total_liquidations'] / 100, 1.0)
            metrics['liquidator_specialization'] = 1 - (l_stats['protocols_used'] / 10)  # More specialized = fewer protocols
            metrics['liquidator_efficiency'] = l_stats['profit_consistency']
            metrics['liquidator_sophistication'] = (
                l_stats['flash_loan_usage'] * 0.4 +
                l_stats['flashbots_usage'] * 0.4 +
                l_stats['success_rate'] * 0.2
            )
        
        # Token context
        token = transaction_data.get('debt_token_name', 'Unknown')
        if token in token_stats:
            t_stats = token_stats[token]
            metrics['token_liquidation_rarity'] = 1 - t_stats['market_dominance']
            metrics['token_profit_efficiency'] = t_stats['profit_efficiency']
            metrics['token_complexity'] = t_stats['protocols_involved'] / 5  # Normalize
        
        return metrics

    def calculate_percentile(self, value, mean, variance):
        if variance == 0:
            return 0.5
        
        std_dev = np.sqrt(variance)
        z_score = (value - mean) / std_dev
        
        # Convert z-score to percentile (approximate)
        percentile = 0.5 + 0.5 * np.tanh(z_score / 2)
        return percentile

    def create_rich_transaction_context(self, transaction_data, advanced_metrics):
        context = {
            'basic_info': {
                'profit_eth': transaction_data.get('profit_eth', 0),
                'cost_eth': transaction_data.get('cost_eth', 0),
                'gain_eth': transaction_data.get('gain_eth', 0),
                'protocol': transaction_data.get('protocol_name', 'Unknown'),
                'token': transaction_data.get('debt_token_name', 'Unknown'),
                'liquidator': transaction_data.get('liquidator', 'Unknown')
            },
            'advanced_features': {
                'flash_loan': transaction_data.get('flash_loan', False),
                'flashbots_bundle': transaction_data.get('flashbots_bundle', False),
                'block_number': transaction_data.get('block_number', 0)
            },
            'contextual_analysis': advanced_metrics,
            'anomaly_indicators': self.detect_anomalies(transaction_data, advanced_metrics)
        }
        
        return context

    def detect_anomalies(self, transaction_data, advanced_metrics):
        anomalies = []
        
        # Profit anomalies
        profit = transaction_data.get('profit_eth', 0)
        cost = transaction_data.get('cost_eth', 0)
        
        if profit < 0:
            anomalies.append("negative_profit_liquidation")
        
        if cost > 0 and profit / cost > 10:
            anomalies.append("extremely_high_profit_ratio")
        
        if cost > 0 and profit / cost < 0.01:
            anomalies.append("extremely_low_profit_ratio")
        
        # Context anomalies
        if advanced_metrics.get('protocol_profit_percentile', 0.5) > 0.95:
            anomalies.append("protocol_profit_outlier")
        
        if advanced_metrics.get('liquidator_sophistication', 0) > 0.9:
            anomalies.append("highly_sophisticated_liquidator")
        
        if advanced_metrics.get('token_liquidation_rarity', 0) > 0.8:
            anomalies.append("rare_token_liquidation")
        
        # Technical anomalies
        if (transaction_data.get('flash_loan', False) and 
            transaction_data.get('flashbots_bundle', False)):
            anomalies.append("flash_loan_flashbots_combination")
        
        return anomalies

    def create_enhanced_prompt(self, rich_context):
        basic = rich_context['basic_info']
        advanced = rich_context['advanced_features']
        contextual = rich_context['contextual_analysis']
        anomalies = rich_context['anomaly_indicators']
        
        system_prompt = """You are an expert blockchain analyst specializing in MEV (Maximal Extractible Value) detection.

Analyze Ethereum liquidation transactions and classify them as:
1. KNOWN MEV - Clear, identifiable liquidation patterns
2. UNKNOWN MEV - Suspicious patterns you cannot fully categorize  
3. NORMAL - Regular transactions without MEV characteristics

KNOWN LIQUIDATION PATTERNS:
- Standard debt liquidations on protocols (Aave, Compound, MakerDAO)
- Automated liquidation bots with normal profit margins
- Clear profit from liquidating undercollateralized positions
- Regular protocol liquidations with expected collateral ratios

UNKNOWN LIQUIDATION CRITERIA (ENHANCED):
- Complex multi-step liquidation strategies with unusual patterns
- Novel liquidation mechanisms beyond standard protocols
- Abnormal profit patterns or loss-making liquidations
- Advanced liquidation timing with sophisticated coordination
- Cross-protocol liquidation strategies with complex routing
- Flash loan liquidations with non-standard profit extraction
- Liquidation MEV extraction through unconventional methods
- Liquidation strategies targeting specific market conditions
- Defensive liquidation patterns with unusual characteristics
- Advanced liquidation bots with anomalous behavior patterns

NORMAL TRANSACTIONS:
- Regular token transfers
- Standard lending protocol interactions
- Simple deposits/withdrawals

Respond with ONLY: KNOWN, UNKNOWN, or NORMAL"""

        # Create detailed user prompt with rich context
        contextual_info = []
        
        if contextual.get('protocol_complexity_score', 0) > 0.7:
            contextual_info.append(f"High protocol complexity score: {contextual['protocol_complexity_score']:.3f}")
        
        if contextual.get('liquidator_sophistication', 0) > 0.8:
            contextual_info.append(f"Highly sophisticated liquidator: {contextual['liquidator_sophistication']:.3f}")
        
        if contextual.get('token_liquidation_rarity', 0) > 0.7:
            contextual_info.append(f"Rare token liquidation: {contextual['token_liquidation_rarity']:.3f}")
        
        anomaly_info = []
        if anomalies:
            anomaly_info = [f"Anomaly: {anomaly}" for anomaly in anomalies[:3]]  # Limit to top 3
        
        user_prompt = f"""Enhanced Liquidation Analysis:

Basic Metrics:
- Profit: {basic['profit_eth']:.6f} ETH
- Cost: {basic['cost_eth']:.6f} ETH
- Net Gain: {basic['gain_eth']:.6f} ETH

Transaction Details:
- Protocol: {basic['protocol']}
- Debt Token: {basic['token']}
- Liquidator: {basic['liquidator']}

Advanced Features:
- Flash Loan: {advanced['flash_loan']}
- Flashbots Bundle: {advanced['flashbots_bundle']}
- Block: {advanced['block_number']}

Contextual Analysis:
{chr(10).join(contextual_info) if contextual_info else "Standard liquidation context"}

Anomaly Detection:
{chr(10).join(anomaly_info) if anomaly_info else "No significant anomalies detected"}

Classify this enhanced liquidation transaction:"""

        return f"[INST] {system_prompt}\n\n{user_prompt} [/INST]"

    def safe_get_numeric(self, value, default=0):
        try:
            if pd.isna(value) or value == '' or value == 'nan':
                return default
            return float(value)
        except (ValueError, TypeError):
            return default
            
    def safe_get_string(self, value, default='Unknown'):
        try:
            if pd.isna(value) or value == '' or value == 'nan':
                return default
            return str(value)
        except (ValueError, TypeError):
            return default
            
    def safe_get_boolean(self, value, default=False):
        try:
            if pd.isna(value) or value == '' or value == 'nan':
                return default
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                return value.lower() in ['true', '1', 'yes']
            return bool(value)
        except (ValueError, TypeError):
            return default

    def process_enhanced_liquidation_data(self, df):
        # Perform analysis
        self.logger.info("Analyzing protocol patterns...")
        protocol_stats = self.analyze_protocol_patterns(df)
        
        self.logger.info("Analyzing liquidator behavior...")
        liquidator_stats = self.analyze_liquidator_behavior(df)
        
        self.logger.info("Analyzing token patterns...")
        token_stats = self.analyze_token_liquidation_patterns(df)
        
        # Cache the analysis results
        self.protocol_analysis_cache = protocol_stats
        self.liquidator_behavior_cache = liquidator_stats
        self.token_analysis_cache = token_stats
        
        # Process individual transactions with rich context
        processed_data = []
        
        for idx, row in df.iterrows():
            try:
                # Extract basic transaction data
                transaction_data = {
                    'transaction_id': f'enhanced_liquidation_{idx}',
                    'mev_type': 'liquidation',
                    'liquidator': self.safe_get_string(row.get('liquidator', '')),
                    'liquidated_user': self.safe_get_string(row.get('liquidated_user', '')),
                    'debt_token_name': self.safe_get_string(row.get('debt_token_name', '')),
                    'debt_token_amount': self.safe_get_numeric(row.get('debt_token_amount', 0)),
                    'received_token_name': self.safe_get_string(row.get('received_token_name', '')),
                    'received_token_amount': self.safe_get_numeric(row.get('received_token_amount', 0)),
                    'protocol_name': self.safe_get_string(row.get('protocol_name', '')),
                    'profit_eth': self.safe_get_numeric(row.get('profit_eth', 0)),
                    'cost_eth': self.safe_get_numeric(row.get('cost_eth', 0)),
                    'gain_eth': self.safe_get_numeric(row.get('gain_eth', 0)),
                    'flashbots_bundle': self.safe_get_boolean(row.get('flashbots_bundle', False)),
                    'flash_loan': self.safe_get_boolean(row.get('flash_loan', False)),
                    'block_number': self.safe_get_numeric(row.get('block_number', 0)),
                    'block_timestamp': self.safe_get_string(row.get('block_timestamp', '')),
                    'processing_timestamp': datetime.now().isoformat()
                }
                
                # Calculate advanced metrics
                advanced_metrics = self.calculate_advanced_metrics(
                    transaction_data, protocol_stats, liquidator_stats, token_stats
                )
                
                # Create rich context
                rich_context = self.create_rich_transaction_context(transaction_data, advanced_metrics)
                
                # Store everything together
                enhanced_transaction = transaction_data.copy()
                enhanced_transaction['advanced_metrics'] = advanced_metrics
                enhanced_transaction['rich_context'] = rich_context
                
                processed_data.append(enhanced_transaction)
                
            except Exception as e:
                self.logger.error(f"Error processing enhanced transaction {idx}: {e}")
                continue
                
        return processed_data

    def analyze_transaction(self, enhanced_transaction):
        rich_context = enhanced_transaction['rich_context']
        full_prompt = self.create_enhanced_prompt(rich_context)
        
        for attempt in range(self.max_retries):
            try:
                inputs = self.tokenizer(full_prompt, return_tensors="pt", truncation=True, max_length=2048)
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                
                with torch.no_grad():
                    outputs = self.model.generate(
                        **inputs,
                        max_new_tokens=15,
                        temperature=0.3,
                        do_sample=True,
                        pad_token_id=self.tokenizer.eos_token_id,
                        repetition_penalty=1.1
                    )
                
                response = self.tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
                response = response.strip().upper()
                
                if "KNOWN" in response:
                    return "KNOWN"
                elif "UNKNOWN" in response:
                    return "UNKNOWN"
                elif "NORMAL" in response:
                    return "NORMAL"
                else:
                    return "UNKNOWN"
                    
            except Exception as e:
                self.logger.error(f"Analysis attempt {attempt+1} failed: {str(e)}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    return "ERROR"
        
        return "ERROR"

    def run_enhanced_deployment(self):
        try:
            self.logger.info("Starting Enhanced Liquidation Deployment")
            self.logger.info("=" * 60)
            
            # Load model
            self.load_model()
            
            # Load and sample data
            self.logger.info("Loading liquidation dataset...")
            df = pd.read_csv(self.liquidation_path, low_memory=False)
            
            self.logger.info(f"Total available transactions: {len(df):,}")
            self.logger.info(f"Sampling {self.target_transactions:,} transactions...")
            
            # Use random sampling for consistency
            sample_df = df.sample(n=self.target_transactions, random_state=42).reset_index(drop=True)
            
            # Enhanced processing
            self.logger.info("Processing enhanced liquidation data...")
            processed_transactions = self.process_enhanced_liquidation_data(sample_df)
            self.logger.info(f"Enhanced processing complete: {len(processed_transactions):,} transactions")
            
            # Analysis
            results = []
            start_time = time.time()
            
            self.logger.info("Starting enhanced analysis...")
            
            for i, transaction in enumerate(processed_transactions):
                try:
                    classification = self.analyze_transaction(transaction)
                    
                    # Store results
                    result = {
                        'transaction_id': transaction['transaction_id'],
                        'mev_type': 'liquidation',
                        'llm_classification': classification,
                        'is_unknown': (classification == 'UNKNOWN'),
                        'profit_eth': transaction['profit_eth'],
                        'cost_eth': transaction['cost_eth'],
                        'gain_eth': transaction['gain_eth'],
                        'protocol_name': transaction['protocol_name'],
                        'debt_token_name': transaction['debt_token_name'],
                        'liquidator': transaction['liquidator'],
                        'flash_loan': transaction['flash_loan'],
                        'flashbots_bundle': transaction['flashbots_bundle'],
                        'block_number': transaction['block_number'],
                        'processing_timestamp': transaction['processing_timestamp'],
                        'advanced_metrics': json.dumps(transaction['advanced_metrics']),
                        'anomalies': json.dumps(transaction['rich_context']['anomaly_indicators'])
                    }
                    
                    results.append(result)
                    
                    # Progress reporting
                    if (i + 1) % 1000 == 0:
                        elapsed = time.time() - start_time
                        speed = (i + 1) / elapsed
                        unknown_count = sum(1 for r in results if r.get('is_unknown', False))
                        unknown_rate = unknown_count / len(results) * 100
                        
                        self.logger.info(f"Progress: {i+1:,}/{len(processed_transactions):,} ({(i+1)/len(processed_transactions)*100:.1f}%) - "
                                       f"{speed:.2f} tx/s - Unknown: {unknown_count} ({unknown_rate:.3f}%)")
                        
                except Exception as e:
                    self.logger.error(f"Error analyzing transaction {i}: {e}")
                    continue
            
            # Final results
            self.analyze_enhanced_results(results, time.time() - start_time)
            
            return results
            
        except Exception as e:
            self.logger.error(f"Enhanced deployment failed: {e}")
            raise

    def analyze_enhanced_results(self, results, total_time):
        self.logger.info("\nENHANCED LIQUIDATION DEPLOYMENT RESULTS")
        self.logger.info("=" * 60)
        
        total = len(results)
        unknown_count = sum(1 for r in results if r.get('is_unknown', False))
        known_count = sum(1 for r in results if r.get('llm_classification') == 'KNOWN')
        normal_count = sum(1 for r in results if r.get('llm_classification') == 'NORMAL')
        
        unknown_rate = unknown_count / total * 100 if total > 0 else 0
        
        self.logger.info(f"Processing Statistics:")
        self.logger.info(f"  Total transactions: {total:,}")
        self.logger.info(f"  Processing time: {total_time/60:.1f} minutes")
        self.logger.info(f"  Speed: {total/total_time:.2f} tx/s")
        
        self.logger.info(f"\nClassification Results:")
        self.logger.info(f"  Unknown patterns: {unknown_count} ({unknown_rate:.3f}%)")
        self.logger.info(f"  Known patterns: {known_count} ({known_count/total*100:.1f}%)")
        self.logger.info(f"  Normal transactions: {normal_count} ({normal_count/total*100:.1f}%)")
        
        self.logger.info(f"\nCross-MEV Comparison:")
        self.logger.info(f"  Arbitrage (successful): 0.043% unknown rate")
        self.logger.info(f"  Sandwich (successful): 0.029% unknown rate")
        self.logger.info(f"  Enhanced Liquidation: {unknown_rate:.3f} unknown rate")
        
        target_min = 0.02
        if unknown_rate >= target_min:
            self.logger.info(f"\nSUCCESS: {unknown_rate:.3f}% meets target ({target_min}%)")
            self.logger.info("Enhanced methodology successfully applied to liquidation!")
        else:
            self.logger.info(f"\nBELOW TARGET: {unknown_rate:.3f}% < {target_min}%")
            self.logger.info("May need further liquidation-specific refinement")
        
        # Save results
        df_results = pd.DataFrame(results)
        df_results.to_csv(self.results_file, index=False)
        self.logger.info(f"\nEnhanced results saved to: {self.results_file}")
        
        if unknown_count > 0:
            self.logger.info(f"\nDISCOVERED ENHANCED UNKNOWN PATTERNS:")
            unknown_df = df_results[df_results['is_unknown'] == True]
            
            # Show top patterns by profit
            unknown_df_sorted = unknown_df.sort_values('profit_eth', key=abs, ascending=False)
            
            for idx, row in unknown_df_sorted.head(10).iterrows():
                self.logger.info(f"  {row['profit_eth']:.6f} ETH - {row['debt_token_name']} on {row['protocol_name']}")
            
            self.logger.info(f"\nEnhanced liquidation patterns discovered: {unknown_count}")

def main():
    deployment = EnhancedLiquidationDeployment()
    
    try:
        results = deployment.run_enhanced_deployment()
        print(f"\nEnhanced deployment completed successfully!")
        print(f"Results: {len(results):,} transactions analyzed")
        
    except KeyboardInterrupt:
        print("\nDeployment interrupted by user")
    except Exception as e:
        print(f"\nDeployment failed: {e}")
        raise

if __name__ == "__main__":
    main()