import collections, csv, hashlib, importlib.util, json, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
REV = os.path.abspath(os.path.join(HERE, "../../.."))
sys.path.insert(0, os.path.join(REV, "scripts/trace_validation/value_flow_v2"))
sys.path.insert(0, os.path.join(REV, "scripts/trace_validation/07_execution"))
RULE = os.path.join(REV, "notes/trace_validation/w2_witness/W2_WITNESS_RULE.md")
REG = os.path.join(REV, "notes/trace_validation/w2_witness/REGISTRATION.txt")
OUT = os.path.join(REV, "out/trace_validation/w2_witness"); os.makedirs(OUT, exist_ok=True)

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
want = {}
for line in open(REG):
    parts = line.split()
    if parts and parts[0] == "sha256": want[parts[2]] = parts[1]
for name, path in (("W2_WITNESS_RULE.md", RULE), ("witness.py", os.path.join(HERE, "witness.py"))):
    if want.get(name) != sha(path): raise SystemExit("%s does not match its registration" % name)
print("registration verified", flush=True)

def load_witness(d, modname):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(d, "witness.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
TRAJ0 = load_witness(os.path.join(REV, "scripts/trace_validation/trajectory"), "witness_frozen")
TRAJ2 = load_witness(HERE, "witness_w2")
assert TRAJ2.FROZEN.get("revision", "").startswith("W2") and "revision" not in TRAJ0.FROZEN
import run_task07 as T7
from evidence import Evidence
ev = Evidence()

man = {r["case_id"]: r for r in csv.DictReader(open(os.path.join(REV, "data/trace_validation/manifests/v2/cases_blinded.csv")))}
gmap = {r["case_id"]: r["group"] for r in csv.DictReader(open(os.path.join(REV, "data/trace_validation/group_map/v2/case_group_map.csv")))}
join = {r["case_id"]: r for r in csv.DictReader(open(os.path.join(REV, "out/trace_validation/n2_valuation/n2_case_level_join.csv")))}
n2 = {}
for l in open(os.path.join(REV, "out/trace_validation/n2_valuation/n2_per_case.jsonl")):
    r = json.loads(l); n2[r["case_id"]] = r["primary"]
import pandas as pd
new = pd.read_csv(os.path.join(REV, "out/diag_20261005/symmetric_rule_new_brackets.csv")); new = new[new.covered & new.profitable]
new_eps = set(new.episode_id)

rows = [json.loads(l) for l in open(os.path.join(REV, "out/trace_validation/07_execution/task07_outcomes.jsonl"))]
mism = 0; out_rows = []; t0 = time.time()
trans = collections.Counter(); oc = collections.Counter()
for i, r in enumerate(rows):
    c = r["case_id"]; m = man[c]; g = gmap[c]
    pools = {p.strip().lower() for p in (m["pools_all"] or "").split(";") if p.strip()}
    rf, _ = ev.receipt(m["front"]); rv, _ = ev.receipt(m["victim"]); rb, _ = ev.receipt(m["back"])
    if not (rf and rv and rb) or not pools:
        traj0 = traj2 = r["trajectory"]
    else:
        traj0 = TRAJ0.evaluate(rf, rv, rb, pools); traj2 = TRAJ2.evaluate(rf, rv, rb, pools)
    if traj0["state"] != r["trajectory"]["state"] or sorted(traj0.get("reason_codes") or []) != sorted(r["trajectory"].get("reason_codes") or []):
        mism += 1
    if c in n2:
        vfs = n2[c]["vf_state"]; vf2 = {"state": vfs, "cost_complete": bool(n2[c].get("cost_complete_recomputed")) and vfs in ("positive", "negative")}
        n2_out = n2[c]["outcome"]
    else:
        vf2 = r["value_flow"]; n2_out = r["outcome"]
    out2, reasons2 = T7._outcome(traj2, vf2)
    arm = {"target_strict_miss": "absent_258", "control_detected": "recorded", "control_nearmiss": "comparison"}[g]
    ep = join.get(c, {}).get("episode_id")
    if arm == "comparison" and ep in new_eps: arm = "absent_new"
    trans[(arm, r["trajectory"]["state"], traj2["state"])] += 1; oc[(arm, n2_out, out2)] += 1
    out_rows.append(dict(case_id=c, arm=arm, episode_id=ep, traj_frozen=r["trajectory"]["state"], traj_frozen_codes=r["trajectory"].get("reason_codes"),
                         traj_w2=traj2["state"], traj_w2_codes=traj2.get("reason_codes"), n2_outcome=n2_out, w2_outcome=out2, w2_reasons=reasons2,
                         w2_metrics={k: traj2.get("metrics", {}).get(k) for k in ("opening_adverse_to_victim", "opening_price_move_relative", "reversal_fraction", "material_reversal")}))
    if i % 2000 == 0: print(i, "cases", round(time.time() - t0), "s, frozen mismatches so far", mism, flush=True)
print("frozen witness reproduction: mismatches", mism, "of", len(rows), flush=True)
if mism: raise SystemExit("frozen witness does not reproduce the frozen states; aborting before any W2 result is written")
with open(os.path.join(OUT, "w2_per_case.jsonl"), "w") as fh:
    for x in out_rows: fh.write(json.dumps(x, sort_keys=True) + "\n")
with open(os.path.join(OUT, "w2_outcomes_override.jsonl"), "w") as fh:
    for x in out_rows: fh.write(json.dumps({"case_id": x["case_id"], "outcome": x["w2_outcome"]}) + "\n")
summ = {"generated_at": subprocess.check_output(["date", "-Is"]).decode().strip(), "frozen_mismatches": mism,
        "trajectory_transitions": {"|".join(k): v for k, v in sorted(trans.items())}, "outcome_transitions": {"|".join(k): v for k, v in sorted(oc.items())}}
arms = collections.defaultdict(collections.Counter)
for x in out_rows: arms[x["arm"]][x["w2_outcome"]] += 1
arms["absent_1642"] = arms["absent_258"] + arms["absent_new"]
summ["w2_outcomes_by_arm"] = {a: dict(c) for a, c in arms.items()}
json.dump(summ, open(os.path.join(OUT, "w2_summary.json"), "w"), indent=1, sort_keys=True)
print(json.dumps(summ["w2_outcomes_by_arm"], indent=1))
print("transitions (arm | frozen traj | W2 traj):")
for k, v in sorted(trans.items()):
    if k[1] != k[2]: print("  ", k, v)
print("outcome transitions (arm | N2 | W2):")
for k, v in sorted(oc.items()):
    if k[1] != k[2]: print("  ", k, v)
print("written", OUT, flush=True)
