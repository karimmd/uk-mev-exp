import csv, glob, hashlib, itertools, json, math, os, statistics, sys, time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(HERE, "..", ".."))
ROOT = os.path.abspath(os.path.join(R, "..", ".."))
VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"
EV = R + "/out/explorer_verification"; API = R + "/out/explorer_verification_api" + ("_v2" if VERSION == "v2" else ""); OUT = API + "/multi_reader"
API_V1 = R + "/out/explorer_verification_api"
os.makedirs(OUT, exist_ok=True)
READERS = ["sonnet", "opus55", "deepseek"]; ALL = ["cc_sonnet"] + READERS
LABEL = {"cc_sonnet": "claude-sonnet-5-5 (Claude Code, earlier reading)", "sonnet": "claude-sonnet-5-5 (API)",
         "opus55": "claude-opus-5-5 (API)", "deepseek": "DeepSeek-V4.1-Flash (API)"}
PRICE = {"claude-sonnet-5-5": (2.0, 10.0), "claude-opus-5-5": (4.0, 20.0)}
SAMPLES = ["f1b", "sym100", "rej53", "arb106"]
ARM = {"target_strict_miss": "missed", "control_detected": "reported", "control_nearmiss": "comparison"}
STATES = ["structurally_supported", "undecidable", "rejected"]
SHORT = {"structurally_supported": "supported", "undecidable": "cannot tell", "rejected": "rejected", None: "no answer"}

def rows(p): return list(csv.DictReader(open(p)))
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def wilson(k, n, z=1.959964):
    if n == 0: return (float("nan"), float("nan"))
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * (c - h), 100 * (c + h)
def w(k, n): return "%d/%d = %.1f%% [%.1f, %.1f]" % (k, n, 100 * k / n, *wilson(k, n)) if n else "---"
def kappa(a, b):
    cats = sorted(set(a) | set(b)); n = len(a)
    if n == 0: return float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((sum(x == c for x in a) / n) * (sum(y == c for y in b) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")
def fleiss(mat):
    mat = [m for m in mat if sum(m) > 1]
    if not mat: return float("nan")
    N = len(mat); n = sum(mat[0]); k = len(mat[0])
    pj = [sum(m[j] for m in mat) / (N * n) for j in range(k)]
    Pi = [(sum(x * x for x in m) - n) / (n * (n - 1)) for m in mat]
    Pbar = sum(Pi) / N; Pe = sum(p * p for p in pj)
    return (Pbar - Pe) / (1 - Pe) if Pe < 1 else float("nan")
def verdict(q1, q2):
    q1 = (q1 or "").strip().lower(); q2 = (q2 or "").strip().lower()
    if q1 == "yes" and q2 == "yes": return "structurally_supported"
    if q1 == "no" or q2 == "no": return "rejected"
    return "undecidable"
def fnum(v):
    try: return float(v)
    except Exception: return None

join = {r["case_id"]: r for r in rows(R + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")}
w2 = {}
for l in open(R + "/out/trace_validation/w2_witness/w2_per_case.jsonl"):
    j = json.loads(l); w2[j["case_id"]] = j["w2_outcome"]
actors = {}
for g in ("target_strict_miss", "control_detected", "control_nearmiss"):
    for r in rows(R + "/out/s0val/cohort_%s_v2.csv" % g): actors[r["episode_id"]] = r["actor"].lower()
e2c = {r["episode_id"]: c for c, r in join.items()}
ledger = {(r["sample"], r["card"]): r for r in rows(ROOT + "/analysis/reframe/data/validator_values.csv")}

maps = {}
mp = R + "/data/f1b/sealed/mapping.csv"
assert sha(mp) == "79fba76de3114473306413ca1222ab5cb8e7f6782a0dda6af1bc693e31c585fe"
for r in rows(mp):
    c = r["case_id"]; j = join[c]
    maps[("f1b", r["pack_id"])] = dict(case_id=c, arm=ARM[r["arm"]], n2=j["n2_outcome"], traj=j["trajectory_state"], vf=j["value_flow_state"],
                                      w2=w2.get(c), rule_actor=actors.get(j["episode_id"]), pattern="buy_first")
for s in ("sym100", "rej53", "arb106"):
    mp = R + "/data/explorer_verification/sealed/%s_mapping.csv" % s
    assert sha(mp) == open(EV + "/%s/MAPPING_SHA256.txt" % s).read().split()[1]
    for r in rows(mp) if s != "rej53" else [dict(zip(["card_id", "episode_id", "case_id", "n2_outcome", "n2_decided_by", "trajectory_state", "value_flow_state", "actor"], x)) for x in list(csv.reader(open(mp)))[1:]]:
        if s == "rej53":
            c = r["case_id"]
            maps[(s, r["card_id"])] = dict(case_id=c, arm="missed", n2=r["n2_outcome"], traj=r["trajectory_state"], vf=r["value_flow_state"], w2=w2.get(c),
                                           rule_actor=actors.get(r["episode_id"]) or r["actor"].lower(), pattern="buy_first", in_M=None)
            continue
        if s == "arb106":
            maps[(s, r["case_id"])] = dict(case_id=r["case_id"], arm="missed", n2=None, traj=None, vf=None, w2=None, rule_actor=r["economic_actor"].lower(),
                                           top6=r["top6"].lower() == "true", hash=r["hash"], profit_eth=fnum(r["profit_eth"]))
        else:
            c = e2c.get(r["episode_id"]); j = join.get(c, {})
            maps[(s, r["case_id"])] = dict(case_id=c, arm="missed", n2=r["n2_outcome"], traj=r.get("trajectory_state") or j.get("trajectory_state"),
                                           vf=r.get("value_flow_state") or j.get("value_flow_state"), w2=w2.get(c), rule_actor=actors.get(r["episode_id"]) or (r.get("actor") or "").lower(),
                                           pattern=r.get("pattern", "buy_first"), in_M=r.get("in_M"))

cards = defaultdict(dict)
usage = defaultdict(lambda: Counter()); refusals = Counter()
for rd in ALL:
    for s in SAMPLES:
        d = (EV + "/" + s) if rd == "cc_sonnet" else (API + "/" + rd + "/" + s)
        for p in glob.glob(d + "/judgments/*.json"):
            j = json.load(open(p)); cards[(s, j["case_id"])][rd] = j
            u = j.get("_usage") or {}
            usage[rd]["in"] += u.get("input_tokens") or 0; usage[rd]["out"] += u.get("output_tokens") or 0; usage[rd]["n"] += 1
            if j.get("_cost_usd"): usage[rd]["usd"] += j["_cost_usd"]
        refusals[rd] += len(glob.glob(d + "/refusals/*.json"))
expected = {s: len(glob.glob(EV + "/%s/cards/*.md" % s)) for s in SAMPLES}

long = []
for (s, cid), byrd in sorted(cards.items()):
    m = maps[(s, cid)]
    for rd in ALL:
        j = byrd.get(rd)
        if j is None: continue
        net, gas = fnum(j.get("net_eth_before_gas", j.get("net_eth"))), fnum(j.get("gas_eth"))
        after = fnum(j.get("profit_after_gas")) if "profit_after_gas" in j else ((net - gas) if (net is not None and gas is not None) else None)
        L = ledger.get((s, cid), {})
        long.append(dict(sample=s, card=cid, case_id=m["case_id"], arm=m["arm"], reader=rd, model=j.get("_model"), Q1=(j.get("Q1") or "").strip().lower(),
                         Q2=(j.get("Q2") or "").strip().lower(), confidence=j.get("confidence"), verdict=verdict(j.get("Q1"), j.get("Q2")),
                         n2_outcome=m["n2"], w2_outcome=m["w2"], trajectory_state=m["traj"], value_flow_state=m["vf"],
                         reader_actor=(j.get("actor") or "").lower(), rule_actor=m["rule_actor"], actor_match=((j.get("actor") or "").lower() == (m["rule_actor"] or "")),
                         net_eth=net, gas_eth=gas, validator_after_gas=after, ledger_after_cost=fnum(L.get("ledger_after_cost")),
                         q1_reason=j.get("Q1_reason"), note=(j.get("note") or "").replace("\n", " ")))
with open(OUT + "/cards_long.csv", "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(long[0].keys())); wr.writeheader(); wr.writerows(long)

stamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
L = ["# Multi-reader explorer validation, protocol %s, scored %s" % (VERSION, stamp), "", "Plan: MULTI_READER_PLAN.md%s (hashes in MULTI_READER_REGISTRATION.txt). Readers:" % (" with amendment 1 (protocol version 2)" if VERSION == "v2" else "")]
for rd in ALL:
    u = usage[rd]; model = next((x["model"] for x in long if x["reader"] == rd and x["model"]), "?")
    pr = PRICE.get(model) if u["in"] else None; usd = (u["in"] * pr[0] + u["out"] * pr[1]) / 1e6 if pr else u["usd"]
    L.append("- %s: %s; judgments %d of %d; refusals %d; tokens in %d, out %d%s" % (rd, LABEL[rd], u["n"], sum(expected.values()), refusals[rd], u["in"], u["out"],
             (", about %.2f USD at list prices" % usd) if pr else (", %.2f USD as recorded" % usd if usd else "")))
L += ["", "Coverage per sample (judgments / cards): " + "; ".join("%s %s" % (s, "/".join(str(sum(1 for x in long if x["sample"] == s and x["reader"] == rd)) for rd in ALL) + " of %d" % expected[s]) for s in SAMPLES), ""]

def sub(s, rd, arm=None): return [x for x in long if x["sample"] == s and x["reader"] == rd and (arm is None or x["arm"] == arm)]

L += ["## 1. Per reader and per sample: called MEV (Q1 yes), supported (Q1 yes and Q2 yes), agreement with REFEREE (original witness), actor", ""]
L += ["| sample | set | reader | n | Q1 yes | supported | agree N2 | kappa N2 | agree W2 | actor match |", "|---|---|---|---:|---|---|---|---:|---|---|"]
for s in SAMPLES:
    arms = ["missed", "reported", "comparison"] if s == "f1b" else ["missed"]
    for arm in arms:
        for rd in ALL:
            g = sub(s, rd, arm)
            if s == "arb106": g = [x for x in g if not maps[(s, x["card"])]["top6"]]
            n = len(g)
            if n == 0: L.append("| %s | %s | %s | 0 | | | | | | |" % (s, arm, rd)); continue
            q1 = sum(x["Q1"] == "yes" for x in g); sup = sum(x["verdict"] == "structurally_supported" for x in g)
            if s == "arb106":
                L.append("| %s | %s | %s | %d | %s | %s | --- | --- | --- | %d/%d |" % (s, arm, rd, n, w(q1, n), w(sup, n), sum(x["actor_match"] for x in g), n))
            else:
                ag = sum(x["verdict"] == x["n2_outcome"] for x in g); ag2 = sum(x["verdict"] == x["w2_outcome"] for x in g if x["w2_outcome"]); n2 = sum(1 for x in g if x["w2_outcome"])
                L.append("| %s | %s | %s | %d | %s | %s | %.1f%% (%d) | %.2f | %s | %d/%d |" % (s, arm, rd, n, w(q1, n), w(sup, n), 100 * ag / n, ag, kappa([x["n2_outcome"] for x in g], [x["verdict"] for x in g]),
                         ("%.1f%% (%d of %d)" % (100 * ag2 / n2, ag2, n2)) if n2 else "---", sum(x["actor_match"] for x in g), n))
L += ["", "Sealed pack, all 200 cards: agreement with REFEREE and kappa per reader"]
for rd in ALL:
    g = sub("f1b", rd)
    if g: L.append("- %s: n %d, agree %.1f%% (%d), kappa %.3f; mean confidence %.2f; confidence 4 or 5 on %.0f%%" % (rd, len(g), 100 * sum(x["verdict"] == x["n2_outcome"] for x in g) / len(g), sum(x["verdict"] == x["n2_outcome"] for x in g),
                  kappa([x["n2_outcome"] for x in g], [x["verdict"] for x in g]), statistics.mean(float(x["confidence"]) for x in g if x["confidence"] is not None), 100 * sum(1 for x in g if str(x["confidence"]) in ("4", "5")) / len(g)))

L += ["", "## 2. Profit agreement with the ledger: cards with both values, within 0.01 ETH, median absolute difference (sandwich samples)", ""]
for rd in ALL:
    g = [x for x in long if x["reader"] == rd and x["sample"] != "arb106" and x["validator_after_gas"] is not None and x["ledger_after_cost"] is not None]
    if g:
        d = [abs(x["validator_after_gas"] - x["ledger_after_cost"]) for x in g]
        L.append("- %s: %d cards, within 0.01 ETH %d (%.1f%%), within 0.001 ETH %d, median abs diff %.2e ETH, above 0.1 ETH %d" % (rd, len(g), sum(v < 0.01 for v in d), 100 * sum(v < 0.01 for v in d) / len(g), sum(v < 0.001 for v in d), statistics.median(d), sum(v > 0.1 for v in d)))

L += ["", "## 3. Between readers (API readers): pairwise agreement and Cohen's kappa on the three-state verdict; Fleiss' kappa over the three", ""]
L += ["| sample | pair | n | agree | kappa |", "|---|---|---:|---|---:|"]
for s in SAMPLES + ["pooled"]:
    for a, b in itertools.combinations(READERS, 2):
        keys = [(x["sample"], x["card"]) for x in long if x["reader"] == a and (s == "pooled" or x["sample"] == s)]
        va = {(x["sample"], x["card"]): x["verdict"] for x in long if x["reader"] == a}; vb = {(x["sample"], x["card"]): x["verdict"] for x in long if x["reader"] == b}
        keys = [k for k in keys if k in vb]
        if keys: L.append("| %s | %s vs %s | %d | %s | %.3f |" % (s, a, b, len(keys), w(sum(va[k] == vb[k] for k in keys), len(keys)), kappa([va[k] for k in keys], [vb[k] for k in keys])))
    mat = []
    for (smp, cid), byrd in cards.items():
        if s != "pooled" and smp != s: continue
        if all(rd in byrd for rd in READERS):
            vs = [verdict(byrd[rd].get("Q1"), byrd[rd].get("Q2")) for rd in READERS]; mat.append([vs.count(st) for st in STATES])
    if mat: L.append("| %s | Fleiss, three readers | %d | all agree %s | %.3f |" % (s, len(mat), w(sum(1 for m in mat if max(m) == 3), len(mat)), fleiss(mat)))
va = {(x["sample"], x["card"]): x for x in long if x["reader"] == "cc_sonnet"}; vb = {(x["sample"], x["card"]): x for x in long if x["reader"] == "sonnet"}
keys = sorted(set(va) & set(vb))
if keys:
    L += ["", "Run-to-run, claude-sonnet-5-5 earlier reading against the API reading: n %d, verdict agreement %s, kappa %.3f; Q1 agreement %s; Q2 agreement %s" % (
        len(keys), w(sum(va[k]["verdict"] == vb[k]["verdict"] for k in keys), len(keys)), kappa([va[k]["verdict"] for k in keys], [vb[k]["verdict"] for k in keys]),
        w(sum(va[k]["Q1"] == vb[k]["Q1"] for k in keys), len(keys)), w(sum(va[k]["Q2"] == vb[k]["Q2"] for k in keys), len(keys)))]

if VERSION == "v2":
    L += ["", "Version 2 against version 1, per reader (same cards, same reader, protocol wording changed): verdict agreement and kappa; Q1 agreement on buy-first and on other patterns"]
    for rd in READERS:
        v1 = {}
        for s in SAMPLES:
            for p in glob.glob(API_V1 + "/" + rd + "/" + s + "/judgments/*.json"):
                j = json.load(open(p)); v1[(s, j["case_id"])] = j
        keys = [(x["sample"], x["card"]) for x in long if x["reader"] == rd and (x["sample"], x["card"]) in v1]
        if not keys: continue
        v2 = {(x["sample"], x["card"]): x for x in long if x["reader"] == rd}
        ag = sum(verdict(v1[k].get("Q1"), v1[k].get("Q2")) == v2[k]["verdict"] for k in keys)
        bf = [k for k in keys if maps[k].get("pattern", "buy_first") == "buy_first" and k[0] != "arb106"]; ot = [k for k in keys if maps[k].get("pattern", "buy_first") != "buy_first" and k[0] != "arb106"]
        q1 = lambda ks: w(sum((v1[k].get("Q1") or "").strip().lower() == v2[k]["Q1"] for k in ks), len(ks)) if ks else "---"
        L.append("- %s: n %d, verdict agreement %s, kappa %.3f; Q1 agreement buy-first %s, other patterns %s" % (rd, len(keys), w(ag, len(keys)),
                 kappa([verdict(v1[k].get("Q1"), v1[k].get("Q2")) for k in keys], [v2[k]["verdict"] for k in keys]), q1(bf), q1(ot)))

L += ["", "## 4. Majority verdict of the three API readers (secondary summary)", "", "| sample | set | n (all three answered) | majority supported | split | agree N2 | kappa N2 | agree W2 |", "|---|---|---:|---|---:|---|---:|---|"]
maj = {}
for (smp, cid), byrd in cards.items():
    if all(rd in byrd for rd in READERS):
        vs = Counter(verdict(byrd[rd].get("Q1"), byrd[rd].get("Q2")) for rd in READERS); top, c = vs.most_common(1)[0]
        maj[(smp, cid)] = top if c >= 2 else "split"
for s in SAMPLES:
    arms = ["missed", "reported", "comparison"] if s == "f1b" else ["missed"]
    for arm in arms:
        ks = [k for k in maj if k[0] == s and maps[k]["arm"] == arm and not (s == "arb106" and maps[k]["top6"])]
        if not ks: continue
        n = len(ks); supn = sum(maj[k] == "structurally_supported" for k in ks); split = sum(maj[k] == "split" for k in ks)
        if s == "arb106": L.append("| %s | %s | %d | %s | %d | --- | --- | --- |" % (s, arm, n, w(supn, n), split)); continue
        dec = [k for k in ks if maj[k] != "split"]
        ag = sum(maj[k] == maps[k]["n2"] for k in dec); ag2 = sum(maj[k] == maps[k]["w2"] for k in dec if maps[k]["w2"]); n2 = sum(1 for k in dec if maps[k]["w2"])
        L.append("| %s | %s | %d | %s | %d | %.1f%% (%d of %d) | %.2f | %s |" % (s, arm, n, w(supn, n), split, 100 * ag / len(dec) if dec else float("nan"), ag, len(dec),
                 kappa([maps[k]["n2"] for k in dec], [maj[k] for k in dec]), ("%.1f%% (%d of %d)" % (100 * ag2 / n2, ag2, n2)) if n2 else "---"))

L += ["", "## 5. The six largest missed arbitrage transactions, per reader", "", "| case | hash | rule profit (ETH) | " + " | ".join(ALL) + " |", "|---|---|---:|" + "---|" * len(ALL)]
for (s, cid), m in sorted(maps.items(), key=lambda kv: -(kv[1].get("profit_eth") or 0)):
    if s == "arb106" and m["top6"]:
        cells = []
        for rd in ALL:
            j = cards[(s, cid)].get(rd)
            x = next((y for y in long if y["reader"] == rd and y["sample"] == s and y["card"] == cid), None)
            cells.append("---" if j is None else "%s (%s), Q2 %s, %s ETH" % (j.get("Q1"), j.get("Q1_reason"), j.get("Q2"), ("%.2f" % x["validator_after_gas"]) if x and x["validator_after_gas"] is not None else "?"))
        L.append("| %s | %s... | %.1f | %s |" % (cid, m["hash"][:10], m["profit_eth"], " | ".join(cells)))
L.append("Validator profit: under v2, profit_after_gas as the reader states it; under v1, net_eth minus gas_eth, which double-counts gas for a reader that states net_eth after gas (check the note before quoting).")

L += ["", "## 6. Cards on which the three API readers do not all agree (verdict, Q1/Q2, confidence), with REFEREE's states", "", "| sample | card | set | N2 | W2 | " + " | ".join(READERS) + " |", "|---|---|---|---|---|" + "---|" * len(READERS)]
for (smp, cid), byrd in sorted(cards.items()):
    if not all(rd in byrd for rd in READERS): continue
    vs = [verdict(byrd[rd].get("Q1"), byrd[rd].get("Q2")) for rd in READERS]
    if len(set(vs)) == 1: continue
    m = maps[(smp, cid)]
    L.append("| %s | %s | %s | %s | %s | %s |" % (smp, cid, m["arm"], SHORT.get(m["n2"], m["n2"]), SHORT.get(m["w2"], m["w2"]),
             " | ".join("%s (%s/%s, c%s)" % (SHORT[v], byrd[rd].get("Q1"), byrd[rd].get("Q2"), byrd[rd].get("confidence")) for v, rd in zip(vs, READERS))))
L += ["", "Notes of the disagreeing readers are in cards_long.csv."]
open(OUT + "/MULTI_READER_RESULTS.md", "w").write("\n".join(L) + "\n")
print("\n".join(L[:40])); print("...\nwrote", OUT)
