import os
"""Is the Weintraub record one-directional? Classify its own triplets on the lattice by the actor
position pattern (buy-first: token bought in front, sold in back; sell-first: the reverse)."""
import json, glob, gzip, sys, pandas as pd, collections
ROOT = os.environ.get("MEV_ROOT", "."); R = ROOT + "/revision"
sys.path.insert(0, R + "/scripts"); from catalog import _economic_actor
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
D = pd.read_csv(R + "/out/diag_20261005/record_sandwiches_on_lattice6.csv")
want = set(D.front.str.lower()) | set(D.back.str.lower()); store = {}
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
c = collections.Counter()
for r in D.itertuples():
    F = store.get(r.front.lower()); B = store.get(r.back.lower())
    if not (F and B): c["no_evidence"] += 1; continue
    aF, aB = _economic_actor(F), _economic_actor(B); dF, dB = deltas(F, aF), deltas(B, aB)
    toks = {t for t in set(dF) | set(dB) if t != WETH}
    bf = any(dF.get(t, 0) > 0 and dB.get(t, 0) < 0 for t in toks); sf = any(dF.get(t, 0) < 0 and dB.get(t, 0) > 0 for t in toks)
    c["buy_first" if bf else "sell_first" if sf else "weth_only" if not toks else "other"] += 1
print("Weintraub record triplets on the lattice by direction:", dict(c), "of", len(D))
