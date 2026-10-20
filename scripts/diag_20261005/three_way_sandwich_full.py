import os
"""Three records on the same blocks: Weintraub (D), the Flashbots mev-inspect classifier (M), and the
canonical rule (C). Sandwich brackets keyed on (front, back) transaction hashes. All 50,000 swept blocks
(every C bracket lives there; M and D restricted to them)."""
import json, pandas as pd, collections
R = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
man = set(int(l) for l in open(R + "/out/mev_inspect/blocks_rep_sweep_manifest_first.txt").read().split())
M = []
for l in open(R + "/out/mev_inspect/rep_sweep.jsonl"):
    r = json.loads(l)
    if r["block"] not in man or "error" in r: continue
    for s in r["sandwiches"]:
        M.append(dict(block=r["block"], front=s["front"].lower(), back=s["back"].lower(), victims=[v.lower() for v in s["victims"]], pool=s["pool"].lower()))
M = pd.DataFrame(M); M["key"] = list(zip(M.front, M.back))
C = pd.read_csv(R + "/out/h3_brackets_rep.csv"); C["front"] = C.front.str.lower(); C["back"] = C.back.str.lower(); C["victim"] = C.victim.str.lower(); C["key"] = list(zip(C.front, C.back))
D = pd.read_csv(R + "/out/diag_20261005/record_sandwiches_on_lattice6.csv"); D = D[D.block.isin(man)].copy(); D["key"] = list(zip(D.front.str.lower(), D.back.str.lower()))
Mk, Ck, Dk = set(M.key), set(C.key), set(D.key)
Mfb = set(M.front) | set(M.back); Cfb = set(C.front) | set(C.back); Dfb = set(D.front.str.lower()) | set(D.back.str.lower())
print("manifest blocks:", len(man))
print("M (mev-inspect) sandwiches:", len(M), "distinct (front,back):", len(Mk))
print("C (rule) brackets:", len(C), "distinct (front,back):", len(Ck))
print("D (Weintraub) triplets:", len(D), "distinct (front,back):", len(Dk))
print()
print("exact (front,back) overlaps: M&C", len(Mk & Ck), " M&D", len(Mk & Dk), " C&D", len(Ck & Dk), " all three", len(Mk & Ck & Dk))
print("M only", len(Mk - Ck - Dk), " C only", len(Ck - Mk - Dk), " D only", len(Dk - Mk - Ck))
def legs_in(keys, fb): return sum(1 for f, b in keys if f in fb and b in fb)
print()
print("looser: M brackets whose front AND back appear as legs in C:", legs_in(Mk, Cfb), "of", len(Mk), "; in D:", legs_in(Mk, Dfb))
print("D brackets whose legs appear in M:", legs_in(Dk, Mfb), "of", len(Dk), "; in C:", legs_in(Dk, Cfb))
print("C brackets whose legs appear in M:", legs_in(Ck, Mfb), "of", len(Ck), "; in D:", legs_in(Ck, Dfb))
co = pd.concat([pd.read_csv(R + "/out/s0val/cohort_%s_v2.csv" % g).assign(arm=g) for g in ("target_strict_miss", "control_detected")])
co["key"] = list(zip(co.front.str.lower(), co.back.str.lower()))
co["in_M_exact"] = co.key.isin(Mk); co["in_M_legs"] = [(f.lower() in Mfb and b.lower() in Mfb) for f, b in zip(co.front, co.back)]
print()
print("Weintraub-absent 258: found by mev-inspect exact", int(co[co.arm == "target_strict_miss"].in_M_exact.sum()), " by legs", int(co[co.arm == "target_strict_miss"].in_M_legs.sum()))
print("Weintraub-recorded 10,299: found by mev-inspect exact", int(co[co.arm == "control_detected"].in_M_exact.sum()), " by legs", int(co[co.arm == "control_detected"].in_M_legs.sum()))
lk = pd.read_csv(R + "/out/diag_20261005/sandwich_linkage.csv")[["episode_id", "front_pools", "back_pools", "token_amount_within_1pct"]]
n2 = pd.read_csv(R + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")[["episode_id", "n2_outcome"]]
a = co[co.arm == "target_strict_miss"].merge(lk, on="episode_id", how="left").merge(n2, on="episode_id", how="left")
a["multi_pool"] = (a.front_pools >= 2) | (a.back_pools >= 2); a["mismatch"] = ~a.token_amount_within_1pct.astype(bool)
print()
print("absent 258 by mev-inspect (legs) x structural cause:"); print(pd.crosstab([a.multi_pool, a.mismatch], a.in_M_legs))
print("absent 258 by mev-inspect (legs) x N2 outcome:"); print(pd.crosstab(a.n2_outcome, a.in_M_legs))
mo = M[~M.key.isin(Ck)].copy(); mo["in_D_legs"] = [(f in Dfb and b in Dfb) for f, b in zip(mo.front, mo.back)]
mo["front_in_C_legs"] = mo.front.isin(Cfb); mo["back_in_C_legs"] = mo.back.isin(Cfb)
print()
print("M-only (not an exact C bracket):", len(mo), "; of which legs in D:", int(mo.in_D_legs.sum()), "; front leg in some C bracket:", int(mo.front_in_C_legs.sum()), "; neither leg in C:", int((~mo.front_in_C_legs & ~mo.back_in_C_legs).sum()))
print("M-only with 2+ victims:", int((mo.victims.map(len) >= 2).sum()), "; same pool as a C bracket in the same block:", int(mo.apply(lambda r: ((C.block == r.block)).any(), axis=1).sum()))
M.to_csv(R + "/out/diag_20261005/mev_inspect_sandwiches_full.csv", index=False); mo.to_csv(R + "/out/diag_20261005/mev_inspect_only_full.csv", index=False)
