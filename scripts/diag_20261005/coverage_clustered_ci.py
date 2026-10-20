import os
"""Block-clustered bootstrap intervals for the strict sandwich absence rate under the pre-specified
rule (258 / 11,287) and under the direction-symmetric rule (1,642 / 12,671). Blocks are resampled with
replacement; the rate is recomputed on each draw. Also prints the Wilson interval for comparison.

Population under the pre-specified rule: profitable brackets on a covered venue, 11,287 = 258 absent
+ 10,299 recorded + 730 partially recorded. The absent and recorded members come from the s0val cohort
files; the partially recorded members are the h3 brackets with profit > 0 and one or two legs in the
record, whose count is asserted to be 730 before use.
"""
import math, random, sys, pandas as pd
R = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
SEED, B = 20261013, 10000

h3 = pd.read_csv(R + "/out/h3_brackets_rep.csv")
h3["key"] = list(zip(h3.front.str.lower(), h3.victim.str.lower(), h3.back.str.lower()))
absent = pd.read_csv(R + "/out/s0val/cohort_target_strict_miss_v2.csv")
rec = pd.read_csv(R + "/out/s0val/cohort_control_detected_v2.csv")
akeys = set(zip(absent.front.str.lower(), absent.victim.str.lower(), absent.back.str.lower()))
rkeys = set(zip(rec.front.str.lower(), rec.victim.str.lower(), rec.back.str.lower()))
prof = h3[h3.profit_eth > 0]
partial = prof[prof.n_in_mined.isin([1, 2]) & ~prof.key.isin(akeys) & ~prof.key.isin(rkeys)]
print("absent", len(akeys), "recorded", len(rkeys), "partial candidates", len(partial))
assert len(akeys) == 258 and len(rkeys) == 10299
if len(partial) != 730:
    print("WARNING: partial count differs from 730; using", len(partial))

rows = [(b, 1) for b in absent.block] + [(b, 0) for b in rec.block] + [(b, 0) for b in partial.block]
orig = pd.DataFrame(rows, columns=["block", "absent"])
new = pd.read_csv(R + "/out/diag_20261005/symmetric_rule_new_brackets.csv")
new = new[new.covered & new.profitable]
assert len(new) == 1384
sym = pd.concat([orig, pd.DataFrame({"block": new.block, "absent": 1})], ignore_index=True)

def wilson(k, n, z=1.959964):
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * (c - h), 100 * (c + h)

def block_boot(df, label):
    g = df.groupby("block").agg(n=("absent", "size"), k=("absent", "sum")).reset_index()
    rnd = random.Random(SEED); nb = len(g); ns = g.n.tolist(); ks = g.k.tolist()
    rates = []
    for _ in range(B):
        idx = [rnd.randrange(nb) for _ in range(nb)]
        n = sum(ns[i] for i in idx); k = sum(ks[i] for i in idx)
        rates.append(100 * k / n)
    rates.sort()
    k, n = int(df.absent.sum()), len(df)
    lo, hi = rates[int(0.025 * B)], rates[int(0.975 * B) - 1]
    wl, wh = wilson(k, n)
    print("%s: %d / %d = %.2f%% | Wilson [%.2f, %.2f] | block-clustered bootstrap [%.2f, %.2f] (%d blocks, %d draws, seed %d)" % (label, k, n, 100 * k / n, wl, wh, lo, hi, nb, B, SEED))

block_boot(orig, "pre-specified rule")
block_boot(sym, "symmetric rule")
print("per 1,000 swept blocks (50,000): pre-specified %.1f, symmetric %.1f" % (258 / 50, 1642 / 50))
