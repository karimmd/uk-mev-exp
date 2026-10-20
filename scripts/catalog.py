WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"


def _deltas(ev, addr):
    d = {}
    for token, frm, to, amt in ev["transfers"]:
        a = int(amt)
        if frm == addr:
            d[token] = d.get(token, 0) - a
        if to == addr:
            d[token] = d.get(token, 0) + a
    return d


def _token_contracts(ev):
    return {t for t, _f, _to, _a in ev["transfers"]}


def _net_by_address(ev):
    net = {}
    for tok, frm, to, amt in ev["transfers"]:
        a = int(amt)
        net.setdefault(frm, {})[tok] = net.setdefault(frm, {}).get(tok, 0) - a
        net.setdefault(to, {})[tok] = net.setdefault(to, {}).get(tok, 0) + a
    return net


def _economic_actor_v1(ev):
    pools = set(ev.get("pools") or [])
    net = _net_by_address(ev)
    best, best_key = None, (-1, -1)
    for addr, d in net.items():
        if addr in pools:
            continue
        nz = sum(1 for v in d.values() if v != 0)
        if nz == 0:
            continue
        key = (nz, abs(d.get(WETH, 0)))
        if key > best_key:
            best, best_key = addr, key
    return best or ev["from"].lower()


def _economic_actor(ev):
    excluded = set(ev.get("pools") or []) | _token_contracts(ev)
    net = _net_by_address(ev)

    best, best_key = None, (-1, -1, -1)
    for addr, d in net.items():
        if addr in excluded:
            continue
        nz = sum(1 for v in d.values() if v != 0)
        if nz == 0:
            continue
        nz_nonbase = sum(1 for t, v in d.items() if v != 0 and t != WETH)
        key = (nz_nonbase, nz, abs(d.get(WETH, 0)))
        if key > best_key:
            best, best_key = addr, key
    return best or _economic_actor_v1(ev)


SANDWICH_TEMPLATE = {
    "id": "sandwich_canonical",
    "sources": [
        "Torres et al., USENIX Sec 2021 - insertion frontrunning: attacker transactions "
        "bracket a victim in the same block",
        "Qin et al., FC 2022 - sandwich: front and back trade the same pool in opposite "
        "directions around the victim",
        "Zhou et al., IEEE S&P 2021 - the attacker's position opens and closes across "
        "the bracket",
    ],
}


def match_sandwich(front, victim, back, bot=None):
    if not (front and victim and back):
        return {"verdict": "no_evidence", "failed": ["evidence_missing"]}

    aF, aB = _economic_actor(front), _economic_actor(back)
    dF, dB = _deltas(front, aF), _deltas(back, aB)
    non_base = {t for t in set(dF) | set(dB) if t != WETH}
    shared = set(front["pools"]) & set(victim["pools"]) & set(back["pools"])

    P = {
        "same_block": front["block"] == victim["block"] == back["block"],
        "ordering": front["index"] < victim["index"] < back["index"],
        "adjacency": victim["index"] == front["index"] + 1
                     and back["index"] == victim["index"] + 1,
        "same_actor": _economic_actor(front) == _economic_actor(back),
        "shared_pool": bool(shared),
        "reversal": any(dF.get(t, 0) > 0 and dB.get(t, 0) < 0 for t in non_base),
        "all_success": front["status"] == victim["status"] == back["status"] == 1,
    }
    core = ["same_block", "ordering", "same_actor", "shared_pool", "reversal", "all_success"]
    failed = [k for k in core if not P[k]]

    gas = sum(t["gas_used"] * t["gas_price"] for t in (front, back))
    profit = (dF.get(WETH, 0) + dB.get(WETH, 0) - gas) / 1e18

    return {
        "verdict": "matches:" + SANDWICH_TEMPLATE["id"] if not failed
                   else "no_match:" + ",".join(failed),
        "matched": not failed,
        "failed": failed,
        "predicates": P,
        "n_shared_pools": len(shared),
        "recomputed_profit_eth": profit,
        "gas_cost_eth": gas / 1e18,
    }


KNOWN_VARIANTS = {
    "multi_address": "Chi et al. 2024 (conjoined family); Torres et al. 2021 -- attacker "
                     "splits the bracket across addresses to defeat same-sender heuristics",
    "multi_layered_burger": "Chi et al. 2024 - more than one victim inside the bracket",
    "toxic_arbitrage": "Chi et al. 2024 - an attacker leg also qualifies as a profitable "
                       "cyclic arbitrage",
}


def _cyclic_swap(ev, addr):
    d = _deltas(ev, addr)
    gained = {t for t, v in d.items() if v > 0}
    lost = {t for t, v in d.items() if v < 0}
    return len(gained & lost) > 0 or (len(ev["pools"]) >= 2 and len(gained) >= 1 and len(lost) >= 1)


def classify_sandwich(front, victim, back, bot=None):
    base = match_sandwich(front, victim, back, bot)
    if base["verdict"] == "no_evidence":
        return {**base, "tier": "no_evidence", "variants": []}
    if base["matched"]:
        return {**base, "tier": "canonical", "variants": []}

    failed = set(base["failed"])
    variants, ev_notes = [], {}

    if "same_actor" in failed:
        aF, aB = _economic_actor(front), _economic_actor(back)
        dF, dB = _deltas(front, aF), _deltas(back, aB)
        non_base = {t for t in set(dF) | set(dB) if t != WETH}
        pair_reversal = any(dF.get(t, 0) > 0 and dB.get(t, 0) < 0 for t in non_base)
        shared = set(front["pools"]) & set(victim["pools"]) & set(back["pools"])
        same_router = front["to"] is not None and front["to"] == back["to"]
        ev_notes["pair_reversal"] = pair_reversal
        ev_notes["same_router"] = same_router
        if pair_reversal and shared:
            variants.append("multi_address")

    inner = back["index"] - front["index"] - 1
    ev_notes["inner_txs"] = inner
    if inner > 1:
        variants.append("multi_layered_burger")

    if _cyclic_swap(front, _economic_actor(front)) or _cyclic_swap(back, _economic_actor(back)):
        ev_notes["toxic_arb_leg"] = True

    explained = set()
    if "multi_address" in variants:
        explained |= {"same_actor", "reversal"}
    rescuing = [v for v in variants if v in ("multi_address",)]
    rescued = bool(rescuing) and not (failed - explained)

    return {**base,
            "tier": "known_variant" if rescued else "out_of_catalog",
            "variants": variants,
            "tier2_evidence": ev_notes}


ARBITRAGE_TEMPLATE = {
    "id": "arbitrage_cyclic",
    "sources": [
        "Chi et al. 2024 - arbitrage as a cyclic swap pattern over a directed token graph",
        "Qin et al., FC 2022 - atomic arbitrage closes within a single transaction",
        "Torres et al., USENIX Sec 2021 - multi-venue price-discrepancy capture",
    ],
}


def _gross(ev, addr):
    gin, gout = {}, {}
    for token, frm, to, amt in ev["transfers"]:
        a = int(amt)
        if to == addr:
            gin[token] = gin.get(token, 0) + a
        if frm == addr:
            gout[token] = gout.get(token, 0) + a
    return gin, gout


def match_arbitrage(ev, rel_tol=0.02):
    if not ev:
        return {"verdict": "no_evidence", "failed": ["evidence_missing"]}

    actor = _economic_actor(ev)
    d = _deltas(ev, actor)
    gin, gout = _gross(ev, actor)
    pools = set(ev.get("pools") or [])

    passthrough = []
    for t in set(gin) & set(gout):
        g = max(gin[t], gout[t])
        if g > 0 and abs(d.get(t, 0)) <= rel_tol * g:
            passthrough.append(t)

    gained = {t: v for t, v in d.items() if v > 0}
    P = {
        "multi_venue": len(pools) >= 2,
        "cyclic": len(passthrough) > 0,
        "single_profit_asset": len(gained) == 1,
        "success": ev["status"] == 1,
    }
    core = ["multi_venue", "cyclic", "single_profit_asset", "success"]
    failed = [k for k in core if not P[k]]

    gas = ev["gas_used"] * ev["gas_price"]
    profit_tok = next(iter(gained), None)
    revenue = gained.get(profit_tok, 0) if profit_tok else 0
    return {
        "verdict": "matches:" + ARBITRAGE_TEMPLATE["id"] if not failed
                   else "no_match:" + ",".join(failed),
        "matched": not failed,
        "failed": failed,
        "predicates": P,
        "actor": actor,
        "n_pools": len(pools),
        "profit_token": profit_tok,
        "revenue_raw": str(revenue),
        "gas_cost_eth": gas / 1e18,
        "passthrough_tokens": len(passthrough),
        "profit_eth": (revenue - gas) / 1e18 if profit_tok == WETH else None,
    }


