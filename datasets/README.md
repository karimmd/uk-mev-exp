# Datasets

The study uses historical Ethereum mainnet MEV transactions mined from a
go-ethereum archive node covering blocks **10,000,000 – 14,444,725**
(May 4, 2020 – March 23, 2022), stored in MongoDB and exported to CSV.

## Availability

The raw per-type CSVs are multi-gigabyte and are **not committed to this repository**:

| File | MEV Type | Rows | Approx. size |
|---|---|---|---|
| `arbitrage_results.csv` | Arbitrage | 3,462,678 | ~11 GB |
| `sandwich_results.csv` | Sandwich | 1,020,000 (≈250K unique attacks) | ~3.7 GB |
| `liquidation_results.csv` | Liquidation | 32,819 | ~110 MB |
| `non_mev_results.csv` / `real_non_mev_results.csv` | Non-MEV negatives | — | — |

The datasets will be made available via an external host; the link will be added
here upon publication. The deduplicated transaction accounting (raw → unique →
sampled → LLM-evaluated) is reported in Table III of the manuscript.

## Schema

See [`DATA_SCHEMA_COMPARISON.md`](DATA_SCHEMA_COMPARISON.md) for the full field-level
schema. Key columns by type:

- **Arbitrage:** `block_number`, `block_timestamp`, `miner`, `swaps` (JSON list of
  hops), `eth_usd_price`, `cost_eth`, `gain_eth`, `profit_eth`, `tokens_acquired`,
  `flashbots_bundle`, `flash_loan`
- **Sandwich:** `block_number`, `block_timestamp`, `first_transaction`,
  `whale_transaction`, `second_transaction` (full JSON per leg), `exchange_address`,
  `token_address`, `profit_eth`, `bot_address`, `flashbots_bundle`, `miner`
- **Liquidation:** `block_number`, `block_timestamp`, `liquidator`,
  `liquidated_user`, `debt_token_*`, `received_token_*`, `protocol_name`
  (Aave / Compound / MakerDAO), `profit_eth`, `flash_loan`

## Reconstructing the CSVs

The raw archive-node export is JSONL (`observed_transactions.json`). The converter
`../1_dataset_analysis/convert_json_to_csv.py` streams that file into the flat CSV
schema used by every downstream script.
