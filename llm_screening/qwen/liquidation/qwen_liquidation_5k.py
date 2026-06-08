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

class QwenLiquidation5K:
    def __init__(self):
        self.model_path = "<PROJECT_ROOT>/Part-2_Unknown_Mev/huggingface_cache/models--Qwen--Qwen2.5-7B-Instruct/snapshots/a09a35458c702b33eeacc393d103063234e8bc28"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = None
        self.model = None

        # Configuration for 5K baseline
        self.target_transactions = 5000
        self.batch_size = 50
        self.checkpoint_interval = 1000
        self.max_retries = 3
        self.retry_delay = 5

        # GPU optimization
        self.enable_kv_cache = True
        self.use_cache = True
        self.num_beams = 1

        # Dataset path
        self.liquidation_path = '<PROJECT_ROOT>/large/liquidation_results.csv'

        # Initialize logging
        self.setup_logging()

        # Rich analysis caches (matching Mistral methodology)
        self.protocol_analysis_cache = {}
        self.liquidator_behavior_cache = {}
        self.token_analysis_cache = {}

        # Performance tracking
        self.deployment_start_time = None

    def setup_logging(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create logs directory
        log_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Logs/Liquidation"
        os.makedirs(log_dir, exist_ok=True)

        # Results directory
        results_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Results/Liquidation"
        os.makedirs(results_dir, exist_ok=True)

        # Main log file
        log_file = f"{log_dir}/qwen_liquidation_5k_{timestamp}.log"

        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )

        self.logger = logging.getLogger(__name__)
        self.log_file = log_file
        self.results_file = f"{results_dir}/qwen_liquidation_5k_{timestamp}.csv"
        self.checkpoint_file = f"{results_dir}/checkpoint_qwen_liquidation_5k_{timestamp}.json"

        # Milestone log
        self.milestone_log = f"{log_dir}/milestones_5k_{timestamp}.log"
        self.milestone_logger = logging.getLogger('milestones')
        milestone_handler = logging.FileHandler(self.milestone_log)
        milestone_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.milestone_logger.addHandler(milestone_handler)
        self.milestone_logger.setLevel(logging.INFO)

        self.logger.info("Qwen2.5-7B Liquidation 5K Baseline Test Initialized")
        self.logger.info(f"Results file: {self.results_file}")

    def load_model(self):
        self.logger.info("Loading Qwen2.5-7B model...")
        start_time = time.time()

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, use_fast=False)
            self.tokenizer.pad_token = self.tokenizer.eos_token

            try:
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_path,
                    torch_dtype=torch.float16,
                    device_map="auto",
                    trust_remote_code=True
                )
                self.logger.info("Model loaded with automatic device mapping")
            except (RuntimeError, ValueError) as e:
                self.logger.warning(f"Automatic device mapping failed: {str(e)}")
                self.logger.info("Attempting to load on first available GPU...")

                gpu_id = 0
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_path,
                    torch_dtype=torch.float16,
                    device_map={"": f"cuda:{gpu_id}"},
                    trust_remote_code=True
                )
                self.logger.info(f"Model loaded on GPU {gpu_id}")

            load_time = time.time() - start_time
            self.logger.info(f"Model loaded successfully in {load_time:.1f}s")

            if torch.cuda.is_available():
                for i in range(torch.cuda.device_count()):
                    allocated = torch.cuda.memory_allocated(i) / (1024**3)
                    self.logger.info(f"GPU {i}: {allocated:.1f}GB allocated")

            return True

        except Exception as e:
            self.logger.error(f"Model loading failed: {str(e)}")
            return False

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

            # Calculate protocol statistics
            stats = {
                'transaction_count': len(protocol_data),
                'avg_profit': avg_profit,
                'median_profit': median_profit,
                'profit_variance': profit_variance,
                'unique_liquidators': protocol_data['liquidator'].nunique() if 'liquidator' in protocol_data.columns else 0,
                'unique_tokens': protocol_data['debt_token_name'].nunique() if 'debt_token_name' in protocol_data.columns else 0,
                'flash_loan_rate': flash_loan_rate
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

            stats = {
                'total_liquidations': len(liquidator_data),
                'protocols_used': liquidator_data['protocol_name'].nunique(),
                'avg_profit_per_liquidation': avg_profit,
                'profit_consistency': profit_consistency,
                'success_rate': success_rate
            }

            liquidator_stats[liquidator] = stats

        return liquidator_stats

    def calculate_advanced_metrics(self, transaction_data, protocol_stats, liquidator_stats):
        metrics = {}

        # Protocol context
        protocol = transaction_data.get('protocol_name', 'Unknown')
        if protocol in protocol_stats:
            p_stats = protocol_stats[protocol]
            metrics['protocol_complexity_score'] = (
                p_stats['unique_liquidators'] * 0.3 +
                p_stats['unique_tokens'] * 0.3 +
                p_stats['flash_loan_rate'] * 0.4
            )

        # Liquidator context
        liquidator = transaction_data.get('liquidator', 'Unknown')
        if liquidator in liquidator_stats:
            l_stats = liquidator_stats[liquidator]
            metrics['liquidator_experience_score'] = min(l_stats['total_liquidations'] / 100, 1.0)
            metrics['liquidator_efficiency'] = l_stats['profit_consistency']

        return metrics

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
        if advanced_metrics.get('protocol_complexity_score', 0) > 0.7:
            anomalies.append("high_protocol_complexity")

        if advanced_metrics.get('liquidator_experience_score', 0) > 0.9:
            anomalies.append("highly_experienced_liquidator")

        return anomalies

    def create_system_prompt(self):
        return """You are an expert blockchain analyst specializing in MEV detection.

Classify this liquidation transaction as KNOWN, UNKNOWN, or NORMAL.

KNOWN MEV (most liquidations):
- Standard Aave, Compound, MakerDAO liquidations
- Flash loan liquidations with typical profit extraction
- Automated liquidation bot activity
- Failed liquidations using standard methods
- Single-protocol liquidations

UNKNOWN MEV (rare - only when clearly anomalous):
- Multi-protocol liquidation chains in single transaction
- Liquidations with unusual token combinations not typically seen
- Coordinated liquidation patterns across multiple transactions
- Liquidations exploiting protocol-specific edge cases

NORMAL:
- Non-liquidation transactions

Note: Profit amount (high or low, positive or negative) does not determine classification.
A failed liquidation is KNOWN if it used standard methods.

Respond with ONLY: KNOWN, UNKNOWN, or NORMAL"""

    def create_enhanced_prompt(self, transaction_data, advanced_metrics, anomalies):
        system_prompt = self.create_system_prompt()

        # Simplified user prompt without anomaly signals that bias toward UNKNOWN
        user_prompt = f"""Liquidation Transaction:

- Protocol: {transaction_data.get('protocol_name', 'Unknown')}
- Profit: {transaction_data.get('profit_eth', 0):.6f} ETH
- Flash Loan: {transaction_data.get('flash_loan', False)}
- Token: {transaction_data.get('debt_token_name', 'Unknown')}

Classify:"""

        return system_prompt, user_prompt

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

    def analyze_transaction(self, transaction_data, advanced_metrics, anomalies):
        system_prompt, user_prompt = self.create_enhanced_prompt(transaction_data, advanced_metrics, anomalies)

        # Use Qwen's native chat template
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        full_prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

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
                        repetition_penalty=1.1,
                        use_cache=self.use_cache,
                        num_beams=self.num_beams
                    )

                response = self.tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
                response = response.strip().upper()

                if "UNKNOWN" in response:
                    return "UNKNOWN"
                elif "KNOWN" in response:
                    return "KNOWN"
                elif "NORMAL" in response:
                    return "NORMAL"
                else:
                    return "UNKNOWN"  # Default for unclear responses

            except Exception as e:
                self.logger.error(f"Analysis attempt {attempt+1} failed: {str(e)}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    return "ERROR"

        return "ERROR"

    def save_checkpoint(self, results, current_index):
        checkpoint_data = {
            'last_processed': current_index,
            'timestamp': datetime.now().isoformat(),
            'total_results': len(results),
            'target_transactions': self.target_transactions
        }

        with open(self.checkpoint_file, 'w') as f:
            json.dump(checkpoint_data, f, indent=2)

        # Save current results
        if results:
            df_results = pd.DataFrame(results)
            df_results.to_csv(self.results_file, index=False)

        unknown_count = sum(1 for r in results if r.get('llm_classification') == 'UNKNOWN')
        self.milestone_logger.info(f"CHECKPOINT: {current_index+1:,}/{self.target_transactions:,} - {unknown_count} unknown patterns")

    def run_deployment(self):
        try:
            self.deployment_start_time = time.time()

            self.logger.info("Starting Qwen 5K Liquidation Deployment")
            self.logger.info("=" * 70)

            # Load model
            if not self.load_model():
                return None

            # Load dataset
            self.logger.info("Loading liquidation dataset...")
            df = pd.read_csv(self.liquidation_path, low_memory=False)

            actual_transactions = len(df)
            self.logger.info(f"Total available transactions: {actual_transactions:,}")

            # Sample 5K transactions
            if actual_transactions > self.target_transactions:
                sample_df = df.sample(n=self.target_transactions, random_state=5000)
                sample_df = sample_df.reset_index(drop=True)
            else:
                sample_df = df
                self.target_transactions = len(sample_df)

            self.logger.info(f"Processing {self.target_transactions:,} transactions")

            # Analyze patterns for rich context
            self.logger.info("Analyzing protocol patterns...")
            protocol_stats = self.analyze_protocol_patterns(sample_df)

            self.logger.info("Analyzing liquidator behavior...")
            liquidator_stats = self.analyze_liquidator_behavior(sample_df)

            self.logger.info(f"Protocol analysis: {len(protocol_stats)} protocols")
            self.logger.info(f"Liquidator analysis: {len(liquidator_stats)} liquidators")

            # Process transactions
            results = []
            start_time = time.time()

            self.logger.info("Starting transaction analysis...")

            for idx, row in sample_df.iterrows():
                try:
                    # Extract transaction data
                    transaction_data = {
                        'transaction_id': f'qwen_liquidation_5k_{idx}',
                        'mev_type': 'liquidation',
                        'liquidator': self.safe_get_string(row.get('liquidator', '')),
                        'debt_token_name': self.safe_get_string(row.get('debt_token_name', '')),
                        'protocol_name': self.safe_get_string(row.get('protocol_name', '')),
                        'profit_eth': self.safe_get_numeric(row.get('profit_eth', 0)),
                        'cost_eth': self.safe_get_numeric(row.get('cost_eth', 0)),
                        'gain_eth': self.safe_get_numeric(row.get('gain_eth', 0)),
                        'flash_loan': self.safe_get_boolean(row.get('flash_loan', False)),
                        'block_number': self.safe_get_numeric(row.get('block_number', 0))
                    }

                    # Calculate advanced metrics
                    advanced_metrics = self.calculate_advanced_metrics(
                        transaction_data, protocol_stats, liquidator_stats
                    )

                    # Detect anomalies
                    anomalies = self.detect_anomalies(transaction_data, advanced_metrics)

                    # Analyze with LLM
                    classification = self.analyze_transaction(transaction_data, advanced_metrics, anomalies)

                    # Store result
                    result = {
                        'transaction_id': transaction_data['transaction_id'],
                        'mev_type': 'liquidation',
                        'llm_classification': classification,
                        'is_unknown': (classification == 'UNKNOWN'),
                        'profit_eth': transaction_data['profit_eth'],
                        'cost_eth': transaction_data['cost_eth'],
                        'gain_eth': transaction_data['gain_eth'],
                        'protocol_name': transaction_data['protocol_name'],
                        'debt_token_name': transaction_data['debt_token_name'],
                        'liquidator': transaction_data['liquidator'],
                        'flash_loan': transaction_data['flash_loan'],
                        'block_number': transaction_data['block_number'],
                        'processing_timestamp': datetime.now().isoformat(),
                        'anomalies': json.dumps(anomalies)
                    }

                    results.append(result)

                    # Progress reporting
                    if (idx + 1) % 500 == 0:
                        elapsed = time.time() - start_time
                        speed = (idx + 1) / elapsed
                        unknown_count = sum(1 for r in results if r.get('is_unknown', False))
                        unknown_rate = unknown_count / len(results) * 100

                        remaining = self.target_transactions - (idx + 1)
                        eta_minutes = remaining / speed / 60 if speed > 0 else 0

                        self.logger.info(f"Progress: {idx+1:,}/{self.target_transactions:,} ({(idx+1)/self.target_transactions*100:.1f}%) - "
                                       f"{speed:.2f} tx/s - Unknown: {unknown_count} ({unknown_rate:.3f}%) - ETA: {eta_minutes:.1f}m")

                        # Save checkpoint
                        self.save_checkpoint(results, idx)

                        # Memory cleanup
                        gc.collect()
                        if torch.cuda.is_available():
                            torch.cuda.empty_cache()

                except Exception as e:
                    self.logger.error(f"Error analyzing transaction {idx}: {e}")
                    continue

            # Final results
            total_time = time.time() - start_time
            self.analyze_results(results, total_time)

            return results

        except Exception as e:
            self.logger.error(f"Deployment failed: {e}")
            raise

    def analyze_results(self, results, total_time):
        self.logger.info("\nQWEN 5K LIQUIDATION DEPLOYMENT RESULTS (Post-Processed)")
        self.logger.info("=" * 70)

        # REMAP OUTPUT: NORMAL → KNOWN (all are liquidations, so none should be NORMAL)
        for r in results:
            if r.get('llm_classification') == 'NORMAL':
                r['llm_classification'] = 'KNOWN'

        total = len(results)
        unknown_count = sum(1 for r in results if r.get('llm_classification') == 'UNKNOWN')
        known_count = sum(1 for r in results if r.get('llm_classification') == 'KNOWN')
        normal_count = sum(1 for r in results if r.get('llm_classification') == 'NORMAL')

        unknown_rate = unknown_count / total * 100 if total > 0 else 0

        self.logger.info(f"Processing Statistics:")
        self.logger.info(f"  Total transactions: {total:,}")
        self.logger.info(f"  Processing time: {total_time/60:.1f} minutes ({total_time/3600:.2f} hours)")
        self.logger.info(f"  Average speed: {total/total_time:.2f} tx/s")

        self.logger.info(f"\nClassification Results (After Remapping):")
        self.logger.info(f"  Unknown patterns: {unknown_count} ({unknown_rate:.3f}%)")
        self.logger.info(f"  Known patterns: {known_count} ({known_count/total*100:.1f}%)")
        self.logger.info(f"  Normal transactions: {normal_count} ({normal_count/total*100:.1f}%)")

        self.logger.info(f"\nComparison with Mistral 5K Baseline:")
        self.logger.info(f"  Mistral 5K: 4 unknown (0.080%)")
        self.logger.info(f"  Qwen 5K: {unknown_count} unknown ({unknown_rate:.3f}%)")

        # Analyze unknown profit distribution
        if unknown_count > 0:
            unknown_results = [r for r in results if r.get('llm_classification') == 'UNKNOWN']
            profits = [r['profit_eth'] for r in unknown_results]
            positive_profit = sum(1 for p in profits if p > 0)
            negative_profit = sum(1 for p in profits if p < 0)

            self.logger.info(f"\nUnknown Profit Analysis:")
            self.logger.info(f"  Positive profit: {positive_profit} ({positive_profit/unknown_count*100:.1f}%)")
            self.logger.info(f"  Negative profit: {negative_profit} ({negative_profit/unknown_count*100:.1f}%)")
            if profits:
                self.logger.info(f"  Avg profit: {sum(profits)/len(profits):.6f} ETH")
                self.logger.info(f"  Max profit: {max(profits):.6f} ETH")
                self.logger.info(f"  Min profit: {min(profits):.6f} ETH")

        # Save results
        df_results = pd.DataFrame(results)
        df_results.to_csv(self.results_file, index=False)
        self.logger.info(f"\nResults saved to: {self.results_file}")
        self.logger.info(f"Note: Output remapped - NORMAL → KNOWN for proper liquidation classification")

        self.milestone_logger.info(f"DEPLOYMENT COMPLETE: {total:,} transactions, {unknown_count} unknown patterns, {unknown_rate:.3f}% rate (remapped)")

def main():
    print("=" * 60)
    print("QWEN2.5-7B LIQUIDATION 5K BASELINE TEST")
    print("Designed to match Mistral methodology for fair comparison")
    print("=" * 60)

    deployment = QwenLiquidation5K()

    try:
        results = deployment.run_deployment()
        print(f"\nDeployment completed successfully!")
        print(f"Results: {len(results):,} transactions analyzed")

    except KeyboardInterrupt:
        print("\nDeployment interrupted by user")
    except Exception as e:
        print(f"\nDeployment failed: {e}")
        raise

if __name__ == "__main__":
    main()
