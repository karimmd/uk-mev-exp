import builtins, csv, hashlib, json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
BASE = os.path.abspath(os.path.join(HERE, "../../../.."))
MANIFEST = os.path.join(BASE, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
SUMS = os.path.join(BASE, "revision/notes/trace_validation/05_value_flow/v2/SHA256SUMS_v2")
FORBIDDEN = ("group_map", "case_group_map", "h4_holdout")


class BlindingViolation(RuntimeError):
    pass


def seal():
    real = builtins.open

    def guarded(file, *a, **kw):
        p = str(file).replace("\\", "/").lower()
        if any(f in p for f in FORBIDDEN):
            raise BlindingViolation("blinded executor may not open %s" % file)
        return real(file, *a, **kw)

    builtins.open = guarded
    return real


def verify_frozen():
    out = subprocess.run(["sha256sum", "-c", SUMS], cwd=BASE,
                         capture_output=True, text=True)
    ok = sum(1 for l in out.stdout.splitlines() if l.endswith(": OK"))
    total = sum(1 for _ in builtins.open(SUMS))
    if out.returncode != 0 or ok != total:
        raise SystemExit("frozen candidate does not verify: %d/%d OK\n%s"
                         % (ok, total, out.stdout[-2000:]))
    return ok, total


def main(out_path):
    ok, total = verify_frozen()
    seal()
    import flow2 as F
    from evidence import Evidence

    ev = Evidence()
    rows = list(csv.reader(builtins.open(MANIFEST)))
    header, body = rows[0], rows[1:]
    col = {name: i for i, name in enumerate(header)}
    for forbidden in ("group", "is_recorded", "match", "outcome", "label"):
        bad = [c for c in header if forbidden in c.lower()]
        if bad:
            raise SystemExit("manifest carries a forbidden column: %s" % bad)

    written = 0
    t0 = time.time()
    with builtins.open(out_path, "w") as fh:
        for r in body:
            case_id = r[col["case_id"]]
            pools = {p.strip().lower()
                     for p in (r[col["pools_all"]] or "").split(";") if p.strip()}
            try:
                if not pools:
                    res = {"state": "technical_unavailable",
                           "reason_codes": ["no_pools_in_manifest"],
                           "observable_net_positive": None, "cost_complete": False,
                           "metrics": {}}
                else:
                    legs = {role: ev.leg(r[col[c]].lower())
                            for role, c in (("opening", "front"), ("closing", "back"))}
                    res = F.evaluate(legs["opening"], legs["closing"], pools,
                                     ev.beneficiary(int(r[col["block"]])))
            except F.PoolsRequired as e:
                res = {"state": "technical_unavailable",
                       "reason_codes": ["pools_required:%s" % e],
                       "observable_net_positive": None, "cost_complete": False, "metrics": {}}
            except Exception as e:
                res = {"state": "technical_unavailable",
                       "reason_codes": ["runner_exception:%s" % type(e).__name__],
                       "observable_net_positive": None, "cost_complete": False,
                       "metrics": {"error": str(e)[:200]}}
            fh.write(json.dumps({"case_id": case_id, "value_flow": res}, sort_keys=True) + "\n")
            written += 1

    if written != len(body):
        raise SystemExit("cardinality invariant failed: %d rows for %d cases"
                         % (written, len(body)))
    digest = hashlib.sha256(builtins.open(out_path, "rb").read()).hexdigest()
    print(json.dumps({"cases": len(body), "rows": written, "frozen_hashes": "%d/%d" % (ok, total),
                      "output": out_path, "output_sha256": digest,
                      "elapsed_s": round(time.time() - t0, 1),
                      "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z")},
                     indent=1, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: run_value_flow_v2.py <output.jsonl>")
    main(sys.argv[1])
