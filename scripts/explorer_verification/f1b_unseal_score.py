import csv, glob, hashlib, json, math, collections, os, subprocess
import pandas as pd
R = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
F = R + "/out/explorer_verification/f1b"
mp = R + "/data/f1b/sealed/mapping.csv"
h = hashlib.sha256(open(mp, "rb").read()).hexdigest()
assert h == "79fba76de3114473306413ca1222ab5cb8e7f6782a0dda6af1bc693e31c585fe", h
stamp = subprocess.check_output(["date", "-Is"]).decode().strip()

sheet = pd.read_csv(F + "/sheet.csv").rename(columns={"case_id": "pack_id"})
J = {}
for p in glob.glob(F + "/judgments/*.json"):
    a = json.load(open(p)); J[a["case_id"]] = a
m = pd.read_csv(mp)
n2 = pd.read_csv(R + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")[["case_id", "episode_id", "cohort", "n2_outcome", "trajectory_state", "value_flow_state", "n2_decided_by", "era", "amm_design"]]
actors = {}
for g in ("target_strict_miss", "control_detected", "control_nearmiss"):
    for r in csv.DictReader(open(R + "/out/s0val/cohort_%s_v2.csv" % g)): actors[r["episode_id"]] = r["actor"].lower()
d = sheet.merge(m, on="pack_id").merge(n2, on="case_id", how="left")
assert len(d) == 200 and d.n2_outcome.notna().all(), (len(d), d.n2_outcome.isna().sum())
d["rule_actor"] = d.episode_id.map(actors)
d["reader_actor"] = d.pack_id.map(lambda p: (J[p].get("actor") or "").lower())
d["actor_match"] = d.reader_actor == d.rule_actor
d["Q1"] = d.Q1_sandwich.astype(str).str.strip().str.lower(); d["Q2"] = d.Q2_positive_after_cost.astype(str).str.strip().str.lower()
def verdict(r):
    if r.Q1 == "yes" and r.Q2 == "yes": return "structurally_supported"
    if r.Q1 == "no" or r.Q2 == "no": return "rejected"
    return "undecidable"
d["reader"] = d.apply(verdict, axis=1)
d["agree"] = d.reader == d.n2_outcome
d.to_csv(F + "/unsealed.csv", index=False)

def wilson(k, n, z=1.959964):
    if n == 0: return (float("nan"), float("nan"))
    p = k / n; dd = 1 + z * z / n; c = (p + z * z / (2 * n)) / dd; hh = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / dd
    return 100 * (c - hh), 100 * (c + hh)
def kappa(a, b):
    cats = sorted(set(a) | set(b)); n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((sum(x == c for x in a) / n) * (sum(y == c for y in b) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")

L = ["# F1b explorer verification, unsealed %s" % stamp, "", "Reader: claude-sonnet-5-5 headless, protocol sha256 e95442c2…6395, 200 cards, mapping sha256 %s…" % h[:8], "",
     "## 1. Reader verdicts by arm (precision of the rule as the reader sees it)", "",
     "| arm | n | Q1 sandwich yes | Q1 no | Q1 cannot tell | Q2 positive yes | reader supported | Wilson 95% |", "|---|---:|---:|---:|---:|---:|---:|---|"]
for arm, g in d.groupby("arm"):
    n = len(g); q1y = (g.Q1 == "yes").sum(); q1n = (g.Q1 == "no").sum(); q1c = n - q1y - q1n; q2y = (g.Q2 == "yes").sum(); sup = (g.reader == "structurally_supported").sum()
    lo, hi = wilson(q1y, n)
    L.append("| %s | %d | %d (%.1f%%) [%.1f, %.1f] | %d | %d | %d (%.1f%%) | %d (%.1f%%) | %s |" % (arm, n, q1y, 100 * q1y / n, lo, hi, q1n, q1c, q2y, 100 * q2y / n, sup, 100 * sup / n, "[%.1f, %.1f]" % wilson(sup, n)))
L += ["", "## 2. Agreement with the adjudicator (N2 outcome)", ""]
ct = pd.crosstab(d.n2_outcome, d.reader, margins=True)
L.append(ct.to_markdown())
L.append("")
L.append("Overall agreement %.1f%% (%d of %d); Cohen's kappa (three states) %.3f" % (100 * d.agree.mean(), d.agree.sum(), len(d), kappa(list(d.n2_outcome), list(d.reader))))
for arm, g in d.groupby("arm"):
    L.append("- %s: agreement %.1f%% (%d of %d), kappa %.3f" % (arm, 100 * g.agree.mean(), g.agree.sum(), len(g), kappa(list(g.n2_outcome), list(g.reader))))
L += ["", "Reader supported among adjudicator-supported: %.1f%%; among adjudicator-rejected: %.1f%%; among undecidable: %.1f%%" % tuple(
    100 * (d[d.n2_outcome == o].reader == "structurally_supported").mean() if (d.n2_outcome == o).any() else float("nan") for o in ("structurally_supported", "rejected", "undecidable"))]
L += ["", "## 3. Actor identification", "", "Reader actor equals the rule's economic actor in %d of %d cards (%.1f%%)." % (d.actor_match.sum(), len(d), 100 * d.actor_match.mean())]
for arm, g in d.groupby("arm"): L.append("- %s: %d of %d" % (arm, g.actor_match.sum(), len(g)))
L += ["", "## 4. Disagreements, itemised", "", "| pack | arm | adjudicator | reader | Q1 | Q2 | conf | reader note |", "|---|---|---|---|---|---|---|---|"]
for r in d[~d.agree].sort_values(["arm", "n2_outcome"]).itertuples():
    note = (J[r.pack_id].get("note") or "").replace("|", "/").replace("\n", " ")[:300]
    L.append("| %s | %s | %s (%s / %s) | %s | %s | %s | %s | %s |" % (r.pack_id, r.arm, r.n2_outcome, r.trajectory_state, r.value_flow_state, r.reader, r.Q1, r.Q2, r.confidence_1to5, note))
L += ["", "## 5. Confidence", "", "Mean confidence %.2f; by agreement: agree %.2f, disagree %.2f" % (d.confidence_1to5.mean(), d[d.agree].confidence_1to5.mean(), d[~d.agree].confidence_1to5.mean() if (~d.agree).any() else float("nan"))]
open(F + "/UNSEALED_RESULTS.md", "w").write("\n".join(L) + "\n")
print("\n".join(L))
