import builtins, collections, csv, hashlib, io, json, math, os, pathlib, random, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "../../../.."))

PLAN = os.path.join(BASE, "revision/notes/trace_validation/08_analysis/TASK08_ANALYSIS_PLAN.md")
SUMS = os.path.join(BASE, "revision/notes/trace_validation/08_analysis/SHA256SUMS")
TASK07 = os.path.join(BASE, "revision/out/trace_validation/07_execution/task07_outcomes.jsonl")
GROUPS = os.path.join(BASE, "revision/data/trace_validation/group_map/v2/case_group_map.csv")
MANIFEST = os.path.join(BASE, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
MAJ2 = os.path.join(BASE, "revision/out/trace_validation/08_analysis/maj2_sensitivity.json")
OUT = os.path.join(BASE, "revision/out/trace_validation/08_analysis/task08_results.json")

SEED = 20260920
PERMUTATIONS = 20000
MIN_CELL = 20
COVERAGE_FLOOR = 0.80

STILL_FORBIDDEN = ("h4_holdout",)
NO_WRITE = ("/07_execution/", "/manifests/", "/etherscan/", "/value_flow_v2/raw/",
            "/value_flow_v2/index/", "/group_map/", "SHA256SUMS")


class BlindingViolation(RuntimeError):
    pass


class FrozenArtifactWrite(RuntimeError):
    pass


def invert_seal():
    real = builtins.open

    def guarded(file, mode="r", *a, **kw):
        p = str(file).replace("\\", "/")
        low = p.lower()
        if any(f in low for f in STILL_FORBIDDEN):
            raise BlindingViolation("the sealed holdout stays unread: %s" % file)
        if any(m in mode for m in ("w", "a", "x", "+")) and any(t in p for t in NO_WRITE):
            raise FrozenArtifactWrite("refusing to write a hash-pinned path: %s" % file)
        return real(file, mode, *a, **kw)

    builtins.open = guarded
    io.open = guarded
    return real


def verify_plan(real):
    want = None
    for line in real(SUMS):
        h, p = line.split()
        if p.endswith("TASK08_ANALYSIS_PLAN.md"):
            want = h
    got = hashlib.sha256(real(PLAN, "rb").read()).hexdigest()
    if want != got:
        raise SystemExit("pre-registration does not match its hash: %s != %s" % (got, want))
    return got


def _np(v):
    v = int(v)
    return "1" if v == 1 else "2" if v == 2 else "3+"


def _rc(v):
    v = int(v)
    return "<=3" if v <= 3 else "4" if v == 4 else "5-6" if v <= 6 else "7+"


def stratum(cov):
    return (cov["era"], cov["amm_design"], _np(cov["n_pools"]),
            _rc(cov["route_complexity_swap_events"]), str(cov["observable_gas_price_zero"]))


def standardized_diff(labels, sup, strata, weights, included):
    num = collections.defaultdict(lambda: [0, 0])
    den = collections.defaultdict(lambda: [0, 0])
    for lab, s, st in zip(labels, sup, strata):
        if st not in included:
            continue
        t = num[st] if lab == "missed" else den[st]
        t[0] += s
        t[1] += 1
    wm = wr = tot = 0.0
    for st in included:
        w = weights[st]
        m, r = num[st], den[st]
        if m[1] == 0 or r[1] == 0:
            continue
        wm += w * m[0] / m[1]
        wr += w * r[0] / r[1]
        tot += w
    if tot == 0:
        return None, None, None
    return 100 * (wm / tot - wr / tot), 100 * wm / tot, 100 * wr / tot


def newcombe(a, n1, b, n2):
    def wilson(x, n):
        if n == 0:
            return 0.0, 1.0
        z, p = 1.959963985, x / n
        d = 1 + z * z / n
        c = (p + z * z / (2 * n)) / d
        h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
        return max(0.0, c - h), min(1.0, c + h)
    l1, u1 = wilson(a, n1)
    l2, u2 = wilson(b, n2)
    p1, p2 = (a / n1 if n1 else 0), (b / n2 if n2 else 0)
    lo = (p1 - p2) - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    hi = (p1 - p2) + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return 100 * lo, 100 * hi


def main():
    real = invert_seal()
    plan_hash = verify_plan(real)

    rows = [json.loads(l) for l in open(TASK07)]
    bad = [r["case_id"] for r in rows
           if r["multi_sender_boundary"] != (r["boundary_size"] > 1)]
    if bad:
        raise SystemExit("multi_sender_boundary is not boundary_size>1 for %d rows" % len(bad))

    with open(GROUPS) as fh:
        gmap = {r["case_id"]: r["group"] for r in csv.DictReader(fh)}
    raw_labels = [gmap.get(r["case_id"]) for r in rows]
    if any(l is None for l in raw_labels):
        raise SystemExit("group map does not cover every case")
    arms = collections.Counter(raw_labels)
    MISS, REC, NEAR = "target_strict_miss", "control_detected", "control_nearmiss"
    labels = ["missed" if l == MISS else "recorded" if l == REC else "nearmiss"
              for l in raw_labels]
    groups = ["missed", "recorded"]
    keep = [i for i, l in enumerate(labels) if l in groups]

    sup_all = [1 if r["outcome"] == "structurally_supported" else 0 for r in rows]
    und_all = [1 if r["outcome"] == "undecidable" else 0 for r in rows]
    strata_all = [stratum(r["covariates"]) for r in rows]
    third_arm = {"n": arms[NEAR],
                 "outcomes": dict(collections.Counter(
                     r["outcome"] for r, l in zip(rows, labels) if l == "nearmiss"))}
    all_rows = list(rows)
    rows_c = [rows[i] for i in keep]
    labels = [labels[i] for i in keep]
    sup = [sup_all[i] for i in keep]
    und = [und_all[i] for i in keep]
    strata = [strata_all[i] for i in keep]
    rows = rows_c

    size = collections.Counter(strata_all)
    per_group = collections.defaultdict(collections.Counter)
    for st, lab in zip(strata, labels):
        per_group[st][lab] += 1
    included = {st for st in size
                if size[st] >= MIN_CELL and all(per_group[st][g] > 0 for g in groups)}
    pooled = [st for st in size if st not in included]
    if pooled:
        other = ("other",) * 5
        pooled_set = set(pooled)
        strata_all = [other if st in pooled_set else st for st in strata_all]
        strata = [other if st in pooled_set else st for st in strata]
        size = collections.Counter(strata_all)
        per_group = collections.defaultdict(collections.Counter)
        for st, lab in zip(strata, labels):
            per_group[st][lab] += 1
        if size[other] >= MIN_CELL and all(per_group[other][g] > 0 for g in groups):
            included.add(other)
    weights = {st: size[st] for st in included}

    n_missed = sum(1 for l in labels if l == "missed")
    cov_missed = sum(1 for l, st in zip(labels, strata) if l == "missed" and st in included)
    coverage = cov_missed / n_missed if n_missed else 0.0

    adj, adj_m, adj_r = standardized_diff(labels, sup, strata, weights, included)

    m_sup = sum(s for s, l in zip(sup, labels) if l == "missed")
    r_sup = sum(s for s, l in zip(sup, labels) if l != "missed")
    n_rec = len(rows) - n_missed
    unadj = 100 * (m_sup / n_missed - r_sup / n_rec)
    ci = newcombe(m_sup, n_missed, r_sup, n_rec)

    m_und = sum(u for u, l in zip(und, labels) if l == "missed")
    r_und = sum(u for u, l in zip(und, labels) if l != "missed")
    und_diff = 100 * (m_und / n_missed - r_und / n_rec)

    cells = []
    for st in included:
        vals = [s for s, lab, t in zip(sup, labels, strata) if t == st]
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
        if tot:
            null.append(100 * (wm / tot - wr / tot))
    null.sort()
    lo, hi = null[int(0.025 * len(null))], null[int(0.975 * len(null))]
    more_extreme = sum(1 for d in null if abs(d) >= abs(adj))
    pval = (more_extreme + 1) / (len(null) + 1)

    bounds = {}
    for name, add in (("all_undecidable_to_support", 1), ("all_undecidable_to_rejection", 0)):
        s2 = [1 if (o == "structurally_supported" or (o == "undecidable" and add)) else 0
              for o in (r["outcome"] for r in rows)]
        d2, _, _ = standardized_diff(labels, s2, strata, weights, included)
        m2 = sum(x for x, l in zip(s2, labels) if l == "missed") / n_missed
        r2 = sum(x for x, l in zip(s2, labels) if l != "missed") / n_rec
        bounds[name] = {"standardized_diff_pp": round(d2, 4) if d2 is not None else None,
                        "unadjusted_diff_pp": round(100 * (m2 - r2), 4),
                        "missed_share_pct": round(100 * m2, 4),
                        "recorded_share_pct": round(100 * r2, 4)}

    pooled_labels = ["missed" if l == MISS else "recorded" for l in raw_labels]
    p_sup = [1 if r["outcome"] == "structurally_supported" else 0 for r in all_rows]
    pm = sum(x for x, l in zip(p_sup, pooled_labels) if l == "missed")
    pr = sum(x for x, l in zip(p_sup, pooled_labels) if l == "recorded")
    npm = pooled_labels.count("missed")
    npr = pooled_labels.count("recorded")
    comparator_sensitivity = {
        "primary_unpooled_diff_pp": round(unadj, 4),
        "pooled_nearmiss_into_comparator_diff_pp": round(100 * (pm / npm - pr / npr), 4),
        "pooled_recorded_support_pct": round(100 * pr / npr, 4),
        "swing_pp": round(abs(unadj - 100 * (pm / npm - pr / npr)), 4),
        "note": "both negative; the unpooled contrast is primary by plan 2b, decided on semantics",
    }

    def tab(key):
        d = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
        for r, l in zip(rows, labels):
            d[r["covariates"][key]][l][r["outcome"]] += 1
        return {str(k): {g: dict(v[g]) for g in groups} for k, v in d.items()}

    b3 = [(r, l) for r, l in zip(rows, labels) if r["boundary_size"] >= 3]
    out = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "plan_sha256": plan_hash,
        "arms_in_group_map": dict(arms),
        "primary_contrast": "target_strict_miss vs control_detected",
        "third_arm_control_nearmiss": third_arm,
        "cases_contrasted": len(rows), "groups": {g: labels.count(g) for g in groups},
        "outcome_by_group": {g: dict(collections.Counter(
            r["outcome"] for r, l in zip(rows, labels) if l == g)) for g in groups},
        "primary_confirmatory": {
            "statistic": "standardized support-share difference, missed - recorded, pp",
            "standardized_diff_pp": round(adj, 4) if adj is not None else None,
            "standardized_missed_pct": round(adj_m, 4) if adj_m is not None else None,
            "standardized_recorded_pct": round(adj_r, 4) if adj_r is not None else None,
            "permutation_null_95_band_pp": [round(lo, 4), round(hi, 4)],
            "permutation_p_two_sided": round(pval, 6),
            "permutations": len(null),
            "strata_included": len(included),
            "coverage_of_missed": round(coverage, 4),
            "coverage_floor": COVERAGE_FLOOR,
            "demoted_to_exploratory": coverage < COVERAGE_FLOOR,
        },
        "unadjusted": {"diff_pp": round(unadj, 4),
                       "missed_support_pct": round(100 * m_sup / n_missed, 4),
                       "recorded_support_pct": round(100 * r_sup / n_rec, 4),
                       "newcombe_95_pp": [round(ci[0], 4), round(ci[1], 4)],
                       "n_missed": n_missed, "n_recorded": n_rec},
        "undecidable_share": {"missed_pct": round(100 * m_und / n_missed, 4),
                              "recorded_pct": round(100 * r_und / n_rec, 4),
                              "diff_pp": round(und_diff, 4),
                              "blinded_null_95_band_pp": [-5.08, 5.15],
                              "exceeds_band": not (-5.08 <= und_diff <= 5.15)},
        "bounds": bounds,
        "comparator_sensitivity": comparator_sensitivity,
        "by_covariate": {k: tab(k) for k in
                         ("era", "amm_design", "n_pools", "observable_gas_price_zero")},
        "boundary_ge3": {"n": len(b3),
                         "by_group": {g: dict(collections.Counter(
                             r["outcome"] for r, l in b3 if l == g)) for g in groups}},
        "maj2_reference": json.load(open(MAJ2)),
    }
    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("by_covariate", "maj2_reference")}, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
