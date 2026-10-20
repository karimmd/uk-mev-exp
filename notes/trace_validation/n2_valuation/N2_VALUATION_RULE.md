# N2 — Registered cross-token valuation rule for the actor-side ledger

**Written by the assistant session of 2026-10-05 on the remote PC, before `run_n2.py` was executed.**
The SHA-256 of this file and the `date -Is` reading at registration are in `N2_REGISTRATION.txt`
beside it. The runner refuses to execute if this file's hash does not match that record.
**Author review of this rule is pending**; if the author amends it, the amended rule is a second
registration and both results are reported.

## 0. Disclosure, stated first

An exploratory diagnostic preceded this registration (`revision/scripts/diag_20261005/`,
logs in `revision/out/diag_20261005/`). It read the frozen Task 07 output and tabulated, by arm,
the sign and magnitude of the residual non-WETH positions in the 5,021 `cross_token_position_unpriced`
cases, and the sign of the ETH-equivalent ledger (`native_net_wei` plus the WETH position) in those
cases. It did **not** apply any valuation. It found that the residual positions are overwhelmingly
long (2,530 of 3,085 in the recorded arm, 108 of 130 in the absent arm) and that the ETH-equivalent
ledger is positive in essentially every such case in the two contrasted arms. A projected outcome
table under a dominance rule was printed. **That projection was seen before this rule was written.**
The rule below is therefore not blind to the direction of its effect. What protects it is that
Rule A is a logical implication with no free parameter, and Rule B is fixed to the conservative
direction (the valuation that works against support) and has no tunable threshold. A reader who
regards a rule registered after an exploratory look as worthless should read the result as
exploratory; it is labelled so wherever it is reported.

## 1. Scope

The rule touches exactly one class of case: those whose frozen Task 07 `value_flow.state` is
`undecidable` with `reason_codes == ["cross_token_position_unpriced"]`. Every other case keeps its
frozen value-flow result unchanged. The trajectory witness is never touched. The outcome rule is
the frozen `_outcome` of `run_task07.py`, imported and applied unchanged. Task 07 itself is not
re-run; this is a re-signing of one ledger state on the frozen evidence.

Notation: B is the frozen strategy boundary; L is `native_net_wei` plus the boundary's WETH
position, both read from the frozen record (L is exactly the quantity flow2 signs when no residual
exists); R_t is the boundary's net position in each non-WETH token t with R_t != 0 (the residuals).

## 2. Rule A — valuation-free dominance

Any valuation of a token is a non-negative number. Therefore:

- if every R_t >= 0 and L > 0, the total position is >= L > 0 under **every** non-negative
  valuation: the ledger is **positive**, with L reported as its lower bound;
- if every R_t <= 0 and L <= 0, the total is <= L <= 0 under every non-negative valuation: the
  ledger is **non-positive**;
- otherwise Rule A does not decide and Rule B is consulted.

Rule A has no parameter and cannot be tuned.

## 3. Rule B — conservative realized-rate valuation

For each residual token t, a leg (front or back) **yields a realized WETH rate for t** iff, over
the boundary B in that leg, (i) the set of non-WETH tokens with non-zero net movement is exactly
{t}, (ii) the WETH movement (ERC-20 `Transfer` net plus WETH9 `Deposit`/`Withdrawal`) is non-zero,
and (iii) the two movements have opposite signs. The rate is |dWETH| / |dt| in wei per raw unit,
computed in exact rational arithmetic.

The valuation used is the one that works **against** support: for a long residual (R_t > 0) the
**minimum** rate over the legs that yield one; for a short residual (R_t < 0) the **maximum**.
If any residual token has no leg yielding a rate, the case stays `undecidable` with the new reason
`cross_token_no_realized_rate`. No external price feed, pool reserve or other transaction is
consulted; only the actor's own realized exchange in the bracket.

Total T = L + sum over t of R_t times rate_t.

## 4. Completeness and sign, exactly as flow2

Cost completeness is recomputed exactly as `flow2.evaluate` does after the point where it
returned early: `zero_gas` iff either outer leg has `effectiveGasPrice == 0`; `cost_complete` is
false iff `zero_gas` and the frozen `native_out_wei == 0` and `top_level_value_out_wei == 0`.
Then: complete gives `positive` if T > 0 else `negative`; incomplete and T > 0 gives `undecidable`
(`unobserved_cost_could_change_sign`); incomplete and T <= 0 gives `negative`.

## 5. Variants, all reported

| variant | definition |
|---|---|
| **primary** | Rule A, then Rule B for what A leaves open |
| A-only | Rule A; everything else stays `undecidable` |
| B-only | Rule B applied to every case in scope, including those A would decide |
| frozen | the Task 07 outcomes unchanged, as the reference and as a self-check of the statistics |

## 6. Analysis, identical to the frozen plan

Per variant, the statistics of `TASK08_ANALYSIS_PLAN.md` sections 2 and 3 are recomputed by the
same code path: primary contrast `target_strict_miss` vs `control_detected`; strata are the frozen
five-way cross with the same bins; a stratum enters iff it holds >= 20 of all 17,637 cases and at
least one case of each contrasted group, the rest pooled into `other`; direct standardization
weighted by stratum share of all 17,637; within-stratum permutation null with **20,000
permutations, seed 20260920**, two-sided p; Newcombe interval on the unadjusted difference; the
undecidable-share difference against the blinded band -5.08/+5.15 with the P5 consequence (if
exceeded, the point estimate is exploratory and the resolution bounds are the reported result);
best/worst bounds; comparator sensitivity with `control_nearmiss` pooled. The frozen variant must
reproduce -23.4493 pp and the band -8.1233/+7.5226 or the runner aborts.

## 7. What a result may and may not say

A `structurally_supported` case under this rule is supported by trajectory and by an
ETH-equivalent ledger that is positive under the most adverse valuation the actor's own trades
admit. It is not mechanically confirmed, it is not true economic profit, and it says nothing about
costs the evidence cannot see beyond what flow2 already bounds. The sampling factor is 88.
