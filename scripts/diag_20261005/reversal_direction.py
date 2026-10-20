import os
"""Do the comparison-arm brackets that mev-inspect calls sandwiches open a position by SELLING a token
first (sell-first sandwich), which the reversal conjunct (positive in front, negative in back) cannot
accept? Classify every comparison-arm bracket by the actor's non-WETH position pattern."""
import json, glob, gzip, sys, pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); R = ROOT + "/revision"
sys.path.insert(0, R + "/scripts"); from catalog import _economic_actor
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
nm = pd.read_csv(R + "/out/s0val/cohort_control_nearmiss_v2.csv")
n2 = pd.read_csv(R + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")[["episode_id", "n2_outcome"]]
nm = nm.merge(n2, on="episode_id", how="left")
M = pd.read_csv(R + "/out/diag_20261005/mev_inspect_sandwiches_manifest.csv"); Mk = set(zip(M.front, M.back))
D = pd.read_csv(R + "/out/diag_20261005/record_sandwiches_on_lattice6.csv")
Dk = set(zip(D.front.str.lower(), D.back.str.lower())); Dfb = set(D.front.str.lower()) | set(D.back.str.lower())
nm["key"] = list(zip(nm.front.str.lower(), nm.back.str.lower()))
nm["in_M"] = nm.key.isin(Mk); nm["in_D"] = nm.key.isin(Dk)
nm["legs_in_D"] = [(f.lower() in Dfb and b.lower() in Dfb) for f, b in zip(nm.front, nm.back)]
want = set(nm.front.str.lower()) | set(nm.back.str.lower()); store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in want: store[x["hash"].lower()] = x


def deltas(E, a):
    d = {}
    for tok, frm, to, amt in E["transfers"]:
        if frm == a: d[tok] = d.get(tok, 0) - int(amt)
        if to == a: d[tok] = d.get(tok, 0) + int(amt)
    return d


pat = []
for r in nm.itertuples():
    F = store.get(r.front.lower()); B = store.get(r.back.lower())
    if not (F and B): pat.append("no_evidence"); continue
    aF, aB = _economic_actor(F), _economic_actor(B); dF, dB = deltas(F, aF), deltas(B, aB)
    toks = {t for t in set(dF) | set(dB) if t != WETH}
    buy_first = any(dF.get(t, 0) > 0 and dB.get(t, 0) < 0 for t in toks)
    sell_first = any(dF.get(t, 0) < 0 and dB.get(t, 0) > 0 for t in toks)
    weth_only = (not toks) and (WETH in dF or WETH in dB)
    pat.append("buy_first" if buy_first else "sell_first" if sell_first else "weth_only" if weth_only else "same_direction_or_other")
nm["pattern"] = pat
print("comparison arm by position pattern x mev-inspect call:"); print(pd.crosstab(nm.pattern, nm.in_M, margins=True))
print("\nN2 outcome by pattern (comparison arm):"); print(pd.crosstab(nm.pattern, nm.n2_outcome))
sf = nm[nm.pattern == "sell_first"]
print("\nsell-first brackets:", len(sf), "| in Weintraub exact", int(sf.in_D.sum()), "| legs in Weintraub", int(sf.legs_in_D.sum()))
print("sell-first AND mev-inspect: N2 outcomes"); print(sf[sf.in_M].n2_outcome.value_counts())
print("sell-first, not mev-inspect: N2 outcomes"); print(sf[~sf.in_M].n2_outcome.value_counts())
print("\nmev-inspect-called comparison cases by pattern x N2:"); print(pd.crosstab(nm[nm.in_M].pattern, nm[nm.in_M].n2_outcome))
nm.to_csv(R + "/out/diag_20261005/comparison_arm_patterns.csv", index=False)
