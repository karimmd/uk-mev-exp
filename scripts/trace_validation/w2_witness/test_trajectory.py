import gzip, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from decode import (V2_SWAP, V2_SYNC, V3_SWAP, decode_v2_swap, decode_v2_sync,
                    decode_v3_swap, price_v2, price_v3, v2_reserves_before, Q96)
from witness import evaluate, REVERSAL_MIN_FRACTION

POOL = "0x" + "ab" * 20
FAILS = []


def check(name, cond, detail=""):
    print(("  PASS  " if cond else "  FAIL  ") + name +
          (("  " + str(detail)) if detail and not cond else ""))
    if not cond:
        FAILS.append(name)


def w(n):
    return "%064x" % (n & ((1 << 256) - 1))


def log_v2_swap(a0in, a1in, a0out, a1out, pool=POOL):
    return {"address": pool, "topics": [V2_SWAP],
            "data": "0x" + w(a0in) + w(a1in) + w(a0out) + w(a1out)}


def log_v2_sync(r0, r1, pool=POOL):
    return {"address": pool, "topics": [V2_SYNC], "data": "0x" + w(r0) + w(r1)}


def log_v3_swap(d0, d1, sqrtp, liq=10 ** 18, tick=0, pool=POOL):
    return {"address": pool, "topics": [V3_SWAP],
            "data": "0x" + w(d0) + w(d1) + w(sqrtp) + w(liq) + w(tick)}


def rc(logs):
    return {"logs": logs}


print("\n1. decoding reproduces known integers")
d = decode_v2_swap(log_v2_swap(1000, 0, 0, 2000))
check("V2 swap amounts", d["amount0In"] == 1000 and d["amount1Out"] == 2000, d)
check("V2 pool deltas", d["delta0"] == 1000 and d["delta1"] == -2000, d)
s = decode_v2_sync(log_v2_sync(5 * 10 ** 18, 7 * 10 ** 18))
check("V2 sync reserves", s["reserve0"] == 5 * 10 ** 18 and s["reserve1"] == 7 * 10 ** 18)
v3 = decode_v3_swap(log_v3_swap(-(10 ** 18), 3 * 10 ** 18, 2 * Q96))
check("V3 signed negative amount0", v3["delta0"] == -(10 ** 18), v3["delta0"])
check("V3 signed positive amount1", v3["delta1"] == 3 * 10 ** 18)
check("V3 price from sqrtPriceX96 == 4.0", abs(price_v3(2 * Q96) - 4.0) < 1e-12,
      price_v3(2 * Q96))
check("V2 price = r1/r0", abs(price_v2(2, 6) - 3.0) < 1e-12)
check("zero reserve gives no price", price_v2(0, 5) is None)

print("\n2. exact integer inversion to the pre-transaction state")
sync = decode_v2_sync(log_v2_sync(1000 + 100, 2000 - 180))
sw = [decode_v2_swap(log_v2_swap(100, 0, 0, 180))]
check("reserves before recovered exactly", v2_reserves_before(sync, sw) == (1000, 2000),
      v2_reserves_before(sync, sw))
sync2 = decode_v2_sync(log_v2_sync(1000 + 100 + 50, 2000 - 180 - 80))
sw2 = [decode_v2_swap(log_v2_swap(100, 0, 0, 180)),
       decode_v2_swap(log_v2_swap(50, 0, 0, 80))]
check("multi-swap inversion in one transaction", v2_reserves_before(sync2, sw2) == (1000, 2000))


def v2_bracket(f_in=100, v_in=200, b_out=95, r0=10 ** 6, r1=10 ** 6):
    a0, b0 = r0, r1
    a0 += f_in; b0 -= 90
    front = rc([log_v2_swap(f_in, 0, 0, 90), log_v2_sync(a0, b0)])
    a1, b1 = a0 + v_in, b0 - 150
    victim = rc([log_v2_swap(v_in, 0, 0, 150), log_v2_sync(a1, b1)])
    a2, b2 = a1 - b_out, b1 + 100
    back = rc([log_v2_swap(0, 100, b_out, 0), log_v2_sync(a2, b2)])
    return front, victim, back


print("\n3. a well-formed V2 sandwich is positive")
r = evaluate(*v2_bracket())
check("state positive", r["state"] == "positive", r["reason_codes"])
check("venue v2", r["metrics"].get("venue") == "v2")
check("one shared pool", r["metrics"]["n_shared_pools"] == 1)
check("pre-opening state reconstructed", r["metrics"]["pre_opening_state_reconstructed"])
check("opening adverse confirmed", r["metrics"].get("opening_adverse_to_victim") is True)
check("material reversal", r["metrics"]["material_reversal"])

print("\n4. mutations that look similar but fail one necessary condition")
f, v, b = v2_bracket()
r0_, r1_ = 10 ** 6, 10 ** 6
f_opp = rc([log_v2_swap(0, 90, 100, 0), log_v2_sync(r0_ - 100, r1_ + 90)])
r = evaluate(f_opp, v, b)
check("opposite-direction opening -> negative", r["state"] == "negative", r)
check("  reason names the direction", "opening_not_same_direction_as_victim" in r["reason_codes"])

b_same = rc([log_v2_swap(50, 0, 0, 40), log_v2_sync(10 ** 6 + 350, 10 ** 6 - 280)])
r = evaluate(f, v, b_same)
check("same-direction closing -> negative", r["state"] == "negative", r["reason_codes"])
check("  reason names the closing", "closing_not_opposite_direction" in r["reason_codes"])

f2, v2_, _ = v2_bracket()
a1 = 10 ** 6 + 100 + 200
b1 = 10 ** 6 - 90 - 150
tiny = rc([log_v2_swap(0, 1, 1, 0), log_v2_sync(a1 - 1, b1 + 1)])
r = evaluate(f2, v2_, tiny)
check("sub-threshold reversal -> negative", r["state"] == "negative", r["reason_codes"])
check("  reason names the threshold",
      "closing_reversal_below_threshold" in r["reason_codes"], r["reason_codes"])

print("\n5. ambiguity and missing evidence never become negative")
r = evaluate(rc([]), rc([]), rc([]))
check("no shared pool -> undecidable", r["state"] == "undecidable")
check("  reason code", "no_shared_pool_with_swaps" in r["reason_codes"])

P2 = "0x" + "cd" * 20
f2p = rc([log_v2_swap(100, 0, 0, 90), log_v2_sync(1, 1),
          log_v2_swap(100, 0, 0, 90, P2), log_v2_sync(1, 1, P2)])
v2p = rc([log_v2_swap(200, 0, 0, 150), log_v2_sync(1, 1),
          log_v2_swap(200, 0, 0, 150, P2), log_v2_sync(1, 1, P2)])
b2p = rc([log_v2_swap(0, 100, 95, 0), log_v2_sync(1, 1),
          log_v2_swap(0, 100, 95, 0, P2), log_v2_sync(1, 1, P2)])
r = evaluate(f2p, v2p, b2p)
check("two shared pools -> undecidable", r["state"] == "undecidable", r["reason_codes"])
check("  reason code", "multiple_shared_pools" in r["reason_codes"])

mixed_b = rc([log_v3_swap(-95, 100, 2 * Q96)])
r = evaluate(f, v, mixed_b)
check("mixed venue on one pool -> undecidable", r["state"] == "undecidable", r["reason_codes"])

nosync_f = rc([log_v2_swap(100, 0, 0, 90)])
nosync_v = rc([log_v2_swap(200, 0, 0, 150)])
nosync_b = rc([log_v2_swap(0, 100, 95, 0)])
r = evaluate(nosync_f, nosync_v, nosync_b)
check("no Sync -> price state unavailable", r["state"] == "undecidable", r["reason_codes"])
check("  reason code", "price_state_unavailable" in r["reason_codes"])

print("\n6. V3 path is exercised separately from V2")
f3 = rc([log_v3_swap(100, -90, int(1.10 * Q96))])
v3_ = rc([log_v3_swap(200, -150, int(1.20 * Q96))])
b3 = rc([log_v3_swap(-95, 100, int(1.05 * Q96))])
r = evaluate(f3, v3_, b3)
check("V3 bracket evaluates", r["state"] in ("positive", "negative", "undecidable"), r["state"])
check("venue reported as v3", r["metrics"].get("venue") == "v3", r["metrics"].get("venue"))
check("V3 has no reconstructed pre-opening state",
      r["metrics"]["pre_opening_state_reconstructed"] is False)
check("V3 positive is direction-based only",
      r["state"] != "positive" or
      "pre_opening_state_unavailable_direction_only" in r["reason_codes"], r["reason_codes"])

print("\n7. invariants")
r = evaluate(*v2_bracket())
check("every result carries a state", "state" in r)
check("every result carries >=1 reason code", len(r["reason_codes"]) >= 1)
check("frozen config is emitted with every result", "frozen_config" in r)
check("threshold is the frozen one", r["frozen_config"]["reversal_min_fraction"] == REVERSAL_MIN_FRACTION)
for name, res in (("positive", evaluate(*v2_bracket())),
                  ("negative", evaluate(f_opp, v, b)),
                  ("undecidable", evaluate(rc([]), rc([]), rc([])))):
    check("state %s is in the allowed enum" % name,
          res["state"] in ("positive", "negative", "undecidable", "technical_unavailable"))

print("\n8. no forbidden dependency")
import ast as _ast
for mod in ("witness.py", "decode.py"):
    tree = _ast.parse(open(os.path.join(HERE, mod)).read())
    imported = set()
    for node in _ast.walk(tree):
        if isinstance(node, _ast.Import):
            imported.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, _ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    forbidden = imported & {"catalog", "s0_isolated", "causal_oracle", "build_s0_cohorts"}
    check("%s imports no canonical matching module" % mod, not forbidden, sorted(forbidden))
    names = {n.id for n in _ast.walk(tree) if isinstance(n, _ast.Name)}
    names |= {n.attr for n in _ast.walk(tree) if isinstance(n, _ast.Attribute)}
    leaked = names & {"match_sandwich", "match_arbitrage", "match_liquidation",
                      "in_mined", "case_group_map", "in_records"}
    check("%s uses no canonical verdict symbol" % mod, not leaked, sorted(leaked))
    strs = {n.value for n in _ast.walk(tree)
            if isinstance(n, _ast.Constant) and isinstance(n.value, str)}
    bad_strs = {x for x in strs if x in ("group", "in_records", "missed", "profitable",
                                         "covered", "case_group_map.csv")}
    check("%s reads no group or outcome field name" % mod, not bad_strs, sorted(bad_strs))

print("\n%s" % ("ALL TESTS PASSED" if not FAILS else "FAILURES (%d): %s" % (len(FAILS), FAILS)))
sys.exit(1 if FAILS else 0)
