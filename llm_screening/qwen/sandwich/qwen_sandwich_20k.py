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

class QwenSandwichDeployment20K:
    def __init__(self):
        self.model_id = "Qwen/Qwen2.5-7B-Instruct"
        self.cache_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/huggingface_cache"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = None
        self.model = None

        # Configuration for 20K sandwich transactions
        self.target_transactions = 20000
        self.batch_size = 50
        self.checkpoint_interval = 1000
        self.max_retries = 3
        self.retry_delay = 5

        # Dataset path
        self.sandwich_path = '<PROJECT_ROOT>/large/sandwich_results.csv'

        # Initialize logging
        self.setup_logging()

    def setup_logging(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create logs directory in Qwen folder
        log_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Logs"
        os.makedirs(log_dir, exist_ok=True)

        # Main log file
        log_file = f"{log_dir}/qwen_sandwich_20k_{timestamp}.log"

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

        # Performance log
        self.perf_log = f"{log_dir}/qwen_performance_sandwich_20k_{timestamp}.log"
        self.perf_logger = logging.getLogger('performance')
        perf_handler = logging.FileHandler(self.perf_log)
        perf_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.perf_logger.addHandler(perf_handler)
        self.perf_logger.setLevel(logging.INFO)

        # Error log
        self.error_log = f"{log_dir}/qwen_errors_sandwich_20k_{timestamp}.log"
        self.error_logger = logging.getLogger('errors')
        error_handler = logging.FileHandler(self.error_log)
        error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.error_logger.addHandler(error_handler)
        self.error_logger.setLevel(logging.ERROR)

        # Results files in Qwen Results folder
        results_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Results"
        os.makedirs(results_dir, exist_ok=True)

        self.results_file = f"{results_dir}/qwen_sandwich_20k_{timestamp}.csv"
        self.unknowns_file = f"{results_dir}/qwen_sandwich_20k_unknowns_{timestamp}.csv"

        # Checkpoint in Qwen Checkpoints folder
        checkpoint_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Checkpoints"
        os.makedirs(checkpoint_dir, exist_ok=True)

        self.checkpoint_file = f"{checkpoint_dir}/qwen_sandwich_20k_{timestamp}.json"

        self.logger.info(f"Qwen2.5-7B 20K Sandwich Attack Deployment Initialized")
        self.logger.info(f"Main log: {log_file}")
        self.logger.info(f"Performance log: {self.perf_log}")
        self.logger.info(f"Error log: {self.error_log}")
        self.logger.info(f"Results file: {self.results_file}")
        self.logger.info(f"Unknowns file: {self.unknowns_file}")

    def log_system_info(self):
        self.logger.info(" SYSTEM INFORMATION - QWEN2.5 20K SANDWICH DEPLOYMENT")
        self.logger.info("=" * 75)

        # System info
        cpu_count = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        self.logger.info(f"CPU: {cpu_count} cores, {cpu_percent}% usage")
        self.logger.info(f"RAM: {memory.total // (1024**3)}GB total, {memory.percent}% used")
        self.logger.info(f"Disk: {disk.total // (1024**3)}GB total, {disk.percent}% used")

        # GPU info
        if torch.cuda.is_available():
            gpu_count = torch.cuda.device_count()
            self.logger.info(f"GPUs: {gpu_count} available")
            for i in range(gpu_count):
                gpu_memory = torch.cuda.get_device_properties(i).total_memory // (1024**3)
                self.logger.info(f"  GPU {i}: {gpu_memory}GB")

        # Time estimates based on Qwen arbitrage performance
        self.logger.info("\nQWEN2.5 20K SANDWICH TIME ESTIMATES")
        self.logger.info("=" * 55)

        baseline_speed = 1.2      # tx/s from arbitrage experience
        optimized_speed = 1.5     # tx/s with optimizations
        optimistic_speed = 1.8    # tx/s best case

        baseline_time = self.target_transactions / baseline_speed / 3600
        optimized_time = self.target_transactions / optimized_speed / 3600
        optimistic_time = self.target_transactions / optimistic_speed / 3600

        self.logger.info(f"Target transactions: {self.target_transactions:,}")
        self.logger.info(f"Baseline (1.2 tx/s): {baseline_time:.1f} hours ({baseline_time/24:.1f} days)")
        self.logger.info(f"Optimized (1.5 tx/s): {optimized_time:.1f} hours ({optimized_time/24:.1f} days)")
        self.logger.info(f"Optimistic (1.8 tx/s): {optimistic_time:.1f} hours ({optimistic_time/24:.1f} days)")
        self.logger.info(f"Expected duration: 3-5 hours")

        # Expected unknown patterns based on Mistral baseline
        self.logger.info(f"\nEXPECTED SANDWICH UNKNOWN PATTERNS:")
        self.logger.info(f"  Mistral 20K baseline: 168 unknown patterns (0.840%)")
        self.logger.info(f"  Qwen expected: Similar or higher discovery rate")
        self.logger.info(f"  Pattern categories: Advanced victim targeting, bot swarms, coordination")

    def load_model(self):
        self.logger.info("Loading Qwen2.5-7B-Instruct model for sandwich detection...")
        start_time = time.time()

        try:
            # Clear GPU cache before loading
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                self.logger.info("Cleared GPU cache")

            # Load tokenizer
            self.logger.info("Loading Qwen tokenizer...")
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_id,
                cache_dir=self.cache_dir,
                use_fast=False,
                trust_remote_code=True
            )

            # Set pad token
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token

            # Load model with optimized memory configuration
            self.logger.info("Loading Qwen model...")

            # Memory allocation for multi-GPU
            max_memory = {}
            for i in range(1, 9):  # GPUs 1-8
                max_memory[i] = "9GB"
            max_memory["cpu"] = "80GB"

            self.logger.info(f"Memory config: {max_memory}")

            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_id,
                cache_dir=self.cache_dir,
                torch_dtype=torch.float16,
                device_map="auto",
                max_memory=max_memory,
                trust_remote_code=True,
                low_cpu_mem_usage=True
            )

            load_time = time.time() - start_time
            self.logger.info(f"Qwen2.5 model loaded successfully in {load_time:.1f}s")

            # GPU memory usage logging
            if torch.cuda.is_available():
                total_gpu_memory = 0
                for i in range(torch.cuda.device_count()):
                    allocated = torch.cuda.memory_allocated(i) / (1024**3)
                    total_gpu_memory += allocated
                    self.logger.info(f"GPU {i}: {allocated:.1f}GB allocated")
                self.logger.info(f"Total GPU memory: {total_gpu_memory:.1f}GB")

            return True

        except Exception as e:
            self.error_logger.error(f"Qwen model loading failed: {str(e)}")
            self.error_logger.error(traceback.format_exc())
            return False

    def create_system_prompt(self):
        return """You are an expert blockchain analyst specializing in MEV (Maximal Extractible Value) detection.

Analyze Ethereum sandwich attack transactions and classify them as:
1. KNOWN MEV - Clear, identifiable sandwich attack patterns
2. UNKNOWN MEV - Suspicious patterns you cannot fully categorize
3. NORMAL - Regular transactions without MEV characteristics

KNOWN SANDWICH ATTACK PATTERNS:
- Front-running: Transaction placed before victim transaction
- Back-running: Transaction placed after victim transaction
- Clear victim exploitation with price manipulation
- Standard 3-transaction sandwich structure (front, victim, back)
- Token price manipulation for profit extraction
- Uniswap/Sushiswap sandwich attacks
- Clear profit from victim's slippage

UNKNOWN SANDWICH CRITERIA:
- Advanced victim selection and targeting algorithms
- Coordinated multi-bot sandwich swarms
- Complex multi-victim simultaneous sandwiching
- Non-standard attack timing (delayed front/back-running)
- Flashbots bundle manipulation and MEV protection bypass
- Sandwich attacks spanning multiple blocks
- Victim transaction prediction and pre-positioning
- Cross-exchange sandwich coordination
- Gas price manipulation for sandwich optimization
- Novel victim targeting strategies

NORMAL TRANSACTIONS:
- Regular token swaps without exploitation
- Standard DEX interactions
- Simple transfers

Respond with ONLY: KNOWN, UNKNOWN, or NORMAL"""

    def parse_sandwich_transaction(self, row):
        try:
            # Parse the three transactions in sandwich attack
            try:
                first_tx = eval(row['first_transaction'].replace("'", '"').replace('$oid', 'oid'))
            except:
                first_tx = {'hash': '', 'gas': 0, 'value': '0'}

            try:
                whale_tx = eval(row['whale_transaction'].replace("'", '"').replace('$oid', 'oid'))
            except:
                whale_tx = {'hash': '', 'gas': 0, 'value': '0'}

            try:
                second_tx = eval(row['second_transaction'].replace("'", '"').replace('$oid', 'oid'))
            except:
                second_tx = {'hash': '', 'gas': 0, 'value': '0'}

            # Create description
            token_name = row.get('token_name', 'Unknown Token')
            exchange_name = row.get('exchange_name', 'Unknown Exchange')
            profit = row.get('profit_eth', 0)

            description = f"Sandwich Attack on {exchange_name}: {token_name} with {profit:.6f} ETH profit"

            # Extract transaction data
            base_data = {
                'transaction_id': f"qwen_sandwich_20k_{row.name}",
                'mev_type': 'sandwich',
                'model': 'qwen2.5-7b',
                'scale': '20k',
                'is_mev': True,
                'block_number': row.get('block_number', 0),
                'block_timestamp': row.get('block_timestamp', ''),
                'first_tx_hash': first_tx.get('hash', ''),
                'whale_tx_hash': whale_tx.get('hash', ''),
                'second_tx_hash': second_tx.get('hash', ''),
                'bot_address': row.get('bot_address', ''),
                'exchange_name': exchange_name,
                'token_name': token_name,
                'profit_eth': float(profit) if profit else 0,
                'cost_eth': float(row.get('cost_eth', 0)) if row.get('cost_eth') else 0,
                'gain_eth': float(row.get('gain_eth', 0)) if row.get('gain_eth') else 0,
                'first_tx_gas': first_tx.get('gas', 0),
                'whale_tx_gas': whale_tx.get('gas', 0),
                'second_tx_gas': second_tx.get('gas', 0),
                'flashbots_bundle': row.get('flashbots_bundle', False),
                'same_sender': row.get('same_sender', False),
                'same_receiver': row.get('same_receiver', False),
                'description': description
            }

            return base_data

        except Exception as e:
            self.error_logger.error(f"Failed to parse sandwich transaction {row.name}: {str(e)}")
            return None

    def analyze_transaction(self, transaction_data):
        system_prompt = self.create_system_prompt()

        user_prompt = f"""Sandwich Attack Analysis:

Profit: {transaction_data.get('profit_eth', 0):.6f} ETH
Cost: {transaction_data.get('cost_eth', 0):.6f} ETH
Net Gain: {transaction_data.get('gain_eth', 0):.6f} ETH

Exchange: {transaction_data.get('exchange_name', 'Unknown')}
Token: {transaction_data.get('token_name', 'Unknown')}
Bot Address: {transaction_data.get('bot_address', 'Unknown')}

Transaction Structure:
- Front-running TX: Gas {transaction_data.get('first_tx_gas', 0):,}
- Victim TX: Gas {transaction_data.get('whale_tx_gas', 0):,}
- Back-running TX: Gas {transaction_data.get('second_tx_gas', 0):,}

Attack Properties:
- Flashbots Bundle: {transaction_data.get('flashbots_bundle', False)}
- Same Sender: {transaction_data.get('same_sender', False)}
- Same Receiver: {transaction_data.get('same_receiver', False)}

Block: {transaction_data.get('block_number', 0)}

Classify this sandwich attack transaction:"""

        full_prompt = f"[INST] {system_prompt}\n\n{user_prompt} [/INST]"

        for attempt in range(self.max_retries):
            try:
                inputs = self.tokenizer(full_prompt, return_tensors="pt", truncation=True, max_length=2048)
                inputs = {k: v.to(self.device) for k, v in inputs.items()}

                with torch.no_grad():
                    outputs = self.model.generate(
                        **inputs,
                        max_new_tokens=10,
                        temperature=0.05,
                        do_sample=True,
                        pad_token_id=self.tokenizer.eos_token_id,
                        repetition_penalty=1.1
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
                    return "KNOWN"  # Default to KNOWN for unclear responses

            except Exception as e:
                self.error_logger.error(f"Analysis attempt {attempt+1} failed: {str(e)}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    return "ERROR"

        return "ERROR"

    def save_checkpoint(self, results, last_processed):
        try:
            # Save results
            results_df = pd.DataFrame(results)
            results_df.to_csv(self.results_file, index=False)

            # Save unknown patterns separately
            unknown_results = [r for r in results if r.get('llm_classification') == 'UNKNOWN']
            if unknown_results:
                unknown_df = pd.DataFrame(unknown_results)
                unknown_df.to_csv(self.unknowns_file, index=False)
                self.logger.info(f"Unknown patterns saved: {len(unknown_results):,}")

            # Save checkpoint
            checkpoint = {
                'model': 'qwen2.5-7b',
                'scale': '20k',
                'mev_type': 'sandwich',
                'last_processed': last_processed,
                'timestamp': datetime.now().isoformat(),
                'total_results': len(results),
                'unknown_count': len(unknown_results),
                'target_transactions': self.target_transactions
            }
            with open(self.checkpoint_file, 'w') as f:
                json.dump(checkpoint, f, indent=2)

            progress_pct = (last_processed + 1) / self.target_transactions * 100
            self.logger.info(f"Checkpoint saved: {last_processed+1:,}/{self.target_transactions:,} ({progress_pct:.2f}%)")

        except Exception as e:
            self.error_logger.error(f"Failed to save checkpoint: {str(e)}")

    def run_sandwich_20k_deployment(self):
        self.logger.info("Starting Qwen2.5 20K Sandwich Attack Deployment")
        self.logger.info("=" * 75)

        # Load dataset
        try:
            self.logger.info(f"Loading sandwich dataset...")
            df = pd.read_csv(self.sandwich_path)
            total_available = len(df)
            self.logger.info(f"Total available transactions: {total_available:,}")

            # Sample 20K transactions
            if total_available < self.target_transactions:
                self.logger.warning(f"Only {total_available:,} transactions available, using all")
                sample_df = df
            else:
                self.logger.info(f"Sampling {self.target_transactions:,} transactions...")
                sample_df = df.sample(n=self.target_transactions, random_state=2024)
                sample_df = sample_df.reset_index(drop=True)

            actual_transactions = len(sample_df)
            self.logger.info(f"Processing {actual_transactions:,} sandwich attack transactions")

        except Exception as e:
            self.error_logger.error(f"Failed to load dataset: {str(e)}")
            return False

        # Check for existing checkpoint
        start_idx = 0
        results = []

        if os.path.exists(self.checkpoint_file):
            try:
                with open(self.checkpoint_file, 'r') as f:
                    checkpoint = json.load(f)
                start_idx = checkpoint['last_processed'] + 1
                self.logger.info(f"Resuming from checkpoint: transaction {start_idx:,}")

                if os.path.exists(self.results_file):
                    existing_results = pd.read_csv(self.results_file)
                    results = existing_results.to_dict('records')

            except Exception as e:
                self.error_logger.error(f"Failed to load checkpoint: {str(e)}")
                start_idx = 0
                results = []

        # Process transactions
        start_time = time.time()
        last_checkpoint = start_time

        self.logger.info(f"Starting analysis from transaction {start_idx:,}...")

        for idx in range(start_idx, actual_transactions):
            try:
                row = sample_df.iloc[idx]

                # Parse transaction
                transaction_data = self.parse_sandwich_transaction(row)
                if transaction_data is None:
                    continue

                # Analyze with Qwen2.5
                classification = self.analyze_transaction(transaction_data)

                # Store result
                result = {
                    'transaction_id': transaction_data['transaction_id'],
                    'mev_type': 'sandwich',
                    'model': 'qwen2.5-7b',
                    'scale': '20k',
                    'llm_classification': classification,
                    'profit_eth': transaction_data.get('profit_eth', 0),
                    'cost_eth': transaction_data.get('cost_eth', 0),
                    'gain_eth': transaction_data.get('gain_eth', 0),
                    'exchange_name': transaction_data.get('exchange_name', ''),
                    'token_name': transaction_data.get('token_name', ''),
                    'bot_address': transaction_data.get('bot_address', ''),
                    'flashbots_bundle': transaction_data.get('flashbots_bundle', False),
                    'block_number': transaction_data.get('block_number', 0),
                    'processing_timestamp': datetime.now().isoformat(),
                    'description': transaction_data['description']
                }
                results.append(result)

                # Progress logging
                current_time = time.time()
                if idx % 500 == 0 or current_time - last_checkpoint > 600:
                    elapsed = current_time - start_time
                    progress = (idx + 1) / actual_transactions * 100
                    transactions_per_sec = (idx + 1) / elapsed if elapsed > 0 else 0
                    eta = (actual_transactions - idx - 1) / transactions_per_sec if transactions_per_sec > 0 else 0

                    unknown_count = len([r for r in results if r['llm_classification'] == 'UNKNOWN'])
                    unknown_rate = unknown_count / len(results) * 100 if results else 0

                    self.logger.info(f"Progress: {idx+1:,}/{actual_transactions:,} ({progress:.2f}%) - "
                                   f"{transactions_per_sec:.2f} tx/s - ETA: {eta/3600:.1f}h - "
                                   f"Unknown: {unknown_count} ({unknown_rate:.3f}%)")

                    # Performance logging
                    self.perf_logger.info(f"qwen2.5,sandwich,20k,{idx+1},{progress:.2f},{transactions_per_sec:.2f},{eta/3600:.1f},{unknown_count},{unknown_rate:.3f}")

                    last_checkpoint = current_time

                # Checkpoint saving
                if (idx + 1) % self.checkpoint_interval == 0:
                    self.save_checkpoint(results, idx)
                    gc.collect()

            except Exception as e:
                self.error_logger.error(f"Failed to process transaction {idx}: {str(e)}")
                continue

        # Final save
        self.save_checkpoint(results, actual_transactions - 1)

        # Analysis summary
        total_time = time.time() - start_time
        self.analyze_sandwich_20k_results(results, total_time)

        return True

    def analyze_sandwich_20k_results(self, results, total_time):
        self.logger.info("\nQWEN2.5 20K SANDWICH ATTACK DEPLOYMENT RESULTS")
        self.logger.info("=" * 75)

        results_df = pd.DataFrame(results)
        total = len(results)

        # Processing stats
        self.logger.info(f"Processing Statistics:")
        self.logger.info(f"  Total time: {total_time/3600:.2f} hours ({total_time/86400:.1f} days)")
        self.logger.info(f"  Transactions processed: {total:,}")
        self.logger.info(f"  Average speed: {total/total_time:.2f} tx/s")

        # Classification results
        classification_counts = results_df['llm_classification'].value_counts()
        self.logger.info(f"\nClassification Results:")
        for classification, count in classification_counts.items():
            percentage = count / total * 100
            self.logger.info(f"  {classification}: {count:,} ({percentage:.2f}%)")

        # Unknown patterns analysis
        unknown_count = len(results_df[results_df['llm_classification'] == 'UNKNOWN'])
        unknown_rate = unknown_count / total * 100

        self.logger.info(f"\nUnknown Pattern Discovery:")
        self.logger.info(f"  Unknown patterns found: {unknown_count:,}")
        self.logger.info(f"  Unknown detection rate: {unknown_rate:.3f}%")

        # Compare with Mistral baseline
        self.logger.info(f"\nComparison with Mistral 20K:")
        self.logger.info(f"  Mistral 20K: 168 unknowns (0.840%)")
        self.logger.info(f"  Qwen 20K: {unknown_count} unknowns ({unknown_rate:.3f}%)")
        if unknown_rate > 0:
            self.logger.info(f"  Ratio: {unknown_rate/0.840:.2f}x Mistral rate")

        if unknown_count > 0:
            # Analyze unknown patterns
            unknown_df = results_df[results_df['llm_classification'] == 'UNKNOWN']
            avg_profit = unknown_df['profit_eth'].mean()
            median_profit = unknown_df['profit_eth'].median()

            self.logger.info(f"\nUnknown Sandwich Pattern Characteristics:")
            self.logger.info(f"  Average profit: {avg_profit:.6f} ETH")
            self.logger.info(f"  Median profit: {median_profit:.6f} ETH")

            # Exchange analysis
            exchange_counts = unknown_df['exchange_name'].value_counts()
            self.logger.info(f"\nUnknown Patterns by Exchange:")
            for exchange, count in exchange_counts.head(5).items():
                self.logger.info(f"  {exchange}: {count} patterns")

            # Token analysis
            token_counts = unknown_df['token_name'].value_counts()
            self.logger.info(f"\nUnknown Patterns by Token:")
            for token, count in token_counts.head(5).items():
                self.logger.info(f"  {token}: {count} patterns")

        self.logger.info(f"\nResults saved to: {self.results_file}")
        self.logger.info(f"Unknown patterns saved to: {self.unknowns_file}")
        self.logger.info(f"Qwen2.5 20K sandwich deployment completed successfully!")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Qwen2.5 20K Sandwich Attack MEV Detection')
    parser.add_argument('--test', action='store_true', help='Run test mode (2K transactions)')
    parser.add_argument('--full', action='store_true', help='Run full 20K deployment')
    args = parser.parse_args()

    if not args.test and not args.full:
        print("Please specify --test or --full")
        print("--test: Process 2,000 transactions for validation")
        print("--full: Process 20,000 transactions for comprehensive research")
        return

    deployment = QwenSandwichDeployment20K()

    # Adjust for test mode
    if args.test:
        deployment.target_transactions = 2000
        deployment.checkpoint_interval = 500
        deployment.logger.info("Test mode: Processing 2,000 transactions")

    deployment.log_system_info()

    # Load model
    if not deployment.load_model():
        deployment.logger.error("Model loading failed. Aborting.")
        return

    # Run deployment
    success = deployment.run_sandwich_20k_deployment()

    if success:
        if args.test:
            deployment.logger.info("Test completed successfully. Ready for --full deployment.")
        else:
            deployment.logger.info("20K sandwich deployment completed successfully!")
    else:
        deployment.logger.error("Deployment encountered issues.")

if __name__ == "__main__":
    main()
