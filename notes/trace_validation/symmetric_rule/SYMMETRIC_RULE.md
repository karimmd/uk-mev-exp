# Registered revision of the canonical sandwich rule: direction-symmetric position conjunct

**Written on 2026-10-13 by the assistant session on the workstation, after the author's decision of the
same day to report the pre-specified rule as the registered coverage result and this rule as a revision
found by the cross-record comparison.** The SHA-256 of this file and the `date -Is` reading at
registration are in `REGISTRATION.txt` beside it. Any change to this file is a new registration.

## 0. Disclosure, stated first

This rule was not pre-specified. It was derived on 2026-10-12 from the comparison arm of the actor-side
adjudication, which was itself a pre-specified arm (every sandwich conjunct except the closing reversal,
7,080 cases, fully adjudicated before this revision was conceived). The three-record comparison of
`CROSS_RECORD_2026-10-12.md` showed that the Flashbots mev-inspect classifier calls 1,543 of the 1,638
sell-first comparison brackets and 249 of the 362 WETH-side brackets sandwiches, and that the adjudicator
supports 919 and 318 of them. The coverage figures under this rule (`symmetric_rule_coverage.py`,
`out/diag_20261005/symmetric_rule_coverage.log`: 1,642 of 12,671 absent, 12.96%; 1,297 supported) were
computed from adjudications already on disk and **were seen before this registration**. What protects
the revision is that it relaxes exactly one conjunct, has no parameter, and was motivated by an
independent detector's disagreement rather than by the size of the omission it reveals. A reader who
regards a rule registered after its effect was seen as exploratory should read every number under it as
a revision of the registered result, which is how the manuscript labels it.

## 1. The pre-specified rule (unchanged, Section 4.1 of the manuscript)

A triplet is accepted when all six conjuncts hold: (1) the three transactions share a block; (2) the
front index precedes the victim index, which precedes the back index; (3) the front and back legs have
the same economic actor (`catalog._economic_actor`); (4) all three touch a common pool; (5) some
non-WETH token opens a **positive** net position for the actor in the front leg and closes it
**negative** in the back leg; (6) no leg reverted.

## 2. The revision: conjunct (5) made direction-symmetric

Conjunct (5) is replaced by: some token opens a non-zero net position for the actor in the front leg and
closes it with the opposite sign in the back leg. Three patterns satisfy it; the other five conjuncts
are untouched. With the actor's per-token net transfer deltas dF (front) and dB (back), computed as in
`reversal_direction.py`:

- **buy-first** (the pre-specified pattern): some non-WETH token t has dF[t] > 0 and dB[t] < 0;
- **sell-first**: some non-WETH token t has dF[t] < 0 and dB[t] > 0;
- **WETH-side**: the actor's non-WETH deltas are empty in both legs and WETH moves in at least one leg
  (the position asset is WETH on a pool not quoted in WETH).

Patterns are evaluated in that order and a bracket takes the first that applies, exactly as the
pattern column of `out/diag_20261005/comparison_arm_patterns.csv` was produced.

## 3. Population, denominators and what is recomputed

- The strict population keeps its two restrictions: every pool of the bracket appears somewhere in the
  record (covered venue), and the actor's WETH net across front and back minus gas is positive
  (profitable after observable gas). Profit is computed as in `symmetric_rule_coverage.py`.
- Absence, recorded and partially recorded keep their definitions (no leg, all legs, one or two legs in
  the record).
- The adjudicator is not changed. The outcomes of the newly admitted brackets are their existing N2
  outcomes, read from `n2_case_level_join.csv`; no case is re-adjudicated.
- Reported under this rule: the strict absence rate with Wilson and block-clustered intervals, the
  enlarged absent arm's outcome shares, omitted sandwiches per 1,000 blocks, and the mev-inspect
  agreement on the new brackets. Explorer verification of a 100-bracket sample of the new brackets
  follows the registered protocol in `notes/explorer_verification/`.

## 4. What is not claimed

The revised rule does not make the record's buy-first omissions more or less supported than before; the
258 and their outcomes are unchanged. It does not alter the arbitrage or liquidation rules. It does not
claim completeness: a sandwich whose position asset moves in neither direction pattern above, or whose
legs the economic-actor rule attributes to different actors, is outside both rules.
