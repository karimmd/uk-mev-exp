import os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from state2 import (rpc, RpcError, ReconstructionError, PRIMARY, SECONDARY, block_diffs, accumulate,
                    apply_diff, assert_overrides_sound, block_context, call_from_tx, flat_logs,
                    receipt_logs, token_deltas, transfer_multiset, swap_pools_of, decode_swap_vector,
                    vectors_comparable, vector_changes, merge_post, accessed_state, intersects,
                    balance_uncertain, contaminated_contract_balances, prefix_changes_state)

TOLERANCE = {
    "T1_integer_equality": "exact",
    "T2_log_comparison": "multiset",
    "T3_token_amounts": "exact_integer",
    "T4_provider_agreement": "exact",
    "T5_state_diff_cardinality": "must_equal_block_tx_count",
    "T8_omission_soundness": "transitive_taint_with_reexecution",
    "design": "FULL_REEXECUTION_FEASIBLE",
    "actual_arm_gate": "status + log_multiset + decoded_token_output + receipt_gas_equality",
    "positive_criterion": "exact_change_in_shared_pool_swap_amount_vector",
    "balance_rule": "conservative_undecidable_no_opcode_detection_at_scale",
    "scope": "ADJACENT_ONLY",
    "subset_rule": "eligible iff victim_index == opening_index + 1",
    "T4_provider_agreement": "exact on gas, logs AND decoded shared-pool vector; disagreement -> undecidable",
    "counterfactual_revert": "recorded separately, returns undecidable, never positive",
}

SUBSET_RULE = "victim_index == opening_index + 1"


def _fail(state, reason, m):
    return {"state": state, "reason": reason, "metrics": m}


def evaluate(case, endpoint=PRIMARY, secondary=SECONDARY):
    b = case["block"]
    oi, vi = case["opening_index"], case["victim_index"]
    m = {"design": TOLERANCE["design"], "block": b, "opening_index": oi, "victim_index": vi,
         "adjacent": vi == oi + 1, "intervening": max(0, vi - oi - 1)}
    if vi <= oi:
        return _fail("technical_unavailable", "victim_not_after_opening", m)
    if vi != oi + 1:
        return _fail("subset_ineligible", "non_adjacent_out_of_frozen_subset",
                     dict(m, subset_rule=SUBSET_RULE))

    blkfull, _ = rpc("eth_getBlockByNumber", [hex(b), True], endpoint=endpoint)
    rcs, _ = rpc("eth_getBlockReceipts", [hex(b)], endpoint=endpoint)
    rv = blkfull["transactions"][vi]
    rc = [x for x in rcs if int(x["transactionIndex"], 16) == vi][0]
    actor = (rv["from"] or "").lower()

    try:
        diffs, txs, tier = block_diffs(b, endpoint=endpoint)
    except RpcError as e:
        return _fail("technical_unavailable", "prefix_diffs_unavailable", dict(m, error=str(e)[:200]))
    m["diff_tier"] = tier

    prefix = diffs[:vi]
    ov_actual = accumulate(prefix)
    try:
        assert_overrides_sound(prefix, ov_actual)
        bov = block_context(blkfull)
    except ReconstructionError as e:
        return _fail("technical_unavailable", "reconstruction_precondition_failed",
                     dict(m, error=str(e)[:200]))
    m["override_accounts"] = len(ov_actual)
    m["override_slots"] = sum(len(v.get("stateDiff") or {}) for v in ov_actual.values())

    call = call_from_tx(rv)
    opts = {"tracer": "callTracer", "tracerConfig": {"withLog": True},
            "stateOverrides": ov_actual, "blockOverrides": bov}
    try:
        act, _ = rpc("debug_traceCall", [call, hex(b - 1), opts], endpoint=endpoint)
    except RpcError as e:
        return _fail("technical_unavailable", "actual_execution_failed", dict(m, error=str(e)[:200]))

    want_gas = int(rc.get("gasUsed", "0x0"), 16)
    got_gas = int(act.get("gasUsed", "0x0"), 16)
    want_logs, got_logs = sorted(receipt_logs(rc)), sorted(flat_logs(act))
    rc_open = [x for x in rcs if int(x["transactionIndex"], 16) == oi][0]
    pools = sorted(swap_pools_of(receipt_logs(rc_open)) & swap_pools_of(want_logs))
    m["shared_pools"] = pools
    declared = {p.lower() for p in (case.get("pools") or [])}
    if declared and not (declared & set(pools)):
        return _fail("undecidable", "declared_pool_set_mismatch",
                     dict(m, declared=sorted(declared)))
    want_tok, verr = decode_swap_vector(want_logs, pools)
    got_tok, _ = decode_swap_vector(got_logs, pools)

    want_ok = rc.get("status") == "0x1"
    got_ok = not act.get("error")
    m.update({"actual_gas_used": got_gas, "onchain_gas_used": want_gas,
              "gas_delta": got_gas - want_gas,
              "actual_reproduces_gas": got_gas == want_gas,
              "actual_reproduces_logs": got_logs == want_logs,
              "actual_reproduces_status": want_ok == got_ok,
              "actual_reproduces_token_output": got_tok == want_tok,
              "actual_swap_vector": [{"pool": e["pool"], "venue": e["venue"],
                                      "amounts": [str(v) for v in e["amounts"]]}
                                     for e in (want_tok or [])]})
    if not (m["actual_reproduces_status"] and m["actual_reproduces_logs"]
            and m["actual_reproduces_token_output"] and m["actual_reproduces_gas"]):
        return _fail("technical_unavailable", "actual_execution_did_not_reproduce", m)

    if verr:
        return _fail("undecidable", "shared_pool_evidence_unusable", dict(m, vector_error=verr))

    m["t4_second_provider"] = secondary
    if secondary:
        try:
            act2, _ = rpc("debug_traceCall", [call, hex(b - 1), opts], endpoint=secondary)
            g2 = int(act2.get("gasUsed", "0x0"), 16)
            l2 = sorted(flat_logs(act2))
            m["t4_checked"] = True
            v2vec, _ = decode_swap_vector(l2, pools)
            m["t4_agrees"] = (g2 == got_gas and l2 == got_logs and v2vec == got_tok)
            if not m["t4_agrees"]:
                m["t4_second_gas"] = g2
                return _fail("undecidable", "provider_disagreement", m)
        except RpcError as e:
            m["t4_checked"] = False
            m["t4_unavailable_reason"] = str(e)[:120]
    else:
        m["t4_checked"] = False
        m["t4_unavailable_reason"] = "no second provider configured"

    opening = diffs[oi]
    fee_recipient = (blkfull.get("miner") or "").lower()
    slots, accts = merge_post(set(), set(), opening)
    contaminated_bal = contaminated_contract_balances(opening, fee_recipient)
    m["opening_tainted_slots"] = len(slots)
    m["opening_tainted_contract_balances"] = len(contaminated_bal)

    ov_cf = accumulate(diffs[:oi])
    reexecuted, uncertain = 0, False
    for i in range(oi + 1, vi):
        try:
            acc = accessed_state(txs[i], endpoint=endpoint)
        except RpcError:
            return _fail("technical_unavailable", "intervening_read_set_unavailable",
                         dict(m, failed_index=i))
        if balance_uncertain(acc, contaminated_bal):
            uncertain = True
            break
        if not intersects(acc, slots, accts):
            apply_diff(ov_cf, diffs[i]); continue
        t = blkfull["transactions"][i]
        try:
            rex, _ = rpc("debug_traceCall",
                         [call_from_tx(t), hex(b - 1),
                          {"tracer": "prestateTracer", "tracerConfig": {"diffMode": True},
                           "stateOverrides": ov_cf, "blockOverrides": bov}],
                         endpoint=endpoint)
        except RpcError:
            return _fail("technical_unavailable", "intervening_reexecution_failed",
                         dict(m, failed_index=i))
        apply_diff(ov_cf, rex)
        slots, accts = merge_post(slots, accts, rex)
        reexecuted += 1
    m["intervening_reexecuted"] = reexecuted
    if uncertain:
        return _fail("undecidable", "contaminated_contract_balance_in_read_set", m)

    try:
        cf, _ = rpc("debug_traceCall",
                    [call, hex(b - 1),
                     {"tracer": "callTracer", "tracerConfig": {"withLog": True},
                      "stateOverrides": ov_cf, "blockOverrides": bov}], endpoint=endpoint)
    except RpcError as e:
        return _fail("technical_unavailable", "counterfactual_execution_failed",
                     dict(m, error=str(e)[:200]))

    cf_logs = sorted(flat_logs(cf))
    cf_tok, cf_err = decode_swap_vector(cf_logs, pools)
    cf_rev = bool(cf.get("error"))
    m.update({"counterfactual_gas_used": int(cf.get("gasUsed", "0x0"), 16),
              "counterfactual_reverted": cf_rev,
              "counterfactual_swap_vector": [{"pool": e["pool"], "venue": e["venue"],
                                              "amounts": [str(v) for v in e["amounts"]]}
                                             for e in (cf_tok or [])],
              "logs_differ": cf_logs != got_logs,
              "token_output_differs": cf_tok != want_tok})

    if cf_rev:
        return _fail("undecidable", "counterfactual_reverts_amounts_incomparable", m)
    if cf_err:
        return _fail("undecidable", "counterfactual_shared_pool_evidence_unusable",
                     dict(m, vector_error=cf_err))
    if not vectors_comparable(want_tok, cf_tok):
        return _fail("undecidable", "swap_vectors_not_comparable", m)
    changes = vector_changes(want_tok, cf_tok)
    m["swap_vector_changes"] = changes
    if changes:
        return _fail("positive", "shared_pool_swap_amounts_change_when_opening_omitted", m)
    if cf_logs != got_logs:
        return _fail("negative", "logs_differ_but_shared_pool_swap_amounts_identical", m)
    return _fail("negative", "counterfactual_output_identical_to_actual", m)
