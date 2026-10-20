import os
"""E4. Arbitrage cross-check against the Flashbots mev-inspect classifier on the residue-50 sweep
(out/mev_inspect/sweep50.jsonl), which is the sweep the arbitrage populations were built on.

Joins mev-inspect arbitrages (by transaction hash) to the rule's closure-qualified population
(data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv, P2 rows, with the canonical-flow flags of
out/diag_20261005/arbitrage_inflow_sources.csv) and reports: recovery of recorded and record-absent P2 and
P4 transactions by M; M-called share by canonical flow; the first-position contrast within M-called
transactions; and M-only arbitrages (not in the rule's candidate set) with their count by block coverage.
"""
import json, collections
import pandas as pd
R = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
M = []; blocks = set(); nfail = 0
for l in open(R + "/out/mev_inspect/sweep50.jsonl"):
    r = json.loads(l); blocks.add(r["block"])
    for a in r.get("arbitrages") or []:
        if a.get("error"): nfail += 1; continue
        M.append(dict(block=r["block"], hash=a["hash"].lower(), account=(a.get("account") or "").lower(), profit_token=(a.get("profit_token") or "").lower(),
                      profit_amount=a.get("profit_amount"), n_swaps=a.get("n_swaps"), n_pools=len(a.get("pools") or [])))
M = pd.DataFrame(M); Mh = set(M.hash)
print("sweep50 blocks in file:", len(blocks), "| mev-inspect arbitrages:", len(M), "distinct hashes:", len(Mh), "| arbitrage rows with error:", nfail)
o = pd.read_csv(R + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv"); o["hash"] = o.hash.str.lower()
cov = o.block.isin(blocks); print("rule candidate rows:", len(o), "| on blocks the sweep covers:", int(cov.sum()))
o = o[cov].copy()
p2 = o[o.in_P2_broad_closure == True].copy()
fl = pd.read_csv(R + "/out/diag_20261005/arbitrage_inflow_sources.csv")
full_p2 = pd.read_csv(R + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv"); full_p2 = full_p2[full_p2.in_P2_broad_closure == True].reset_index(drop=True)
assert len(full_p2) == len(fl)
flow = dict(zip(full_p2.hash.str.lower(), fl.canonical_flow.astype(bool)))
p2["canonical"] = p2.hash.map(flow); p2["absent"] = ~p2.in_records.astype(bool); p2["in_M"] = p2.hash.isin(Mh); p2["p4"] = p2.in_P4_profitable_closure == True
p2["first"] = p2.first_conjunctive.astype(str).str.lower() == "true"; p2["contested"] = p2.contested.astype(str).str.lower() == "true"
res = {"blocks_covered": len(blocks), "M_arbitrages": len(M), "rule_P2_on_covered_blocks": len(p2)}
def share(df, lab):
    k, n = int(df.in_M.sum()), len(df); res[lab] = [k, n]; return "%d/%d = %.1f%%" % (k, n, 100 * k / n if n else float("nan"))
print("\nM recovers the rule's closure-qualified (P2) transactions:")
print("  recorded:", share(p2[~p2.absent], "P2_recorded_in_M"), "| absent:", share(p2[p2.absent], "P2_absent_in_M"))
print("  canonical flow, recorded:", share(p2[~p2.absent & p2.canonical], "P2_canonical_recorded_in_M"), "| absent:", share(p2[p2.absent & p2.canonical], "P2_canonical_absent_in_M"))
print("  non-canonical, recorded:", share(p2[~p2.absent & ~p2.canonical], "P2_noncanonical_recorded_in_M"), "| absent:", share(p2[p2.absent & ~p2.canonical], "P2_noncanonical_absent_in_M"))
print("\nProfitable (P4):")
print("  recorded:", share(p2[p2.p4 & ~p2.absent], "P4_recorded_in_M"), "| absent:", share(p2[p2.p4 & p2.absent], "P4_absent_in_M"), "| absent canonical:", share(p2[p2.p4 & p2.absent & p2.canonical], "P4_canonical_absent_in_M"))
c = p2[p2.canonical & p2.contested & p2.in_M]
fa, fr = c[c.absent]["first"].mean(), c[~c.absent]["first"].mean()
res["first_position_within_M_called_canonical_contested"] = dict(absent=[int(c[c.absent]["first"].sum()), int(c.absent.sum())], recorded=[int(c[~c.absent]["first"].sum()), int((~c.absent).sum())])
print("\nFirst-on-all-pools within M-called canonical-flow contested transactions: absent %.1f%% (n=%d) vs recorded %.1f%% (n=%d)" % (100 * fa, c.absent.sum(), 100 * fr, (~c.absent).sum()))
c2 = p2[p2.canonical & p2.contested]
print("  (all canonical contested, for reference): absent %.1f%% (n=%d) vs recorded %.1f%% (n=%d)" % (100 * c2[c2.absent]["first"].mean(), c2.absent.sum(), 100 * c2[~c2.absent]["first"].mean(), (~c2.absent).sum()))
mo = M[~M.hash.isin(set(o.hash))]
res["M_only_not_in_rule_candidates"] = len(mo); res["M_only_weth_profit"] = int((mo.profit_token == "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2").sum())
print("\nM arbitrages not among the rule's candidate rows:", len(mo), "| with WETH profit token:", res["M_only_weth_profit"], "| by n_pools:", mo.n_pools.value_counts().to_dict())
in_p2 = M[M.hash.isin(set(p2.hash))]; print("M arbitrages that are rule P2:", len(in_p2), "| rule P1 broad but not P2:", int(M.hash.isin(set(o[o.in_P1_broad_shipped == True].hash) - set(p2.hash)).sum()))
json.dump(res, open(R + "/out/diag_20261005/arbitrage_cross_check.json", "w"), indent=1)
M.to_csv(R + "/out/diag_20261005/mev_inspect_arbitrages_sweep50.csv", index=False)
print("written arbitrage_cross_check.json and mev_inspect_arbitrages_sweep50.csv")
