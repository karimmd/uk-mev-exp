ZERO = "0x0000000000000000000000000000000000000000"
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
TRANSFER = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
WITHDRAWAL = "0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65"
DEPOSIT = "0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c"


class PoolsRequired(ValueError):
    pass


def _addr(topic):
    return "0x" + topic[-40:].lower() if topic else None


def _lc(x):
    return x.lower() if isinstance(x, str) else x


def _hexint(x):
    if x is None:
        return None
    if isinstance(x, int):
        return x
    try:
        return int(x, 16)
    except (TypeError, ValueError):
        return None


def erc20_deltas(receipt):
    d = {}
    for lg in (receipt.get("logs") or []):
        t = lg.get("topics") or []
        if not t or t[0] != TRANSFER or len(t) < 3:
            continue
        tok = _lc(lg.get("address") or "")
        frm, to = _addr(t[1]), _addr(t[2])
        try:
            amt = int(lg.get("data") or "0x0", 16)
        except ValueError:
            continue
        if frm:
            d.setdefault(frm, {})[tok] = d.setdefault(frm, {}).get(tok, 0) - amt
        if to:
            d.setdefault(to, {})[tok] = d.setdefault(to, {}).get(tok, 0) + amt
    return d


def weth_conversion_deltas(receipt):
    d = {}
    for lg in (receipt.get("logs") or []):
        if _lc(lg.get("address") or "") != WETH:
            continue
        t = lg.get("topics") or []
        if len(t) < 2:
            continue
        try:
            wad = int(lg.get("data") or "0x0", 16)
        except ValueError:
            continue
        who = _addr(t[1])
        if not who:
            continue
        if t[0] == DEPOSIT:
            d[who] = d.get(who, 0) + wad
        elif t[0] == WITHDRAWAL:
            d[who] = d.get(who, 0) - wad
    return d


def economic_recipient(receipt, pools):
    if pools is None:
        raise PoolsRequired("economic_recipient requires the case's pool set")
    pset = {_lc(p) for p in pools if p}
    if not pset:
        raise PoolsRequired("economic_recipient received an empty pool set")
    d = erc20_deltas(receipt)
    tokens = {_lc(lg.get("address") or "") for lg in (receipt.get("logs") or [])
              if (lg.get("topics") or [None])[0] == TRANSFER}
    excluded = tokens | {ZERO} | pset
    ranked = []
    for a, m in d.items():
        if a in excluded:
            continue
        nz = sum(1 for v in m.values() if v != 0)
        if nz == 0:
            continue
        nz_nonbase = sum(1 for t, v in m.items() if v != 0 and t != WETH)
        ranked.append(((nz_nonbase, nz, abs(m.get(WETH, 0))), a))
    if not ranked:
        return None
    top = max(k for k, _ in ranked)
    winners = [a for k, a in ranked if k == top]
    if len(winners) > 1:
        return None
    return winners[0]


def gas_cost_wei(receipt):
    g = _hexint(receipt.get("gasUsed"))
    p = _hexint(receipt.get("effectiveGasPrice"))
    if g is None or p is None:
        return None
    return g * p


def _internal_endpoints(row):
    frm = _lc(row.get("from") or "")
    to = _lc(row.get("to") or "")
    if not to and (row.get("type") or "").lower() in ("create", "create2"):
        to = _lc(row.get("contractAddress") or "")
    return frm or None, to or None


def native_crossings(internal_rows, boundary):
    inflow = outflow = 0
    n_in = n_out = n_internal = n_failed = 0
    for r in (internal_rows or []):
        if str(r.get("isError", "0")) not in ("0", "False", "false"):
            n_failed += 1
            continue
        try:
            v = int(r.get("value") or 0)
        except (TypeError, ValueError):
            continue
        if v <= 0:
            continue
        frm, to = _internal_endpoints(r)
        f_in, t_in = frm in boundary, to in boundary
        if f_in and t_in:
            n_internal += 1
        elif t_in:
            inflow += v
            n_in += 1
        elif f_in:
            outflow += v
            n_out += 1
    return {"in_wei": inflow, "out_wei": outflow, "n_in": n_in, "n_out": n_out,
            "n_intra_boundary": n_internal, "n_failed_calls": n_failed}


def _mirrors_top_level(internal_rows, tx):
    v = _hexint(tx.get("value")) or 0
    frm, to = _lc(tx.get("from")), _lc(tx.get("to"))
    for r in (internal_rows or []):
        try:
            rv = int(r.get("value") or 0)
        except (TypeError, ValueError):
            continue
        rf, rt = _internal_endpoints(r)
        if rv == v and rf == frm and rt == to:
            return True
    return False


def beneficiary_payment_wei(internal_rows, beneficiary):
    if not beneficiary:
        return 0, 0
    b = _lc(beneficiary)
    tot, n = 0, 0
    for r in (internal_rows or []):
        if str(r.get("isError", "0")) not in ("0", "False", "false"):
            continue
        _, to = _internal_endpoints(r)
        if to != b:
            continue
        try:
            v = int(r.get("value") or 0)
        except (TypeError, ValueError):
            continue
        if v > 0:
            tot += v
            n += 1
    return tot, n


def body_consistent(tx, receipt):
    diffs = []
    if _lc(tx.get("hash")) != _lc(receipt.get("transactionHash")):
        diffs.append("hash")
    for k in ("blockNumber", "transactionIndex"):
        if _hexint(tx.get(k)) != _hexint(receipt.get(k)):
            diffs.append(k)
    if _lc(tx.get("from")) != _lc(receipt.get("from")):
        diffs.append("from")
    rt, tt = _lc(receipt.get("to")), _lc(tx.get("to"))
    if rt is not None and tt is not None and rt != tt:
        diffs.append("to")
    return diffs


def _out(state, reasons, net, complete, m):
    return {"state": state, "reason_codes": list(reasons),
            "observable_net_positive": (None if net is None else net > 0),
            "cost_complete": bool(complete), "metrics": m}


def evaluate(opening, closing, pools, beneficiary=None):
    if pools is None:
        raise PoolsRequired("evaluate requires the case's pool set")
    pset = {_lc(p) for p in pools if p}
    if not pset:
        raise PoolsRequired("evaluate received an empty pool set")

    legs = (("opening", opening), ("closing", closing))
    reasons, m = [], {"pool_count": len(pset)}

    for label, leg in legs:
        rc = leg.get("receipt")
        if not rc:
            return _out("technical_unavailable", ["receipt_missing_%s" % label], None, False, m)
        if gas_cost_wei(rc) is None:
            return _out("technical_unavailable", ["gas_fields_missing_%s" % label], None, False, m)
        if leg.get("internal_state") not in ("success", "empty"):
            return _out("technical_unavailable",
                        ["internal_transfer_evidence_unresolved_%s" % label], None, False, m)
        if leg.get("internal") is None:
            return _out("technical_unavailable",
                        ["internal_transfer_rows_absent_%s" % label], None, False, m)
        if leg.get("tx_state") != "success" or not leg.get("tx"):
            return _out("technical_unavailable",
                        ["transaction_body_missing_%s" % label], None, False, m)

    body_diffs = {}
    for label, leg in legs:
        d = body_consistent(leg["tx"], leg["receipt"])
        if d:
            body_diffs[label] = d
    if body_diffs:
        m["transaction_body_differences"] = body_diffs
        return _out("undecidable", ["transaction_body_inconsistent"], None, False, m)

    recips = {label: economic_recipient(leg["receipt"], pset) for label, leg in legs}
    m["economic_recipient"] = recips
    unresolved = [label for label, a in recips.items() if a is None]
    if unresolved:
        m["recipient_unresolved_legs"] = unresolved
        return _out("undecidable", ["economic_recipient_unresolved"], None, False, m)
    if recips["opening"] != recips["closing"]:
        return _out("undecidable", ["recipient_disagreement"], None, False, m)
    actor = recips["opening"]
    m["actor"] = actor
    m["recipients_agree"] = True

    boundary, basis = {actor}, {}
    for label, leg in legs:
        sender = _lc(leg["tx"].get("from"))
        target = _lc(leg["tx"].get("to"))
        if sender == actor:
            basis[label] = "actor_is_sender"
        elif target == actor:
            basis[label] = "sender_invokes_actor"
        else:
            m["boundary_basis"] = basis
            m["unresolved_leg"] = label
            return _out("undecidable", ["strategy_boundary_unresolved"], None, False, m)
        boundary.add(sender)
    m["boundary_basis"] = basis
    m["boundary"] = sorted(boundary)

    if beneficiary and _lc(beneficiary) in boundary:
        return _out("undecidable", ["actor_is_block_beneficiary"], None, False, m)

    native_in = native_out = gas = top_level_out = 0
    pay = pay_n = 0
    counts, reverted, mirrored = {}, [], []
    for label, leg in legs:
        cr = native_crossings(leg.get("internal"), boundary)
        counts[label] = cr
        native_in += cr["in_wei"]
        native_out += cr["out_wei"]
        gas += gas_cost_wei(leg["receipt"])
        tx = leg["tx"]
        v = _hexint(tx.get("value")) or 0
        target = _lc(tx.get("to"))
        if v > 0 and target not in boundary:
            top_level_out += v
        m["top_level_value_wei_%s" % label] = str(v)
        if v > 0 and _mirrors_top_level(leg.get("internal"), tx):
            mirrored.append(label)
        p, n = beneficiary_payment_wei(leg.get("internal"), beneficiary)
        pay += p
        pay_n += n
        if _hexint(leg["receipt"].get("status")) == 0:
            reverted.append(label)
    m["internal_crossings"] = counts
    m["top_level_mirrored_in_internal"] = mirrored
    m["native_in_wei"] = str(native_in)
    m["native_out_wei"] = str(native_out)
    m["top_level_value_out_wei"] = str(top_level_out)
    m["gas_cost_wei"] = str(gas)
    m["beneficiary_payment_wei"] = str(pay)
    m["beneficiary_payment_transfers"] = pay_n
    m["beneficiary_payment_is_subset_of_native_out"] = True
    m["reverted_legs"] = reverted
    native_net = native_in - native_out - top_level_out - gas
    m["native_net_wei"] = str(native_net)

    net = {}
    for _, leg in legs:
        d = erc20_deltas(leg["receipt"])
        for a in boundary:
            for tok, v in (d.get(a) or {}).items():
                net[tok] = net.get(tok, 0) + v
        for a, wad in weth_conversion_deltas(leg["receipt"]).items():
            if a in boundary:
                net[WETH] = net.get(WETH, 0) + wad
    net = {t: v for t, v in net.items() if v != 0}
    m["token_position"] = {t: str(v) for t, v in net.items()}

    non_weth = {t: v for t, v in net.items() if t != WETH}
    m["non_weth_assets_held"] = len(non_weth)
    if non_weth:
        reasons.append("cross_token_position_unpriced")
        return _out("undecidable", reasons, None, False, m)

    weth = net.get(WETH, 0)
    m["weth_position_wei"] = str(weth)
    net_wei = native_net + weth
    m["net_after_observable_cost_wei"] = str(net_wei)
    reasons.append("eth_equivalent_ledger_native_plus_weth")
    reasons.append("cost_basis_gas_plus_boundary_native_outflow")

    zero_gas = any(_hexint(leg["receipt"].get("effectiveGasPrice")) == 0 for _, leg in legs)
    m["zero_gas_price_leg"] = zero_gas
    cost_complete = True
    if zero_gas:
        reasons.append("zero_gas_price_leg_present")
        if native_out == 0 and top_level_out == 0:
            reasons.append("zero_gas_price_with_no_observable_payment")
            cost_complete = False
    if any(leg.get("internal_state") == "empty" and leg["internal"] for _, leg in legs):
        reasons.append("internal_state_empty_with_rows")
    m["cost_complete"] = cost_complete

    if not cost_complete:
        if net_wei > 0:
            reasons.append("unobserved_cost_could_change_sign")
            return _out("undecidable", reasons, None, False, m)
        reasons.append("non_positive_survives_any_additional_cost")
        return _out("negative", reasons, net_wei, False, m)

    return _out("positive" if net_wei > 0 else "negative", reasons, net_wei, True, m)
