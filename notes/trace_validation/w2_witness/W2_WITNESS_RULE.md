# W2: registered revision of the trajectory witness, relative price floors

**Written 2026-10-14 by the assistant session on the workstation, after the author's decision of
2026-10-14 to register a witness revision and recompute rather than report the defect as a bound.** The
SHA-256 of this file and of `scripts/trace_validation/w2_witness/witness.py`, with the `date -Is` reading
at registration, are in `REGISTRATION.txt` beside it. The runner refuses to execute if either hash
differs. Author review of this text is pending; an amendment is a second registration.

## 0. Disclosure, stated first

The defect was found on 2026-10-13 through the explorer verification (`out/explorer_verification/`):
a blind automated reader called 98 of 100 record-absent brackets sandwiches and overturned 44 of the 53
record-absent rejections. The diagnostic (`scripts/diag_20261005/witness_rejection_diagnostic.py`) then
showed that 43 of those 53, 309 of the 532 recorded-arm rejections and 259 comparison-arm verdicts carry
the reason "opening not adverse to victim" although the relative price move is 0.5% to 5%. **The
direction of this revision's effect was therefore known before it was written**: it will turn an
unknown number of rejections into supported or undecidable outcomes in every arm. What protects it is
that it changes no threshold and no condition; it restores the floor the frozen configuration already
documents (`price_epsilon_relative`) where the code applied it as an absolute floor.

## 1. The defect, exactly

`witness.py` (frozen, sha256 634deca5…) tests T3 with

    if abs(move) <= PRICE_EPS * max(abs(p_pre), 1.0):   # PRICE_EPS = 1e-12

and T4b with

    frac = (reverted / denom) if denom > PRICE_EPS else None

Price is token1 per token0 in raw units. On a pool whose token1 has 6 decimals and token0 has 18
(USDC, USDT quoted pools), the raw price is of order 1e-12 to 1e-14, so `max(abs(p_pre), 1.0)` makes the
first test an absolute floor of 1e-12 and any move on such a pool is "below epsilon"; the second test
then discards the reversal denominator for the same reason. The witness returns `negative` with
"opening_not_adverse_to_victim" regardless of the sign of the move. These pools enter the study as the
shared pool when a leg routes through a stablecoin (WETH to USDT to the token), which is why the defect
tracks routed brackets: 38 of the 43 affected record-absent cases are routed.

## 2. The revision

Two lines, nothing else:

    if abs(move) <= PRICE_EPS * abs(p_pre):
    ...
    p_ref = p_pre if p_pre is not None else p_open
    frac = (reverted / denom) if denom > PRICE_EPS * abs(p_ref) else None

`p_pre` and `p_open` are positive whenever reached (reserves and sqrt prices are positive). The frozen
`PRICE_EPS` (1e-12), `REVERSAL_MIN_FRACTION` (0.10), the orientation, the shared-pool rule, the venue
rule and the verdict precedence are unchanged. The 42 frozen fixtures must pass on the revised file.

## 3. What is recomputed, and how

`run_w2.py` reads the frozen Task 07 outcomes, re-evaluates the trajectory of every one of the 17,637
cases with the frozen witness first (every state must reproduce, or the runner aborts) and then with the
revised witness, keeps the value-flow state exactly as N2 left it (the registered valuation rule is not
touched), applies the frozen `_outcome` precedence, and writes one outcome per case. The Task 08
estimator is then applied to the three contrasts already reported (258, 1,642 and 1,384 new, each
against the recorded arm), and the magnitudes are recomputed over the W2-supported sets. The N2 results
stay in the paper as the registered pre-revision result, in the same way the frozen Task 07 table stays
beside N2.

## 4. What is not claimed

The revision does not make any case mechanically confirmed, does not change which brackets the rules
accept, and does not touch the record comparison. A case the revised witness moves from rejected to
undecidable is reported as undecidable.
