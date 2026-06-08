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

class Qwen25Arbitrage100K:
    def __init__(self):
        self.model_path = "<PROJECT_ROOT>/Part-2_Unknown_Mev/huggingface_cache/models--Qwen--Qwen2.5-7B-Instruct/snapshots/a09a35458c702b33eeacc393d103063234e8bc28"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = None
        self.model = None

        # Configuration for 100K transactions (matching Mistral)
        self.target_transactions = 100000
        self.batch_size = 50
        self.checkpoint_interval = 1000  # More frequent checkpoints
        self.max_retries = 3
        self.retry_delay = 5

        # GPU optimization for shared server
        self.enable_kv_cache = True  # Key-value cache for faster generation
        self.use_cache = True  # Model caching
        self.num_beams = 1  # Beam search (1 = greedy, matches Mistral behavior)

        # Dataset path
        self.arbitrage_path = '<PROJECT_ROOT>/large/arbitrage_results.csv'

        # Initialize logging
        self.setup_logging()

    def setup_logging(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create logs directory
        log_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Logs/Arbitrage"
        os.makedirs(log_dir, exist_ok=True)

        # Main log file
        log_file = f"{log_dir}/qwen25_arbitrage_100k_{timestamp}.log"

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
        self.perf_log = f"{log_dir}/qwen_performance_100k_{timestamp}.log"
        self.perf_logger = logging.getLogger('performance')
        perf_handler = logging.FileHandler(self.perf_log)
        perf_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.perf_logger.addHandler(perf_handler)
        self.perf_logger.setLevel(logging.INFO)

        # Error log
        self.error_log = f"{log_dir}/qwen_errors_100k_{timestamp}.log"
        self.error_logger = logging.getLogger('errors')
        error_handler = logging.FileHandler(self.error_log)
        error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.error_logger.addHandler(error_handler)
        self.error_logger.setLevel(logging.ERROR)

        # Progress log for monitoring
        self.progress_log = f"{log_dir}/qwen_progress_100k_{timestamp}.log"
        self.progress_logger = logging.getLogger('progress')
        progress_handler = logging.FileHandler(self.progress_log)
        progress_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.progress_logger.addHandler(progress_handler)
        self.progress_logger.setLevel(logging.INFO)

        # Milestone log for major checkpoints
        self.milestone_log = f"{log_dir}/qwen_milestones_100k_{timestamp}.log"
        self.milestone_logger = logging.getLogger('milestones')
        milestone_handler = logging.FileHandler(self.milestone_log)
        milestone_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.milestone_logger.addHandler(milestone_handler)
        self.milestone_logger.setLevel(logging.INFO)

        # Results file
        self.results_file = f"results_qwen25_arbitrage_100k_{timestamp}.csv"
        self.checkpoint_file = f"checkpoint_qwen25_arbitrage_100k_{timestamp}.json"

        self.logger.info(f"Massive 100K Qwen Arbitrage Deployment Initialized")
        self.logger.info(f"Main log: {log_file}")
        self.logger.info(f"Performance log: {self.perf_log}")
        self.logger.info(f"Progress log: {self.progress_log}")
        self.logger.info(f"Milestone log: {self.milestone_log}")
        self.logger.info(f"Error log: {self.error_log}")
        self.logger.info(f"Results file: {self.results_file}")

    def log_system_info(self):
        self.logger.info("SYSTEM INFORMATION")
        self.logger.info("=" * 50)

        # System info
        cpu_count = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        self.logger.info(f"CPU: {cpu_count} cores, {cpu_percent}% usage")
        self.logger.info(f"RAM: {memory.total // (1024**3)}GB total, {memory.percent}% used")

        # GPU info
        if torch.cuda.is_available():
            gpu_count = torch.cuda.device_count()
            self.logger.info(f"GPUs: {gpu_count} available")
            for i in range(gpu_count):
                gpu_memory = torch.cuda.get_device_properties(i).total_memory // (1024**3)
                self.logger.info(f"  GPU {i}: {gpu_memory}GB")

        # Time estimates based on 100K results (2.93 tx/s)
        self.logger.info("\nTIME ESTIMATES (Based on Mistral 100K Performance)")
        self.logger.info("=" * 50)
        estimated_time_2_93_tx_per_sec = self.target_transactions / 2.93 / 3600  # hours
        estimated_time_conservative = self.target_transactions / 2.7 / 3600  # conservative estimate
        estimated_time_optimistic = self.target_transactions / 3.1 / 3600  # optimistic estimate

        self.logger.info(f"Target transactions: {self.target_transactions:,}")
        self.logger.info(f"Based on Mistral 100K performance (2.93 tx/s): {estimated_time_2_93_tx_per_sec:.1f} hours ({estimated_time_2_93_tx_per_sec/24:.1f} days)")
        self.logger.info(f"Conservative estimate (2.7 tx/s): {estimated_time_conservative:.1f} hours ({estimated_time_conservative/24:.1f} days)")
        self.logger.info(f"Optimistic estimate (3.1 tx/s): {estimated_time_optimistic:.1f} hours ({estimated_time_optimistic/24:.1f} days)")
        self.logger.info(f"Expected duration: ~9.5 hours")

        # Expected unknown patterns (matching Mistral baseline)
        self.logger.info(f"\nEXPECTED UNKNOWN PATTERNS:")
        self.logger.info(f"  Mistral 100K baseline: 65 unknown patterns (0.065%)")
        self.logger.info(f"  100K expected: ~650 unknown patterns")
        self.logger.info(f"  Pattern diversity: Unprecedented categories likely")
        self.logger.info(f"  Ultra-rare patterns: Expecting patterns only visible at 100K scale")

        # Milestone tracking
        milestones = [100000, 250000, 500000, 750000, 100000]
        self.logger.info(f"\nMILESTONE TRACKING:")
        for milestone in milestones:
            expected_unknowns = int(milestone * 0.00065)
            eta_hours = milestone / 2.93 / 3600
            self.logger.info(f"  {milestone:,} tx: ~{expected_unknowns} unknowns, ETA: {eta_hours:.1f}h")

    def load_model(self):
        self.logger.info("Loading Qwen2.5-7B model...")
        start_time = time.time()

        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, use_fast=False)
            self.tokenizer.pad_token = self.tokenizer.eos_token

            # Use device_map="auto" for multi-GPU distribution
            # Model is 14GB, individual GPUs are 11GB - multi-GPU required
            # This matches the successful 20K experiment configuration
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

                # Use GPU 0 as default fallback
                gpu_id = 0
                if torch.cuda.is_available():
                    self.logger.info(f"Using GPU {gpu_id}")

                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_path,
                    torch_dtype=torch.float16,
                    device_map={"": f"cuda:{gpu_id}"},
                    trust_remote_code=True
                )
                self.logger.info(f"Model loaded on GPU {gpu_id} successfully")

            load_time = time.time() - start_time
            self.logger.info(f"Model loaded successfully in {load_time:.1f}s")

            # GPU memory usage
            if torch.cuda.is_available():
                total_gpu_memory = 0
                for i in range(torch.cuda.device_count()):
                    allocated = torch.cuda.memory_allocated(i) / (1024**3)
                    total_gpu_memory += allocated
                    self.logger.info(f"GPU {i}: {allocated:.1f}GB allocated")
                self.logger.info(f"Total GPU memory: {total_gpu_memory:.1f}GB")

            return True

        except Exception as e:
            self.error_logger.error(f"Model loading failed: {str(e)}")
            self.error_logger.error(traceback.format_exc())
            return False

    def create_system_prompt(self):
        return """You are an expert blockchain analyst specializing in MEV (Maximal Extractible Value) detection.

Analyze Ethereum transactions and classify them as:
1. KNOWN MEV - Clear, identifiable MEV patterns
2. UNKNOWN MEV - Suspicious patterns you cannot fully categorize
3. NORMAL - Regular transactions without MEV characteristics

KNOWN ARBITRAGE PATTERNS include:
- Standard cross-DEX arbitrage (profitable or unprofitable)
- Multi-hop token swaps for price exploitation
- Common token arbitrage (WETH, USDC, DAI, LINK, APE, etc.)
- Flash loan arbitrage strategies
- Typical Uniswap/Balancer/Curve arbitrage
- Failed arbitrage attempts using standard methods

UNKNOWN ARBITRAGE CRITERIA (be very selective):
- Completely novel cross-protocol mechanisms
- Unusual multi-step strategies with unclear logic
- Complex arbitrage involving obscure or experimental tokens
- Arbitrage patterns that don't match known MEV strategies
- Emerging techniques with non-standard execution flow

IMPORTANT NOTES:
- Profit/loss does NOT indicate unknown patterns
- Token type alone does NOT make a pattern unknown
- Most arbitrage (99%+) should be classified as KNOWN
- Only truly novel or suspicious strategies are UNKNOWN

Respond with ONLY: KNOWN, UNKNOWN, or NORMAL"""

    def parse_arbitrage_transaction(self, row):
        try:
            # Parse transaction JSON
            transaction = json.loads(row['transaction'].replace("'", '"'))

            # Parse swaps for detailed description
            swaps = json.loads(row['swaps'].replace("'", '"'))

            # Create description
            if len(swaps) >= 2:
                in_token = swaps[0]['in_token_name']
                out_token = swaps[-1]['out_token_name']
                num_swaps = len(swaps)
                profit = row.get('profit_eth', 0)
                description = f"Arbitrage ({num_swaps} swaps): {in_token} → {out_token} with {profit:.6f} ETH profit"
            else:
                description = f"Arbitrage transaction with {row.get('profit_eth', 0):.6f} ETH profit"

            # Extract transaction data
            base_data = {
                'transaction_id': f"arbitrage_{row.name}",
                'mev_type': 'arbitrage',
                'is_mev': True,
                'block_number': row['block_number'],
                'block_timestamp': row['block_timestamp'],
                'transaction_hash': transaction.get('hash', ''),
                'from_address': transaction.get('from', ''),
                'to_address': transaction.get('to', ''),
                'gas_used': transaction.get('gas', 0),
                'value_eth': float(transaction.get('value', '0')) / 10**18 if transaction.get('value') != '0' else 0,
                'profit_eth': row.get('profit_eth', 0),
                'cost_eth': row.get('cost_eth', 0),
                'gain_eth': row.get('gain_eth', 0),
                'num_swaps': len(swaps),
                'description': description
            }

            return base_data

        except Exception as e:
            self.error_logger.error(f"Failed to parse arbitrage transaction {row.name}: {str(e)}")
            return None

    def parse_qwen_response(self, response):
        import re

        response = response.strip()
        upper_response = response.upper()

        # Remove <THINK>...</THINK> blocks and special tokens
        while "<THINK>" in upper_response:
            start_idx = upper_response.find("<THINK>")
            end_idx = upper_response.find("</THINK>")
            if start_idx != -1 and end_idx != -1:
                response = response[:start_idx] + response[end_idx + 8:]
                upper_response = response.upper()
            else:
                break

        # Remove common special tokens
        upper_response = upper_response.replace("<|ENDOFTEXT|>", "").strip()

        # Check UNKNOWN first (must check before KNOWN since UNKNOWN contains "KNOWN")
        # Use case-insensitive prefix matching to handle cases like "UNKNOWNTWN", "UNKNOWNArbitrage"
        if upper_response.startswith("UNKNOWN"):
            return "UNKNOWN"

        # Check KNOWN - handle cases like "KNOWNTWN", "KNOWNArbitrage", "KNOWNTOPIC"
        if upper_response.startswith("KNOWN"):
            return "KNOWN"

        # Check NORMAL - handle cases like "NORMALTWN", etc.
        if upper_response.startswith("NORMAL"):
            return "NORMAL"

        # Fallback: Try word boundary matching on first 50 chars for edge cases
        # where response starts with whitespace or punctuation
        first_part = upper_response[:50]
        if re.search(r"\bUNKNOWN\b", first_part):
            return "UNKNOWN"
        if re.search(r"\bKNOWN\b", first_part):
            return "KNOWN"
        if re.search(r"\bNORMAL\b", first_part):
            return "NORMAL"

        # Final fallback: Check entire response
        if "UNKNOWN" in upper_response:
            return "UNKNOWN"
        if "KNOWN" in upper_response:
            return "KNOWN"
        if "NORMAL" in upper_response:
            return "NORMAL"

        return None

    def analyze_transaction(self, transaction_data):
        system_prompt = self.create_system_prompt()

        user_prompt = f"""Arbitrage Transaction Analysis:

Profit: {transaction_data.get('profit_eth', 0):.6f} ETH
Cost: {transaction_data.get('cost_eth', 0):.6f} ETH
Net Gain: {transaction_data.get('gain_eth', 0):.6f} ETH
Number of Swaps: {transaction_data.get('num_swaps', 0)}
Gas Used: {transaction_data.get('gas_used', 0):,}

Description: {transaction_data.get('description', 'No description')}

Block: {transaction_data.get('block_number', 0)}
Timestamp: {transaction_data.get('block_timestamp', 0)}

Classify this arbitrage transaction:"""

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
                    # MATCHING MISTRAL PARAMETERS EXACTLY
                    # GPU optimization: use key-value cache and proper beam search
                    outputs = self.model.generate(
                        **inputs,
                        max_new_tokens=30,
                        temperature=0.3,
                        do_sample=True,
                        pad_token_id=self.tokenizer.eos_token_id,
                        repetition_penalty=1.1,
                        use_cache=self.use_cache,
                        num_beams=self.num_beams
                    )

                response = self.tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
                response = response.strip()

                # Parse response with proper word boundary matching
                classification = self.parse_qwen_response(response)

                if classification:
                    return classification
                else:
                    self.logger.warning(f"Unclear response (attempt {attempt+1}): {response}")
                    if attempt == self.max_retries - 1:
                        return "UNKNOWN"  # Default after all retries

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

            # Save checkpoint
            checkpoint = {
                'last_processed': last_processed,
                'timestamp': datetime.now().isoformat(),
                'total_results': len(results),
                'target_transactions': self.target_transactions
            }
            with open(self.checkpoint_file, 'w') as f:
                json.dump(checkpoint, f, indent=2)

            # Log progress
            progress_pct = (last_processed + 1) / self.target_transactions * 100
            self.progress_logger.info(f"CHECKPOINT: {last_processed+1}/{self.target_transactions} ({progress_pct:.2f}%) - {len(results)} results saved")

            # Check for milestones
            milestones = [10000, 25000, 50000, 75000, 100000]
            for milestone in milestones:
                if last_processed + 1 == milestone:
                    unknown_count = len([r for r in results if r['llm_classification'] == 'UNKNOWN'])
                    elapsed_time = time.time() - self.deployment_start_time
                    self.milestone_logger.info(f"MILESTONE {milestone:,}: {unknown_count} unknowns found in {elapsed_time/3600:.1f} hours")
                    self.logger.info(f"MILESTONE REACHED: {milestone:,} transactions processed!")
                    self.logger.info(f"   Unknown patterns found: {unknown_count}")
                    self.logger.info(f"   Processing time: {elapsed_time/3600:.1f} hours")

        except Exception as e:
            self.error_logger.error(f"Failed to save checkpoint: {str(e)}")

    def run_100k_deployment(self):
        self.logger.info("Starting 100K Qwen Arbitrage Deployment")
        self.logger.info("=" * 60)

        # Load dataset
        try:
            self.logger.info(f"Loading arbitrage dataset...")
            df = pd.read_csv(self.arbitrage_path)
            total_available = len(df)
            self.logger.info(f"Total available transactions: {total_available:,}")

            # Sample 100K transactions using dual-seed strategy for methodology alignment
            if total_available < self.target_transactions:
                self.logger.warning(f"Only {total_available:,} transactions available, using all")
                sample_df = df
            else:
                self.logger.info(f"Sampling {self.target_transactions:,} transactions...")
                self.logger.info(f"  - First 20,000: seed=2000 (matching 20K baseline)")
                self.logger.info(f"  - Additional 80,000: seed=3000 (new transactions)")

                # Sample 20K with seed 2000 (matching 20K baseline for methodology alignment)
                sample_20k = df.sample(n=20000, random_state=2000)

                # Remove sampled transactions and sample 80K more with seed 3000
                remaining_df = df.drop(sample_20k.index)
                sample_80k = remaining_df.sample(n=80000, random_state=3000)

                # Concatenate and reset index
                sample_df = pd.concat([sample_20k, sample_80k], ignore_index=True)
                sample_df = sample_df.reset_index(drop=True)

                self.logger.info(f"Sampling strategy: 20K (seed 2000) + 80K (seed 3000)")

            actual_transactions = len(sample_df)
            self.logger.info(f"Processing {actual_transactions:,} arbitrage transactions")

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
        self.deployment_start_time = time.time()
        start_time = self.deployment_start_time
        last_checkpoint = start_time
        last_progress_log = start_time

        self.logger.info(f"Starting analysis from transaction {start_idx:,}...")

        for idx in range(start_idx, actual_transactions):
            try:
                row = sample_df.iloc[idx]

                # Parse transaction
                transaction_data = self.parse_arbitrage_transaction(row)
                if transaction_data is None:
                    continue

                # Analyze with LLM
                classification = self.analyze_transaction(transaction_data)

                # Store result
                result = {
                    'transaction_id': transaction_data['transaction_id'],
                    'mev_type': 'arbitrage',
                    'llm_classification': classification,
                    'profit_eth': transaction_data.get('profit_eth', 0),
                    'cost_eth': transaction_data.get('cost_eth', 0),
                    'gain_eth': transaction_data.get('gain_eth', 0),
                    'num_swaps': transaction_data.get('num_swaps', 0),
                    'block_number': transaction_data.get('block_number', 0),
                    'processing_timestamp': datetime.now().isoformat(),
                    'description': transaction_data['description'][:200] + "..." if len(transaction_data['description']) > 200 else transaction_data['description']
                }
                results.append(result)

                # Progress logging every 1000 transactions or 10 minutes
                current_time = time.time()
                if idx % 1000 == 0 or current_time - last_progress_log > 600:
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
                    self.perf_logger.info(f"arbitrage,{idx+1},{progress:.2f},{transactions_per_sec:.2f},{eta/3600:.1f}")

                    # Progress logging
                    self.progress_logger.info(f"PROGRESS: {idx+1}/{actual_transactions} ({progress:.1f}%) - "
                                            f"Speed: {transactions_per_sec:.2f} tx/s - "
                                            f"Unknown: {unknown_count} ({unknown_rate:.3f}%) - ETA: {eta/3600:.1f}h")

                    last_progress_log = current_time

                # Checkpoint saving
                if (idx + 1) % self.checkpoint_interval == 0:
                    self.save_checkpoint(results, idx)
                    gc.collect()  # Garbage collection for long deployment

            except Exception as e:
                self.error_logger.error(f"Failed to process transaction {idx}: {str(e)}")
                continue

        # Final save
        self.save_checkpoint(results, actual_transactions - 1)

        # Analysis summary
        total_time = time.time() - start_time
        self.analyze_100k_results(results, total_time)

        return True

    def analyze_100k_results(self, results, total_time):
        self.logger.info("\n100K QWEN ARBITRAGE DEPLOYMENT RESULTS")
        self.logger.info("=" * 60)

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
        unknown_percentage = unknown_count / total * 100

        self.logger.info(f"\nUnknown Pattern Analysis:")
        self.logger.info(f"  Total unknown patterns: {unknown_count:,} ({unknown_percentage:.3f}%)")
        self.logger.info(f"  Mistral 100K baseline: 65 (0.065%)")
        self.logger.info(f"  Expected at 100K scale: ~650 patterns")

        # Comparison with Mistral
        if unknown_count > 0:
            self.logger.info(f"\nComparison with Mistral baseline:")
            ratio = unknown_count / (total * 0.00065) if total > 0 else 0
            self.logger.info(f"  Detection ratio vs baseline: {ratio:.2f}x")

        # Save final summary
        summary = {
            'model': 'Qwen2.5-7B',
            'total_transactions': total,
            'processing_time_hours': total_time / 3600,
            'average_speed_tx_per_sec': total / total_time,
            'unknown_count': unknown_count,
            'unknown_percentage': unknown_percentage,
            'classification_counts': classification_counts.to_dict()
        }

        summary_file = f"summary_qwen_100k_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)

        self.logger.info(f"\nSummary saved to: {summary_file}")
        self.logger.info(f"Results saved to: {self.results_file}")

        return results_df

def main():
    print("=" * 60)
    print("QWEN2.5-7B 100K ARBITRAGE DEPLOYMENT")
    print("Designed to match Mistral experiment methodology")
    print("=" * 60)

    deployment = Qwen25Arbitrage100K()

    # Log system information
    deployment.log_system_info()

    # Load model
    if not deployment.load_model():
        print("Failed to load model. Exiting.")
        return

    # Run deployment
    print("\nStarting 100K transaction deployment...")
    print("This will take approximately ~9.5 hours")
    print("Progress will be logged to files and console")

    success = deployment.run_100k_deployment()

    if success:
        print("\nDeployment completed successfully!")
    else:
        print("\nDeployment encountered errors. Check error logs.")

if __name__ == "__main__":
    main()
