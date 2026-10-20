#!/usr/bin/env python3
"""Agent 03b -- pool-state trajectory witness. W2 REVISION (2026-10-14): the two price-scale floors are
relative to the pool price, as the frozen configuration already documents; nothing else changed. See
notes/trace_validation/w2_witness/W2_WITNESS_RULE.md.

Tests the economic price trajectory of a bracket from decoded V2/V3 events. Returns metrics and
reason codes; it never emits a prose judgment and never reads a group label or a stored verdict.

The four conditions, frozen here before any study execution:

  T1  a single shared pool is identifiable
  T2  the opening transaction trades the SAME direction as the victim on that pool
  T3  the victim executes after that movement, and where a pre-opening state is reconstructible,
      the price moved against the victim
  T4  the closing transaction trades the OPPOSITE direction and reverses a material fraction of
      the movement

`positive` requires T1-T4. Any deterministically false necessary condition gives `negative`.
Missing or ambiguous evidence gives `undecidable` or `technical_unavailable`, never `negative`.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode import (decode_pool_events, net_direction, price_v2, price_v3,
                    v2_reserves_before)

# ---------------------------------------------------------------- frozen configuration
REVERSAL_MIN_FRACTION = 0.10   # closing must undo >=10% of the opening's price move
PRICE_EPS = 1e-12              # relative floor below which a price move is treated as no move
FROZEN = {"revision": "W2_relative_price_floors_2026-10-14",
          "reversal_min_fraction": REVERSAL_MIN_FRACTION,
          "price_epsilon_relative": PRICE_EPS,
          "price_orientation": "token1_per_token0",
          "multiple_shared_pools": "undecidable",
          "v2_price_source": "Sync reserves",
          "v3_price_source": "sqrtPriceX96"}


def shared_pools(rf, rv, rb):
    """Pools on which all three legs emitted a decodable swap."""
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
    """Pool price after this transaction, from its last state-bearing event."""
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
    """Return a trajectory witness result for one bracket."""
    reasons, m = [], {}

    # -- T1: a single shared pool -------------------------------------------
    sp = shared_pools(receipt_front, receipt_victim, receipt_back)
    m["n_shared_pools"] = len(sp)
    if not sp:
        return {"state": "undecidable", "reason_codes": ["no_shared_pool_with_swaps"],
                "metrics": m, "frozen_config": FROZEN}
    if len(sp) > 1:
        # OUTCOME_RULES names multiple shared pools as an undecidable trigger. No tie-break is
        # invented here, because any such rule would be unregistered and outcome-adjacent.
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

    # a net-zero leg has no direction and cannot be tested
    if df[0] == 0 or dv[0] == 0 or db[0] == 0:
        return {"state": "undecidable", "reason_codes": ["net_zero_direction_on_shared_pool"],
                "metrics": m, "frozen_config": FROZEN}

    # -- T2: opening trades the same direction as the victim ----------------
    same_dir = (df[0] > 0) == (dv[0] > 0)
    m["opening_same_direction_as_victim"] = same_dir
    # -- T4a: closing trades the opposite direction -------------------------
    opp_dir = (db[0] > 0) != (dv[0] > 0)
    m["closing_opposite_direction_to_victim"] = opp_dir

    # -- prices along the trajectory ----------------------------------------
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

    # -- T3: the opening moved the price against the victim -----------------
    # Price P is token1 per token0. A victim SENDING token0 (delta0 > 0) receives token1 and is
    # hurt when P FALLS, because it then gets less token1 per token0. A victim sending token1 is
    # hurt when P RISES. An opening that trades the victim's direction always pushes P that way.
    adverse = None
    move = None
    if p_pre is not None:
        move = p_open - p_pre
        m["opening_price_move"] = move
        m["opening_price_move_relative"] = (abs(move) / p_pre) if p_pre else None
        if abs(move) <= PRICE_EPS * abs(p_pre):   # W2: floor relative to the pool price, as documented
            adverse = False
            reasons.append("opening_price_move_below_epsilon")
        else:
            adverse = (move < 0) if dv[0] > 0 else (move > 0)
        m["opening_adverse_to_victim"] = adverse

    # -- T4b: the closing reversed a material fraction ----------------------
    # Reversal is movement AGAINST the opening's displacement. Where no pre-opening state exists
    # the victim's own displacement stands in for the direction.
    if move is not None and abs(move) > PRICE_EPS:
        sign = 1.0 if move > 0 else -1.0
        denom = abs(move)
    else:
        alt = p_vict - p_open
        sign = 1.0 if alt > 0 else -1.0
        denom = abs(alt)
    reverted = (p_vict - p_close) * sign
    m["reversal_absolute"] = reverted
    p_ref = p_pre if p_pre is not None else p_open   # W2: denominator floor relative to the pool price
    frac = (reverted / denom) if denom > PRICE_EPS * abs(p_ref) else None
    m["reversal_fraction"] = frac
    material_reversal = bool(frac is not None and frac >= REVERSAL_MIN_FRACTION)
    m["material_reversal"] = material_reversal

    # -- verdict -------------------------------------------------------------
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
        # direction conditions all hold but no pre-opening state exists to confirm the move
        reasons.append("pre_opening_state_unavailable_direction_only")
    reasons.append("same_direction_opening")
    reasons.append("opposite_direction_closing")
    reasons.append("material_reversal")
    if adverse:
        reasons.append("opening_adverse_price_move_confirmed")
    return {"state": "positive", "reason_codes": reasons, "metrics": m,
            "frozen_config": FROZEN}
