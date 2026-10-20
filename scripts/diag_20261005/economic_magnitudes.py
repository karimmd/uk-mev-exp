import os
"""Economic magnitudes for the results text (descriptive, on data already on disk).

A. Sandwich actor profit by arm, from the adjudication ledger (frozen net where priced, N2 L or T
   where the registered rule signed it), summed over structurally supported cases.
B. Victim loss in ETH on the replay-eligible subset: if the victim received WETH, the loss is
   victim_loss_raw in wei; if the victim paid WETH, the loss is valued at the victim's own realized
   rate, W * lambda / (1 - lambda).
C. Arbitrage profit by arm from the catalog's recomputed WETH profit after observable gas.
All totals are sample totals over the 50,000-block sweep; per-1,000-block rates divide by 50;
the implied full-window figure multiplies the per-block rate by 4,444,725 and is heavy-tailed.
"""
import csv, glob, gzip, json, collections
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
BLOCKS, WINDOW = 50000, 4444725

gmap = {r["case_id"]: r["group"] for r in csv.DictReader(open(REV + "/data/trace_validation/group_map/v2/case_group_map.csv"))}
man = {r["case_id"]: r for r in csv.DictReader(open(REV + "/data/trace_validation/manifests/v2/cases_blinded.csv"))}
n2 = {}
for l in open(REV + "/out/trace_validation/n2_valuation/n2_per_case.jsonl"):
    r = json.loads(l); n2[r["case_id"]] = r["primary"]

prof = collections.defaultdict(list)
for l in open(REV + "/out/trace_validation/07_execution/task07_outcomes.jsonl"):
    r = json.loads(l); c = r["case_id"]; arm = gmap[c]
    out = n2[c]["outcome"] if c in n2 else r["outcome"]
    if out != "structurally_supported": continue
    if c in n2:
        d = n2[c]; wei = int(d.get("T_wei") or d["L_wei"])
    else:
        wei = int(r["value_flow"]["metrics"]["net_after_observable_cost_wei"])
    prof[arm].append(wei / 1e18)
print("A. actor profit (ETH) over structurally supported cases, by arm")
for arm, v in prof.items():
    s = pd.Series(v)
    print(f"  {arm:20s} n={len(s):5d} total={s.sum():9.2f} median={s.median():.4f} p90={s.quantile(.9):.3f} max={s.max():.2f} per1000blocks={s.sum()/BLOCKS*1000:.2f} implied_window={s.sum()/BLOCKS*WINDOW:,.0f}")

need = set()
ver = {}
for l in open(REV + "/out/s0val/s0_verdicts_v4.jsonl"):
    r = json.loads(l)
    if r.get("licensed") in (True, "True") and r.get("victim_loss_frac") is not None:
        ver[r["victim"].lower()] = r; need.add(r["victim"].lower())
store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in need: store[x["hash"].lower()] = x
import sys; sys.path.insert(0, REV + "/scripts"); from catalog import _economic_actor
loss = collections.defaultdict(list); unpriced = collections.Counter()
for h, r in ver.items():
    E = store.get(h)
    if not E: unpriced[r["group"]] += 1; continue
    a = _economic_actor(E); w = 0
    for tok, frm, to, amt in E["transfers"]:
        if tok == WETH and to == a: w += int(amt)
        if tok == WETH and frm == a: w -= int(amt)
    lam = float(r["victim_loss_frac"])
    if w > 0:
        eth = int(r["victim_loss_raw"]) / 1e18
    elif w < 0 and lam < 1:
        eth = (-w / 1e18) * lam / (1 - lam)
    else:
        unpriced[r["group"]] += 1; continue
    loss[r["group"]].append((eth, lam, r.get("verdict")))
print("\nB. victim loss (ETH) on replay-eligible episodes, by arm (valued at the victim's own rate)")
for arm, v in loss.items():
    s = pd.Series([e for e, _, _ in v]); lam = pd.Series([l for _, l, _ in v])
    print(f"  {arm:20s} n={len(s):5d} unpriced={unpriced[arm]} total={s.sum():9.2f} median={s.median():.4f} p90={s.quantile(.9):.3f} max={s.max():.2f} medianLambda={lam.median():.3f} per1000blocks={s.sum()/BLOCKS*1000:.2f}")
t = loss.get("target_strict_miss", [])
print("  omitted, exceeding T=0.14821:", sum(1 for e, l, _ in t if l >= 0.14821), "cases, ETH", round(sum(e for e, l, _ in t if l >= 0.14821), 2))

h = pd.read_csv(REV + "/out/h5_arbitrage_missed.csv"); o = pd.read_csv(REV + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")
m = o.merge(h[["hash", "profit_eth"]], on="hash", how="left"); p4 = m[m.in_P4_profitable_closure == True]
print("\nC. arbitrage profit after observable gas (ETH), P4 population, by presence")
for present, g in p4.groupby("in_records"):
    s = g.profit_eth
    print(f"  {'present' if present else 'absent ':8s} n={len(s):6d} total={s.sum():9.2f} median={s.median():.4f} p90={s.quantile(.9):.3f} max={s.max():.2f} per1000blocks={s.sum()/BLOCKS*1000:.2f} implied_window={s.sum()/BLOCKS*WINDOW:,.0f}")
print("\nCounts per 1,000 blocks: absent sandwiches", 258 / BLOCKS * 1000, "recorded", 10299 / BLOCKS * 1000, "absent arbitrage", 255 / BLOCKS * 1000)
print("Implied full-window counts: absent sandwiches", round(258 / BLOCKS * WINDOW), "absent arbitrage", round(255 / BLOCKS * WINDOW))
