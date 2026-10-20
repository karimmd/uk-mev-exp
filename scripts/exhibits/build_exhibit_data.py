import csv, glob, gzip, json, collections, os, sys
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"; OUT = REV + "/out/exhibits"
os.makedirs(OUT, exist_ok=True)
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
STABLE = {"0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48": "USDC", "0xdac17f958d2ee523a2206206994597c13d831ec7": "USDT",
          "0x6b175474e89094c44da98b954eedeac495271d0f": "DAI"}
FLASHBOTS, LONDON = 11_600_000, 12_965_000
def era(b): return "pre_flashbots" if b < FLASHBOTS else ("flashbots_pre_london" if b < LONDON else "post_london")

join = pd.read_csv(REV + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")
man = pd.read_csv(REV + "/data/trace_validation/manifests/v2/cases_blinded.csv")
join = join.merge(man[["case_id", "block", "front", "victim", "back", "pools_all"]], on="case_id", how="left")
new = pd.read_csv(REV + "/out/diag_20261005/symmetric_rule_new_brackets.csv"); new = new[new.covered & new.profitable]
new_pat = dict(zip(new.episode_id, new.pattern))
cmp_pat = dict(zip(pd.read_csv(REV + "/out/diag_20261005/comparison_arm_patterns.csv").episode_id.tolist(),
                   pd.read_csv(REV + "/out/diag_20261005/comparison_arm_patterns.csv").pattern.tolist()))
def arm_of(row):
    c = row.cohort; e = row.episode_id
    if c == "target_strict_miss": return "absent_258"
    if c == "control_detected": return "recorded"
    if c == "control_nearmiss": return "absent_new" if e in new_pat else "comparison"
    return "other"
join["arm"] = join.apply(arm_of, axis=1)
join["pattern"] = join.apply(lambda r: "buy_first" if r.arm in ("absent_258", "recorded") else (new_pat.get(r.episode_id) or cmp_pat.get(r.episode_id, "other")), axis=1)
w2 = {}
for l in open(REV + "/out/trace_validation/w2_witness/w2_per_case.jsonl"):
    r = json.loads(l); w2[r["case_id"]] = r
join["w2_outcome"] = join.case_id.map(lambda c: w2[c]["w2_outcome"] if c in w2 else None)
print("manifest", len(join), join.arm.value_counts().to_dict())

need = set(join.front.str.lower())
store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in need: store[x["hash"].lower()] = x
print("front legs in store", len(store), "of", len(need))
def quote_of(h, pattern):
    E = store.get(h.lower())
    if not E: return "unknown"
    toks = {t.lower() for t, frm, to, a in E["transfers"]}
    if pattern != "weth_only" and WETH in toks: return "WETH"
    st = [STABLE[t] for t in toks if t in STABLE]
    if st: return sorted(st)[0]
    if pattern == "weth_only": return "other"
    return "WETH" if WETH in toks else "other"
join["quote"] = join.apply(lambda r: quote_of(r.front, r.pattern), axis=1)
qp = join.groupby(["arm", "pattern", "quote"]).size().reset_index(name="n")
qp.to_csv(OUT + "/quote_pattern_counts.csv", index=False)
print(qp.to_string())

rows = []
for c, r in w2.items():
    m = r.get("w2_metrics") or {}
    rows.append(dict(case_id=c, arm=r["arm"], n2_outcome=r["n2_outcome"], traj_frozen=r["traj_frozen"], traj_w2=r["traj_w2"],
                     below_eps_frozen="opening_price_move_below_epsilon" in (r.get("traj_frozen_codes") or []),
                     reversal_fraction=m.get("reversal_fraction"), opening_move_rel=m.get("opening_price_move_relative"),
                     w2_outcome=r["w2_outcome"]))
rm = pd.DataFrame(rows); rm["arm2"] = rm.case_id.map(dict(zip(join.case_id, join.arm)))
rm.to_csv(OUT + "/reversal_metrics.csv", index=False)
print("reversal metrics", len(rm), rm.below_eps_frozen.sum(), "below-eps under the frozen witness")

lk = pd.read_csv(REV + "/out/diag_20261005/sandwich_linkage.csv")
wc = pd.read_csv(REV + "/out/diag_20261005/witness_rejection_cases.csv")
lk["arm"] = lk.group.map({"target_strict_miss": "absent_258", "control_detected": "recorded"})
lk["two_pool_leg"] = (lk.front_pools > 1) | (lk.back_pools > 1)
lk["amount_mismatch"] = ~lk.token_amount_within_1pct.astype(bool)
lk["either"] = lk.two_pool_leg | lk.amount_mismatch
mech = []
for arm, s in lk.groupby("arm"):
    d = dict(arm=arm, n=len(s))
    for col in ("two_pool_leg", "amount_mismatch", "either", "victim_adjacent", "same_sender", "actor_is_sender_F"):
        d[col] = int(s[col].astype(bool).sum()); d[col + "_pct"] = round(100 * s[col].astype(bool).mean(), 1)
    d["n_inner_median"] = float(s.n_inner.median()); mech.append(d)
wc["arm2"] = wc.case_id.map(dict(zip(join.case_id, join.arm)))
for arm, s in wc.groupby("arm2"):
    d = next((x for x in mech if x["arm"] == arm), None)
    if d is None: d = dict(arm=arm, n=len(s)); mech.append(d)
    d["routed"] = int(s.routed.astype(bool).sum()); d["routed_pct"] = round(100 * s.routed.astype(bool).mean(), 1)
    d["adjacent_w"] = int(s.victim_adjacent.astype(bool).sum()); d["adjacent_w_pct"] = round(100 * s.victim_adjacent.astype(bool).mean(), 1)
pd.DataFrame(mech).to_csv(OUT + "/mechanism_by_arm.csv", index=False); print(pd.DataFrame(mech).to_string())

oc = pd.read_csv(REV + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")
oc = oc[oc.in_P2_broad_closure.astype(bool)]
oc["era"] = oc.block.map(era)
oc[["hash", "block", "tx_index", "in_records", "contested", "first_conjunctive", "n_pools", "era", "in_P4_profitable_closure"]].to_csv(OUT + "/arb_tx_index.csv", index=False)
print("arbitrage P2 rows", len(oc), "contested", int(oc.contested.astype(bool).sum()))

vl = join[join.licensed.astype(str) == "True"][["case_id", "arm", "pattern", "era", "victim_loss_frac", "exceeds_T", "n2_outcome", "w2_outcome"]]
vl.to_csv(OUT + "/victim_loss_states.csv", index=False); print("eligible rows", len(vl), vl.arm.value_counts().to_dict())
el = join.groupby(["arm", "licensed", "license_reason"]).size().reset_index(name="n")
el.to_csv(OUT + "/eligibility_by_arm.csv", index=False)

EV = REV + "/out/explorer_verification"
e2c = dict(zip(join.episode_id, join.case_id)); e2arm = dict(zip(join.episode_id, join.arm))
cards = []
f1b = pd.read_csv(EV + "/f1b/unsealed.csv")
for r in f1b.itertuples():
    c = e2c.get(r.episode_id)
    cards.append(dict(sample="f1b", card=r.pack_id, arm=e2arm.get(r.episode_id, r.arm), pattern="buy_first" if r.arm != "control_nearmiss" else cmp_pat.get(r.episode_id, "other"),
                      n2_outcome=r.n2_outcome, trajectory_state=r.trajectory_state, value_flow_state=r.value_flow_state,
                      w2_outcome=w2[c]["w2_outcome"] if c in w2 else None, reader=r.reader, Q1=r.Q1, Q2=r.Q2, confidence=r.confidence_1to5, actor_match=r.actor_match))
sy = pd.read_csv(EV + "/sym100/unsealed.csv")
tv = dict(zip(wc.case_id, zip(wc.trajectory_state, wc.value_flow_state)))
for r in sy.itertuples():
    c = e2c.get(r.episode_id); t = tv.get(c, (None, None))
    cards.append(dict(sample="sym100", card=r.case_id, arm="absent_new", pattern=r.pattern, n2_outcome=r.n2_outcome, trajectory_state=t[0], value_flow_state=t[1],
                      w2_outcome=w2[c]["w2_outcome"] if c in w2 else None, reader=r.reader, Q1=r.Q1, Q2=r.Q2, confidence=r.confidence_1to5, actor_match=r.actor_match, in_M=r.in_M))
rj = pd.read_csv(EV + "/rej53/unsealed.csv")
for r in rj.itertuples():
    c = r.case_id if str(r.case_id).startswith("case_") else getattr(r, "_9", None)
    c = e2c.get(r.episode_id, c)
    cards.append(dict(sample="rej53", card=r.case_id, arm="absent_258", pattern="buy_first", n2_outcome=r.n2_outcome, trajectory_state=r.trajectory_state, value_flow_state=r.value_flow_state,
                      w2_outcome=w2[c]["w2_outcome"] if c in w2 else None, reader=r.reader, Q1=r.Q1, Q2=r.Q2, confidence=r.confidence_1to5, actor_match=None))
pd.DataFrame(cards).to_csv(OUT + "/explorer_cards.csv", index=False); print("cards", len(cards))

mm = pd.read_csv(REV + "/out/diag_20261005/mev_inspect_sandwiches_manifest.csv")
mkeys = set(zip(mm.front.str.lower(), mm.back.str.lower()))
rc = pd.read_csv(EV + "/rej53/cases.csv")
rows = []
for r in rj.itertuples():
    c = e2c.get(r.episode_id); cs = rc[rc.case_id == r.case_id].iloc[0]; j = join[join.case_id == c].iloc[0] if c in set(join.case_id) else None
    rows.append(dict(card=r.case_id, block=int(cs.block), front=cs.front, victim=cs.victim, back=cs.back, era=j.era if j is not None else None,
                     amm=j.amm_design if j is not None else None, n2_reason=("trajectory " + str(r.trajectory_state) + " / ledger " + str(r.value_flow_state)),
                     w2_outcome=w2[c]["w2_outcome"] if c in w2 else None, in_M=(cs.front.lower(), cs.back.lower()) in mkeys, reader=r.reader, Q1=r.Q1, Q2=r.Q2, confidence=r.confidence_1to5))
pd.DataFrame(rows).to_csv(OUT + "/rej53_table.csv", index=False)
ar = pd.read_csv(EV + "/arb106/unsealed.csv")
ar[ar.top6.astype(str).isin(["True", "1", "yes"])][["case_id", "hash", "profit_eth", "canonical_flow", "mint_in", "nonpool_in", "n_pools", "first_conjunctive", "contested", "Q1", "Q2", "reader", "confidence_1to5", "note"]].to_csv(OUT + "/arb_top6.csv", index=False)
ar.assign(top6=ar.top6.astype(str)).to_csv(OUT + "/arb106_cards.csv", index=False)
print("done; files:", sorted(os.listdir(OUT)))
