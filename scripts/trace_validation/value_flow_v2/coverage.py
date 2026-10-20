import collections, csv, json, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence import Evidence, BASE
import flow2 as F

MANIFEST = os.path.join(BASE, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
OUT = os.path.join(BASE, "revision/out/trace_validation/value_flow_v2/coverage.json")

PRECURSOR = ["evidence_incomplete", "body_inconsistent", "recipient_unresolved",
             "recipient_disagreement", "boundary_unresolved", "actor_is_beneficiary",
             "reaches_ledger"]


def pools_of(row):
    return {p.strip().lower() for p in (row["pools_all"] or "").split(";") if p.strip()}


def main(limit=None):
    ev = Evidence()
    rows = list(csv.DictReader(open(MANIFEST)))
    if limit:
        rows = rows[:limit]
    t = collections.Counter()
    basis = collections.Counter()
    for row in rows:
        t["cases"] += 1
        pools = pools_of(row)
        if not pools:
            t["no_pools_in_manifest"] += 1
            continue
        legs = {}
        incomplete = False
        for role, col in (("opening", "front"), ("closing", "back")):
            h = row[col].lower()
            legs[role] = ev.leg(h)
            L = legs[role]
            if (L["receipt"] is None or L["tx_state"] != "success"
                    or L["internal_state"] not in ("success", "empty")
                    or L["internal"] is None):
                incomplete = True
        if incomplete:
            t["evidence_incomplete"] += 1
            continue

        diffs = {r: F.body_consistent(legs[r]["tx"], legs[r]["receipt"]) for r in legs}
        if any(diffs.values()):
            t["body_inconsistent"] += 1
            continue

        recips = {r: F.economic_recipient(legs[r]["receipt"], pools) for r in legs}
        if any(v is None for v in recips.values()):
            t["recipient_unresolved"] += 1
            continue
        if recips["opening"] != recips["closing"]:
            t["recipient_disagreement"] += 1
            continue
        actor = recips["opening"]

        ok = True
        for role in ("opening", "closing"):
            tx = legs[role]["tx"]
            if (tx.get("from") or "").lower() == actor:
                basis[role + ":actor_is_sender"] += 1
            elif (tx.get("to") or "").lower() == actor:
                basis[role + ":sender_invokes_actor"] += 1
            else:
                ok = False
        if not ok:
            t["boundary_unresolved"] += 1
            continue

        ben = ev.beneficiary(int(row["block"]))
        if ben and (ben == actor or any((legs[r]["tx"].get("from") or "").lower() == ben
                                        for r in legs)):
            t["actor_is_beneficiary"] += 1
            continue
        t["reaches_ledger"] += 1

    n = t["cases"]
    summary = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "cases": n,
        "precursor_tally": {k: t[k] for k in PRECURSOR if t[k]},
        "precursor_rate": {k: round(t[k] / n, 6) for k in PRECURSOR if t[k]},
        "boundary_basis": dict(basis),
        "other": {k: v for k, v in t.items() if k not in PRECURSOR and k != "cases"},
        "note": "precursor gates only; no sign, no outcome distribution, no group label",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(summary, fh, indent=1, sort_keys=True)
    print(json.dumps(summary, indent=1, sort_keys=True))


if __name__ == "__main__":
    lim = None
    if "--limit" in sys.argv:
        lim = int(sys.argv[sys.argv.index("--limit") + 1])
    main(lim)
