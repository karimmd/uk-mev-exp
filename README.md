# uk-mev-exp
References for implementation and reproducibility


## Layout

```
.
├── dataset_analysis/      # Stage 1–2: data conversion + characterization
│   ├── convert_json_to_csv.py   # JSONL archive export -> flat CSV schema
│   └── dataset_analysis.py      # miner concentration, feature correlations,
│                                # gas-strategy ratios, DEX mapping (analysis-only)
├── llm_screening/         # Stage 3 (LLM) + Stage 4
│   ├── mistral/             # Mistral-7B deployment runners (arb / sand / liq, 20K→1M)
│   ├── qwen/                # Qwen2.5-7B deployment runners
│   ├── taxonomy/            # 877-candidate pattern categorization
│   ├── cross_model/         # Mistral vs Qwen overlap + false-positive analysis
│   └── validation/          # Etherscan validation + stricter-prompt frameworks
├── baselines/             # Stage 3 (structural baselines)
│   ├── gat/                 # OOD-aware Graph Attention Network
│   ├── xgboost/             # GAT-aligned XGBoost baseline
│   └── classical_ml/        # LogReg + MLP + XGBoost shared-feature comparison
├── models/                  # LLM provenance notes + config/tokenizer metadata (no weights)
├── datasets/                # Data schema + availability notes (raw CSVs hosted externally)
└── requirements.txt
```