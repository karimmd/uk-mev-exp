import os
"""E4b. The arbitrages mev-inspect finds on the residue-50 sweep that are not among the rule's candidate
rows: are they in the evidence store, and which conjunct of the canonical arbitrage rule do they fail?
Mirrors m_only_breakdown_full.py for sandwiches. Also reports how many become cyclic under a looser
pass-through tolerance, and how many have a WETH profit above gas by the classifier's own figure.
"""
import json, glob, gzip, sys, collections
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); R = ROOT + "/revision"
sys.path.insert(0, R + "/scripts"); from catalog import match_arbitrage, _economic_actor
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
M = pd.read_csv(R + "/out/diag_20261005/mev_inspect_arbitrages_sweep50.csv")
o = pd.read_csv(R + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv"); cand = set(o.hash.str.lower())
mo = M[~M.hash.isin(cand)].drop_duplicates("hash").copy()
print("mev-inspect arbitrages:", len(M), "| not among rule candidates (distinct):", len(mo))
want = set(mo.hash); store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            if not line.strip(): continue
            x = json.loads(line)
            if x["hash"].lower() in want: store[x["hash"].lower()] = x
print("in the evidence store (swap-bearing, decoded):", len(store), "| not in store:", len(mo) - len(store))
res = collections.Counter(); loose = collections.Counter(); prof = []
for h in store:
    ev = store[h]; r = match_arbitrage(ev)
    key = "matches" if r["matched"] else "fail:" + ",".join(r["failed"])
    res[key] += 1
    if not r["matched"] and "cyclic" in r["failed"]:
        r2 = match_arbitrage(ev, rel_tol=0.10)
        loose["cyclic at 10%" if r2["predicates"]["cyclic"] else "still not cyclic at 10%"] += 1
    if r["profit_eth"] is not None: prof.append(r["profit_eth"])
print("\nrule verdict on the M-only transactions in the store:")
for k, v in res.most_common(): print("  %6d  %s" % (v, k))
print("\nof those failing 'cyclic' at the shipped 2%% tolerance:", dict(loose))
mo["profit_amount"] = pd.to_numeric(mo.profit_amount, errors="coerce")
w = mo[mo.profit_token.str.lower() == WETH]
print("\nclassifier's own profit on M-only with WETH profit token: n=%d, median %.4f ETH, total %.1f ETH, share with profit > 0.001 ETH: %.1f%%" % (
    len(w), (w.profit_amount / 1e18).median(), (w.profit_amount / 1e18).sum(), 100 * ((w.profit_amount / 1e18) > 0.001).mean()))
print("M-only by n_pools:", mo.n_pools.value_counts().sort_index().to_dict(), "| by n_swaps:", mo.n_swaps.value_counts().sort_index().head(8).to_dict())
pools_in_store = sum(1 for h in store if len(set(store[h].get("pools") or [])) >= 2)
print("M-only in store with 2+ decoded pools:", pools_in_store)
json.dump({"M_only": int(len(mo)), "in_store": len(store), "verdicts": dict(res), "loose_tolerance": dict(loose)}, open(R + "/out/diag_20261005/arbitrage_m_only_breakdown.json", "w"), indent=1)
print("written arbitrage_m_only_breakdown.json")
