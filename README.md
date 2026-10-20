# uk-mev-exp

Reference implementation and released artefacts for *Who Audits the MEV Detectors? Evidence-Based Adjudication of MEV Detections on Ethereum*.

| Path | Contents |
|---|---|
| `scripts/catalog.py` | Economic-actor rule and the canonical sandwich and arbitrage rules over decoded on-chain evidence |
| `scripts/causal_oracle.py`, `scripts/build_s0_cohorts.py` | Evidence decoding from public RPC and the populations of the evaluation |
| `scripts/trace_validation/02_manifest` | Case manifest of the 17,637 adjudicated sandwich attacks |
| `scripts/trace_validation/trajectory`, `scripts/trace_validation/w2_witness` | Trajectory witness, original and revised (W2), with its fixtures |
| `scripts/trace_validation/value_flow_v2`, `scripts/trace_validation/n2_valuation` | Value-flow ledger and the residual-token valuation rule N2 |
| `scripts/trace_validation/07_execution`, `scripts/trace_validation/08_analysis`, `scripts/trace_validation/10_decision` | Outcome rule, the pre-specified analysis and the permutation nulls |
| `scripts/trace_validation/counterfactual_v2` | Victim-side replay |
| `scripts/diag_20261005`, `scripts/exhibits`, `analysis` | Detector comparison, S5', magnitudes, execution position and the exhibits |
| `scripts/explorer_verification` | Explorer cards, the validator runs and their scoring |
| `notes` | Registered rule texts, protocols, plans and registration files with hashes |
| `data` | Block manifests, case manifest, set map and sealed mappings |
| `out/explorer_verification`, `out/explorer_verification_api`, `out/explorer_verification_api_v2` | Every card, judgement and unsealed sheet of the explorer validation: the first reading and the two three-validator runs |
| `out/trace_validation` | Evidence state of every adjudicated attack under the original and the revised witness, with the results of the pre-specified analysis, N2, W2, the permutation nulls and the ledger checks |
| `out/exhibits`, `out/diag_20261005` | The data behind every figure and table: detector comparison, mev-inspect outputs on the sampled blocks, S5' coverage, linkage, magnitudes, execution position, replay eligibility and the validator cards |

Paths of the form `revision/...` in the source are relative to `MEV_ROOT`.
