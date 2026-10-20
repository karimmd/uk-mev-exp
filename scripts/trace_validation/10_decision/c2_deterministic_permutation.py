import collections, csv, hashlib, json, os, platform, random, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "../../../.."))

TASK07 = os.path.join(BASE, "revision/out/trace_validation/07_execution/task07_outcomes.jsonl")
GROUPS = os.path.join(BASE, "revision/data/trace_validation/group_map/v2/case_group_map.csv")
OUT = os.path.join(BASE, "revision/out/trace_validation/10_decision/c2_deterministic_permutation.json")

SEED = 20260920
PERMUTATIONS = 20000
MIN_CELL = 20

EXPECT = {"support": -23.4493, "undecidable_to_support": -11.0894}
TOL = 0.0051

MISS, REC = "target_strict_miss", "control_detected"


def _np(v):
    v = int(v)
    return "1" if v == 1 else "2" if v == 2 else "3+"


def _rc(v):
    v = int(v)
    return "<=3" if v <= 3 else "4" if v == 4 else "5-6" if v <= 6 else "7+"


def stratum(cov):
    return (cov["era"], cov["amm_design"], _np(cov["n_pools"]),
            _rc(cov["route_complexity_swap_events"]), str(cov["observable_gas_price_zero"]))


def standardized_diff(labels, sup, strata, weights, included_sorted):
    num = collections.defaultdict(lambda: [0, 0])
    den = collections.defaultdict(lambda: [0, 0])
    inc = set(included_sorted)
    for lab, s, st in zip(labels, sup, strata):
        if st not in inc:
            continue
        t = num[st] if lab == "missed" else den[st]
        t[0] += s
        t[1] += 1
    wm = wr = tot = 0.0
    for st in included_sorted:
        w = weights[st]
        m, r = num[st], den[st]
        if m[1] == 0 or r[1] == 0:
            continue
        wm += w * m[0] / m[1]
        wr += w * r[0] / r[1]
        tot += w
    if tot == 0:
        return None
    return 100 * (wm / tot - wr / tot)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    rows = [json.loads(l) for l in open(TASK07)]
    with open(GROUPS) as fh:
        gmap = {r["case_id"]: r["group"] for r in csv.DictReader(fh)}
    raw = [gmap[r["case_id"]] for r in rows]

    labels_all = ["missed" if l == MISS else "recorded" if l == REC else "nearmiss" for l in raw]
    strata_all = [stratum(r["covariates"]) for r in rows]
    keep = [i for i, l in enumerate(labels_all) if l in ("missed", "recorded")]

    labels = [labels_all[i] for i in keep]
    strata = [strata_all[i] for i in keep]
    outcomes = [rows[i]["outcome"] for i in keep]

    size = collections.Counter(strata_all)
    per_group = collections.defaultdict(collections.Counter)
    for st, lab in zip(strata, labels):
        per_group[st][lab] += 1
    included = {st for st in size
                if size[st] >= MIN_CELL and all(per_group[st][g] > 0 for g in ("missed", "recorded"))}
    pooled = {st for st in size if st not in included}
    if pooled:
        other = ("other",) * 5
        strata_all = [other if st in pooled else st for st in strata_all]
        strata = [other if st in pooled else st for st in strata]
        size = collections.Counter(strata_all)
        per_group = collections.defaultdict(collections.Counter)
        for st, lab in zip(strata, labels):
            per_group[st][lab] += 1
        if size[other] >= MIN_CELL and all(per_group[other][g] > 0 for g in ("missed", "recorded")):
            included.add(other)
    included_sorted = sorted(included)
    weights = {st: size[st] for st in included_sorted}

    indicators = {
        "support": [1 if o == "structurally_supported" else 0 for o in outcomes],
        "undecidable_to_support": [1 if o in ("structurally_supported", "undecidable") else 0
                                   for o in outcomes],
    }

    result = {}
    for name in ("support", "undecidable_to_support"):
        sup = indicators[name]
        obs = standardized_diff(labels, sup, strata, weights, included_sorted)

        cells = []
        for st in included_sorted:
            vals = [s for s, t in zip(sup, strata) if t == st]
            k = sum(1 for lab, t in zip(labels, strata) if t == st and lab == "missed")
            if k == 0 or k == len(vals):
                continue
            cells.append((weights[st], vals, sum(vals), k, len(vals)))

        rnd = random.Random(SEED)
        null = []
        for _ in range(PERMUTATIONS):
            wm = wr = tot = 0.0
            for w, vals, tot_sup, k, n_st in cells:
                ms = sum(rnd.sample(vals, k))
                wm += w * ms / k
                wr += w * (tot_sup - ms) / (n_st - k)
                tot += w
            null.append(100 * (wm / tot - wr / tot))
        null.sort()
        lo = null[int(0.025 * len(null))]
        hi = null[int(0.975 * len(null))]
        more = sum(1 for d in null if abs(d) >= abs(obs))
        result[name] = {
            "observed_standardized_diff_pp": round(obs, 4),
            "null_95_band_pp": [round(lo, 4), round(hi, 4)],
            "outside_own_band": bool(obs < lo or obs > hi),
            "permutation_p_two_sided": (more + 1) / (len(null) + 1),
            "permutation_p_as_fraction": "%d/%d" % (more + 1, len(null) + 1),
            "permutations": len(null),
            "cells_contributing": len(cells),
            "null_sd_pp": round((sum((d - sum(null) / len(null)) ** 2 for d in null)
                                 / (len(null) - 1)) ** 0.5, 4),
        }
        d = abs(round(obs, 4) - EXPECT[name])
        result[name]["reproduces_published_point_estimate"] = bool(d <= TOL)
        result[name]["published_point_estimate_pp"] = EXPECT[name]
        result[name]["point_estimate_abs_difference_pp"] = round(d, 6)

    out = {
        "produced_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "purpose": "R2-08 C2 -- deterministic, bound-specific permutation nulls",
        "defect_corrected": ("set iteration over stratum keys made the seeded permutation stream "
                             "order-dependent across processes; and the resolved-undecidable "
                             "endpoint was compared against the original indicator's null"),
        "seed": SEED,
        "permutations": PERMUTATIONS,
        "min_cell": MIN_CELL,
        "strata_included": len(included_sorted),
        "n_contrasted": len(labels),
        "n_missed": labels.count("missed"),
        "n_recorded": labels.count("recorded"),
        "n_all_rows": len(rows),
        "determinism": {
            "stratum_keys_sorted_before_every_accumulation_and_draw": True,
            "pythonhashseed_env": os.environ.get("PYTHONHASHSEED", "(unset)"),
            "note": ("with the sort in place the result no longer depends on PYTHONHASHSEED; the "
                     "run is repeated under two explicit values as the proof"),
        },
        "environment": {
            "python": sys.version.split()[0],
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "inputs": {
            "task07_outcomes.jsonl": sha256(TASK07),
            "case_group_map.csv": sha256(GROUPS),
            "this_script": sha256(os.path.abspath(__file__)),
        },
        "results": result,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("\nwrote %s" % OUT)
    ok = all(result[k]["reproduces_published_point_estimate"] for k in result)
    print("reproduces both published point estimates: %s" % ok)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
