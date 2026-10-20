import builtins, csv, hashlib, io, json, os, pathlib, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "../../../.."))
sys.path.insert(0, os.path.join(BASE, "revision/scripts/trace_validation/value_flow_v2"))
sys.path.insert(0, os.path.join(BASE, "revision/scripts/trace_validation/trajectory"))

MANIFEST = os.path.join(BASE, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
SUMS = [
    "revision/notes/trace_validation/05_value_flow/v2/SHA256SUMS_v2",
    "revision/notes/trace_validation/03b_trajectory/SHA256SUMS",
    "revision/notes/trace_validation/07_execution/SHA256SUMS_TASK07_INPUTS",
]
FORBIDDEN = ("group_map", "case_group_map", "h4_holdout")

COVARIATES = ["era", "amm_design", "n_pools", "observable_gas_price_zero",
              "route_complexity_swap_events"]


class BlindingViolation(RuntimeError):
    pass


def _forbidden(path):
    p = str(path).replace("\\", "/").lower()
    return any(f in p for f in FORBIDDEN)


def seal():
    real_open, real_io, real_os = builtins.open, io.open, os.open
    real_p_open = pathlib.Path.open
    real_bytes, real_text = pathlib.Path.read_bytes, pathlib.Path.read_text

    def guard(fn, argno=0):
        def wrapped(*a, **kw):
            target = a[argno] if len(a) > argno else kw.get("file", kw.get("path", ""))
            if _forbidden(target):
                raise BlindingViolation("blinded executor may not open %s" % target)
            return fn(*a, **kw)
        return wrapped

    builtins.open = guard(real_open)
    io.open = guard(real_io)
    os.open = guard(real_os)
    pathlib.Path.open = guard(real_p_open)
    pathlib.Path.read_bytes = guard(real_bytes)
    pathlib.Path.read_text = guard(real_text)
    return real_open


def verify_frozen(real_open):
    out = {}
    for rel in SUMS:
        path = os.path.join(BASE, rel)
        r = subprocess.run(["sha256sum", "-c", path], cwd=BASE, capture_output=True, text=True)
        ok = sum(1 for l in r.stdout.splitlines() if l.endswith(": OK"))
        total = sum(1 for _ in real_open(path))
        if r.returncode != 0 or ok != total:
            raise SystemExit("frozen input does not verify: %s %d/%d\n%s"
                             % (rel, ok, total, r.stdout[-2000:]))
        out[os.path.basename(rel)] = "%d/%d" % (ok, total)
    return out


def _outcome(traj, vf):
    r = []
    if traj["state"] == "negative":
        r.append("trajectory_negative")
    if vf["state"] == "negative":
        r.append("value_flow_non_positive")
    if r:
        return "rejected", r
    if traj["state"] == "positive" and vf["state"] == "positive" and vf.get("cost_complete"):
        return "structurally_supported", ["trajectory_positive",
                                          "value_flow_positive_after_observable_cost",
                                          "counterfactual_unavailable_task04_no_go"]
    if traj["state"] != "positive":
        r.append("trajectory_" + traj["state"])
    if vf["state"] != "positive":
        r.append("value_flow_" + vf["state"])
    elif not vf.get("cost_complete"):
        r.append("value_flow_cost_basis_incomplete")
    return "undecidable", r


def main(out_path):
    real_open = seal()
    verified = verify_frozen(real_open)
    import flow2 as F
    import witness as TRAJ
    from evidence import Evidence

    ev = Evidence()
    with builtins.open(MANIFEST) as fh:
        rows = list(csv.DictReader(fh))
    for c in rows[0]:
        if any(k in c.lower() for k in ("group", "is_recorded", "match", "outcome", "label")):
            raise SystemExit("manifest carries a forbidden column: %s" % c)

    tally, written = {}, 0
    t0 = time.time()
    with builtins.open(out_path, "w") as fh:
        for row in rows:
            case_id = row["case_id"]
            try:
                pools = {p.strip().lower()
                         for p in (row["pools_all"] or "").split(";") if p.strip()}
                rf, sf = ev.receipt(row["front"])
                rv, sv = ev.receipt(row["victim"])
                rb, sb = ev.receipt(row["back"])
                if not (rf and rv and rb):
                    traj = {"state": "undecidable", "reason_codes": ["receipt_unavailable"],
                            "metrics": {"receipt_states": [sf, sv, sb]}}
                    vf = {"state": "technical_unavailable",
                          "reason_codes": ["receipt_unavailable"],
                          "observable_net_positive": None, "cost_complete": False, "metrics": {}}
                elif not pools:
                    traj = {"state": "undecidable", "reason_codes": ["no_pools_in_manifest"],
                            "metrics": {}}
                    vf = {"state": "technical_unavailable",
                          "reason_codes": ["no_pools_in_manifest"],
                          "observable_net_positive": None, "cost_complete": False, "metrics": {}}
                else:
                    traj = TRAJ.evaluate(rf, rv, rb, pools)
                    vf = F.evaluate(ev.leg(row["front"]), ev.leg(row["back"]), pools,
                                    ev.beneficiary(int(row["block"])))
                state, reasons = _outcome(traj, vf)
            except Exception as e:
                traj = {"state": "technical_unavailable",
                        "reason_codes": ["driver_exception:%s" % type(e).__name__], "metrics": {}}
                vf = {"state": "technical_unavailable",
                      "reason_codes": ["driver_exception:%s" % type(e).__name__],
                      "observable_net_positive": None, "cost_complete": False,
                      "metrics": {"error": str(e)[:200]}}
                state, reasons = "undecidable", ["driver_exception"]

            b = (vf.get("metrics") or {}).get("boundary") or []
            fh.write(json.dumps({
                "case_id": case_id,
                "outcome": state,
                "reason_codes": reasons,
                "mechanically_confirmed_available": False,
                "mechanically_confirmed_blocked_by": "task_04_counterfactual_final_no_go",
                "trajectory": traj,
                "value_flow": vf,
                "covariates": {k: row.get(k) for k in COVARIATES},
                "boundary_size": len(b),
                "multi_sender_boundary": len(b) > 1,
            }, sort_keys=True) + "\n")
            written += 1
            tally[state] = tally.get(state, 0) + 1

    if written != len(rows):
        raise SystemExit("cardinality invariant failed: %d rows for %d cases"
                         % (written, len(rows)))
    with real_open(out_path, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    summary = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
               "cases": len(rows), "rows": written, "outcomes": tally,
               "mechanically_confirmed": 0,
               "frozen_inputs_verified": verified,
               "output": os.path.relpath(out_path, BASE), "output_sha256": digest,
               "elapsed_s": round(time.time() - t0, 1)}
    with builtins.open(os.path.splitext(out_path)[0] + "_summary.json", "w") as fh:
        json.dump(summary, fh, indent=1, sort_keys=True)
    print(json.dumps(summary, indent=1, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: run_task07.py <output.jsonl>")
    main(sys.argv[1])
