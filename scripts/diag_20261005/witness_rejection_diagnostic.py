import os
"""Why does the trajectory witness reject brackets an explorer reader calls sandwiches?
Cross-tab the witness reason codes and metrics of every N2-rejected case (and, for contrast, every
supported case) against routing: whether the front or back leg trades through two or more pools
(sandwich_linkage.csv front_pools / back_pools), by arm. Also per-era omission rates under both rules,
for the propagated example in the Discussion.
"""
import json, csv, collections
import pandas as pd
R = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
j = pd.read_csv(R + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")[["case_id", "episode_id", "cohort", "n2_outcome", "trajectory_state", "value_flow_state", "era", "amm_design"]]
lk = pd.read_csv(R + "/out/diag_20261005/sandwich_linkage.csv")[["episode_id", "front_pools", "back_pools", "shared_pools", "token_amount_within_1pct", "victim_adjacent"]]
new = pd.read_csv(R + "/out/diag_20261005/symmetric_rule_new_brackets.csv"); new = new[new.covered & new.profitable]
new_eps = set(new.episode_id); pat = dict(zip(new.episode_id, new.pattern))
rows = {}
for l in open(R + "/out/trace_validation/07_execution/task07_outcomes.jsonl"):
    r = json.loads(l); t = r["trajectory"]; m = t.get("metrics") or {}
    rows[r["case_id"]] = dict(traj_codes="|".join(sorted(t.get("reason_codes") or [])), n_shared=m.get("n_shared_pools"),
        same_dir=m.get("opening_same_direction_as_victim"), adverse=m.get("opening_adverse_to_victim"), closing_opp=m.get("closing_opposite_direction_to_victim"),
        reversal=m.get("material_reversal"), n_open_swaps=(m.get("n_swaps") or {}).get("opening"), n_close_swaps=(m.get("n_swaps") or {}).get("closing"))
t = pd.DataFrame.from_dict(rows, orient="index"); t.index.name = "case_id"; t = t.reset_index()
d = j.merge(t, on="case_id", how="left").merge(lk, on="episode_id", how="left")
d["arm"] = d.cohort.map({"target_strict_miss": "absent_258", "control_detected": "recorded", "control_nearmiss": "comparison"})
d.loc[d.episode_id.isin(new_eps), "arm"] = "absent_new"
d["routed"] = (d.front_pools >= 2) | (d.back_pools >= 2)
pd.set_option("display.width", 200)
print("=== N2-rejected cases: trajectory reason codes x routed, by arm ===")
rej = d[d.n2_outcome == "rejected"]
for arm, g in rej.groupby("arm"):
    print("\n--", arm, "n =", len(g), "| routed share %.1f%%" % (100 * g.routed.mean()))
    print(pd.crosstab(g.traj_codes, g.routed, margins=True))
print("\n=== witness metrics among rejected with negative trajectory, by arm x routed ===")
neg = rej[rej.trajectory_state == "negative"]
for (arm, routed), g in neg.groupby(["arm", "routed"]):
    print("%-12s routed=%-5s n=%4d | same_dir False: %d | adverse False: %d | closing_opp False: %d | reversal False: %d | n_shared!=1: %d | opening swaps>1: %d | closing swaps>1: %d" % (
        arm, routed, len(g), (g.same_dir == False).sum(), (g.adverse == False).sum(), (g.closing_opp == False).sum(), (g.reversal == False).sum(), (g.n_shared != 1).sum(), (g.n_open_swaps.fillna(0) > 1).sum(), (g.n_close_swaps.fillna(0) > 1).sum()))
print("\n=== routed share by arm and outcome ===")
print(pd.crosstab([d.arm, d.n2_outcome], d.routed, margins=True))
print("\n=== support share by arm x routed ===")
print(d.groupby(["arm", "routed"]).n2_outcome.value_counts(normalize=True).unstack().round(3))
print("\n=== per-era omission, pre-specified population (258 absent + 10,299 recorded + partial not available here: rates among absent+recorded) and symmetric ===")
ps = d[d.arm.isin(["absent_258", "recorded"])]; sy = d[d.arm.isin(["absent_258", "absent_new", "recorded"])]
for name, x in (("pre-specified", ps), ("symmetric", sy)):
    g = x.groupby("era").apply(lambda s: pd.Series(dict(n=len(s), absent=int((s.arm != "recorded").sum()), rate=100 * (s.arm != "recorded").mean())))
    print("\n", name); print(g.round(2))
json.dump({"routed_share_rejected_by_arm": rej.groupby("arm").routed.mean().round(4).to_dict(),
           "per_era_symmetric": sy.groupby("era").apply(lambda s: 100 * (s.arm != "recorded").mean()).round(2).to_dict(),
           "per_era_prespecified": ps.groupby("era").apply(lambda s: 100 * (s.arm != "recorded").mean()).round(2).to_dict()},
          open(R + "/out/diag_20261005/witness_rejection_diagnostic.json", "w"), indent=1)
d.to_csv(R + "/out/diag_20261005/witness_rejection_cases.csv", index=False)
