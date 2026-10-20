import os
"""Decode the largest absent arbitrages that chain exactly (slack <= 1e-6), to see whether the
profit that survives the tolerance check is genuine arbitrage."""
import json, glob, gzip, sys
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"
sys.path.insert(0, REV + "/scripts"); from catalog import _economic_actor
meta = json.load(open(REV + "/data/f1b/token_meta.json"))
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
def fmt(t, a):
    m = meta.get(t) or {}; s = m.get("symbol") or t[:8]; d = m.get("decimals")
    return ("%.4f %s" % (int(a) / 10 ** d, s)) if d is not None else ("%d raw %s" % (int(a), s))
d = pd.read_csv(REV + "/out/diag_20261005/arbitrage_tolerance.csv")
o = pd.read_csv(REV + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")[["hash", "block", "n_pools", "first_conjunctive"]]
d = d.merge(o, on="hash")
top = d[d.absent & d.p4 & (d.slack <= 1e-6)].nlargest(6, "profit")
print("absent, exact-chained, top 6 by profit: total of this subset %.1f ETH of %.1f" % (top.profit.sum(), d[d.absent & d.p4 & (d.slack <= 1e-6)].profit.sum()))
want = set(top.hash.str.lower()); store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in want: store[x["hash"].lower()] = x
for r in top.itertuples():
    E = store[r.hash.lower()]; a = _economic_actor(E)
    print(f"\n{r.hash} block {r.block} idx {E['index']} profit {r.profit:.3f} ETH pools {r.n_pools} first={r.first_conjunctive} gas {E['gas_used']}@{int(E['gas_price'])/1e9:.1f}gwei to {(E.get('to') or '')[:12]} actor {a[:12]}")
    for tok, frm, to, amt in E["transfers"]:
        tag = "ACTOR->" if frm == a else ("->ACTOR" if to == a else "")
        print(f"   {fmt(tok, amt):>34s}  {frm[:8]} -> {to[:8]} {tag}")
print("\nabsent P4 profit by slack class: exact(<=1e-6) %.1f ETH (n=%d); slack>1e-6 %.1f ETH (n=%d)" % (
    d[d.absent & d.p4 & (d.slack <= 1e-6)].profit.sum(), (d.absent & d.p4 & (d.slack <= 1e-6)).sum(),
    d[d.absent & d.p4 & (d.slack > 1e-6)].profit.sum(), (d.absent & d.p4 & (d.slack > 1e-6)).sum()))
print("median absent P4 profit, exact-chained: %.4f ETH; present: %.4f ETH" % (d[d.absent & d.p4 & (d.slack <= 1e-6)].profit.median(), d[~d.absent & d.p4].profit.median()))
