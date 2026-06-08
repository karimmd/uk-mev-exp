#!/usr/bin/env python3

import pandas as pd
import requests
import time
import json
from datetime import datetime
from typing import Dict, List, Optional
import os

class EtherscanValidator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.etherscan.io/v2/api"  # V2 API
        self.chain_id = 1  # Ethereum mainnet
        self.rate_limit_delay = 0.2  # 5 calls per second (free tier)
        self.cache = {}  # Cache API responses

    def get_transaction(self, tx_hash: str) -> Optional[Dict]:
        if not tx_hash or tx_hash == '':
            return None

        # Check cache
        if tx_hash in self.cache:
            return self.cache[tx_hash]

        params = {
            'chainid': self.chain_id,
            'module': 'proxy',
            'action': 'eth_getTransactionByHash',
            'txhash': tx_hash,
            'apikey': self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            time.sleep(self.rate_limit_delay)  # Rate limiting

            if response.status_code == 200:
                data = response.json()
                if data.get('result'):
                    self.cache[tx_hash] = data['result']
                    return data['result']
            return None
        except Exception as e:
            print(f"Error fetching tx {tx_hash[:10]}...: {str(e)}")
            return None

    def get_transaction_receipt(self, tx_hash: str) -> Optional[Dict]:
        if not tx_hash or tx_hash == '':
            return None

        cache_key = f"receipt_{tx_hash}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        params = {
            'chainid': self.chain_id,
            'module': 'proxy',
            'action': 'eth_getTransactionReceipt',
            'txhash': tx_hash,
            'apikey': self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            time.sleep(self.rate_limit_delay)

            if response.status_code == 200:
                data = response.json()
                if data.get('result'):
                    self.cache[cache_key] = data['result']
                    return data['result']
            return None
        except Exception as e:
            print(f"Error fetching receipt {tx_hash[:10]}...: {str(e)}")
            return None

    def get_block(self, block_number: int) -> Optional[Dict]:
        cache_key = f"block_{block_number}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        params = {
            'chainid': self.chain_id,
            'module': 'proxy',
            'action': 'eth_getBlockByNumber',
            'tag': hex(block_number),
            'boolean': 'true',
            'apikey': self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            time.sleep(self.rate_limit_delay)

            if response.status_code == 200:
                data = response.json()
                if data.get('result'):
                    self.cache[cache_key] = data['result']
                    return data['result']
            return None
        except Exception as e:
            print(f"Error fetching block {block_number}: {str(e)}")
            return None

    def validate_sandwich(self, row: pd.Series) -> Dict:
        result = {
            'verified_on_etherscan': 'NO',
            'first_tx_status': 'NOT_FOUND',
            'whale_tx_status': 'NOT_FOUND',
            'second_tx_status': 'NOT_FOUND',
            'auto_pattern_category': 'unknown',
            'confidence': 'LOW',
            'analysis_notes': []
        }

        # Fetch all 3 transactions
        first_tx = self.get_transaction(row['first_tx_hash'])
        whale_tx = self.get_transaction(row['whale_tx_hash'])
        second_tx = self.get_transaction(row['second_tx_hash'])

        # Verify existence
        txs_found = sum([first_tx is not None, whale_tx is not None, second_tx is not None])

        if txs_found == 3:
            result['verified_on_etherscan'] = 'YES'
        elif txs_found >= 2:
            result['verified_on_etherscan'] = 'PARTIAL'
            result['analysis_notes'].append(f"Only {txs_found}/3 transactions found")
        else:
            result['verified_on_etherscan'] = 'NO'
            result['analysis_notes'].append("Transactions not found on Etherscan")
            return result

        # Get transaction receipts for status
        if first_tx:
            first_receipt = self.get_transaction_receipt(row['first_tx_hash'])
            if first_receipt and isinstance(first_receipt, dict):
                status = int(first_receipt.get('status', '0x0'), 16)
                result['first_tx_status'] = 'SUCCESS' if status == 1 else 'FAILED'

        if whale_tx:
            whale_receipt = self.get_transaction_receipt(row['whale_tx_hash'])
            if whale_receipt and isinstance(whale_receipt, dict):
                status = int(whale_receipt.get('status', '0x0'), 16)
                result['whale_tx_status'] = 'SUCCESS' if status == 1 else 'FAILED'

        if second_tx:
            second_receipt = self.get_transaction_receipt(row['second_tx_hash'])
            if second_receipt and isinstance(second_receipt, dict):
                status = int(second_receipt.get('status', '0x0'), 16)
                result['second_tx_status'] = 'SUCCESS' if status == 1 else 'FAILED'

        # Automated pattern analysis
        result = self.analyze_pattern(row, first_tx, whale_tx, second_tx, result)

        return result

    def analyze_pattern(self, row: pd.Series, first_tx: Dict, whale_tx: Dict,
                       second_tx: Dict, result: Dict) -> Dict:
        notes = result['analysis_notes']

        # Check if all transactions in same block
        if (first_tx and isinstance(first_tx, dict) and
            whale_tx and isinstance(whale_tx, dict) and
            second_tx and isinstance(second_tx, dict)):
            first_block = int(first_tx.get('blockNumber', '0x0'), 16)
            whale_block = int(whale_tx.get('blockNumber', '0x0'), 16)
            second_block = int(second_tx.get('blockNumber', '0x0'), 16)

            if first_block == whale_block == second_block:
                notes.append(f"All 3 txs in same block {first_block}")
            else:
                # Multi-block sandwich!
                result['auto_pattern_category'] = 'multi_block'
                result['confidence'] = 'HIGH'
                notes.append(f"Multi-block: first={first_block}, whale={whale_block}, second={second_block}")
                return result

        # Check for failed transactions
        all_success = (result['first_tx_status'] == 'SUCCESS' and
                      result['whale_tx_status'] == 'SUCCESS' and
                      result['second_tx_status'] == 'SUCCESS')

        if not all_success:
            notes.append(f"Failed txs: first={result['first_tx_status']}, "
                        f"whale={result['whale_tx_status']}, second={result['second_tx_status']}")

        # Check profit vs success
        profit = row.get('profit_eth', 0)
        if profit <= 0 and all_success:
            notes.append(f"Loss-making ({profit:.4f} ETH) despite all txs successful")
        elif profit > 0 and not all_success:
            notes.append(f"Profitable ({profit:.4f} ETH) despite failed txs - unusual")

        # Check Flashbots
        if row.get('flashbots_bundle', False):
            notes.append("Uses Flashbots bundle")

            # High-profit Flashbots might be advanced
            if profit > 0.1:
                result['confidence'] = 'MEDIUM'
                notes.append(f"High-profit Flashbots sandwich ({profit:.4f} ETH)")

        # Check for multiple exchanges (would need additional data)
        # For now, mark unknown exchanges as potentially cross-exchange
        exchange = row.get('exchange_name', '')
        if exchange not in ['Uniswap V2', 'Uniswap V3', 'SushiSwap']:
            notes.append(f"Non-standard exchange: {exchange}")
            result['confidence'] = 'MEDIUM'

        # Check transaction order within block
        if first_tx and whale_tx and second_tx:
            try:
                first_idx = int(first_tx.get('transactionIndex', '0x0'), 16)
                whale_idx = int(whale_tx.get('transactionIndex', '0x0'), 16)
                second_idx = int(second_tx.get('transactionIndex', '0x0'), 16)

                if first_idx < whale_idx < second_idx:
                    notes.append(f"Standard order: {first_idx} → {whale_idx} → {second_idx}")
                else:
                    # Non-standard ordering!
                    result['auto_pattern_category'] = 'non_standard_timing'
                    result['confidence'] = 'HIGH'
                    notes.append(f"NON-STANDARD ORDER: {first_idx} → {whale_idx} → {second_idx}")
            except:
                pass

        # Check bot address frequency (would need to count across dataset)
        bot = row.get('bot_address', '')
        if bot and isinstance(bot, str):
            notes.append(f"Bot: {bot[:10]}...")
        else:
            notes.append(f"Bot: N/A")

        # If no specific pattern detected, check if it's likely false positive
        if result['auto_pattern_category'] == 'unknown':
            # Standard sandwich with Flashbots on Uniswap V2 = likely false positive
            if (exchange == 'Uniswap V2' and
                row.get('flashbots_bundle', False) and
                -0.1 < profit < 0.1 and
                all_success):
                result['auto_pattern_category'] = 'false_positive'
                result['confidence'] = 'MEDIUM'
                notes.append("Likely false positive: standard Flashbots sandwich on Uniswap V2")

        result['analysis_notes'] = ' | '.join(notes)
        return result

    def validate_dataset(self, input_csv: str, output_csv: str,
                        sample_size: Optional[int] = None):
        print("="*70)
        print("ETHERSCAN AUTOMATED VALIDATION")
        print("="*70)

        # Load data
        df = pd.read_csv(input_csv)
        print(f"\nLoaded {len(df)} unknown transactions")

        if sample_size:
            df = df.head(sample_size)
            print(f"Validating sample of {len(df)} transactions")

        # Validate each transaction
        results = []
        start_time = time.time()
        cache_file = output_csv.replace('.csv', '_cache.json')

        for idx, row in df.iterrows():
            if (idx + 1) % 10 == 0:
                elapsed = time.time() - start_time
                rate = (idx + 1) / elapsed if elapsed > 0 else 0
                eta = (len(df) - idx - 1) / rate if rate > 0 else 0
                print(f"Progress: {idx+1}/{len(df)} ({(idx+1)/len(df)*100:.1f}%) - "
                      f"{rate:.2f} tx/s - ETA: {eta/60:.1f}m")

            # Validate
            validation = self.validate_sandwich(row)

            # Combine original row with validation results
            result_row = row.to_dict()
            result_row.update(validation)
            results.append(result_row)

            # Periodic checkpoint saves (every 100 transactions)
            if (idx + 1) % 100 == 0:
                # Save intermediate results
                temp_df = pd.DataFrame(results)
                temp_df.to_csv(output_csv, index=False)
                # Save cache
                self.save_cache(cache_file)
                print(f"  Checkpoint saved ({idx+1} transactions)")

        # Create results dataframe
        results_df = pd.DataFrame(results)

        # Save results
        results_df.to_csv(output_csv, index=False)

        total_time = time.time() - start_time
        print(f"\n{'='*70}")
        print(f"VALIDATION COMPLETE")
        print(f"{'='*70}")
        print(f"Total time: {total_time/60:.1f} minutes")
        print(f"Transactions validated: {len(results_df)}")
        print(f"Results saved to: {output_csv}")

        # Generate summary
        self.generate_summary(results_df)

        return results_df

    def generate_summary(self, df: pd.DataFrame):
        print(f"\n{'='*70}")
        print("VALIDATION SUMMARY")
        print(f"{'='*70}")

        # Verification rate
        verified = df[df['verified_on_etherscan'] == 'YES']
        partial = df[df['verified_on_etherscan'] == 'PARTIAL']
        not_found = df[df['verified_on_etherscan'] == 'NO']

        print(f"\nTransaction Verification:")
        print(f"  Verified: {len(verified)} ({len(verified)/len(df)*100:.1f}%)")
        print(f"   Partial: {len(partial)} ({len(partial)/len(df)*100:.1f}%)")
        print(f"  Not Found: {len(not_found)} ({len(not_found)/len(df)*100:.1f}%)")

        # Transaction status
        verified_df = df[df['verified_on_etherscan'].isin(['YES', 'PARTIAL'])]
        if len(verified_df) > 0:
            print(f"\nTransaction Status (for verified):")
            first_success = sum(verified_df['first_tx_status'] == 'SUCCESS')
            whale_success = sum(verified_df['whale_tx_status'] == 'SUCCESS')
            second_success = sum(verified_df['second_tx_status'] == 'SUCCESS')

            print(f"  First TX success: {first_success}/{len(verified_df)} ({first_success/len(verified_df)*100:.1f}%)")
            print(f"  Whale TX success: {whale_success}/{len(verified_df)} ({whale_success/len(verified_df)*100:.1f}%)")
            print(f"  Second TX success: {second_success}/{len(verified_df)} ({second_success/len(verified_df)*100:.1f}%)")

        # Auto-categorization
        if 'auto_pattern_category' in df.columns:
            print(f"\nAutomated Pattern Categories:")
            categories = df['auto_pattern_category'].value_counts()
            for category, count in categories.items():
                print(f"  {category}: {count} ({count/len(df)*100:.1f}%)")

        # Confidence distribution
        if 'confidence' in df.columns:
            print(f"\nConfidence Distribution:")
            confidence = df['confidence'].value_counts()
            for conf, count in confidence.items():
                print(f"  {conf}: {count} ({count/len(df)*100:.1f}%)")

    def save_cache(self, cache_file: str):
        with open(cache_file, 'w') as f:
            json.dump(self.cache, f, indent=2)
        print(f"Cache saved to: {cache_file}")

    def load_cache(self, cache_file: str):
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                self.cache = json.load(f)
            print(f"Loaded {len(self.cache)} cached responses")


def main():
    import sys

    if len(sys.argv) < 4:
        print("Usage: python etherscan_validator.py <input_csv> <output_csv> <api_key> [sample_size]")
        print("\nExample:")
        print("  python etherscan_validator.py \\")
        print("    qwen_sandwich_1m_unknowns_with_hashes.csv \\")
        print("    qwen_sandwich_1m_validated.csv \\")
        print("    YOUR_ETHERSCAN_API_KEY \\")
        print("    100  # Optional: validate only 100 transactions for testing")
        return

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    api_key = sys.argv[3]
    sample_size = int(sys.argv[4]) if len(sys.argv) > 4 else None

    # Initialize validator
    validator = EtherscanValidator(api_key)

    # Load cache if exists
    cache_file = output_csv.replace('.csv', '_cache.json')
    if os.path.exists(cache_file):
        validator.load_cache(cache_file)

    # Run validation
    results_df = validator.validate_dataset(input_csv, output_csv, sample_size)

    # Save cache
    validator.save_cache(cache_file)

    print(f"\nValidation complete!")
    print(f"Results: {output_csv}")
    print(f"Cache: {cache_file}")


if __name__ == "__main__":
    main()
