#!/usr/bin/env python3

import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import logging
import json
import os
import sys
import re
from datetime import datetime
import time
import traceback
import psutil
import gc

class QwenSandwich100KTest:
    def __init__(self):
        self.model_id = "Qwen/Qwen2.5-7B-Instruct"
        self.cache_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/huggingface_cache"
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = None
        self.model = None
        self.run_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Configuration - 100K validation test
        self.target_transactions = 100000
        self.batch_size = 100
        self.checkpoint_interval = 5000
        self.max_retries = 3
        self.retry_delay = 5

        # Dataset path
        self.sandwich_path = '<PROJECT_ROOT>/large/sandwich_results.csv'

        # Initialize logging
        self.setup_logging()

    def setup_logging(self):
        timestamp = self.run_id

        # Create logs directory
        log_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Logs/Sandwich"
        os.makedirs(log_dir, exist_ok=True)

        # Main log file
        log_file = f"{log_dir}/qwen_sandwich_100k_test_{timestamp}.log"

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

        # Results files
        results_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Results/Sandwich"
        os.makedirs(results_dir, exist_ok=True)

        self.results_file = f"{results_dir}/qwen_sandwich_100k_test_{timestamp}.csv"
        self.unknowns_file = f"{results_dir}/qwen_sandwich_100k_test_unknowns_{timestamp}.csv"

        # Checkpoint
        checkpoint_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Checkpoints/Sandwich"
        os.makedirs(checkpoint_dir, exist_ok=True)
        self.checkpoint_file = f"{checkpoint_dir}/qwen_sandwich_100k_test_{timestamp}.json"

        self.logger.info("=" * 70)
        self.logger.info("QWEN2.5 SANDWICH 100K VALIDATION TEST")
        self.logger.info("Fixed version aligned with Qwen Arbitrage parameters")
        self.logger.info("=" * 70)
        self.logger.info(f"Run ID: {self.run_id}")
        self.logger.info(f"Results file: {self.results_file}")

    def load_model(self):
        self.logger.info("Loading Qwen2.5-7B-Instruct model...")
        start_time = time.time()

        try:
            # Clear GPU cache
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

            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token

            # Load model with multi-GPU configuration
            self.logger.info("Loading Qwen model...")

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
            self.logger.info(f"Model loaded successfully in {load_time:.1f}s")

            # Log GPU memory
            if torch.cuda.is_available():
                total_gpu_memory = 0
                for i in range(torch.cuda.device_count()):
                    allocated = torch.cuda.memory_allocated(i) / (1024**3)
                    total_gpu_memory += allocated
                    self.logger.info(f"GPU {i}: {allocated:.1f}GB allocated")
                self.logger.info(f"Total GPU memory: {total_gpu_memory:.1f}GB")

            return True

        except Exception as e:
            self.logger.error(f"Model loading failed: {str(e)}")
            self.logger.error(traceback.format_exc())
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
- Failed sandwich attacks that lost money (standard pattern that failed)
- Flashbots/private orderflow execution (common for sandwich bots)

UNKNOWN SANDWICH CRITERIA:
- Advanced victim selection and targeting algorithms
- Coordinated multi-bot sandwich swarms
- Complex multi-victim simultaneous sandwiching
- Non-standard attack timing (delayed front/back-running)
- MEV protection bypass / bundle manipulation beyond standard private orderflow
- Sandwich attacks spanning multiple blocks
- Victim transaction prediction and pre-positioning
- Cross-exchange sandwich coordination (Uniswap + SushiSwap)
- Gas price manipulation for sandwich optimization
- Sandwich attacks targeting specific user behaviors
- Novel victim targeting strategies

IMPORTANT: Do NOT classify as UNKNOWN just because the attack failed or lost money.
A failed standard sandwich is KNOWN. Only flag truly suspicious or unusual patterns.

NORMAL TRANSACTIONS:
- Regular token swaps without exploitation
- Standard DEX interactions
- Simple transfers

Respond with ONLY: KNOWN, UNKNOWN, or NORMAL"""

    def parse_classification(self, response: str) -> str:
        if response is None:
            return None

        # Strip thinking blocks if present
        cleaned = response
        upper = cleaned.upper()
        while "<THINK>" in upper:
            start_idx = upper.find("<THINK>")
            end_idx = upper.find("</THINK>")
            if start_idx != -1 and end_idx != -1:
                cleaned = cleaned[:start_idx] + cleaned[end_idx + len("</THINK>"):]
                upper = cleaned.upper()
            else:
                break

        cleaned = cleaned.replace("<|endoftext|>", "").replace("<|ENDOFTEXT|>", "")
        cleaned = cleaned.strip()
        upper = cleaned.upper()

        # Direct match
        if upper in {"KNOWN", "UNKNOWN", "NORMAL"}:
            return upper

        # Simple substring matching - Mistral style
        # Check KNOWN first (before UNKNOWN since UNKNOWN contains KNOWN)
        # Important: Check UNKNOWN before KNOWN to avoid false positives
        if "UNKNOWN" in upper:
            return "UNKNOWN"
        if "KNOWN" in upper:
            return "KNOWN"
        if "NORMAL" in upper:
            return "NORMAL"

        # Couldn't parse - return None
        return None

    def parse_sandwich_transaction(self, row):
        try:
            # Parse transactions
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

            token_name = row.get('token_name', 'Unknown Token')
            exchange_name = row.get('exchange_name', 'Unknown Exchange')
            profit = row.get('profit_eth', 0)

            description = f"Sandwich Attack on {exchange_name}: {token_name} with {profit:.6f} ETH profit"

            base_data = {
                'transaction_id': f"qwen_sandwich_100k_{row.name}",
                'mev_type': 'sandwich',
                'model': 'qwen2.5-7b',
                'scale': '100k_test',
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
                'first_tx_value': float(first_tx.get('value', '0')) / 10**18 if first_tx.get('value') != '0' else 0,
                'whale_tx_value': float(whale_tx.get('value', '0')) / 10**18 if whale_tx.get('value') != '0' else 0,
                'second_tx_value': float(second_tx.get('value', '0')) / 10**18 if second_tx.get('value') != '0' else 0,
                'flashbots_bundle': row.get('flashbots_bundle', False),
                'same_sender': row.get('same_sender', False),
                'same_receiver': row.get('same_receiver', False),
                'description': description
            }

            return base_data

        except Exception as e:
            self.logger.error(f"Failed to parse transaction {row.name}: {str(e)}")
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
- Front-running TX: {transaction_data.get('first_tx_value', 0):.6f} ETH value, Gas {transaction_data.get('first_tx_gas', 0):,}
- Victim TX: {transaction_data.get('whale_tx_value', 0):.6f} ETH value, Gas {transaction_data.get('whale_tx_gas', 0):,}
- Back-running TX: {transaction_data.get('second_tx_value', 0):.6f} ETH value, Gas {transaction_data.get('second_tx_gas', 0):,}

Attack Properties:
- Flashbots Bundle: {transaction_data.get('flashbots_bundle', False)}
- Same Sender: {transaction_data.get('same_sender', False)}
- Same Receiver: {transaction_data.get('same_receiver', False)}

Block: {transaction_data.get('block_number', 0)}

Classify this sandwich attack transaction:"""

        # FIX 1: Use apply_chat_template (correct for Qwen)
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
                        max_new_tokens=15,        # FIX 2: 15 instead of 10
                        temperature=0.3,           # FIX 3: 0.3 instead of 0.05
                        do_sample=True,
                        pad_token_id=self.tokenizer.eos_token_id,
                        repetition_penalty=1.1
                    )

                response = self.tokenizer.decode(
                    outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
                )
                parsed = self.parse_classification(response)

                # Default to KNOWN for unparseable responses (conservative - avoids inflating UNKNOWN)
                if parsed is None:
                    return "KNOWN"

                return parsed

            except Exception as e:
                self.logger.error(f"Analysis attempt {attempt+1} failed: {str(e)}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    return "ERROR"

        return "ERROR"

    def save_checkpoint(self, results, last_processed):
        try:
            results_df = pd.DataFrame(results)
            results_df.to_csv(self.results_file, index=False)

            unknown_results = [r for r in results if r.get('llm_classification') == 'UNKNOWN']
            if unknown_results:
                unknown_df = pd.DataFrame(unknown_results)
                unknown_df.to_csv(self.unknowns_file, index=False)

            checkpoint = {
                'model': 'qwen2.5-7b',
                'scale': '100k_test',
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
            self.logger.error(f"Failed to save checkpoint: {str(e)}")

    def run_test(self):
        self.logger.info("Starting Qwen2.5 Sandwich 100K Validation Test")
        self.logger.info("=" * 70)

        # Load dataset
        try:
            self.logger.info(f"Loading sandwich dataset...")
            df = pd.read_csv(self.sandwich_path)
            total_available = len(df)
            self.logger.info(f"Total available transactions: {total_available:,}")

            # Sample 100K transactions
            self.logger.info(f"Sampling {self.target_transactions:,} transactions...")
            sample_df = df.sample(n=self.target_transactions, random_state=100000)
            sample_df = sample_df.reset_index(drop=True)

            self.logger.info(f"Processing {len(sample_df):,} transactions")

        except Exception as e:
            self.logger.error(f"Failed to load dataset: {str(e)}")
            return False

        # Process transactions
        results = []
        start_time = time.time()

        self.logger.info("Starting transaction analysis...")

        for idx in range(len(sample_df)):
            try:
                row = sample_df.iloc[idx]
                transaction_data = self.parse_sandwich_transaction(row)
                if transaction_data is None:
                    continue

                classification = self.analyze_transaction(transaction_data)

                result = {
                    'transaction_id': transaction_data['transaction_id'],
                    'mev_type': 'sandwich',
                    'model': 'qwen2.5-7b',
                    'scale': '100k_test',
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
                if (idx + 1) % 500 == 0:
                    elapsed = time.time() - start_time
                    progress = (idx + 1) / len(sample_df) * 100
                    tx_per_sec = (idx + 1) / elapsed if elapsed > 0 else 0
                    eta = (len(sample_df) - idx - 1) / tx_per_sec if tx_per_sec > 0 else 0

                    unknown_count = len([r for r in results if r['llm_classification'] == 'UNKNOWN'])
                    unknown_rate = unknown_count / len(results) * 100 if results else 0

                    self.logger.info(f"Progress: {idx+1:,}/{len(sample_df):,} ({progress:.1f}%) - "
                                   f"{tx_per_sec:.2f} tx/s - ETA: {eta/60:.1f}m - "
                                   f"Unknown: {unknown_count} ({unknown_rate:.3f}%)")

                # Checkpoint
                if (idx + 1) % self.checkpoint_interval == 0:
                    self.save_checkpoint(results, idx)
                    gc.collect()
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()

            except Exception as e:
                self.logger.error(f"Failed to process transaction {idx}: {str(e)}")
                continue

        # Final save
        self.save_checkpoint(results, len(sample_df) - 1)

        # Analysis
        total_time = time.time() - start_time
        self.analyze_results(results, total_time)

        return True

    def analyze_results(self, results, total_time):
        self.logger.info("\n" + "=" * 70)
        self.logger.info("QWEN2.5 SANDWICH 100K TEST RESULTS")
        self.logger.info("=" * 70)

        results_df = pd.DataFrame(results)
        total = len(results)

        self.logger.info(f"Processing Statistics:")
        self.logger.info(f"  Total time: {total_time/60:.1f} minutes")
        self.logger.info(f"  Transactions processed: {total:,}")
        self.logger.info(f"  Average speed: {total/total_time:.2f} tx/s")

        # Classification counts
        classification_counts = results_df['llm_classification'].value_counts()
        self.logger.info(f"\nClassification Results:")
        for classification, count in classification_counts.items():
            percentage = count / total * 100
            self.logger.info(f"  {classification}: {count:,} ({percentage:.3f}%)")

        # Unknown analysis
        unknown_count = len(results_df[results_df['llm_classification'] == 'UNKNOWN'])
        unknown_rate = unknown_count / total * 100

        self.logger.info(f"\nUnknown Pattern Analysis:")
        self.logger.info(f"  Unknown patterns found: {unknown_count:,}")
        self.logger.info(f"  Unknown detection rate: {unknown_rate:.3f}%")

        # Expected vs actual comparison
        self.logger.info(f"\nValidation Against Baselines:")
        self.logger.info(f"  Mistral 1M baseline: 289 unknowns (0.029%)")
        self.logger.info(f"  Qwen Arbitrage 1M: ~1,400 unknowns (0.14%)")
        self.logger.info(f"  This test (100K): {unknown_count} unknowns ({unknown_rate:.3f}%)")

        # Scaling projection
        projected_1m = int(unknown_count * 10)  # 100K -> 1M is 50x
        self.logger.info(f"\nProjection for 1M scale:")
        self.logger.info(f"  Projected unknowns at 1M: ~{projected_1m:,}")
        self.logger.info(f"  Projected rate: ~{unknown_rate:.3f}%")

        # Assessment
        self.logger.info(f"\nASSESSMENT:")
        if 0.01 <= unknown_rate <= 0.5:
            self.logger.info(f"  PASS: Unknown rate is within acceptable range (0.01-0.5%)")
            self.logger.info(f"  Recommendation: Proceed with full 1M deployment")
        elif unknown_rate < 0.01:
            self.logger.info(f"  WARNING: Unknown rate may be too low")
            self.logger.info(f"  Recommendation: Review prompt and parameters")
        else:
            self.logger.info(f"  WARNING: Unknown rate may be too high")
            self.logger.info(f"  Recommendation: Tighten unknown criteria")

        self.logger.info(f"\nResults saved to: {self.results_file}")
        self.logger.info(f"Unknown patterns saved to: {self.unknowns_file}")

def main():
    print("=" * 70)
    print("QWEN2.5 SANDWICH 100K VALIDATION TEST")
    print("Fixed version aligned with Qwen Arbitrage parameters")
    print("=" * 70)

    test = QwenSandwich100KTest()

    # Load model
    if not test.load_model():
        print("Model loading failed. Aborting.")
        return

    # Run test
    success = test.run_test()

    if success:
        print("\n100K validation test completed successfully!")
    else:
        print("\nTest encountered issues.")

if __name__ == "__main__":
    main()
