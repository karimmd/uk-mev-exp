import ast, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import flow2 as F

A = "0x" + "a1" * 20
S = "0x" + "5e" * 20
S2 = "0x" + "52" * 20
P = "0x" + "b0" * 20
P2 = "0x" + "b2" * 20
TOK = "0x" + "70" * 20
BEN = "0x" + "be" * 20
OUT = "0x" + "00ff" * 10
WETH = F.WETH
POOLS = {P, P2}
ETH = 10 ** 18

FAILS = []
CHECKS = [0]


def ck(name, cond, extra=""):
    CHECKS[0] += 1
    if not cond:
        FAILS.append("%s %s" % (name, extra))
        print("FAIL %s %s" % (name, extra))


def topic(a):
    return "0x" + "00" * 12 + a[2:]


def xfer(token, frm, to, amt):
    return {"address": token, "topics": [F.TRANSFER, topic(frm), topic(to)],
            "data": hex(amt)}


def dep(who, wad):
    return {"address": WETH, "topics": [F.DEPOSIT, topic(who)], "data": hex(wad)}


def wdr(who, wad):
    return {"address": WETH, "topics": [F.WITHDRAWAL, topic(who)], "data": hex(wad)}


def receipt(logs=None, gas_used=100000, price=10 ** 9, sender=S, to=A,
            h="0x" + "11" * 32, block=1000, index=3, status=1):
    return {"transactionHash": h, "blockNumber": hex(block), "transactionIndex": hex(index),
            "from": sender, "to": to, "status": hex(status), "gasUsed": hex(gas_used),
            "effectiveGasPrice": hex(price), "logs": logs or []}


def tx(value=0, sender=S, to=A, h="0x" + "11" * 32, block=1000, index=3):
    return {"hash": h, "blockNumber": hex(block), "transactionIndex": hex(index),
            "from": sender, "to": to, "value": hex(value), "input": "0x"}


def irow(frm, to, value, is_error=0, typ="call"):
    return {"from": frm, "to": to, "value": str(value), "isError": str(is_error), "type": typ}


def leg(rcpt, body, internal=None, tx_state="success", internal_state=None):
    if internal_state is None:
        internal_state = "success" if internal else "empty"
    return {"receipt": rcpt, "tx": body, "tx_state": tx_state,
            "internal": internal or [], "internal_state": internal_state}


def pair(open_logs, close_logs, **kw):
    o = leg(receipt(open_logs, h="0x" + "11" * 32, index=3, **kw.pop("orcpt", {})),
            tx(h="0x" + "11" * 32, index=3, **kw.pop("otx", {})),
            kw.pop("ointernal", None), kw.pop("otx_state", "success"),
            kw.pop("ointernal_state", None))
    c = leg(receipt(close_logs, h="0x" + "22" * 32, index=9, **kw.pop("crcpt", {})),
            tx(h="0x" + "22" * 32, index=9, **kw.pop("ctx", {})),
            kw.pop("cinternal", None), kw.pop("ctx_state", "success"),
            kw.pop("cinternal_state", None))
    assert not kw, kw
    return o, c


for fn, args in (("economic_recipient", (receipt(), None)),
                 ("economic_recipient", (receipt(), set())),
                 ("evaluate", (leg(receipt(), tx()), leg(receipt(), tx()), None)),
                 ("evaluate", (leg(receipt(), tx()), leg(receipt(), tx()), set()))):
    try:
        getattr(F, fn)(*args)
        ck("C_pools_mandatory_%s" % fn, False, "no raise for %r" % (args[-1],))
    except F.PoolsRequired:
        ck("C_pools_mandatory_%s" % fn, True)

ck("C_pool_never_selected",
   F.economic_recipient(receipt([xfer(TOK, TOK, P, 5)]), POOLS) is None)
ck("C_pool_would_win_without_exclusion",
   F.economic_recipient(receipt([xfer(TOK, TOK, P, 5)]), {OUT}) == P)
ck("C_actor_still_selected",
   F.economic_recipient(receipt([xfer(TOK, P, A, 5)]), POOLS) == A)
ck("C_token_contract_excluded",
   F.economic_recipient(receipt([xfer(TOK, TOK, A, 5)]), POOLS) == A)
ck("C_zero_address_excluded",
   F.economic_recipient(receipt([xfer(TOK, A, F.ZERO, 5)]), POOLS) == A)
ck("C_pass_through_excluded",
   F.economic_recipient(receipt([xfer(TOK, P, OUT, 5), xfer(TOK, OUT, A, 5)]), POOLS) == A)
ck("C_sender_not_selected_when_flat",
   F.economic_recipient(receipt([xfer(TOK, P, A, 5)], sender=S), POOLS) == A)


R1, R2 = "0x" + "d1" * 20, "0x" + "d2" * 20
tie = [xfer(TOK, P, R1, 5), xfer(TOK, P, R2, 5)]
ck("C_tie_unresolved", F.economic_recipient(receipt(tie), POOLS) is None)
ck("C_tie_order_independent",
   F.economic_recipient(receipt(tie), POOLS)
   == F.economic_recipient(receipt(list(reversed(tie))), POOLS))
ck("C_strict_winner",
   F.economic_recipient(receipt(tie + [xfer(WETH, P, R1, 7)]), POOLS) == R1)
ROUTER = "0x" + "e0" * 20
ck("C_router_dust_does_not_win",
   F.economic_recipient(receipt([xfer(TOK, P, A, 5), xfer(WETH, P, ROUTER, 1)]), POOLS) == A)


def run(o, c, pools=POOLS, ben=BEN):
    return F.evaluate(o, c, pools, ben)


o, c = pair([xfer(TOK, P, A, 5)], [xfer(TOK, A, P, 5), xfer(WETH, P, A, 3 * ETH)])
r = run(o, c)
ck("A_agree_reaches_verdict", r["state"] in ("positive", "negative"), r["state"])
ck("A_agree_flag", r["metrics"]["recipients_agree"] is True)

o, c = pair([xfer(TOK, P, A, 5)], [xfer(TOK, P, OUT, 5), xfer(WETH, P, OUT, 9 * ETH)])
r = run(o, c)
ck("A_disagreement_undecidable", r["state"] == "undecidable", r["state"])
ck("A_disagreement_reason", r["reason_codes"] == ["recipient_disagreement"], r["reason_codes"])
ck("A_disagreement_unsigned", r["observable_net_positive"] is None)
ck("A_disagreement_not_closing_actor", "actor" not in r["metrics"])

o, c = pair([xfer(TOK, P, A, 5)], [])
r = run(o, c)
ck("A_one_leg_unresolved_undecidable", r["state"] == "undecidable", r["state"])
ck("A_one_leg_unresolved_reason",
   r["reason_codes"] == ["economic_recipient_unresolved"], r["reason_codes"])
ck("A_one_leg_unresolved_names_leg",
   r["metrics"]["recipient_unresolved_legs"] == ["closing"],
   r["metrics"].get("recipient_unresolved_legs"))

o, c = pair([], [])
r = run(o, c)
ck("A_both_unresolved_undecidable", r["state"] == "undecidable", r["state"])


o, c = pair([xfer(WETH, P, A, ETH)], [xfer(WETH, P, A, ETH)],
            orcpt={"sender": A, "to": P}, otx={"sender": A, "to": P},
            crcpt={"sender": A, "to": P}, ctx={"sender": A, "to": P})
r = run(o, c)
ck("B_boundary_actor_is_sender",
   r["metrics"]["boundary_basis"] == {"opening": "actor_is_sender", "closing": "actor_is_sender"},
   r["metrics"].get("boundary_basis"))
ck("B_boundary_is_actor_only", r["metrics"]["boundary"] == [A], r["metrics"].get("boundary"))

o, c = pair([xfer(WETH, P, A, ETH)], [xfer(WETH, P, A, ETH)])
r = run(o, c)
ck("B_boundary_sender_invokes_actor",
   set(r["metrics"]["boundary_basis"].values()) == {"sender_invokes_actor"})
ck("B_boundary_includes_sender", r["metrics"]["boundary"] == sorted({A, S}))

o, c = pair([xfer(WETH, P, A, ETH)], [xfer(WETH, P, A, ETH)],
            crcpt={"sender": S2}, ctx={"sender": S2})
r = run(o, c)
ck("B_boundary_two_senders", r["metrics"]["boundary"] == sorted({A, S, S2}))

o, c = pair([xfer(WETH, P, A, ETH)], [xfer(WETH, P, A, ETH)],
            crcpt={"sender": S2, "to": OUT}, ctx={"sender": S2, "to": OUT})
r = run(o, c)
ck("B_boundary_unresolved", r["state"] == "undecidable", r["state"])
ck("B_boundary_unresolved_reason",
   r["reason_codes"] == ["strategy_boundary_unresolved"], r["reason_codes"])
ck("B_boundary_unresolved_names_leg", r["metrics"]["unresolved_leg"] == "closing")

o, c = pair([xfer(WETH, P, A, ETH)], [xfer(WETH, P, A, ETH)])
r = F.evaluate(o, c, POOLS, A)
ck("B_actor_is_beneficiary", r["reason_codes"] == ["actor_is_block_beneficiary"],
   r["reason_codes"])


GAS = 100000 * 10 ** 9

o, c = pair([], [], cinternal=[irow(P, A, 5 * ETH)])
r = run(o, c)
ck("B_native_in_needs_actor", r["state"] == "undecidable")

base_o, base_c = [xfer(TOK, P, A, 5)], [xfer(TOK, A, P, 5), xfer(WETH, P, A, 1)]
o, c = pair(base_o, base_c, cinternal=[irow(P, A, 5 * ETH)])
r = run(o, c)
ck("B_native_inflow_counted", r["metrics"]["native_in_wei"] == str(5 * ETH),
   r["metrics"]["native_in_wei"])
ck("B_native_inflow_positive", r["state"] == "positive", r["state"])

o, c = pair(base_o, base_c, cinternal=[irow(A, OUT, 5 * ETH)])
r = run(o, c)
ck("B_native_outflow_counted", r["metrics"]["native_out_wei"] == str(5 * ETH))
ck("B_native_outflow_negative", r["state"] == "negative", r["state"])

o, c = pair(base_o, base_c, cinternal=[irow(A, OUT, 5 * ETH, is_error=1)])
r = run(o, c)
ck("B_failed_internal_ignored", r["metrics"]["native_out_wei"] == "0")
ck("B_failed_internal_counted_in_metrics",
   r["metrics"]["internal_crossings"]["closing"]["n_failed_calls"] == 1)

o, c = pair(base_o, base_c, cinternal=[irow(S, A, 5 * ETH)])
r = run(o, c)
ck("B_intra_boundary_not_counted",
   r["metrics"]["native_in_wei"] == "0" and r["metrics"]["native_out_wei"] == "0")
ck("B_intra_boundary_counted_in_metrics",
   r["metrics"]["internal_crossings"]["closing"]["n_intra_boundary"] == 1)

o, c = pair(base_o, base_c, cinternal=[irow(P, OUT, 5 * ETH)])
r = run(o, c)
ck("B_outside_flow_ignored",
   r["metrics"]["native_in_wei"] == "0" and r["metrics"]["native_out_wei"] == "0")

row = irow(A, "", 2 * ETH, typ="create")
row["contractAddress"] = OUT
o, c = pair(base_o, base_c, cinternal=[row])
r = run(o, c)
ck("B_create_destination_resolved", r["metrics"]["native_out_wei"] == str(2 * ETH))

o, c = pair(base_o, base_c, cinternal=[irow(OUT, A, 3 * ETH, typ="suicide")])
r = run(o, c)
ck("B_selfdestruct_inflow", r["metrics"]["native_in_wei"] == str(3 * ETH))


AS = {"sender": A, "to": P}
o, c = pair(base_o, base_c, ctx=dict(AS, value=4 * ETH), crcpt=AS,
            otx=dict(AS), orcpt=dict(AS))
r = run(o, c)
ck("B_top_level_out_counted", r["metrics"]["top_level_value_out_wei"] == str(4 * ETH))
ck("B_top_level_out_negative", r["state"] == "negative", r["state"])

o, c = pair(base_o, base_c, ctx={"value": 4 * ETH})
r = run(o, c)
ck("B_top_level_into_boundary_neutral", r["metrics"]["top_level_value_out_wei"] == "0")
ck("B_top_level_into_boundary_recorded",
   r["metrics"]["top_level_value_wei_closing"] == str(4 * ETH))

o2, c2 = pair(base_o, base_c)
ck("B_no_double_count_sign_identical",
   run(o2, c2)["metrics"]["net_after_observable_cost_wei"]
   == r["metrics"]["net_after_observable_cost_wei"])

o, c = pair(base_o, base_c, ctx=dict(AS, value=4 * ETH), crcpt=AS,
            otx=dict(AS), orcpt=dict(AS), cinternal=[irow(A, P, 4 * ETH)])
r = run(o, c)
ck("B_mirror_detected", r["metrics"]["top_level_mirrored_in_internal"] == ["closing"])
ck("B_mirror_not_double_counted",
   r["metrics"]["top_level_value_out_wei"] == str(4 * ETH)
   and r["metrics"]["native_out_wei"] == str(4 * ETH))


o, c = pair(base_o, base_c + [dep(A, 7 * ETH)], cinternal=[irow(A, WETH, 7 * ETH)])
r = run(o, c)
ck("W_wrap_neutral_native", r["metrics"]["native_out_wei"] == str(7 * ETH))
ck("W_wrap_neutral_weth", r["metrics"]["weth_position_wei"] == str(7 * ETH + 1))
ck("W_wrap_net_equals_gas",
   int(r["metrics"]["net_after_observable_cost_wei"]) == 1 - 2 * GAS,
   r["metrics"]["net_after_observable_cost_wei"])

o, c = pair(base_o, base_c + [wdr(A, 7 * ETH)], cinternal=[irow(WETH, A, 7 * ETH)])
r = run(o, c)
ck("W_unwrap_neutral_native", r["metrics"]["native_in_wei"] == str(7 * ETH))
ck("W_unwrap_net_equals_gas",
   int(r["metrics"]["net_after_observable_cost_wei"]) == 1 - 2 * GAS,
   r["metrics"]["net_after_observable_cost_wei"])

import inspect
_src_wcd = inspect.getsource(F.weth_conversion_deltas)
ck("W_deposit_topic_used", "DEPOSIT" in _src_wcd and "WITHDRAWAL" in _src_wcd)
ck("W_conversion_deltas_deposit", F.weth_conversion_deltas(receipt([dep(A, 5)])) == {A: 5})
ck("W_conversion_deltas_withdrawal", F.weth_conversion_deltas(receipt([wdr(A, 5)])) == {A: -5})
other = {"address": OUT, "topics": [F.DEPOSIT, topic(A)], "data": hex(5)}
ck("W_foreign_deposit_ignored", F.weth_conversion_deltas(receipt([other])) == {})


o, c = pair(base_o, base_c, cinternal=[irow(A, BEN, 2 * ETH)])
r = run(o, c)
ck("P_payment_reported", r["metrics"]["beneficiary_payment_wei"] == str(2 * ETH))
ck("P_payment_transfers", r["metrics"]["beneficiary_payment_transfers"] == 1)
ck("P_payment_is_subset", r["metrics"]["native_out_wei"] == str(2 * ETH))
ck("P_payment_not_double_counted",
   int(r["metrics"]["native_net_wei"]) == -2 * ETH - 2 * GAS,
   r["metrics"]["native_net_wei"])

zg = {"price": 0}
o, c = pair(base_o, base_c, orcpt=zg, crcpt=zg, cinternal=[irow(A, BEN, 2 * ETH)])
r = run(o, c)
ck("P_zero_gas_flagged", r["metrics"]["zero_gas_price_leg"] is True)
ck("P_zero_gas_with_payment_complete", r["cost_complete"] is True)
ck("P_zero_gas_with_payment_negative", r["state"] == "negative", r["state"])

o, c = pair(base_o, base_c, orcpt=zg, crcpt=zg)
r = run(o, c)
ck("P_zero_gas_no_payment_incomplete", r["cost_complete"] is False)
ck("P_zero_gas_no_payment_undecidable", r["state"] == "undecidable", r["state"])
ck("P_zero_gas_no_payment_reason",
   "unobserved_cost_could_change_sign" in r["reason_codes"], r["reason_codes"])

o, c = pair(base_o, [xfer(TOK, A, P, 5), xfer(WETH, A, P, ETH)], orcpt=zg, crcpt=zg)
r = run(o, c)
ck("P_zero_gas_negative_survives", r["state"] == "negative", r["state"])
ck("P_zero_gas_negative_reason",
   "non_positive_survives_any_additional_cost" in r["reason_codes"], r["reason_codes"])
ck("P_zero_gas_negative_marked_incomplete", r["cost_complete"] is False)


o, c = pair(base_o, base_c, orcpt={"price": 25 * 10 ** 9}, crcpt={"price": 25 * 10 ** 9})
r = run(o, c)
ck("G_effective_gas_price_used",
   r["metrics"]["gas_cost_wei"] == str(2 * 100000 * 25 * 10 ** 9), r["metrics"]["gas_cost_wei"])
ck("G_gas_missing_is_technical",
   F.gas_cost_wei({"gasUsed": None, "effectiveGasPrice": "0x1"}) is None)
bad = leg(receipt(base_c), tx())
bad["receipt"].pop("effectiveGasPrice")
r = F.evaluate(leg(receipt(base_o), tx()), bad, POOLS, BEN)
ck("G_gas_missing_state", r["state"] == "technical_unavailable", r["state"])
ck("G_gas_missing_reason", r["reason_codes"] == ["gas_fields_missing_closing"], r["reason_codes"])


o, c = pair(base_o, base_c, crcpt={"status": 0})
r = run(o, c)
ck("R_reverted_leg_recorded", r["metrics"]["reverted_legs"] == ["closing"])
ck("R_reverted_still_charges_gas", int(r["metrics"]["gas_cost_wei"]) == 2 * GAS)


o, c = pair(base_o, base_c)
c["tx"], c["tx_state"] = None, "missing"
r = run(o, c)
ck("E_missing_body_state", r["state"] == "technical_unavailable", r["state"])
ck("E_missing_body_reason",
   r["reason_codes"] == ["transaction_body_missing_closing"], r["reason_codes"])
ck("E_missing_body_unsigned", r["observable_net_positive"] is None)

o, c = pair(base_o, base_c)
c["tx_state"] = "failed"
r = run(o, c)
ck("E_failed_body_state", r["state"] == "technical_unavailable", r["state"])

o, c = pair(base_o, base_c)
c["tx"]["blockNumber"] = hex(999)
r = run(o, c)
ck("E_inconsistent_body_state", r["state"] == "undecidable", r["state"])
ck("E_inconsistent_body_reason",
   r["reason_codes"] == ["transaction_body_inconsistent"], r["reason_codes"])
ck("E_inconsistent_body_lists_field",
   r["metrics"]["transaction_body_differences"]["closing"] == ["blockNumber"])

o, c = pair(base_o, base_c)
c["tx"]["from"] = OUT
r = run(o, c)
ck("E_body_sender_mismatch", r["state"] == "undecidable", r["state"])

o, c = pair(base_o, base_c)
c["tx"]["hash"] = "0x" + "99" * 32
r = run(o, c)
ck("E_body_hash_mismatch", r["state"] == "undecidable", r["state"])

ck("E_creation_to_null_ok",
   F.body_consistent(tx(to=None), receipt(to=None)) == [])

o, c = pair(base_o, base_c)
c["internal_state"] = "failed"
r = run(o, c)
ck("E_internal_unresolved_state", r["state"] == "technical_unavailable", r["state"])
ck("E_internal_unresolved_reason",
   r["reason_codes"] == ["internal_transfer_evidence_unresolved_closing"], r["reason_codes"])

o, c = pair(base_o, base_c)
o["receipt"] = None
r = run(o, c)
ck("E_missing_receipt", r["reason_codes"] == ["receipt_missing_opening"], r["reason_codes"])

for st in ("missing", "rate_limited", "something_new"):
    o, c = pair(base_o, base_c)
    c["internal_state"] = st
    r = run(o, c)
    ck("E_internal_state_%s_unresolved" % st,
       r["state"] == "technical_unavailable"
       and r["reason_codes"] == ["internal_transfer_evidence_unresolved_closing"],
       (r["state"], r["reason_codes"]))

o, c = pair(base_o, base_c)
c["internal"], c["internal_state"] = None, "success"
r = run(o, c)
ck("E_internal_rows_absent",
   r["state"] == "technical_unavailable"
   and r["reason_codes"] == ["internal_transfer_rows_absent_closing"], r["reason_codes"])


o, c = pair(base_o, base_c, cinternal=[irow(A, OUT, ETH), irow(A, OUT, ETH)])
r = run(o, c)
ck("D_duplicate_rows_counted_twice", r["metrics"]["native_out_wei"] == str(2 * ETH))
ck("D_duplicate_rows_count_published",
   r["metrics"]["internal_crossings"]["closing"]["n_out"] == 2)


o, c = pair([xfer(TOK, P, A, 5)], [xfer(WETH, P, A, 3 * ETH)])
r = run(o, c)
ck("X_cross_token_undecidable", r["state"] == "undecidable", r["state"])
ck("X_cross_token_reason",
   r["reason_codes"] == ["cross_token_position_unpriced"], r["reason_codes"])
ck("X_cross_token_unsigned", r["observable_net_positive"] is None)
ck("X_cross_token_position_recorded", r["metrics"]["non_weth_assets_held"] == 1)


STATES = {"positive", "negative", "undecidable", "technical_unavailable"}
cases = [
    pair(base_o, base_c),
    pair(base_o, base_c, cinternal=[irow(A, BEN, 2 * ETH)]),
    pair([xfer(TOK, P, A, 5)], [xfer(WETH, P, A, 3 * ETH)]),
    pair(base_o, []),
    pair(base_o, base_c, ctx=dict(AS, value=ETH), crcpt=AS, otx=dict(AS), orcpt=dict(AS)),
]
for i, (oo, cc) in enumerate(cases):
    a = run(oo, cc)
    b = run(oo, cc)
    ck("S_deterministic_%d" % i, a == b)
    ck("S_state_in_vocabulary_%d" % i, a["state"] in STATES, a["state"])
    ck("S_schema_%d" % i,
       set(a) == {"state", "reason_codes", "observable_net_positive", "cost_complete", "metrics"})
    ck("S_reasons_are_strings_%d" % i, all(isinstance(x, str) for x in a["reason_codes"]))
    ck("S_unsigned_iff_unsignable_%d" % i,
       (a["observable_net_positive"] is None) == (a["state"] not in ("positive", "negative")))
    ck("S_single_state_%d" % i, isinstance(a["state"], str))


src = open(F.__file__).read()
tree = ast.parse(src)
FORBIDDEN = ("case_group_map", "group_map", "is_recorded", "recorded_group", "missed_group",
             "match_verdict", "failed_rule", "model_label", "outcome_label", "group_label",
             "h4_holdout", "build_all")
lowered = src.lower()
for name in FORBIDDEN:
    ck("I_no_reference_%s" % name, name not in lowered)
imports = set()
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        imports |= {a.name for a in node.names}
    elif isinstance(node, ast.ImportFrom):
        imports.add(node.module or "")
ck("I_no_v1_import", not any("value_flow." in i or i.endswith("flow") for i in imports), imports)
ck("I_no_counterfactual_import", not any("counterfactual" in i for i in imports), imports)
ck("I_no_network_import", not ({"requests", "urllib", "http", "socket"} & imports), imports)
ck("I_stdlib_only", imports == set(), imports)

import builtins
import run_value_flow_v2 as R

_real_open = R.seal()
try:
    for path in ("data/trace_validation/group_map/v2/case_group_map.csv",
                 "/x/CASE_GROUP_MAP.CSV", "some/h4_holdout.parquet"):
        try:
            open(path)
            ck("T_blinding_seal_%s" % path.split("/")[-1][:12], False, "no raise")
        except R.BlindingViolation:
            ck("T_blinding_seal_%s" % path.split("/")[-1][:12], True)
        except Exception as e:
            ck("T_blinding_seal_%s" % path.split("/")[-1][:12], False, type(e).__name__)
    try:
        open(F.__file__).close()
        ck("T_blinding_seal_allows_ordinary_path", True)
    except Exception as e:
        ck("T_blinding_seal_allows_ordinary_path", False, type(e).__name__)
finally:
    builtins.open = _real_open

rsrc = open(R.__file__).read()
ck("T_runner_verifies_frozen_hashes", "sha256sum" in rsrc and "SHA256SUMS_v2" in rsrc)
ck("T_runner_asserts_cardinality", "cardinality invariant failed" in rsrc)
ck("T_runner_never_drops_a_case", "runner_exception" in rsrc)
ck("T_runner_rejects_label_columns", "forbidden column" in rsrc)

print("\n%d checks, %d failures" % (CHECKS[0], len(FAILS)))
if FAILS:
    for f in FAILS:
        print("  " + f)
    sys.exit(1)
