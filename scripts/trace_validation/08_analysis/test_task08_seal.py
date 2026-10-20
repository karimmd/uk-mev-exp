import builtins, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_task08 as R

FAILS, N = [], [0]


def ck(name, cond, extra=""):
    N[0] += 1
    if not cond:
        FAILS.append("%s %s" % (name, extra))
        print("FAIL %s %s" % (name, extra))


real = R.invert_seal()
try:
    for m in ("r", "w", "rb"):
        try:
            open("some/dir/h4_holdout.parquet", m)
            ck("holdout_sealed_%s" % m, False, "no raise")
        except R.BlindingViolation:
            ck("holdout_sealed_%s" % m, True)
        except Exception as e:
            ck("holdout_sealed_%s" % m, False, type(e).__name__)

    pinned = [
        R.BASE + "/revision/out/trace_validation/07_execution/task07_outcomes.jsonl",
        R.BASE + "/revision/data/trace_validation/manifests/v2/cases_blinded.csv",
        R.BASE + "/revision/data/trace_validation/group_map/v2/case_group_map.csv",
        R.BASE + "/revision/data/trace_validation/etherscan/v1/raw/etherscan_raw.jsonl",
        R.BASE + "/revision/notes/trace_validation/08_analysis/SHA256SUMS",
    ]
    for p in pinned:
        for m in ("w", "a", "r+"):
            try:
                open(p, m)
                ck("write_refused_%s_%s" % (os.path.basename(p)[:18], m), False, "NO RAISE")
            except R.FrozenArtifactWrite:
                ck("write_refused_%s_%s" % (os.path.basename(p)[:18], m), True)
            except Exception as e:
                ck("write_refused_%s_%s" % (os.path.basename(p)[:18], m), False, type(e).__name__)

    for p in pinned[:2]:
        try:
            open(p).close()
            ck("read_allowed_%s" % os.path.basename(p)[:18], True)
        except Exception as e:
            ck("read_allowed_%s" % os.path.basename(p)[:18], False, type(e).__name__)

    try:
        open(R.GROUPS).close()
        ck("group_map_now_readable", True)
    except Exception as e:
        ck("group_map_now_readable", False, type(e).__name__)

    tmp = R.BASE + "/revision/out/trace_validation/08_analysis/_seal_probe.tmp"
    try:
        with open(tmp, "w") as fh:
            fh.write("probe")
        ck("ordinary_write_allowed", True)
    except Exception as e:
        ck("ordinary_write_allowed", False, type(e).__name__)
finally:
    builtins.open = real
    if os.path.exists(R.BASE + "/revision/out/trace_validation/08_analysis/_seal_probe.tmp"):
        os.remove(R.BASE + "/revision/out/trace_validation/08_analysis/_seal_probe.tmp")

print("\n%d checks, %d failures" % (N[0], len(FAILS)))
if FAILS:
    for f in FAILS:
        print("  " + f)
    sys.exit(1)
