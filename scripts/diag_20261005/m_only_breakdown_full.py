import os
"""Why does the rule not accept the 1,919 mev-inspect sandwiches it lacks? And why does mev-inspect lack
1,509 rule brackets? Venue aperture first, then conjunct failures where the evidence exists."""
import json, glob, gzip, sys, collections
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); R = ROOT + "/revision"
sys.path.insert(0, R + "/scripts"); from catalog import match_sandwich
mo = pd.read_csv(R + "/out/diag_20261005/mev_inspect_only_full.csv")
import ast as _ast
want = set(mo.front) | set(mo.back) | {v for vs in mo.victims for v in (_ast.literal_eval(vs) if isinstance(vs, str) else vs)}; store = {}; pools_in_store = set()
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line); pools_in_store.update(x["pools"])
            if x["hash"].lower() in want: store[x["hash"].lower()] = x
mo["pool_in_store"] = mo.pool.isin(pools_in_store)
mo["front_in_store"] = mo.front.isin(store); mo["back_in_store"] = mo.back.isin(store)
print("M-only:", len(mo))
print("  pool is a V2/V3-like pool the store decodes:", int(mo.pool_in_store.sum()))
print("  front and back transactions both in the evidence store:", int((mo.front_in_store & mo.back_in_store).sum()))
import ast
fails = collections.Counter(); n_eval = 0
for r in mo.itertuples():
    F = store.get(r.front); B = store.get(r.back)
    vs = ast.literal_eval(r.victims) if isinstance(r.victims, str) else r.victims
    V = None
    for v in vs:
        if v in store: V = store[v]; break
    if not (F and B): fails["leg_not_in_store"] += 1; continue
    if not V: fails["victim_not_in_store"] += 1; continue
    m = match_sandwich(F, V, B); n_eval += 1
    fails["MATCH" if m["matched"] else "fail:" + ",".join(m["failed"])] += 1
print("  rule evaluated on", n_eval, "; outcomes:"); 
for k, v in fails.most_common(12): print("   ", v, k)
C = pd.read_csv(R + "/out/h3_brackets_rep.csv"); C["front"] = C.front.str.lower(); C["back"] = C.back.str.lower()
M = pd.read_csv(R + "/out/diag_20261005/mev_inspect_sandwiches_full.csv"); Mk = set(zip(M.front, M.back))
D = pd.read_csv(R + "/out/diag_20261005/record_sandwiches_on_lattice6.csv"); Dk = set(zip(D.front.str.lower(), D.back.str.lower()))
C["key"] = list(zip(C.front, C.back)); co = C[~C.key.isin(Mk) & ~C.key.isin(Dk)]
print()
print("C-only brackets (neither record):", len(co), "; profitable after gas:", int((co.profit_eth > 0).sum()), "; fully_mined flag:", int(co.fully_mined.sum()))
s0 = pd.concat([pd.read_csv(R + "/out/s0val/cohort_%s_v2.csv" % g).assign(arm=g) for g in ("target_strict_miss", "control_detected")])
s0["key"] = list(zip(s0.front.str.lower(), s0.back.str.lower()))
print("  of which in the covered-venue profitable population (258 strict absent):", int(co.key.isin(set(s0[s0.arm == "target_strict_miss"].key)).sum()))
print("  C-only brackets with 2+ swaps in the front leg (routed) share:", round(float(co.front.map(lambda h: len(store[h]["pools"]) if h in store else 0).ge(2).mean()), 3) if len(co) else None)
