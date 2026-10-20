import csv, glob, hashlib, json, math, os, subprocess, sys
import pandas as pd
R = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
EV = R + "/out/explorer_verification"; SEALED = R + "/data/explorer_verification/sealed"
stamp = subprocess.check_output(["date", "-Is"]).decode().strip()

def wilson(k, n, z=1.959964):
    if n == 0: return (float("nan"), float("nan"))
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * (c - h), 100 * (c + h)
def w(k, n): return "%d/%d = %.1f%% [%.1f, %.1f]" % (k, n, 100 * k / n if n else float("nan"), *wilson(k, n))
def kappa(a, b):
    cats = sorted(set(a) | set(b)); n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((sum(x == c for x in a) / n) * (sum(y == c for y in b) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")

def load(name):
    d = EV + "/" + name
    mp = SEALED + "/%s_mapping.csv" % name
    h = hashlib.sha256(open(mp, "rb").read()).hexdigest()
    rec = open(d + "/MAPPING_SHA256.txt").read().split()[1]
    assert h == rec, (h, rec)
    sheet = pd.read_csv(d + "/sheet.csv")
    J = {json.load(open(p))["case_id"]: json.load(open(p)) for p in glob.glob(d + "/judgments/*.json")}
    m = pd.read_csv(mp)
    x = sheet.merge(m, on="case_id")
    x["Q1"] = x.Q1_sandwich.astype(str).str.strip().str.lower(); x["Q2"] = x.Q2_positive_after_cost.astype(str).str.strip().str.lower()
    x["reader"] = ["structurally_supported" if (a == "yes" and b == "yes") else ("rejected" if (a == "no" or b == "no") else "undecidable") for a, b in zip(x.Q1, x.Q2)]
    x["reader_actor"] = x.case_id.map(lambda c: (J[c].get("actor") or "").lower())
    x["note"] = x.case_id.map(lambda c: (J[c].get("note") or "").replace("|", "/").replace("\n", " ")[:300])
    x["q1_reason"] = x.case_id.map(lambda c: J[c].get("Q1_reason"))
    return d, x, h, len(J)

def sandwich_report(name, title, extra):
    d, x, h, nj = load(name)
    L = ["# %s, unsealed %s" % (title, stamp), "", "Reader claude-sonnet-5-5 headless, PROTOCOL.md sha256 e95442c2…6395, %d cards, mapping sha256 %s…" % (nj, h[:8]), ""]
    L += ["## 1. Reader verdicts", "", "- Q1 sandwich yes: %s" % w((x.Q1 == "yes").sum(), len(x)), "- Q2 positive after cost yes: %s" % w((x.Q2 == "yes").sum(), len(x)),
          "- reader supported (Q1 yes and Q2 yes): %s" % w((x.reader == "structurally_supported").sum(), len(x)),
          "- reader rejected: %d; undecidable: %d" % ((x.reader == "rejected").sum(), (x.reader == "undecidable").sum())]
    L += ["", "## 2. Agreement with the adjudicator (N2)", "", pd.crosstab(x.n2_outcome, x.reader, margins=True).to_markdown(), "",
          "Agreement %.1f%% (%d of %d), kappa %.3f" % (100 * (x.reader == x.n2_outcome).mean(), (x.reader == x.n2_outcome).sum(), len(x), kappa(list(x.n2_outcome), list(x.reader)))]
    L += extra(x)
    actor_col = "actor" if "actor" in x.columns else None
    if actor_col:
        x["actor_match"] = x.reader_actor == x[actor_col].str.lower()
        L += ["", "## Actor identification", "", "Reader actor equals the rule's actor in %d of %d" % (x.actor_match.sum(), len(x))]
    L += ["", "## Disagreements, itemised", "", "| case | adjudicator | reader | Q1 | Q2 | conf | note |", "|---|---|---|---|---|---|---|"]
    for r in x[x.reader != x.n2_outcome].itertuples():
        L.append("| %s | %s | %s | %s | %s | %s | %s |" % (r.case_id, r.n2_outcome, r.reader, r.Q1, r.Q2, r.confidence_1to5, r.note))
    x.to_csv(d + "/unsealed.csv", index=False); open(d + "/UNSEALED_RESULTS.md", "w").write("\n".join(L) + "\n"); print("\n".join(L[:12]))

def sym_extra(x):
    L = ["", "## 3. By direction pattern (the new brackets the symmetric rule admits)", "", "| pattern | n | reader Q1 yes | reader supported | adjudicator supported | called by mev-inspect |", "|---|---:|---|---|---|---|"]
    for p, g in x.groupby("pattern"):
        L.append("| %s | %d | %s | %s | %s | %d |" % (p, len(g), w((g.Q1 == "yes").sum(), len(g)), w((g.reader == "structurally_supported").sum(), len(g)), w((g.n2_outcome == "structurally_supported").sum(), len(g)), g.in_M.astype(bool).sum()))
    L += ["", "Reader Q1 yes among brackets mev-inspect calls: %s; among those it does not: %s" % (w((x[x.in_M.astype(bool)].Q1 == "yes").sum(), x.in_M.astype(bool).sum()), w((x[~x.in_M.astype(bool)].Q1 == "yes").sum(), (~x.in_M.astype(bool)).sum()))]
    return L

def rej_extra(x):
    L = ["", "## 3. Do the adjudicator's rejections hold up? (all 53 are N2-rejected record-absent brackets)", "",
         "- reader also rejects (Q1 no or Q2 no): %s" % w((x.reader == "rejected").sum(), len(x)),
         "- reader says sandwich (Q1 yes): %s; reader supports (Q1 yes and Q2 yes): %s" % (w((x.Q1 == "yes").sum(), len(x)), w((x.reader == "structurally_supported").sum(), len(x))),
         "", "| rejection ground (trajectory / value flow) | n | reader rejects | reader supports |", "|---|---:|---:|---:|"]
    for k, g in x.groupby(["trajectory_state", "value_flow_state"]):
        L.append("| %s / %s | %d | %d | %d |" % (k[0], k[1], len(g), (g.reader == "rejected").sum(), (g.reader == "structurally_supported").sum()))
    return L

def arb_report():
    d, x, h, nj = load("arb106")
    x["top6"] = x.top6.astype(str).str.lower() == "true"
    s = x[~x.top6]; t = x[x.top6]
    L = ["# arb106 explorer verification, unsealed %s" % stamp, "", "Reader claude-sonnet-5-5 headless, PROTOCOL_ARBITRAGE.md sha256 b20e6fd0…6156, %d cards, mapping sha256 %s…" % (nj, h[:8]), "",
         "## 1. Random sample of 100 record-absent, canonical-flow, profitable arbitrage transactions", "",
         "- reader Q1 arbitrage yes: %s" % w((s.Q1 == "yes").sum(), len(s)), "- reader Q2 positive after cost yes: %s" % w((s.Q2 == "yes").sum(), len(s)),
         "- reader supported (both yes): %s" % w((s.reader == "structurally_supported").sum(), len(s)), "- Q1 reasons: %s" % s.q1_reason.value_counts().to_dict(),
         "- reader actor equals the rule's economic actor: %d of %d" % ((s.reader_actor == s.economic_actor.str.lower()).sum(), len(s)),
         "- first-on-all-pools (rule flag) among reader-confirmed arbitrages: %d of %d" % (s[s.Q1 == "yes"].first_conjunctive.astype(str).str.lower().eq("true").sum(), (s.Q1 == "yes").sum()),
         "", "## 2. The six largest record-absent transactions by apparent profit", "", "| case | hash | profit (ETH, rule) | reader Q1 | reason | Q2 | conf | note |", "|---|---|---:|---|---|---|---|---|"]
    for r in t.sort_values("profit_eth", ascending=False).itertuples():
        L.append("| %s | %s… | %.2f | %s | %s | %s | %s | %s |" % (r.case_id, r.hash[:12], r.profit_eth, r.Q1, r.q1_reason, r.Q2, r.confidence_1to5, r.note))
    L += ["", "Reader says arbitrage for %d of the six (the magnitudes note says none is)." % (t.Q1 == "yes").sum()]
    L += ["", "## 3. Non-arbitrage cases in the random sample, itemised", "", "| case | hash | reader Q1 | reason | note |", "|---|---|---|---|---|"]
    for r in s[s.Q1 != "yes"].itertuples():
        L.append("| %s | %s… | %s | %s | %s |" % (r.case_id, r.hash[:12], r.Q1, r.q1_reason, r.note))
    x.to_csv(d + "/unsealed.csv", index=False); open(d + "/UNSEALED_RESULTS.md", "w").write("\n".join(L) + "\n"); print("\n".join(L[:12]))

names = sys.argv[1:] or ["sym100", "rej53", "arb106"]
for n in names:
    if not os.path.exists(EV + "/" + n + "/DONE"): print(n, "not DONE, skipped"); continue
    if n == "sym100": sandwich_report(n, "sym100 explorer verification (100 brackets added by the direction-symmetric rule)", sym_extra)
    elif n == "rej53": sandwich_report(n, "rej53 explorer verification (the 53 record-absent brackets N2 rejects)", rej_extra)
    elif n == "arb106": arb_report()
print("unseal complete", stamp)
