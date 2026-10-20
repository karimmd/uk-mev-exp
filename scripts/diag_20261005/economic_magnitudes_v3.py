import os
"""Diagnose the victim-loss outliers and inspect the largest absent arbitrages."""
import json, glob, gzip, collections, sys
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"
sys.path.insert(0, REV + "/scripts/trace_validation/value_flow_v2"); sys.path.insert(0, REV + "/scripts")
from evidence import Evidence
from catalog import _economic_actor
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
SYNC = "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1"
BLOCKS = 50000
meta = json.load(open(REV + "/data/f1b/token_meta.json"))
def sym(t):
    m = meta.get(t) or {}; return (m.get("symbol") or t[:8]), m.get("decimals")
def fmt(t, a):
    s, d = sym(t); return ("%.4f %s" % (int(a) / 10 ** d, s)) if d is not None else ("%d raw %s" % (int(a), s))
ev = Evidence()

ver = [json.loads(l) for l in open(REV + "/out/s0val/s0_verdicts_v4.jsonl")]
ver = [r for r in ver if r.get("licensed") in (True, "True") and r.get("victim_loss_raw") is not None]
need = {r["victim"].lower() for r in ver}
o = pd.read_csv(REV + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")
h = pd.read_csv(REV + "/out/h5_arbitrage_missed.csv")
p4 = o[(o.in_P4_profitable_closure == True) & (~o.in_records)].merge(h[["hash", "profit_eth"]], on="hash")
top = p4.nlargest(6, "profit_eth")
need_arb = set(top.hash.str.lower())
store = {}; store_arb = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in need: store[x["hash"].lower()] = x
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in need_arb: store_arb[x["hash"].lower()] = x

rows = []
for r in ver:
    g = r["group"]; pool = r["pool"].lower(); E = store.get(r["victim"].lower())
    if not E: continue
    toks_in = {t for t, frm, to, a in E["transfers"] if to == pool}; toks_out = {t for t, frm, to, a in E["transfers"] if frm == pool}
    ptoks = toks_in | toks_out
    if WETH not in ptoks or len(ptoks) != 2 or len(toks_out) != 1: continue
    out_tok = next(iter(toks_out)); raw = int(r["victim_loss_raw"]); lam = float(r["victim_loss_frac"])
    if out_tok == WETH:
        eth = raw / 1e18; price = 1.0
    else:
        rc, st = ev.receipt(r["victim"])
        syncs = [lg["data"] for lg in (rc or {}).get("logs", []) if lg.get("topics") and lg["topics"][0] == SYNC and lg["address"].lower() == pool]
        if len(syncs) != 1: continue
        d = syncs[0]; r0, r1 = int(d[2:66], 16), int(d[66:130], 16); t0 = min(ptoks)
        weth_res, tok_res = (r0, r1) if t0 == WETH else (r1, r0)
        if tok_res == 0: continue
        price = weth_res / tok_res; eth = raw * price / 1e18
    a = E["from"].lower(); paid = sum(int(x[3]) for x in E["transfers"] if x[0] == WETH and x[1] == a) / 1e18
    rows.append(dict(group=g, eth=eth, lam=lam, out_tok=out_tok, weth_paid=paid, victim=r["victim"], block=r["block"]))
df = pd.DataFrame(rows)
print("victim-loss outliers, absent arm (top 5 by eth):")
print(df[df.group == "target_strict_miss"].nlargest(5, "eth")[["eth", "lam", "weth_paid", "out_tok", "block", "victim"]].to_string(index=False))
print("victim-loss outliers, recorded arm (top 5):")
print(df[df.group == "control_detected"].nlargest(5, "eth")[["eth", "lam", "weth_paid", "out_tok", "block"]].to_string(index=False))
df["eth_bounded"] = df.apply(lambda r: min(r.eth, r.weth_paid) if (r.out_tok != WETH and r.weth_paid > 0) else r.eth, axis=1)
df["plausible"] = (df.lam < 0.9) & (df.eth_bounded < 50)
print("\nvictim loss with the bound loss <= WETH paid, and excluding lambda>=0.9 or >50 ETH:")
for g, s in df.groupby("group"):
    p = s[s.plausible]
    print(f"  {g:20s} n={len(s)} kept={len(p)} total={p.eth_bounded.sum():8.2f} median={p.eth_bounded.median():.4f} IQR=[{p.eth_bounded.quantile(.25):.4f},{p.eth_bounded.quantile(.75):.4f}] p90={p.eth_bounded.quantile(.9):.3f} per1000blocks={p.eth_bounded.sum()/BLOCKS*1000:.2f}")
t = df[(df.group == "target_strict_miss") & df.plausible & (df.lam >= 0.14821)]
print("  omitted exceeding T, plausible: n=%d total=%.2f median=%.3f" % (len(t), t.eth_bounded.sum(), t.eth_bounded.median()))

print("\nlargest absent arbitrages, decoded:")
for r in top.itertuples():
    E = store_arb[r.hash.lower()]; a = _economic_actor(E)
    print(f"\n{r.hash} block {r.block} index {E['index']} profit {r.profit_eth:.3f} ETH pools {len(E['pools'])} first={r.first_conjunctive} sender {E['from'][:10]} to {(E.get('to') or '')[:10]} actor {a[:10]} gas {E['gas_used']}@{int(E['gas_price'])/1e9:.1f}gwei")
    for tok, frm, to, amt in E["transfers"]:
        tag = "ACTOR->" if frm == a else ("->ACTOR" if to == a else "")
        print(f"   {fmt(tok, amt):>32s}  {frm[:8]} -> {to[:8]} {tag}")
