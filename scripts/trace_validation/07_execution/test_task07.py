import builtins, io, itertools, os, pathlib, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_task07 as R

FAILS, N = [], [0]


def ck(name, cond, extra=""):
    N[0] += 1
    if not cond:
        FAILS.append("%s %s" % (name, extra))
        print("FAIL %s %s" % (name, extra))


def t(state):
    return {"state": state, "reason_codes": [], "metrics": {}}


def v(state, cost_complete=True):
    return {"state": state, "reason_codes": [], "observable_net_positive": None,
            "cost_complete": cost_complete, "metrics": {}}


STATES_T = ["positive", "negative", "undecidable", "technical_unavailable"]
STATES_V = ["positive", "negative", "undecidable", "technical_unavailable"]

for a, b, cc in itertools.product(STATES_T, STATES_V, (True, False)):
    state, reasons = R._outcome(t(a), v(b, cost_complete=cc))
    ck("D1_never_mechanically_confirmed_%s_%s_%s" % (a, b, cc),
       state != "mechanically_confirmed", state)
    ck("D1_state_in_vocabulary_%s_%s_%s" % (a, b, cc),
       state in ("structurally_supported", "rejected", "undecidable"), state)
    ck("D1_reasons_nonempty_%s_%s_%s" % (a, b, cc), bool(reasons))

src = open(R.__file__).read()
body = src.split('"""', 2)[2]
ck("D1_not_emitted_anywhere",
   'return "mechanically_confirmed"' not in body and "'mechanically_confirmed'" not in body)

ck("P_support_needs_both",
   R._outcome(t("positive"), v("positive"))[0] == "structurally_supported")
ck("P_support_cites_counterfactual_reason",
   "counterfactual_unavailable_task04_no_go" in R._outcome(t("positive"), v("positive"))[1])
ck("P_traj_negative_rejects", R._outcome(t("negative"), v("positive"))[0] == "rejected")
ck("P_vf_negative_rejects", R._outcome(t("positive"), v("negative"))[0] == "rejected")
ck("P_both_negative_rejects_once",
   R._outcome(t("negative"), v("negative")) == ("rejected",
                                                ["trajectory_negative", "value_flow_non_positive"]))
for b in ("undecidable", "technical_unavailable"):
    st, rs = R._outcome(t("positive"), v(b))
    ck("D2_unsignable_value_is_undecidable_%s" % b, st == "undecidable", st)
    ck("D2_reason_names_value_flow_%s" % b, ("value_flow_" + b) in rs, rs)
_st, _rs = R._outcome(t("positive"), v("positive", cost_complete=False))
ck("D2_positive_with_incomplete_cost_not_support", _st == "undecidable", _st)
ck("D2_positive_with_incomplete_cost_reason",
   "value_flow_cost_basis_incomplete" in _rs, _rs)
ck("D2_positive_with_complete_cost_is_support",
   R._outcome(t("positive"), v("positive", cost_complete=True))[0] == "structurally_supported")

for a in ("undecidable", "technical_unavailable"):
    ck("D2_trajectory_%s_not_support" % a,
       R._outcome(t(a), v("positive"))[0] == "undecidable")

_real = R.seal()
_io, _os, _po = io.open, os.open, pathlib.Path.open
try:
    P = "data/trace_validation/group_map/v2/case_group_map.csv"
    for name, fn in (("builtins_open", lambda: builtins.open(P)),
                     ("io_open", lambda: io.open(P)),
                     ("os_open", lambda: os.open(P, os.O_RDONLY)),
                     ("pathlib_open", lambda: pathlib.Path(P).open()),
                     ("pathlib_read_bytes", lambda: pathlib.Path(P).read_bytes()),
                     ("pathlib_read_text", lambda: pathlib.Path(P).read_text())):
        try:
            fn()
            ck("S_seal_blocks_%s" % name, False, "no raise")
        except R.BlindingViolation:
            ck("S_seal_blocks_%s" % name, True)
        except Exception as e:
            ck("S_seal_blocks_%s" % name, False, type(e).__name__)
    for p in ("/x/CASE_GROUP_MAP.CSV", "some/h4_holdout.parquet", "a/group_map/b"):
        try:
            builtins.open(p)
            ck("S_seal_variant_%s" % p.split("/")[-1][:14], False, "no raise")
        except R.BlindingViolation:
            ck("S_seal_variant_%s" % p.split("/")[-1][:14], True)
        except Exception as e:
            ck("S_seal_variant_%s" % p.split("/")[-1][:14], False, type(e).__name__)
    try:
        builtins.open(R.__file__).close()
        ck("S_seal_allows_ordinary_path", True)
    except Exception as e:
        ck("S_seal_allows_ordinary_path", False, type(e).__name__)
finally:
    builtins.open, io.open, os.open, pathlib.Path.open = _real, _io, _os, _po
    pathlib.Path.read_bytes = pathlib.Path.__dict__.get("read_bytes", pathlib.Path.read_bytes)

ck("G_verifies_all_three_manifests", len(R.SUMS) == 3
   and any("05_value_flow/v2" in s for s in R.SUMS)
   and any("03b_trajectory" in s for s in R.SUMS)
   and any("TASK07_INPUTS" in s for s in R.SUMS))
ck("G_cardinality_invariant", "cardinality invariant failed" in src)
ck("G_exception_becomes_a_row", "driver_exception" in src)
ck("G_rejects_label_columns", "forbidden column" in src)
import ast
_imports = set()
for _n in ast.walk(ast.parse(src)):
    if isinstance(_n, ast.Import):
        _imports |= {a.name for a in _n.names}
    elif isinstance(_n, ast.ImportFrom):
        _imports.add(_n.module or "")
ck("G_no_counterfactual_import",
   not any("counterfactual" in i or i in ("state2", "witness2") for i in _imports), _imports)
ck("G_imports_both_surviving_witnesses",
   "flow2" in src and "import witness as TRAJ" in src)
ck("G_carries_covariates_for_MAJ1",
   set(R.COVARIATES) == {"era", "amm_design", "n_pools", "observable_gas_price_zero",
                         "route_complexity_swap_events"})
ck("G_reports_multi_sender_boundary", "multi_sender_boundary" in src)

print("\n%d checks, %d failures" % (N[0], len(FAILS)))
if FAILS:
    for f in FAILS:
        print("  " + f)
    sys.exit(1)
