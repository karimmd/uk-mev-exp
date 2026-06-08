# Stage 3 (LLM) + Stage 4: LLM-Driven Unknown MEV Screening

The core contribution: instruction-tuned LLMs screen each transaction and emit one
of three labels — `KNOWN`, `UNKNOWN`, or `NORMAL` — via attack-type-specific
prompts. Each deployment script is a self-contained runner with checkpoint/resume
support, FP16 inference, and a 3-attempt retry budget (defaulting to `UNKNOWN` on
parse failure). See [`../models/README.md`](../models/README.md) for model origins.

## `mistral/` — Mistral-7B-Instruct (primary screener)

Exploratory prompt; `[INST] … [/INST]` chat template. Progressive scales validate
that the unknown rate is stable across sample sizes.

| Script | Scale | Duration | Output |
|---|---|---|---|
| `arbitrage/mistral_arbitrage_20k.py` | 20K | 1.95 h | baseline validation |
| `arbitrage/mistral_arbitrage_100k.py` | 100K | 9.32 h | scale check |
| `arbitrage/mistral_arbitrage_1m.py` | 1M | 92.6 h | **428 candidates** (headline) |
| `sandwich/mistral_sandwich_20k.py` | 20K | 2.70 h | — |
| `sandwich/mistral_sandwich_100k.py` | 100K | — | — |
| `sandwich/mistral_sandwich_1m.py` | 1M | 134.8 h | **289 candidates** (headline) |
| `liquidation/mistral_liquidation_5k.py` | 5K | — | pilot |
| `liquidation/mistral_liquidation_10k.py` | 10K | — | — |
| `liquidation/mistral_liquidation_32k.py` | Full | 6.51 h | **160 candidates** (headline) |

Total headline screen: **2,032,566 txs → 877 candidate unknowns**.

## `qwen/` — Qwen2.5-7B-Instruct (cross-model sensitivity)

Constrained prompt; native chat template via `apply_chat_template()`.

| Script | Scale | Duration | Output |
|---|---|---|---|
| `arbitrage/qwen_arbitrage_20k.py` | 20K | — | pilot |
| `arbitrage/qwen_arbitrage_100k.py` | 100K | — | — |
| `arbitrage/qwen_arbitrage_1m.py` | 1M | 90.7 h | **99 candidates** |
| `sandwich/qwen_sandwich_20k.py` | 20K | — | pilot |
| `sandwich/qwen_sandwich_100k.py` | 100K | 16.1 h | **485 candidates** |
| `sandwich/qwen_sandwich_1m.py` | 1M | 140.3 h | **3,976 candidates** (corrected parser) |
| `liquidation/qwen_liquidation_5k.py` | 5K | — | pilot |
| `liquidation/qwen_liquidation_20k.py` | 20K | — | — |
| `liquidation/qwen_liquidation_32k.py` | Full | 1.8 h | **63 candidates** |

Total: **2,132,570 txs → 4,623 candidate unknowns**. `qwen_sandwich_1m.py` uses the
corrected response parser (matches `UNKNOWN` before `KNOWN`); see its module docstring.
Qwen's intermediate liquidation scale was **20K** (Mistral used 10K), so the scale
grids differ at that one tier.

## `taxonomy/` — Stage 4: candidate categorization

| Script | Purpose |
|---|---|
| `analyze_patterns_local.py` | Categorizes the flagged unknowns by on-chain attributes (hash completeness, profitability, exchange distribution, bot-address frequency, Flashbots usage) → produces the 16-category taxonomy. |
| `qwen_1m_precision_patches.py` | Ultra-strict prompt variant derived from analyzing Mistral's 1M false positives (informational; documents the prompt-tuning rationale). |

## `cross_model/` — Mistral vs Qwen sensitivity

| Script | Purpose |
|---|---|
| `compare_qwen_mistral_100k.py` | Per-transaction Jaccard overlap on a matched 100K slice. |
| `llm_comparison.py` | Aggregate cross-model rate comparison. |
| `false_positive_analysis.py` | Cross-model false-positive risk assessment. |
| `mistral_false_positive_analysis.py` | Mistral-specific false-positive breakdown. |

## `validation/` — candidate adjudication support

| Script | Purpose |
|---|---|
| `etherscan_validator.py` | Fetches on-chain data for flagged candidates via the Etherscan API (supply your own key). |
| `improved_classification_framework.py` | Stricter-prompt framework (90%+ confidence threshold for `UNKNOWN`). |
| `select_validation_samples.py` | Stratified sampling of candidates for expert review. |
| `expert_validation_template.md` | Template for human adjudication. |

## Inference settings (all runs)

Temperature 0.3 · max new tokens 15 · repetition penalty 1.1 · input truncation
2,048 tokens · 3-attempt retry · checkpoint every 1,000 txs.
