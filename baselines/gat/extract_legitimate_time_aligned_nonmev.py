#!/usr/bin/env python3

import os
import sys
import pandas as pd
import numpy as np
import time
import json
import subprocess
import logging
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import argparse
import random

# Configuration
ETHERSCAN_API_KEY = "<ETHERSCAN_API_KEY>"
ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"
USE_PROXYCHAINS = True
RATE_LIMIT_DELAY = 0.6  # Conservative 600ms between requests
MAX_WORKERS = 2  # Conservative for stability

# Target time periods based on MEV data analysis
JUNE_2020_BLOCKS = {
    'start': 10200000,
    'end': 10500000,
    'description': 'June 2020 (Arbitrage/Sandwich period)'
}

AUGUST_2021_BLOCKS = {
    'start': 13000000,
    'end': 13100000, 
    'description': 'August 2021 (Liquidation period)'
}

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Thread-safe counters
extraction_lock = Lock()
total_extracted = 0
total_valid = 0
total_blocks_processed = 0

def check_proxychains():
    try:
        result = subprocess.run(['which', 'proxychains4'], capture_output=True, text=True)
        return result.returncode == 0
    except:
        return False

def proxychains_request(url, params=None, timeout=30, max_retries=3):
    if not USE_PROXYCHAINS or not check_proxychains():
        # Fallback to direct requests
        try:
            import requests
            response = requests.get(url, params=params, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {'error': f'Direct request failed: {str(e)}'}
    
    # Build curl command with proxychains
    cmd = ['proxychains4', '-q', 'curl', '-s', '--connect-timeout', str(timeout)]
    
    # Add URL with parameters
    if params:
        param_str = '&'.join([f"{k}={v}" for k, v in params.items()])
        full_url = f"{url}?{param_str}"
    else:
        full_url = url
    
    cmd.append(full_url)
    
    for attempt in range(max_retries):
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                timeout=timeout + 10
            )
            
            if result.returncode == 0 and result.stdout.strip():
                try:
                    return json.loads(result.stdout)
                except json.JSONDecodeError:
                    continue
            else:
                continue
                
        except subprocess.TimeoutExpired:
            continue
        except Exception:
            continue
        
        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)  # Exponential backoff
    
    return {'error': f'All {max_retries} attempts failed'}

def get_block_transactions(block_number):
    global total_blocks_processed, total_extracted, total_valid
    
    try:
        # Get block by number
        params = {
            'module': 'proxy',
            'action': 'eth_getBlockByNumber',
            'tag': hex(block_number),
            'boolean': 'true',
            'apikey': ETHERSCAN_API_KEY
        }
        
        data = proxychains_request(ETHERSCAN_BASE_URL, params=params, timeout=30)
        
        with extraction_lock:
            total_blocks_processed += 1
        
        if 'error' in data:
            logger.warning(f"Block {block_number}: API error - {data['error']}")
            return []
        
        if 'result' not in data or data['result'] is None:
            logger.warning(f"Block {block_number}: No result in API response")
            return []
        
        if 'result' in data and data['result'] is not None:
            block_data = data['result']
            transactions = block_data.get('transactions', [])
            
            if not transactions:
                return []
            
            # Filter for simple non-MEV transactions
            legitimate_txs = []
            for tx in transactions:
                try:
                    # Basic filters for likely non-MEV transactions
                    gas_used = int(tx.get('gas', '0x0'), 16)
                    gas_price = int(tx.get('gasPrice', '0x0'), 16)
                    value_wei = int(tx.get('value', '0x0'), 16)
                    
                    # Filter criteria for non-MEV transactions
                    is_simple_transfer = (
                        gas_used <= 50000 and  # Simple transactions
                        len(tx.get('input', '0x')) <= 10 and  # Minimal input data
                        value_wei > 0  # Has value transfer
                    )
                    
                    if is_simple_transfer:
                        legitimate_txs.append({
                            'tx_hash': tx['hash'],
                            'from_address': tx['from'].lower(),
                            'to_address': tx['to'].lower() if tx['to'] else '',
                            'block_number': block_number,
                            'gas_used': gas_used,
                            'gas_price': gas_price,
                            'value_eth': value_wei / 1e18,
                            'profit_eth': 0.0,  # Non-MEV transactions have no profit
                            'cost_eth': (gas_used * gas_price) / 1e18,
                            'gain_eth': value_wei / 1e18,
                            'is_mev': 0,
                            'mev_type': 'normal'
                        })
                        
                except (ValueError, KeyError, TypeError):
                    continue
            
            with extraction_lock:
                total_extracted += len(legitimate_txs)
                total_valid += len(legitimate_txs)
            
            logger.info(f"Block {block_number}: Found {len(legitimate_txs)} legitimate non-MEV transactions")
            return legitimate_txs
        
        return []
        
    except Exception as e:
        logger.error(f"Block {block_number}: Extraction error - {e}")
        return []

def extract_from_block_range(start_block, end_block, description, target_count):
    logger.info(f"Extracting from {description}")
    logger.info(f"   Block range: {start_block:,} to {end_block:,}")
    logger.info(f"   Target count: {target_count:,}")
    
    all_transactions = []
    blocks_to_sample = list(range(start_block, end_block + 1))
    random.shuffle(blocks_to_sample)  # Random sampling for diversity
    
    # Process blocks in batches
    batch_size = 10
    processed_blocks = 0
    
    for i in range(0, len(blocks_to_sample), batch_size):
        if len(all_transactions) >= target_count:
            break
            
        batch = blocks_to_sample[i:i + batch_size]
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # Submit batch extraction tasks
            future_to_block = {}
            for block_num in batch:
                future = executor.submit(get_block_transactions, block_num)
                future_to_block[future] = block_num
            
            # Collect results as they complete
            for future in as_completed(future_to_block):
                block_num = future_to_block[future]
                try:
                    block_transactions = future.result()
                    all_transactions.extend(block_transactions)
                    processed_blocks += 1
                    
                    if len(all_transactions) >= target_count:
                        logger.info(f"Target reached! Found {len(all_transactions)} transactions")
                        break
                        
                except Exception as e:
                    logger.error(f"Block {block_num} failed: {e}")
        
        # Progress update
        logger.info(f"Progress: {len(all_transactions)}/{target_count} transactions from {processed_blocks} blocks")
        
        # Rate limiting between batches
        time.sleep(RATE_LIMIT_DELAY * 2)
    
    return all_transactions[:target_count]

def main():
    parser = argparse.ArgumentParser(description='Extract legitimate time-aligned non-MEV transactions')
    parser.add_argument('--sample-size', type=int, default=25000, help='Total transactions to extract (default: 25000)')
    parser.add_argument('--blocks-per-batch', type=int, default=10, help='Blocks to process per batch (default: 10)')
    
    args = parser.parse_args()
    
    logger.info("Legitimate Time-Aligned Non-MEV Transaction Extraction")
    logger.info("=" * 80)
    
    # Check proxychains availability
    if USE_PROXYCHAINS:
        if check_proxychains():
            logger.info("ProxyChains4 detected - using enhanced connectivity")
        else:
            logger.info("ProxyChains4 not found - using direct connection")
    
    # Calculate target counts for each period
    june_2020_target = int(args.sample_size * 0.7)  # 70% from June 2020 (Arbitrage/Sandwich period)
    august_2021_target = args.sample_size - june_2020_target  # 30% from August 2021 (Liquidation period)
    
    logger.info(f"Extraction Plan:")
    logger.info(f"   June 2020 target: {june_2020_target:,} transactions")
    logger.info(f"   August 2021 target: {august_2021_target:,} transactions")
    logger.info(f"   Total target: {args.sample_size:,} transactions")
    logger.info("")
    
    start_time = time.time()
    all_transactions = []
    
    # Extract from June 2020 period (Arbitrage/Sandwich aligned)
    june_transactions = extract_from_block_range(
        JUNE_2020_BLOCKS['start'],
        JUNE_2020_BLOCKS['end'],
        JUNE_2020_BLOCKS['description'],
        june_2020_target
    )
    all_transactions.extend(june_transactions)
    
    logger.info(f"June 2020 extraction complete: {len(june_transactions):,} transactions")
    
    # Extract from August 2021 period (Liquidation aligned)
    august_transactions = extract_from_block_range(
        AUGUST_2021_BLOCKS['start'],
        AUGUST_2021_BLOCKS['end'],
        AUGUST_2021_BLOCKS['description'],
        august_2021_target
    )
    all_transactions.extend(august_transactions)
    
    logger.info(f"August 2021 extraction complete: {len(august_transactions):,} transactions")
    
    # Create final dataset
    extraction_time = time.time() - start_time
    
    if all_transactions:
        df = pd.DataFrame(all_transactions)
        
        # Save dataset with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = f'legitimate_time_aligned_non_mev_{timestamp}.csv'
        df.to_csv(output_path, index=False)
        
        # Replace the corrupted dataset
        corrupted_path = '../../large/time_aligned_non_mev_results.csv'
        backup_path = f'../../large/time_aligned_non_mev_results_backup_{timestamp}.csv'
        
        # Backup corrupted file
        if os.path.exists(corrupted_path):
            os.rename(corrupted_path, backup_path)
            logger.info(f"Backed up corrupted file to: {backup_path}")
        
        # Replace with legitimate data
        df.to_csv(corrupted_path, index=False)
        
        # Final statistics
        logger.info("")
        logger.info("EXTRACTION RESULTS SUMMARY")
        logger.info("=" * 50)
        logger.info(f"Total legitimate transactions: {len(df):,}")
        logger.info(f"June 2020 transactions: {len(june_transactions):,}")
        logger.info(f"August 2021 transactions: {len(august_transactions):,}")
        logger.info(f"Total blocks processed: {total_blocks_processed:,}")
        logger.info(f"Extraction time: {extraction_time:.1f} seconds ({extraction_time/3600:.2f} hours)")
        logger.info(f"Extraction rate: {len(df)/extraction_time:.1f} transactions/second")
        
        # Dataset statistics
        logger.info("")
        logger.info("DATASET STATISTICS:")
        logger.info(f"   Block range: {df['block_number'].min():,} to {df['block_number'].max():,}")
        logger.info(f"   Average gas used: {df['gas_used'].mean():.0f}")
        logger.info(f"   Average gas price: {df['gas_price'].mean()/1e9:.1f} Gwei")
        logger.info(f"   Average value: {df['value_eth'].mean():.6f} ETH")
        logger.info(f"   Total value: {df['value_eth'].sum():.2f} ETH")
        
        logger.info("")
        logger.info("SUCCESS: Legitimate time-aligned non-MEV dataset created")
        logger.info(f"Saved to: {output_path}")
        logger.info(f"Replaced: {corrupted_path}")
        logger.info("")
        logger.info("Next: Run GAT with legitimate time-aligned dataset:")
        logger.info("   python3 gnn_gat.py --mev_types arbitrage --max_samples 10000")
        
    else:
        logger.error("No transactions extracted")

if __name__ == "__main__":
    main()