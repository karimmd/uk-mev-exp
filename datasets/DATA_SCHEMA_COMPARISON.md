# Data Schema Comparison

## Overview

This document compares the schema of `observed_transactions.csv` (raw mempool data) with existing processed MEV datasets.

## File: observed_transactions.json → observed_transactions.csv

**Source:** Raw mempool transactions from Ethereum blockchain
**Total Records:** 125,661,539 transactions
**File Size:** 145 GB (JSON) → ~150-180 GB (CSV estimated)
**Data Type:** Raw, unlabeled blockchain transactions (pending/mempool transactions)
**Time Period:** Based on timestamps (~Nov 2021 from samples)

### Schema (21 columns):

| Column | Type | Description | Critical for MEV? |
|--------|------|-------------|-------------------|
| `_id` | string | MongoDB ObjectId | Unique identifier |
| `hash` | string | Transaction hash | Primary key |
| `blockNumber` | int/null | Block number (null for pending) | Block context |
| `blockHash` | string/null | Block hash | - |
| `transactionIndex` | int/null | Position in block | - |
| `timestamp` | float | Unix timestamp with microseconds | Temporal analysis |
| `from` | address | Sender address | Bot detection |
| `to` | address | Recipient/contract address | Contract interaction |
| `nonce` | int | Transaction nonce | Sequence detection |
| `value` | string | ETH value in wei | Value extraction |
| `gas` | int | Gas limit | Gas analysis |
| `gasPrice` | string | Gas price in wei | Priority/cost |
| `maxFeePerGas` | string | EIP-1559 max fee | MEV bidding |
| `maxPriorityFeePerGas` | string | EIP-1559 priority fee | Miner tip |
| `input` | string | Transaction data (hex) | Function calls |
| `type` | int | Transaction type (0/1/2) | EIP-1559 detection |
| `v` | string | Signature v | - |
| `r` | string | Signature r | - |
| `s` | string | Signature s | - |
| `accessList` | string | EIP-2930 access list | - |
| `chainId` | string | Chain identifier | - |

---

## Existing MEV Datasets Comparison

### 1. arbitrage_results.csv (11 GB, processed MEV)

**Schema (18 columns):**
```
_id, block_number, block_timestamp, miner, transaction, swaps, eth_usd_price,
cost_eth, cost_usd, gain_eth, gain_usd, profit_eth, profit_usd,
tokens_acquired, flashbots_bundle, flashbots_coinbase_transfer,
frontrunning_arbitrage, flash_loan
```

**Relationship to observed_transactions:**
- `transaction` field contains full raw transaction dict (similar structure to observed_transactions)
- Adds processed features: profit metrics, swap details, MEV labels
- **Usage:** Training data for arbitrage MEV detection

### 2. sandwich_results.csv (3.5 GB, processed MEV)

**Schema (30 columns):**
```
_id, block_number, block_timestamp, first_transaction, whale_transaction,
second_transaction, eth_usd_price, cost_eth, cost_usd, gain_eth, gain_usd,
profit_eth, profit_usd, exchange_address, exchange_name, token_address,
token_name, first_transaction_eth_amount, whale_transaction_eth_amount,
second_transaction_eth_amount, first_transaction_token_amount,
whale_transaction_token_amount, second_transaction_token_amount, interface,
bot_address, same_sender, same_receiver, same_token_amount,
flashbots_bundle, flashbots_coinbase_transfer, miner
```

**Relationship to observed_transactions:**
- Contains 3 transactions per sandwich attack
- Adds relational features: transaction sequences, victim transactions
- **Usage:** Training data for sandwich attack detection

### 3. liquidation_results.csv (105 MB, processed MEV)

**Structure:** Similar to arbitrage_results with liquidation-specific features

### 4. real_non_mev_results.csv (227 MB, labeled non-MEV)

**Schema (12 columns):**
```
tx_hash, from_address, to_address, block_number, gas_used, gas_price,
value_eth, profit_eth, cost_eth, gain_eth, is_mev, mev_type
```

**Relationship to observed_transactions:**
- Simplified schema focusing on key features
- `tx_hash` maps to `hash` in observed_transactions
- Adds labels: `is_mev`, `mev_type`
- **Usage:** Negative samples for binary classification

---

## How observed_transactions.csv Should Be Used

### Purpose:
**Raw dataset for creating new labeled training data**

### Potential Uses:

1. **Expand Non-MEV Dataset:**
   - Sample from observed_transactions where transactions are NOT in arbitrage/sandwich/liquidation CSVs
   - Use as negative samples (normal transactions)
   - Addresses XGBoost temporal data mismatch issue (same time period as MEV data)

2. **Contextual Analysis:**
   - For each MEV transaction in arbitrage/sandwich CSVs, find surrounding transactions in same block
   - Analyze transaction ordering and MEV extraction patterns
   - Study mempool behavior before block inclusion

3. **Feature Engineering:**
   - Extract features from raw `input` data (function signatures, contract calls)
   - Calculate derived features: effective_gas_price, value_usd, etc.
   - Build temporal features: transaction sequences, nonce gaps

4. **Unknown MEV Discovery:**
   - Apply trained LLM models to unlabeled observed_transactions
   - Find novel MEV patterns not in existing labeled datasets
   - Validate LLM predictions against GAT/baseline models

### Integration with Existing Experiments:

**For XGBoost Baseline Fix:**
```python
# Pseudo-code for temporal matching
observed_timestamps = get_timestamps(observed_transactions.csv)
mev_timestamps = get_timestamps(arbitrage_results.csv + sandwich_results.csv)

# Sample non-MEV from same time period
non_mev_samples = observed_transactions[
    observed_transactions.timestamp.between(
        mev_timestamps.min(),
        mev_timestamps.max()
    ) &
    ~observed_transactions.hash.isin(mev_hashes)
].sample(n=desired_size)
```

**For LLM Experiments:**
```python
# Convert raw transaction to LLM prompt format
def create_prompt(row):
    return f"""
    Transaction: {row['hash']}
    From: {row['from']} → To: {row['to']}
    Value: {wei_to_eth(row['value'])} ETH
    Gas: {row['gas']} @ {wei_to_gwei(row['gasPrice'])} Gwei
    Input: {decode_input(row['input'])}
    Timestamp: {format_timestamp(row['timestamp'])}

    Classify as: KNOWN MEV / UNKNOWN MEV / NORMAL
    """
```

---

## Critical Fields for MEV Detection

### Must-Have Fields (Core 10):
1. `hash` - Unique identifier
2. `blockNumber` - Block context
3. `timestamp` - Temporal ordering
4. `from` - Bot/attacker identification
5. `to` - Contract interaction patterns
6. `value` - Profit/value extraction
7. `gas` - Economic cost
8. `gasPrice` - Priority/bidding
9. `input` - Function call analysis
10. `nonce` - Transaction sequencing

### Important for Advanced Analysis:
11. `maxFeePerGas` / `maxPriorityFeePerGas` - EIP-1559 MEV bidding strategies
12. `type` - Distinguish legacy vs EIP-1559 transactions
13. `transactionIndex` - In-block ordering for sandwich detection

### Schema Verification:

**All critical fields are included in the conversion script**

**Column order optimized:** identifiers → participants → economics → data → signatures

**Compatible with existing datasets:** `hash` maps to `tx_hash`, basic Ethereum fields preserved

---

## Conversion Statistics

- **Input:** 125,661,539 transactions (145 GB JSON)
- **Expected Output:** ~150-180 GB CSV
- **Estimated Time:** 1-4 hours depending on disk I/O
- **Progress Updates:** Every 10,000 records

## Next Steps

1. Run conversion: `python3 convert_json_to_csv.py`
2. Verify CSV integrity after conversion
3. Create temporal analysis to match MEV dataset time periods
4. Sample non-MEV transactions for balanced training data
5. Extract features for XGBoost/GAT baselines
6. Apply LLM models to discover unknown MEV patterns
