import os
"""What the coverage audit looks like if the reversal conjunct is made direction-symmetric and the
position asset may be either pool token. The comparison arm already holds every bracket that passes
all conjuncts except reversal and was fully adjudicated, so the enlarged population can be built from
existing outcomes without a new run. Reports: venue coverage, profitability after observable gas,
presence in Weintraub (D) and in mev-inspect (M), and the N2 outcome, for the newly admitted brackets.
"""
import json, glob, gzip, sys, pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); R = ROOT + "/revision"
sys.path.insert(0, R + "/scripts"); from catalog import _economic_actor
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
nm = pd.read_csv(R + "/out/diag_20261005/comparison_arm_patterns.csv")
new = nm[nm.pattern.isin(["sell_first", "weth_only"])].copy()
want = set(new.front.str.lower()) | set(new.back.str.lower()); store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in want: store[x["hash"].lower()] = x
prof = []
for r in new.itertuples():
    F = store[r.front.lower()]; B = store[r.back.lower()]
    aF, aB = _economic_actor(F), _economic_actor(B); w = 0
    for E, a in ((F, aF), (B, aB)):
        for tok, frm, to, amt in E["transfers"]:
            if tok == WETH and to == a: w += int(amt)
            if tok == WETH and frm == a: w -= int(amt)
    gas = F["gas_used"] * int(F["gas_price"]) + B["gas_used"] * int(B["gas_price"])
    prof.append((w - gas) / 1e18)
new["profit_eth"] = prof
new["covered"] = new.pools_covered.notna() & (new.pools_covered.astype(str).str.len() > 2)
new["profitable"] = new.profit_eth > 0
print("newly admitted brackets (sell-first or WETH-side position):", len(new))
print(pd.crosstab([new.pattern, new.covered], new.profitable, margins=True))
strict = new[new.covered & new.profitable]
print("\nstrict (covered venue, profitable after gas):", len(strict), "| in Weintraub exact:", int(strict.in_D.sum()), "legs in Weintraub:", int(strict.legs_in_D.sum()), "| called by mev-inspect:", int(strict.in_M.sum()))
print("N2 outcome of the strict new brackets:"); print(pd.crosstab(strict.pattern, strict.n2_outcome, margins=True))
print("\nweth_only brackets: in Weintraub exact", int(new[new.pattern == "weth_only"].in_D.sum()), "legs", int(new[new.pattern == "weth_only"].legs_in_D.sum()))
old_abs, old_rec, old_part = 258, 10299, 730
k = int((~strict.legs_in_D).sum()); kr = int(strict.legs_in_D.sum())
print("\nSYMMETRIC-RULE COVERAGE (strict population): old 258/11,287 = 2.29%%; new absent = 258 + %d, new population = 11,287 + %d" % (k, len(strict)))
print("  new strict absence rate: %.2f%%" % (100 * (old_abs + k) / (11287 + len(strict))))
sup_new = int((strict[~strict.legs_in_D].n2_outcome == "structurally_supported").sum()); rej_new = int((strict[~strict.legs_in_D].n2_outcome == "rejected").sum())
print("  enlarged absent arm: supported %d + %d = %d of %d (%.1f%%), rejected %d + %d, undecidable %d" % (177, sup_new, 177 + sup_new, 258 + k, 100 * (177 + sup_new) / (258 + k), 53, rej_new, (258 + k) - (177 + sup_new) - (53 + rej_new)))
print("  per 1,000 blocks: absent sandwiches %.1f (was 5.2)" % ((258 + k) / 50))
new.to_csv(R + "/out/diag_20261005/symmetric_rule_new_brackets.csv", index=False)
