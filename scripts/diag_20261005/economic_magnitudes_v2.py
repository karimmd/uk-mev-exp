import os
"""Economic magnitudes, v2 (descriptive, data on disk).

B. Victim loss in ETH on the replay-eligible subset, priced from the shared pool's own post-victim
   reserves: if the victim's output token is WETH the loss is in wei already; otherwise the loss in
   output-token units is converted at reserve_WETH / reserve_T read from the Sync event the victim
   transaction itself emitted. Pools not paired with WETH are reported as unpriced.
C. Arbitrage profit after observable cost, with the direct proposer payment evidence of task 00c
   subtracted where it was measured (zero-gas-price transactions), by presence in the record.
"""
import json, glob, gzip, collections, sys
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"
sys.path.insert(0, REV + "/scripts/trace_validation/value_flow_v2")
from evidence import Evidence
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
SYNC = "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1"
BLOCKS, WINDOW = 50000, 4444725
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

loss = collections.defaultdict(list); why = collections.defaultdict(collections.Counter)
for r in ver:
    g = r["group"]; pool = r["pool"].lower(); E = store.get(r["victim"].lower())
    if not E: why[g]["no_store_record"] += 1; continue
    toks_in = {t for t, frm, to, a in E["transfers"] if to == pool}
    toks_out = {t for t, frm, to, a in E["transfers"] if frm == pool}
    ptoks = toks_in | toks_out
    if WETH not in ptoks or len(ptoks) != 2: why[g]["pool_not_weth_pair"] += 1; continue
    out_tok = next(iter(toks_out)) if len(toks_out) == 1 else None
    if out_tok is None: why[g]["ambiguous_output"] += 1; continue
    raw = int(r["victim_loss_raw"])
    if out_tok == WETH:
        eth = raw / 1e18
    else:
        rc, st = ev.receipt(r["victim"])
        syncs = [lg["data"] for lg in (rc or {}).get("logs", []) if lg.get("topics") and lg["topics"][0] == SYNC and lg["address"].lower() == pool]
        if len(syncs) != 1: why[g]["no_single_sync"] += 1; continue
        d = syncs[0]; r0, r1 = int(d[2:66], 16), int(d[66:130], 16)
        t0 = min(ptoks); weth_res, tok_res = (r0, r1) if t0 == WETH else (r1, r0)
        if tok_res == 0: why[g]["zero_reserve"] += 1; continue
        eth = raw * weth_res / tok_res / 1e18
    loss[g].append((eth, float(r["victim_loss_frac"]), int(r.get("attacker_gross") or 0) / 1e18))

print("B. victim loss (ETH) on replay-eligible episodes, priced at the pool's post-victim reserves")
for g in ("target_strict_miss", "control_detected", "control_nearmiss"):
    v = loss[g]; s = pd.Series([e for e, _, _ in v]); gross = pd.Series([x for _, _, x in v])
    print(f"  {g:20s} priced={len(s):5d} unpriced={dict(why[g])} total={s.sum():10.2f} median={s.median():.4f} p90={s.quantile(.9):.3f} max={s.max():.2f} per1000blocks={s.sum()/BLOCKS*1000:.2f}  attacker_gross_total={gross.sum():.2f}")
t = loss["target_strict_miss"]
hi = [(e, l) for e, l, _ in t if l >= 0.14821]
print("  omitted exceeding T: n=%d, ETH=%.2f, median lambda=%.3f" % (len(hi), sum(e for e, _ in hi), pd.Series([l for _, l in hi]).median() if hi else float("nan")))

h = pd.read_csv(REV + "/out/h5_arbitrage_missed.csv"); o = pd.read_csv(REV + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")
pay = pd.read_csv(REV + "/out/arbitrage_finalization/venue_cost_v1/zero_cost_payment_evidence.csv")[["hash", "observable_payment_wei_total", "classification"]]
m = o.merge(h[["hash", "profit_eth"]], on="hash", how="left").merge(pay, on="hash", how="left")
p4 = m[m.in_P4_profitable_closure == True].copy()
p4["pay_eth"] = p4.observable_payment_wei_total.fillna(0) / 1e18
p4["profit_net"] = p4.profit_eth - p4.pay_eth
p4["zero_gas"] = p4.gas_price == 0
print("\nC. arbitrage profit (ETH), P4 population, by presence")
for present, g in p4.groupby("in_records"):
    lab = "present" if present else "absent "
    for col in ("profit_eth", "profit_net"):
        s = g[col]
        print(f"  {lab} {col:10s} n={len(s):6d} total={s.sum():8.2f} median={s.median():.4f} p90={s.quantile(.9):.3f} max={s.max():.2f} per1000blocks={s.sum()/BLOCKS*1000:.2f}")
    nz = g[~g.zero_gas].profit_eth
    print(f"  {lab} nonzero-gas only n={len(nz)} total={nz.sum():.2f} median={nz.median():.4f} p90={nz.quantile(.9):.3f}")
    print(f"  {lab} share of profit_net in the top 10 transactions: {g.profit_net.nlargest(10).sum()/g.profit_net.sum():.2%}; zero-gas rows {int(g.zero_gas.sum())}, with payment evidence {int(g.observable_payment_wei_total.notna().sum())}")
print("\nabsent arbitrage, top 8 by net profit:"); print(p4[~p4.in_records].nlargest(8, "profit_net")[["hash", "block", "profit_eth", "pay_eth", "profit_net", "n_pools", "first_conjunctive"]].to_string(index=False))
