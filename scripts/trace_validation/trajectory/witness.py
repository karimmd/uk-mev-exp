import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode import (decode_pool_events, net_direction, price_v2, price_v3,
                    v2_reserves_before)

REVERSAL_MIN_FRACTION = 0.10
PRICE_EPS = 1e-12
FROZEN = {"reversal_min_fraction": REVERSAL_MIN_FRACTION,
          "price_epsilon_relative": PRICE_EPS,
          "price_orientation": "token1_per_token0",
          "multiple_shared_pools": "undecidable",
          "v2_price_source": "Sync reserves",
          "v3_price_source": "sqrtPriceX96"}


def shared_pools(rf, rv, rb):
    def sp(rc):
        s = set()
        for lg in (rc.get("logs") or []):
            t = (lg.get("topics") or [None])[0]
            if t in ("0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822",
                     "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"):
                s.add((lg.get("address") or "").lower())
        return s
    return sp(rf) & sp(rv) & sp(rb)


def _venue(events):
    kinds = {e["kind"] for e in events}
    if "v3_swap" in kinds and "v2_swap" in kinds:
        return "mixed"
    if "v3_swap" in kinds:
        return "v3"
    if "v2_swap" in kinds:
        return "v2"
    return None


def _post_price(events, venue):
    if venue == "v2":
        syncs = [e for e in events if e["kind"] == "v2_sync"]
        if not syncs:
            return None
        return price_v2(syncs[-1]["reserve0"], syncs[-1]["reserve1"])
    if venue == "v3":
        sw = [e for e in events if e["kind"] == "v3_swap"]
        if not sw:
            return None
        return price_v3(sw[-1]["sqrtPriceX96"])
    return None


def evaluate(receipt_front, receipt_victim, receipt_back, manifest_pools=None):
    reasons, m = [], {}

    sp = shared_pools(receipt_front, receipt_victim, receipt_back)
    m["n_shared_pools"] = len(sp)
    if not sp:
        return {"state": "undecidable", "reason_codes": ["no_shared_pool_with_swaps"],
                "metrics": m, "frozen_config": FROZEN}
    if len(sp) > 1:
        return {"state": "undecidable", "reason_codes": ["multiple_shared_pools"],
                "metrics": m, "frozen_config": FROZEN}
    pool = next(iter(sp))
    m["shared_pool"] = pool
    if manifest_pools is not None:
        m["shared_pool_in_manifest"] = pool in manifest_pools

    ef = decode_pool_events(receipt_front, pool)
    ev = decode_pool_events(receipt_victim, pool)
    eb = decode_pool_events(receipt_back, pool)
    venues = {_venue(ef), _venue(ev), _venue(eb)}
    venues.discard(None)
    if "mixed" in venues or len(venues) != 1:
        return {"state": "undecidable",
                "reason_codes": ["mixed_or_inconsistent_venue_on_shared_pool"],
                "metrics": {**m, "venues": sorted(str(v) for v in venues)},
                "frozen_config": FROZEN}
    venue = venues.pop()
    m["venue"] = venue
    m["n_swaps"] = {"opening": len([e for e in ef if e["kind"].endswith("swap")]),
                    "victim": len([e for e in ev if e["kind"].endswith("swap")]),
                    "closing": len([e for e in eb if e["kind"].endswith("swap")])}

    df, dv, db = net_direction(ef), net_direction(ev), net_direction(eb)
    if not (df and dv and db):
        return {"state": "undecidable", "reason_codes": ["missing_swap_on_shared_pool"],
                "metrics": m, "frozen_config": FROZEN}
    m["net_delta0"] = {"opening": df[0], "victim": dv[0], "closing": db[0]}
    m["net_delta1"] = {"opening": df[1], "victim": dv[1], "closing": db[1]}

    if df[0] == 0 or dv[0] == 0 or db[0] == 0:
        return {"state": "undecidable", "reason_codes": ["net_zero_direction_on_shared_pool"],
                "metrics": m, "frozen_config": FROZEN}

    same_dir = (df[0] > 0) == (dv[0] > 0)
    m["opening_same_direction_as_victim"] = same_dir
    opp_dir = (db[0] > 0) != (dv[0] > 0)
    m["closing_opposite_direction_to_victim"] = opp_dir

    p_open = _post_price(ef, venue)
    p_vict = _post_price(ev, venue)
    p_close = _post_price(eb, venue)
    p_pre = None
    if venue == "v2":
        syncs = [e for e in ef if e["kind"] == "v2_sync"]
        swaps = [e for e in ef if e["kind"] == "v2_swap"]
        if syncs and swaps:
            rb_ = v2_reserves_before(syncs[-1], swaps)
            if rb_:
                p_pre = price_v2(*rb_)
    m["price"] = {"pre_opening": p_pre, "after_opening": p_open,
                  "after_victim": p_vict, "after_closing": p_close}
    m["pre_opening_state_reconstructed"] = p_pre is not None
    if p_open is None or p_vict is None or p_close is None:
        return {"state": "undecidable", "reason_codes": ["price_state_unavailable"],
                "metrics": m, "frozen_config": FROZEN}

    adverse = None
    move = None
    if p_pre is not None:
        move = p_open - p_pre
        m["opening_price_move"] = move
        m["opening_price_move_relative"] = (abs(move) / p_pre) if p_pre else None
        if abs(move) <= PRICE_EPS * max(abs(p_pre), 1.0):
            adverse = False
            reasons.append("opening_price_move_below_epsilon")
        else:
            adverse = (move < 0) if dv[0] > 0 else (move > 0)
        m["opening_adverse_to_victim"] = adverse

    if move is not None and abs(move) > PRICE_EPS:
        sign = 1.0 if move > 0 else -1.0
        denom = abs(move)
    else:
        alt = p_vict - p_open
        sign = 1.0 if alt > 0 else -1.0
        denom = abs(alt)
    reverted = (p_vict - p_close) * sign
    m["reversal_absolute"] = reverted
    frac = (reverted / denom) if denom > PRICE_EPS else None
    m["reversal_fraction"] = frac
    material_reversal = bool(frac is not None and frac >= REVERSAL_MIN_FRACTION)
    m["material_reversal"] = material_reversal

    if not same_dir:
        return {"state": "negative", "reason_codes": ["opening_not_same_direction_as_victim"],
                "metrics": m, "frozen_config": FROZEN}
    if adverse is False:
        return {"state": "negative", "reason_codes": ["opening_not_adverse_to_victim"],
                "metrics": m, "frozen_config": FROZEN}
    if not opp_dir:
        return {"state": "negative", "reason_codes": ["closing_not_opposite_direction"],
                "metrics": m, "frozen_config": FROZEN}
    if frac is None:
        return {"state": "undecidable", "reason_codes": ["reversal_fraction_indeterminate"],
                "metrics": m, "frozen_config": FROZEN}
    if not material_reversal:
        return {"state": "negative", "reason_codes": ["closing_reversal_below_threshold"],
                "metrics": m, "frozen_config": FROZEN}

    if adverse is None:
        reasons.append("pre_opening_state_unavailable_direction_only")
    reasons.append("same_direction_opening")
    reasons.append("opposite_direction_closing")
    reasons.append("material_reversal")
    if adverse:
        reasons.append("opening_adverse_price_move_confirmed")
    return {"state": "positive", "reason_codes": reasons, "metrics": m,
            "frozen_config": FROZEN}
