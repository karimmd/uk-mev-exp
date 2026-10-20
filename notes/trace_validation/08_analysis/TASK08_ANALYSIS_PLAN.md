# Task 08 — Pre-registered Analysis Plan (v2, after R2-07 G3A)

**Written and hashed 2026-09-20, BEFORE the group map was opened.** This is R2-07's first Task 08
guard and the only one that becomes worthless if deferred by a step: it is what makes "no threshold
was tuned after seeing outcomes" checkable rather than asserted.

At the moment of writing, `data/trace_validation/group_map/v2/case_group_map.csv` has **never been
read** by this session beyond its two column names (`case_id,group`), disclosed in
`../05_value_flow/v2/VALUE_FLOW_V2_ERRATUM.md` §D2.

**v2 incorporates R2-07 G3A findings P1–P10.** v1 was gated `GO` only conditional on them.

## 1. Inputs, fixed

| input | sha256 |
|---|---|
| `out/.../07_execution/task07_outcomes.jsonl` | `298bd947…4fbd` |
| `out/.../07_execution/task07_outcomes_summary.json` | `744a4847…5002` |
| `out/.../08_analysis/maj2_sensitivity.json` | pinned in this directory's `SHA256SUMS` |
| `out/.../08_analysis/null_distribution.json` | pinned in this directory's `SHA256SUMS` |
| `data/.../manifests/v2/cases_blinded.csv` | `1e8e63c4…b7b71` |
| `data/.../group_map/v2/case_group_map.csv` | `10bb0837…4ba1f` (unopened) |

**Task 07 is final and will not be re-run for any reason** (R2-07 G3 guard 2). After unblinding a
re-run is unfalsifiably contaminated, and "one frozen run" must not bend for convenience — not for
a schema defect, not for anything.

## 2. The single confirmatory comparison (P1)

**Exactly one comparison is confirmatory.** Everything in §3 is secondary and is reported as
supportive or exploratory, never as independent confirmation. No multiplicity correction is claimed
for §3 because no §3 result may carry a conclusion (P9).

**Primary:** the outcome distribution of `recorded` versus `missed` cases over the three reachable
states, on all 17,637 with no case dropped.

- Statistic: the difference in `structurally_supported` share, `missed − recorded`.
- **Composition-adjusted (P2):** the primary statistic is the **within-stratum** difference,
  standardized over the five blinded covariates. MAJ-1 establishes that the unstratified difference
  is impermissible alone — a detector's misses are not random, so an aggregate difference may be
  composition rather than genuineness.
- Null: **within-stratum permutation of the group labels**, 20,000 permutations, seed 20260920.
  Permutation is exact under the null of label-independence given strata and needs no distributional
  assumption; the critical value comes out of the permutation rather than a table, so nothing is
  chosen after the answer is visible.
- **If the adjusted and unadjusted results disagree, the adjusted one governs** and the
  disagreement is reported prominently as evidence that composition is doing the work.
- Interval: Newcombe hybrid-score for the difference of proportions; Fisher's exact where any cell
  is below 5 (P6). Minimum stratum cell size for a stratum to enter the standardization: **20**;
  smaller strata are pooled into an `other` stratum declared in advance (P7).

### 2a. Stratum definition — added before the join, and the reason it is added here

v2 said "standardized over the five blinded covariates" without saying how two of them are binned.
Two are continuous-ish, so leaving it open would have let me choose bins after seeing the answer —
the exact failure §5 forbids. **Fixed now, while the group map is still unopened:**

| covariate | levels |
|---|---|
| `era` | `pre_flashbots`, `flashbots_pre_london`, `post_london` |
| `amm_design` | `v2_only`, `v3_only`, `mixed_v2_v3` |
| `n_pools` | `1`, `2`, `3+` |
| `route_complexity_swap_events` | `<=3`, `4`, `5-6`, `7+` |
| `observable_gas_price_zero` | `True`, `False` |

The stratum is the full cross (216 cells). Standardization is **direct**, weighting each stratum by
its share of all 17,637. A stratum enters only if it holds **>= 20 cases and at least one case from
each group**; the rest are pooled into `other`, which enters under the same rule. **Coverage — the
share of `missed` cases in included strata — is reported**, and if it falls below 80% the
standardized estimate is demoted to exploratory and the bounds in §3.3 become the reported result.

The permutation null respects the identical restriction, so the null and the statistic are computed
on the same strata.
- The **union boundary is primary** throughout; the per-leg boundary is the sensitivity (P8).

### 2b. Amendment at the join — the group map has THREE arms, not two

**Recorded 2026-09-20 21:07 CST, at the moment of the join and before any outcome-by-group figure
was computed.** v2 §2 says "`recorded` versus `missed`", assuming two arms. The group map has
three:

| label | n |
|---|---|
| `control_detected` | 10,299 |
| `control_nearmiss` | 7,080 |
| `target_strict_miss` | **258** |

`target_strict_miss` is the 258 missed sandwiches the programme exists to test. The gap is real and
is mine: I pre-registered a two-arm contrast without checking the arity of a file I had committed
not to open.

**Resolution, decided on semantics and not on numbers.** The primary contrast is
**`target_strict_miss` vs `control_detected`**. The question is whether the missed set looks like
the *recorded* set, so the comparator must be the recorded sandwiches. `control_nearmiss` is by
construction a population whose status is uncertain; folding it into "recorded" would contaminate
the comparator with cases that may themselves be genuine-but-unrecorded, which is the very thing
under test.

`control_nearmiss` is reported as a **third arm**, separately, so no case is dropped and §5's
"no case dropped from any denominator" is honoured. It is **not** pooled with either arm.

Both the pooled and unpooled contrasts are reported, and **`target_strict_miss` vs
`control_detected` governs**; the pooled variant is a sensitivity, labelled so.

**This decision was made with the group *sizes* visible and every outcome-by-group figure still
uncomputed.** Composition was visible; the answer was not.

**Consequence for the pre-registered critical value.** The blind n = 258 null in §6 was drawn
against the other 17,379 cases, not against the 10,299-case comparator. It stands as the
pre-registered reference, but **the operative critical value is the within-stratum permutation
null of §2**, which permutes the actual label vector and is exact for whatever arms exist.

## 3. Pre-specified secondary analyses

1. Stratified results by each of `era`, `amm_design`, `n_pools`, `observable_gas_price_zero`,
   `route_complexity_swap_events`, reported with cell counts.
2. **The undecidable share by group, with a consequence attached (P5).** Null SD **2.70 pp**, 95%
   band −5.08/+5.15. If the undecidable-share difference exceeds that band, **every support rate is
   conditioned on a group-dependent denominator**, the point-estimate comparison is demoted to
   exploratory, and the bounds in §3.3 become the reported result.
3. **Best/worst-case bounds, with a consequence attached (P4).** Assign all 4,369 undecidables
   first to support, then to rejection. **The falsifier in §6 is evaluated at the point estimate
   and at both bounds.** A claim surviving all three is robust; one surviving only the point
   estimate is reported as conditional and cannot support a conclusion. Undecidables are **never**
   dropped.
4. **MAJ-2 bound.** Every support rate reported at both boundaries: 44.51% union / 44.11% per-leg
   overall. The MAJ-2 headline is the **gradient** — the `boundary_size` 2→3 gap falls 19.6 pp to
   15.4 pp, so cancellation explains **21.5%** of it.
5. The 1,661 `boundary_size >= 3` cases reported separately, selected on `boundary_size >= 3`.
   Task 08 **asserts on load** that `multi_sender_boundary == (boundary_size > 1)` so the mis-named
   field cannot be silently reinterpreted (R2-07 G3).
6. **Rejection provenance.** 96.9% of rejections rest on `trajectory_negative` alone, so any claim
   about rejected cases is a claim about the 03b witness, not the value-flow ledger. Stated wherever
   rejections are discussed.

## 4. Denominators

Every rate is a rate **within a 1-in-88 block sample**, not a census.
`COORD_VERIFICATION_01_sweep_independence.md` (2026-09-16) records three 50,000-block sweeps at
stride 88; the sandwich manifest occupies 10,175 of its sweep's 50,000 blocks. **Sampling factor
88.** No rate is extrapolated to the full block range and no count is presented as a population
total.

## 5. Forbidden, and checkable against this document

- No new threshold, tolerance, tie-break, exclusion or stratum definition after opening the group map.
- No re-running of Task 07, any witness, or any acquisition.
- Nothing outside §2 reported as confirmatory. Anything outside §2 and §3 is **exploratory**,
  labelled so, and **may not appear in any conclusion** (P9).
- No case dropped from any denominator.
- No claim of `mechanically_confirmed` at any level of aggregation.
- The sealed holdout stays unread.

## 6. Stated in advance: the falsifier, with its critical value

Computed **blind**, before the join: 20,000 random draws of n = 258 from the frozen outcomes, seed
20260920, no label read. `out/.../08_analysis/null_distribution.json`.

| statistic | null SD | 95% band |
|---|---|---|
| support-share difference | **3.13 pp** | −6.23 / +5.97 |
| undecidable-share difference | **2.70 pp** | −5.08 / +5.15 |

Overall support is 44.51%, so **missed support must exceed 50.5% or fall below 38.3% to clear
chance** at α = 0.05 two-sided. (R2-07 quoted 38.5% for the lower bound; the 0.2 pp difference is
quantile rounding and is recorded rather than reconciled silently.)

**Falsifier.** If the composition-adjusted `missed` support share is at or below the `recorded`
share, **or** the difference lies within the permutation band, **the evidence does not support
treating the missed set as genuine-but-unrecorded.** Evaluated at the point estimate and at both
§3.3 bounds.

**The maximum claim a pass may support (P3).** `mechanically_confirmed` is unreachable, so **no
result of this study can license the claim that a missed case is genuine.** The ceiling, fixed here
in advance, is:

> A higher composition-adjusted support share among missed cases is **consistent with** the missed
> set containing genuine-but-unrecorded sandwiches, on trajectory and value-flow evidence alone,
> **without exact counterfactual mechanical confirmation for any case**, within a 1-in-88 block
> sample.

No stronger wording is available to Task 10 whatever the result.

**And the honest power statement (R2-07).** At n = 258 this comparison is **underpowered for
anything subtle**: a 3–4 pp difference is indistinguishable from noise. **A null result is
uninformative about small effects and must not be reported as evidence of absence.**

## 7. Blinding at the transition

The Task 07 seal is **inverted, not removed** (R2-07 G3): `group_map` drops out of `FORBIDDEN`,
`h4_holdout` is **retained**, and writes to any hash-pinned path are refused. **The write-refusal
is exercised by a fixture before the analysis runs** (P10). The join is one-way: labels enter the
analysis and nothing flows back into Task 07's output or any frozen input.

## 8. Supervisor

R2-07 verified this plan while still blinded. After this it takes on Task 09 and will see
group-linked results it cannot un-see, so this is the final blinded gate.

**Recorded, at R2-07's own instance:** a hash proves a file **unmodified, not unread**. Nothing
either agent can compute proves the latter. The evidence for blinding is structural — the armed
seal, the AST scan of the import graph, zero group or outcome tokens across all 17,637 output rows,
and the disclosures both agents filed. That is strong, and it is not proof, and neither agent
describes it as proof.
