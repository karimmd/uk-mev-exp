import os
"""Where do the actor inflows of closure-qualified arbitrage come from? A canonical arbitrage receives
every token from a pool it swapped on. Inflows from the zero address (mints) or from non-pool
addresses (claims, flash loans, transfers in) are structurally different, and the record would not
chain them. Share by arm."""
import json, glob, gzip, sys, collections
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"
sys.path.insert(0, REV + "/scripts"); from catalog import _economic_actor
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"; ZERO = "0x" + "0" * 40
o = pd.read_csv(REV + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")
o = o[o.in_P2_broad_closure == True]
want = set(o.hash.str.lower()); store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in want: store[x["hash"].lower()] = x
rows = []
for r in o.itertuples():
    E = store[r.hash.lower()]; a = _economic_actor(E); pools = set(E["pools"])
    inflow_src = [frm for tok, frm, to, amt in E["transfers"] if to == a]
    outflow_dst = [to for tok, frm, to, amt in E["transfers"] if frm == a]
    rows.append(dict(absent=not r.in_records, p4=bool(r.in_P4_profitable_closure), first=bool(r.first_conjunctive), contested=bool(r.contested),
        mint_in=any(f == ZERO for f in inflow_src), nonpool_in=any(f not in pools and f != ZERO for f in inflow_src),
        all_in_from_pools=all(f in pools for f in inflow_src) and bool(inflow_src),
        all_out_to_pools=all(t in pools for t in outflow_dst) and bool(outflow_dst),
        burn_out=any(t == ZERO for t in outflow_dst)))
d = pd.DataFrame(rows)
print("P2 closure-qualified, shares by arm (absent=True is record-absent):")
print(d.groupby("absent")[["mint_in", "nonpool_in", "all_in_from_pools", "all_out_to_pools", "burn_out"]].mean().round(4).T)
d["canonical_flow"] = d.all_in_from_pools & d.all_out_to_pools
print("\ncanonical flow (every actor inflow from a swapped pool and every outflow to one):")
print(d.groupby("absent").canonical_flow.agg(["mean", "sum", "count"]))
c = d[d.canonical_flow]
print("\nabsence rate among canonical-flow P2: %.2f%% (%d/%d); among non-canonical-flow: %.2f%% (%d/%d)" % (
    100 * c.absent.mean(), c.absent.sum(), len(c), 100 * d[~d.canonical_flow].absent.mean(), d[~d.canonical_flow].absent.sum(), (~d.canonical_flow).sum()))
cc = c[c.contested]
print("first-on-all-pools among canonical-flow contested: absent %.1f%% (n=%d) vs present %.1f%% (n=%d)" % (
    100 * cc[cc.absent]["first"].mean(), cc.absent.sum(), 100 * cc[~cc.absent]["first"].mean(), (~cc.absent).sum()))
p4 = d[d.p4]
print("\nP4 absent: canonical flow %d of %d; non-canonical %d" % (p4[p4.absent].canonical_flow.sum(), p4.absent.sum(), (p4.absent & ~p4.canonical_flow).sum()))
d.to_csv(REV + "/out/diag_20261005/arbitrage_inflow_sources.csv", index=False)
