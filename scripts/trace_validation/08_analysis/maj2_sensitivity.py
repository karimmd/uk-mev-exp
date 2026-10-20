import collections, csv, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "../../../.."))
sys.path.insert(0, os.path.join(BASE, "revision/scripts/trace_validation/value_flow_v2"))
import flow2 as F
from evidence import Evidence

MANIFEST = os.path.join(BASE, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
TASK07 = os.path.join(BASE, "revision/out/trace_validation/07_execution/task07_outcomes.jsonl")
OUT = os.path.join(BASE, "revision/out/trace_validation/08_analysis/maj2_sensitivity.json")


def per_leg_ledger(legs, actor, beneficiary):
    native_in = native_out = gas = top_out = 0
    net = {}
    for label, leg in legs:
        sender = F._lc(leg["tx"].get("from"))
        b = {actor, sender}
        cr = F.native_crossings(leg.get("internal"), b)
        native_in += cr["in_wei"]
        native_out += cr["out_wei"]
        gas += F.gas_cost_wei(leg["receipt"])
        v = F._hexint(leg["tx"].get("value")) or 0
        if v > 0 and F._lc(leg["tx"].get("to")) not in b:
            top_out += v
        if beneficiary and F._lc(beneficiary) in b:
            return None, "actor_is_block_beneficiary"
        d = F.erc20_deltas(leg["receipt"])
        for a in b:
            for tok, amt in (d.get(a) or {}).items():
                net[tok] = net.get(tok, 0) + amt
        for a, wad in F.weth_conversion_deltas(leg["receipt"]).items():
            if a in b:
                net[F.WETH] = net.get(F.WETH, 0) + wad
    net = {t: v for t, v in net.items() if v != 0}
    if any(t != F.WETH for t in net):
        return None, "cross_token_position_unpriced"
    native_net = native_in - native_out - top_out - gas
    total = native_net + net.get(F.WETH, 0)
    zero_gas = any(F._hexint(l["receipt"].get("effectiveGasPrice")) == 0 for _, l in legs)
    complete = not (zero_gas and native_out == 0 and top_out == 0)
    if not complete:
        return (None, "unobserved_cost_could_change_sign") if total > 0 else (total, "negative")
    return total, ("positive" if total > 0 else "negative")


def main():
    ev = Evidence()
    with open(MANIFEST) as fh:
        manifest = {r["case_id"]: r for r in csv.DictReader(fh)}
    rows = [json.loads(l) for l in open(TASK07)]

    t = collections.Counter()
    moved, by_size = [], collections.defaultdict(collections.Counter)
    for r in rows:
        size = r["boundary_size"]
        frozen_vf = r["value_flow"]["state"]
        by_size[size][r["outcome"]] += 1
        if size < 3:
            t["unaffected_by_construction"] += 1
            continue
        row = manifest[r["case_id"]]
        pools = {p.strip().lower() for p in (row["pools_all"] or "").split(";") if p.strip()}
        legs = [("opening", ev.leg(row["front"])), ("closing", ev.leg(row["back"]))]
        actor = (r["value_flow"]["metrics"] or {}).get("actor")
        if not actor:
            t["no_actor_recorded"] += 1
            continue
        try:
            _, state = per_leg_ledger(legs, actor, ev.beneficiary(int(row["block"])))
        except Exception as e:
            t["sensitivity_error:" + type(e).__name__] += 1
            continue
        t["recomputed"] += 1
        same = (state == frozen_vf)
        t["same" if same else "changed"] += 1
        if not same:
            t["%s_to_%s" % (frozen_vf, state)] += 1
            moved.append({"case_id": r["case_id"], "outcome": r["outcome"],
                          "frozen_value_flow": frozen_vf, "per_leg_value_flow": state})

    supported = sum(1 for r in rows if r["outcome"] == "structurally_supported")
    sup_ge3 = sum(1 for r in rows if r["outcome"] == "structurally_supported"
                  and r["boundary_size"] >= 3)
    lost = sum(1 for m in moved
               if m["outcome"] == "structurally_supported" and m["per_leg_value_flow"] != "positive")
    n = len(rows)
    out = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "question": "does folding a second sender into the boundary manufacture support?",
        "test": "per-leg boundary {actor, sender-of-that-leg} vs frozen union boundary",
        "blinded": True,
        "cases": n,
        "two_sender_cases": sum(1 for r in rows if r["boundary_size"] >= 3),
        "tally": dict(t),
        "support_total": supported,
        "support_rate": round(supported / n, 6),
        "support_from_boundary_ge3": sup_ge3,
        "support_rate_excluding_boundary_ge3": round((supported - sup_ge3) / n, 6),
        "support_lost_under_per_leg_boundary": lost,
        "support_rate_under_per_leg_boundary": round((supported - lost) / n, 6),
        "outcomes_by_boundary_size": {str(k): dict(v) for k, v in sorted(by_size.items())},
        "moved_examples": moved[:20],
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(json.dumps({k: v for k, v in out.items() if k != "moved_examples"},
                     indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
