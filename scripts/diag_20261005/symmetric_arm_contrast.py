import json, csv, collections, random, sys, math
REV = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
sys.path.insert(0, REV + "/scripts/trace_validation/08_analysis")
import run_task08 as T8
import pandas as pd
SEED, PERM, MIN_CELL = 20261013, 20000, 20

rows = [json.loads(l) for l in open(REV + "/out/trace_validation/07_execution/task07_outcomes.jsonl")]
import os
pc = {}
for l in open(REV + "/out/trace_validation/n2_valuation/n2_per_case.jsonl"):
    r = json.loads(l); pc[r["case_id"]] = r["primary"]["outcome"]
OVR = os.environ.get("OUTCOMES_OVERRIDE"); SUF = os.environ.get("OUT_SUFFIX", "")
if OVR:
    for l in open(OVR):
        r = json.loads(l); pc[r["case_id"]] = r["outcome"]
    print("outcomes overridden from", OVR)
man = {r["case_id"]: r for r in csv.DictReader(open(REV + "/data/trace_validation/manifests/v2/cases_blinded.csv"))}
gmap = {r["case_id"]: r["group"] for r in csv.DictReader(open(REV + "/data/trace_validation/group_map/v2/case_group_map.csv"))}
join = pd.read_csv(REV + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")[["case_id", "episode_id"]]
c2e = dict(zip(join.case_id, join.episode_id))
new = pd.read_csv(REV + "/out/diag_20261005/symmetric_rule_new_brackets.csv")
new_eps = set(new[new.covered & new.profitable].episode_id); assert len(new_eps) == 1384

def build(include_new, include_orig=True):
    recs = []
    for r in rows:
        c = r["case_id"]; g = gmap[c]; e = c2e.get(c)
        if g == "target_strict_miss" and include_orig: lab = "missed"
        elif g == "control_nearmiss" and e in new_eps and include_new: lab = "missed"
        elif g == "control_detected": lab = "recorded"
        else: continue
        out = pc.get(c, r["outcome"])
        actor = (r["value_flow"].get("metrics") or {}).get("actor") or ("na_" + c)
        recs.append(dict(lab=lab, sup=1 if out == "structurally_supported" else 0, und=1 if out == "undecidable" else 0,
                         st=T8.stratum(r["covariates"]), block=man[c]["block"], actor=actor))
    return recs

strata_all = [T8.stratum(r["covariates"]) for r in rows]
size = collections.Counter(strata_all)

def analyse(recs, label):
    per = collections.defaultdict(collections.Counter)
    for x in recs: per[x["st"]][x["lab"]] += 1
    included = {st for st in size if size[st] >= MIN_CELL and per[st]["missed"] > 0 and per[st]["recorded"] > 0}
    other = ("other",) * 5
    pooled = {st for st in size if st not in included}
    for x in recs:
        if x["st"] in pooled: x["st"] = other
    size2 = collections.Counter(other if st in pooled else st for st in strata_all)
    per = collections.defaultdict(collections.Counter)
    for x in recs: per[x["st"]][x["lab"]] += 1
    if size2[other] >= MIN_CELL and per[other]["missed"] > 0 and per[other]["recorded"] > 0: included.add(other)
    inc = sorted(included); weights = {st: size2[st] for st in inc}
    def sdiff(sample, inc_set, key="sup"):
        num = collections.defaultdict(lambda: [0, 0]); den = collections.defaultdict(lambda: [0, 0])
        for x in sample:
            if x["st"] not in inc_set: continue
            t = num[x["st"]] if x["lab"] == "missed" else den[x["st"]]; t[0] += x[key]; t[1] += 1
        wm = wr = tot = 0.0
        for st in sorted(inc_set):
            m, r = num[st], den[st]
            if m[1] == 0 or r[1] == 0: continue
            w = weights[st]; wm += w * m[0] / m[1]; wr += w * r[0] / r[1]; tot += w
        return (100 * (wm / tot - wr / tot), 100 * wm / tot, 100 * wr / tot) if tot else (None, None, None)
    full, lm, lr = sdiff(recs, set(inc))
    rnd = random.Random(SEED); bystr = collections.defaultdict(list)
    for x in recs: bystr[x["st"]].append(x)
    null = []
    for _ in range(PERM):
        perm = []
        for st in sorted(bystr):
            xs = bystr[st]; labs = [x["lab"] for x in xs]; rnd.shuffle(labs)
            perm.extend(dict(x, lab=l) for x, l in zip(xs, labs))
        d, _, _ = sdiff(perm, set(inc)); null.append(d)
    null.sort(); lo, hi = null[int(0.025 * PERM)], null[int(0.975 * PERM) - 1]
    p = (sum(abs(v) >= abs(full) for v in null) + 1) / (PERM + 1)
    und, _, _ = sdiff(recs, set(inc), "und")
    nm = sum(1 for x in recs if x["lab"] == "missed"); sm = sum(x["sup"] for x in recs if x["lab"] == "missed")
    nr = sum(1 for x in recs if x["lab"] == "recorded"); sr = sum(x["sup"] for x in recs if x["lab"] == "recorded")
    nlo, nhi = T8.newcombe(sm, nm, sr, nr)
    def cboot(key, B=2000):
        groups = collections.defaultdict(list)
        for x in recs: groups[x[key]].append(x)
        keys = list(groups); r2 = random.Random(SEED); out = []
        for _ in range(B):
            s = []
            for k in r2.choices(keys, k=len(keys)): s.extend(groups[k])
            d, _, _ = sdiff(s, set(inc))
            if d is not None: out.append(d)
        out.sort(); return out[int(.025 * len(out))], out[int(.975 * len(out))]
    loo = [sdiff(recs, set(inc) - {st})[0] for st in inc]
    res = dict(label=label, n_missed=nm, sup_missed=sm, n_recorded=nr, sup_recorded=sr, unadj_pp=100 * (sm / nm - sr / nr), newcombe=[nlo, nhi],
               standardized_pp=full, level_missed=lm, level_recorded=lr, strata=len(inc), perm_band=[lo, hi], perm_p=p, undecidable_gap_pp=und,
               block_boot=cboot("block"), actor_boot=cboot("actor"), loo_range=[min(v for v in loo if v is not None), max(v for v in loo if v is not None)],
               distinct_blocks=len({x["block"] for x in recs}), distinct_actors=len({x["actor"] for x in recs}))
    print(json.dumps(res, indent=1)); return res

out = {}
out["original_258"] = analyse(build(include_new=False), "original 258 vs recorded" + ("" if OVR else " (check: should reproduce -14.29)"))
out["symmetric_1642"] = analyse(build(include_new=True), "symmetric 1,642 vs recorded")
out["new_1384_only"] = analyse(build(include_new=True, include_orig=False), "new 1,384 only vs recorded")
json.dump(out, open(REV + "/out/diag_20261005/symmetric_arm_contrast%s.json" % SUF, "w"), indent=1)
print("written symmetric_arm_contrast.json")
