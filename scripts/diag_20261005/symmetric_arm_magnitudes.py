import csv, glob, gzip, json, collections, sys
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"
sys.path.insert(0, REV + "/scripts/trace_validation/value_flow_v2"); sys.path.insert(0, REV + "/scripts")
from evidence import Evidence
from catalog import _economic_actor
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
SYNC = "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1"
BLOCKS = 50000
new = pd.read_csv(REV + "/out/diag_20261005/symmetric_rule_new_brackets.csv")
new = new[new.covered & new.profitable]; new_eps = set(new.episode_id); new_keys = set(zip(new.front.str.lower(), new.back.str.lower()))
pat = dict(zip(new.episode_id, new.pattern))
gmap = {r["case_id"]: r["group"] for r in csv.DictReader(open(REV + "/data/trace_validation/group_map/v2/case_group_map.csv"))}
join = pd.read_csv(REV + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")[["case_id", "episode_id"]]
c2e = dict(zip(join.case_id, join.episode_id))
n2 = {}
for l in open(REV + "/out/trace_validation/n2_valuation/n2_per_case.jsonl"):
    r = json.loads(l); n2[r["case_id"]] = r["primary"]
import os
OVR = os.environ.get("OUTCOMES_OVERRIDE"); SUF = os.environ.get("OUT_SUFFIX", ""); ovr = {}
if OVR:
    for l in open(OVR):
        r = json.loads(l); ovr[r["case_id"]] = r["outcome"]
    print("outcomes overridden from", OVR)

def arm_of(c):
    g = gmap[c]; e = c2e.get(c)
    if g == "target_strict_miss": return "absent_258"
    if g == "control_nearmiss" and e in new_eps: return "absent_new_" + pat[e]
    if g == "control_detected": return "recorded"
    return None

print("A. actor profit (ETH) over structurally supported cases")
prof = collections.defaultdict(list)
for l in open(REV + "/out/trace_validation/07_execution/task07_outcomes.jsonl"):
    r = json.loads(l); c = r["case_id"]; arm = arm_of(c)
    if arm is None: continue
    out = ovr.get(c, n2[c]["outcome"] if c in n2 else r["outcome"])
    if out != "structurally_supported": continue
    if c in n2:
        d = n2[c]; wei = int(d.get("T_wei") or d["L_wei"])
    else:
        wei = int(r["value_flow"]["metrics"]["net_after_observable_cost_wei"])
    prof[arm].append(wei / 1e18)
prof["absent_new_all"] = prof["absent_new_sell_first"] + prof["absent_new_weth_only"]
prof["absent_1642"] = prof["absent_258"] + prof["absent_new_all"]
res = {}
for arm in ("absent_258", "absent_new_sell_first", "absent_new_weth_only", "absent_new_all", "absent_1642", "recorded"):
    s = pd.Series(prof[arm])
    res[arm] = dict(n=int(len(s)), total_eth=float(s.sum()), median=float(s.median()), p90=float(s.quantile(.9)), max=float(s.max()), per_1000_blocks=float(s.sum() / BLOCKS * 1000))
    print("  %-24s n=%5d total=%9.2f median=%.4f p90=%.3f max=%.2f per1000blocks=%.2f" % (arm, len(s), s.sum(), s.median(), s.quantile(.9), s.max(), s.sum() / BLOCKS * 1000))

print("\nB. victim loss (ETH), replay-eligible, priced at post-victim reserves, bounded and trimmed (v3 method)")
ev = Evidence()
ver = [json.loads(l) for l in open(REV + "/out/s0val/s0_verdicts_v4.jsonl")]
ver = [r for r in ver if r.get("licensed") in (True, "True") and r.get("victim_loss_raw") is not None]
need = {r["victim"].lower() for r in ver}
store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in need: store[x["hash"].lower()] = x
rows = []
for r in ver:
    g = r["group"]; key = (r["front"].lower(), r["back"].lower())
    if g == "control_nearmiss" and key in new_keys: g = "absent_new"
    elif g == "target_strict_miss": g = "absent_258"
    elif g == "control_detected": g = "recorded"
    else: continue
    pool = r["pool"].lower(); E = store.get(r["victim"].lower())
    if not E: continue
    toks_in = {t for t, frm, to, a in E["transfers"] if to == pool}; toks_out = {t for t, frm, to, a in E["transfers"] if frm == pool}
    ptoks = toks_in | toks_out
    if WETH not in ptoks or len(ptoks) != 2 or len(toks_out) != 1: continue
    out_tok = next(iter(toks_out)); raw = int(r["victim_loss_raw"]); lam = float(r["victim_loss_frac"])
    if out_tok == WETH:
        eth = raw / 1e18
    else:
        rc, st = ev.receipt(r["victim"])
        syncs = [lg["data"] for lg in (rc or {}).get("logs", []) if lg.get("topics") and lg["topics"][0] == SYNC and lg["address"].lower() == pool]
        if len(syncs) != 1: continue
        d = syncs[0]; r0, r1 = int(d[2:66], 16), int(d[66:130], 16); t0 = min(ptoks)
        weth_res, tok_res = (r0, r1) if t0 == WETH else (r1, r0)
        if tok_res == 0: continue
        eth = raw * (weth_res / tok_res) / 1e18
    a = E["from"].lower(); paid = sum(int(x[3]) for x in E["transfers"] if x[0] == WETH and x[1] == a) / 1e18
    rows.append(dict(group=g, eth=eth, lam=lam, out_tok=out_tok, weth_paid=paid))
df = pd.DataFrame(rows)
df["eth_bounded"] = df.apply(lambda r: min(r.eth, r.weth_paid) if (r.out_tok != WETH and r.weth_paid > 0) else r.eth, axis=1)
df["plausible"] = (df.lam < 0.9) & (df.eth_bounded < 50)
df2 = pd.concat([df, df[df.group.isin(["absent_258", "absent_new"])].assign(group="absent_1642")])
for g, s in df2.groupby("group"):
    p = s[s.plausible]
    res["victim_loss_" + g] = dict(n=int(len(s)), kept=int(len(p)), total_eth=float(p.eth_bounded.sum()), median=float(p.eth_bounded.median()), per_1000_blocks=float(p.eth_bounded.sum() / BLOCKS * 1000))
    print("  %-14s n=%5d kept=%5d total=%9.2f median=%.4f p90=%.3f per1000blocks=%.2f" % (g, len(s), len(p), p.eth_bounded.sum(), p.eth_bounded.median(), p.eth_bounded.quantile(.9), p.eth_bounded.sum() / BLOCKS * 1000))
json.dump(res, open(REV + "/out/diag_20261005/symmetric_arm_magnitudes%s.json" % SUF, "w"), indent=1)
print("written symmetric_arm_magnitudes.json")
