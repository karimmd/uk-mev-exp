import os
"""How much of the arbitrage result depends on the 2% pass-through tolerance.

For every closure-qualified transaction, recompute the pass-through condition at tighter
tolerances (relative slack of each non-WETH pass-through token) and report, by presence in the
record: how many survive, the absence rate, the first-position difference, and the profit total.
Also value the slack where the pass-through token is a stablecoin (USDC, USDT, DAI at 6/6/18
decimals) against the WETH profit, using the transaction's own realized WETH/stablecoin rate when
it traded the two directly, to show how often the slack exceeds the profit.
"""
import json, glob, gzip, sys, collections
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"
sys.path.insert(0, REV + "/scripts"); from catalog import _economic_actor
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
STABLE = {"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48": 6, "0xdac17f958d2ee523a2206206994597c13d831ec7": 6, "0x6b175474e89094c44da98b954eedeac495271d0f": 18}
BLOCKS = 50000
o = pd.read_csv(REV + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")
h = pd.read_csv(REV + "/out/h5_arbitrage_missed.csv")
o = o[o.in_P2_broad_closure == True].merge(h[["hash", "profit_eth"]], on="hash", how="left")
want = set(o.hash.str.lower()); store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in want: store[x["hash"].lower()] = x
rows = []
for r in o.itertuples():
    E = store[r.hash.lower()]; a = _economic_actor(E)
    gi, go, net = {}, {}, {}
    for tok, frm, to, amt in E["transfers"]:
        amt = int(amt)
        if to == a: gi[tok] = gi.get(tok, 0) + amt; net[tok] = net.get(tok, 0) + amt
        if frm == a: go[tok] = go.get(tok, 0) + amt; net[tok] = net.get(tok, 0) - amt
    pt = {t: abs(net.get(t, 0)) / max(gi[t], go[t]) for t in set(gi) & set(go) if t != WETH and max(gi[t], go[t]) > 0}
    slack = max(pt.values()) if pt else 0.0
    weth_net = net.get(WETH, 0)
    stable_cost_eth = None
    for t, dec in STABLE.items():
        if t in net and net[t] < 0 and weth_net > 0:
            if go.get(t, 0) > 0 and gi.get(WETH, 0) > 0:
                rate = (gi[WETH] / 1e18) / (go[t] / 10 ** dec)
                stable_cost_eth = (stable_cost_eth or 0) + (-net[t] / 10 ** dec) * rate
    rows.append(dict(hash=r.hash, absent=not r.in_records, contested=bool(r.contested), first=bool(r.first_conjunctive),
                     profit=r.profit_eth, p4=bool(r.in_P4_profitable_closure), slack=slack, n_pt=len(pt),
                     stable_cost_eth=stable_cost_eth, era=("pre" if r.block < 11600000 else "fb" if r.block < 12965000 else "post")))
d = pd.DataFrame(rows); d.to_csv(REV + "/out/diag_20261005/arbitrage_tolerance.csv", index=False)
print("closure-qualified P2 n=%d absent=%d; profitable P4 n=%d absent=%d" % (len(d), d.absent.sum(), d.p4.sum(), (d.p4 & d.absent).sum()))
for tol in (0.02, 0.005, 0.001, 1e-6):
    k = d[(d.slack <= tol)]; k4 = k[k.p4]
    c = k[k.contested]; ab = c[c.absent]; pr = c[~c.absent]
    print(f"\ntolerance <= {tol:g}: P2 kept {len(k)} ({len(k)/len(d):.1%}), absent {k.absent.sum()} rate {k.absent.mean():.2%}; "
          f"P4 kept {len(k4)}, absent {k4.absent.sum()} rate {k4.absent.mean():.2%}, absent profit {k4[k4.absent].profit.sum():.1f} ETH vs present {k4[~k4.absent].profit.sum():.1f} ETH")
    print(f"   first-on-all-pools (contested): absent {ab['first'].mean():.1%} (n={len(ab)}) vs present {pr['first'].mean():.1%} (n={len(pr)})")
print("\nslack distribution by arm (P4):")
print(d[d.p4].groupby("absent").slack.describe(percentiles=[.5, .75, .9, .95]).T)
s = d[d.p4 & d.stable_cost_eth.notna()]
print("\nP4 transactions with a stablecoin spent (net < 0) alongside a WETH gain: n=%d, absent %d" % (len(s), s.absent.sum()))
s = s.assign(cost_exceeds_profit=lambda x: x.stable_cost_eth > x.profit)
print(pd.crosstab(s.absent, s.cost_exceeds_profit))
print("absent such cases, profit total %.1f ETH, of which cost>profit %.1f ETH" % (s[s.absent].profit.sum(), s[s.absent & s.cost_exceeds_profit].profit.sum()))
