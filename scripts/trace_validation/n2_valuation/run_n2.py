import collections, csv, hashlib, json, os, random, sys, time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "../../../.."))
REV = os.path.join(BASE, "revision")
sys.path.insert(0, os.path.join(REV, "scripts/trace_validation/value_flow_v2"))
sys.path.insert(0, os.path.join(REV, "scripts/trace_validation/07_execution"))
sys.path.insert(0, os.path.join(REV, "scripts/trace_validation/08_analysis"))

RULE = os.path.join(REV, "notes/trace_validation/n2_valuation/N2_VALUATION_RULE.md")
REG = os.path.join(REV, "notes/trace_validation/n2_valuation/N2_REGISTRATION.txt")
TASK07 = os.path.join(REV, "out/trace_validation/07_execution/task07_outcomes.jsonl")
MANIFEST = os.path.join(REV, "data/trace_validation/manifests/v2/cases_blinded.csv")
GROUPS = os.path.join(REV, "data/trace_validation/group_map/v2/case_group_map.csv")
OUTDIR = os.path.join(REV, "out/trace_validation/n2_valuation")

SEED, PERMUTATIONS, MIN_CELL = 20260920, 20000, 20
FROZEN_REF = {"standardized_diff_pp": -23.4493, "band": [-8.1233, 7.5226]}
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
MISS, REC, NEAR = "target_strict_miss", "control_detected", "control_nearmiss"


def verify_registration():
    want = None
    for line in open(REG):
        if line.startswith("sha256"):
            want = line.split()[1]
    got = hashlib.sha256(open(RULE, "rb").read()).hexdigest()
    if want != got:
        raise SystemExit("rule file does not match its registration: %s != %s" % (got, want))
    return got


def leg_boundary_deltas(F, receipt, boundary):
    d = F.erc20_deltas(receipt)
    conv = F.weth_conversion_deltas(receipt)
    net = {}
    for a in boundary:
        for tok, v in (d.get(a) or {}).items():
            net[tok] = net.get(tok, 0) + v
        if a in conv:
            net[WETH] = net.get(WETH, 0) + conv[a]
    return {t: v for t, v in net.items() if v != 0}


def realized_rates(F, legs, boundary, residuals):
    rates = {t: [] for t in residuals}
    for rc in legs:
        net = leg_boundary_deltas(F, rc, boundary)
        non_weth = {t for t in net if t != WETH}
        w = net.get(WETH, 0)
        for t in residuals:
            if non_weth == {t} and w != 0 and net[t] != 0 and (w > 0) != (net[t] > 0):
                rates[t].append(Fraction(abs(w), abs(net[t])))
    return rates


def rule_A(L, residuals):
    if all(v >= 0 for v in residuals.values()) and L > 0:
        return "positive", L
    if all(v <= 0 for v in residuals.values()) and L <= 0:
        return "negative", L
    return None, None


def rule_B(F, legs, boundary, L, residuals):
    rates = realized_rates(F, legs, boundary, residuals)
    if any(not rates[t] for t in residuals):
        return "undecidable", None, "cross_token_no_realized_rate"
    total = Fraction(L)
    for t, R in residuals.items():
        r = min(rates[t]) if R > 0 else max(rates[t])
        total += R * r
    return ("positive" if total > 0 else "negative"), total, None


def finish(state, total, cost_complete, reasons):
    if state == "undecidable":
        return {"state": "undecidable", "reason_codes": reasons, "observable_net_positive": None,
                "cost_complete": False}
    if not cost_complete:
        if total > 0:
            return {"state": "undecidable", "reason_codes": reasons + ["unobserved_cost_could_change_sign"],
                    "observable_net_positive": None, "cost_complete": False}
        return {"state": "negative", "reason_codes": reasons + ["non_positive_survives_any_additional_cost"],
                "observable_net_positive": False, "cost_complete": False}
    return {"state": "positive" if total > 0 else "negative", "reason_codes": reasons,
            "observable_net_positive": total > 0, "cost_complete": True}


def resign(F, ev, row, man, variant):
    vf = row["value_flow"]
    m = vf["metrics"]
    boundary = set(m["boundary"])
    tp = {t: int(v) for t, v in m["token_position"].items()}
    L = int(m["native_net_wei"]) + tp.get(WETH, 0)
    residuals = {t: v for t, v in tp.items() if t != WETH and v != 0}
    rf, _ = ev.receipt(man["front"])
    rb, _ = ev.receipt(man["back"])
    legs = [rf, rb]
    zero_gas = any(F._hexint(rc.get("effectiveGasPrice")) == 0 for rc in legs)
    cost_complete = not (zero_gas and int(m["native_out_wei"]) == 0
                         and int(m["top_level_value_out_wei"]) == 0)
    base = ["eth_equivalent_ledger_native_plus_weth", "cost_basis_gas_plus_boundary_native_outflow"]
    detail = {"L_wei": str(L), "residuals": {t: str(v) for t, v in residuals.items()},
              "zero_gas": zero_gas, "cost_complete_recomputed": cost_complete}
    if variant in ("primary", "A_only"):
        st, tot = rule_A(L, residuals)
        if st:
            detail["decided_by"] = "A"
            return finish(st, tot, cost_complete, base + ["n2_rule_A_dominance"]), detail
        if variant == "A_only":
            detail["decided_by"] = None
            return finish("undecidable", None, cost_complete, ["cross_token_position_unpriced", "n2_rule_A_undecided"]), detail
    st, tot, why = rule_B(F, legs, boundary, L, residuals)
    detail["decided_by"] = "B" if st != "undecidable" else None
    if st == "undecidable":
        return finish("undecidable", None, cost_complete, ["cross_token_position_unpriced", why]), detail
    detail["T_wei"] = str(int(tot))
    return finish(st, tot, cost_complete, base + ["n2_rule_B_conservative_realized_rate"]), detail


def analyse(rows, gmap, T8):
    labels_raw = [gmap[r["case_id"]] for r in rows]
    labels = ["missed" if l == MISS else "recorded" if l == REC else "nearmiss" for l in labels_raw]
    groups = ["missed", "recorded"]
    keep = [i for i, l in enumerate(labels) if l in groups]
    sup_all = [1 if r["outcome"] == "structurally_supported" else 0 for r in rows]
    und_all = [1 if r["outcome"] == "undecidable" else 0 for r in rows]
    strata_all = [T8.stratum(r["covariates"]) for r in rows]
    rows_c = [rows[i] for i in keep]
    lab = [labels[i] for i in keep]
    sup = [sup_all[i] for i in keep]
    und = [und_all[i] for i in keep]
    strata = [strata_all[i] for i in keep]

    size = collections.Counter(strata_all)
    per_group = collections.defaultdict(collections.Counter)
    for st, l in zip(strata, lab):
        per_group[st][l] += 1
    included = {st for st in size if size[st] >= MIN_CELL and all(per_group[st][g] > 0 for g in groups)}
    pooled = [st for st in size if st not in included]
    if pooled:
        other = ("other",) * 5
        ps = set(pooled)
        strata_all = [other if st in ps else st for st in strata_all]
        strata = [other if st in ps else st for st in strata]
        size = collections.Counter(strata_all)
        per_group = collections.defaultdict(collections.Counter)
        for st, l in zip(strata, lab):
            per_group[st][l] += 1
        if size[other] >= MIN_CELL and all(per_group[other][g] > 0 for g in groups):
            included.add(other)
    included_sorted = sorted(included)
    weights = {st: size[st] for st in included_sorted}
    n_missed = lab.count("missed")
    n_rec = len(rows_c) - n_missed
    coverage = sum(1 for l, st in zip(lab, strata) if l == "missed" and st in included) / n_missed

    def std_diff(ind):
        num = collections.defaultdict(lambda: [0, 0])
        den = collections.defaultdict(lambda: [0, 0])
        for l, s, st in zip(lab, ind, strata):
            if st not in included:
                continue
            t = num[st] if l == "missed" else den[st]
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
        return 100 * (wm / tot - wr / tot), 100 * wm / tot, 100 * wr / tot

    def perm_null(ind):
        cells = []
        for st in included_sorted:
            vals = [s for s, t in zip(ind, strata) if t == st]
            k = sum(1 for l, t in zip(lab, strata) if t == st and l == "missed")
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
        return null

    adj, adj_m, adj_r = std_diff(sup)
    m_sup = sum(s for s, l in zip(sup, lab) if l == "missed")
    r_sup = sum(s for s, l in zip(sup, lab) if l != "missed")
    unadj = 100 * (m_sup / n_missed - r_sup / n_rec)
    ci = T8.newcombe(m_sup, n_missed, r_sup, n_rec)
    m_und = sum(u for u, l in zip(und, lab) if l == "missed")
    r_und = sum(u for u, l in zip(und, lab) if l != "missed")
    und_diff = 100 * (m_und / n_missed - r_und / n_rec)

    null = perm_null(sup)
    lo, hi = null[int(0.025 * len(null))], null[int(0.975 * len(null))]
    pval = (sum(1 for d in null if abs(d) >= abs(adj)) + 1) / (len(null) + 1)

    bounds = {}
    for name, add in (("all_undecidable_to_support", 1), ("all_undecidable_to_rejection", 0)):
        s2 = [1 if (r["outcome"] == "structurally_supported" or (r["outcome"] == "undecidable" and add)) else 0
              for r in rows_c]
        d2, _, _ = std_diff(s2)
        n2 = perm_null(s2)
        lo2, hi2 = n2[int(0.025 * len(n2))], n2[int(0.975 * len(n2))]
        p2 = (sum(1 for d in n2 if abs(d) >= abs(d2)) + 1) / (len(n2) + 1)
        m2 = sum(x for x, l in zip(s2, lab) if l == "missed") / n_missed
        r2 = sum(x for x, l in zip(s2, lab) if l != "missed") / n_rec
        bounds[name] = {"standardized_diff_pp": round(d2, 4), "own_null_95_band_pp": [round(lo2, 4), round(hi2, 4)],
                        "outside_own_band": bool(d2 < lo2 or d2 > hi2), "permutation_p_two_sided": round(p2, 6),
                        "unadjusted_diff_pp": round(100 * (m2 - r2), 4),
                        "missed_share_pct": round(100 * m2, 4), "recorded_share_pct": round(100 * r2, 4)}

    pooled_labels = ["missed" if l == MISS else "recorded" for l in labels_raw]
    pm = sum(s for s, l in zip(sup_all, pooled_labels) if l == "missed")
    pr = sum(s for s, l in zip(sup_all, pooled_labels) if l == "recorded")
    npm, npr = pooled_labels.count("missed"), pooled_labels.count("recorded")
    pooled_diff = 100 * (pm / npm - pr / npr)

    by_arm = {g: dict(collections.Counter(r["outcome"] for r, l in zip(rows, labels_raw) if l == g))
              for g in (MISS, REC, NEAR)}
    rej_prov = {g: dict(collections.Counter("|".join(r["reason_codes"]) for r, l in zip(rows, labels_raw)
                                            if l == g and r["outcome"] == "rejected")) for g in (MISS, REC)}
    und_prov = {g: dict(collections.Counter("|".join(r["value_flow"]["reason_codes"]) for r, l in zip(rows, labels_raw)
                                            if l == g and r["outcome"] == "undecidable")) for g in (MISS, REC)}
    return {
        "outcome_by_arm": by_arm,
        "primary": {"standardized_diff_pp": round(adj, 4), "standardized_missed_pct": round(adj_m, 4),
                    "standardized_recorded_pct": round(adj_r, 4),
                    "permutation_null_95_band_pp": [round(lo, 4), round(hi, 4)],
                    "permutation_p_two_sided": round(pval, 6), "permutations": len(null),
                    "strata_included": len(included), "coverage_of_missed": round(coverage, 4),
                    "demoted_by_coverage": coverage < 0.80},
        "unadjusted": {"diff_pp": round(unadj, 4), "missed_support_pct": round(100 * m_sup / n_missed, 4),
                       "recorded_support_pct": round(100 * r_sup / n_rec, 4),
                       "newcombe_95_pp": [round(ci[0], 4), round(ci[1], 4)], "n_missed": n_missed, "n_recorded": n_rec},
        "undecidable_share": {"missed_pct": round(100 * m_und / n_missed, 4), "recorded_pct": round(100 * r_und / n_rec, 4),
                              "diff_pp": round(und_diff, 4), "blinded_null_95_band_pp": [-5.08, 5.15],
                              "P5_fires": not (-5.08 <= und_diff <= 5.15)},
        "bounds": bounds,
        "comparator_sensitivity": {"primary_unpooled_diff_pp": round(unadj, 4),
                                   "pooled_nearmiss_into_comparator_diff_pp": round(pooled_diff, 4),
                                   "swing_pp": round(abs(unadj - pooled_diff), 4)},
        "rejection_provenance": rej_prov,
        "undecidable_provenance": und_prov,
    }


def main():
    rule_hash = verify_registration()
    import flow2 as F
    from evidence import Evidence
    import run_task07 as T7
    import run_task08 as T8
    ev = Evidence()
    rows = [json.loads(l) for l in open(TASK07)]
    man = {r["case_id"]: r for r in csv.DictReader(open(MANIFEST))}
    gmap = {r["case_id"]: r["group"] for r in csv.DictReader(open(GROUPS))}
    in_scope = [r for r in rows if r["value_flow"]["state"] == "undecidable"
                and r["value_flow"]["reason_codes"] == ["cross_token_position_unpriced"]]
    print("cases in scope:", len(in_scope), "of", len(rows), flush=True)

    os.makedirs(OUTDIR, exist_ok=True)
    results = {"rule_sha256": rule_hash, "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
               "cases_in_scope": len(in_scope), "variants": {}}

    ref = analyse(rows, gmap, T8)
    results["variants"]["frozen"] = ref
    got = ref["primary"]["standardized_diff_pp"]
    band = ref["primary"]["permutation_null_95_band_pp"]
    if abs(got - FROZEN_REF["standardized_diff_pp"]) > 1e-3 or any(abs(a - b) > 1e-3 for a, b in zip(band, FROZEN_REF["band"])):
        raise SystemExit("statistics replica does not reproduce Task 08: %s %s" % (got, band))
    print("frozen reference reproduced:", got, band, flush=True)

    percase = collections.defaultdict(dict)
    for variant in ("primary", "A_only", "B_only"):
        new_rows = []
        for r in rows:
            if r["value_flow"]["state"] == "undecidable" and r["value_flow"]["reason_codes"] == ["cross_token_position_unpriced"]:
                vf_new, detail = resign(F, ev, r, man[r["case_id"]], variant)
                vf2 = dict(r["value_flow"])
                vf2.update(vf_new)
                state, reasons = T7._outcome(r["trajectory"], vf2)
                r2 = dict(r)
                r2["value_flow"] = vf2
                r2["outcome"], r2["reason_codes"] = state, reasons
                new_rows.append(r2)
                percase[r["case_id"]][variant] = {"outcome": state, "vf_state": vf2["state"], **detail}
            else:
                new_rows.append(r)
        res = analyse(new_rows, gmap, T8)
        res["resolution_of_scope"] = {
            g: dict(collections.Counter(percase[r["case_id"]][variant]["decided_by"] or "undecided"
                                        for r in in_scope if gmap[r["case_id"]] == g)) for g in (MISS, REC, NEAR)}
        results["variants"][variant] = res
        print(variant, json.dumps({k: res[k] for k in ("primary", "unadjusted", "undecidable_share")}, indent=1), flush=True)

    with open(os.path.join(OUTDIR, "n2_per_case.jsonl"), "w") as fh:
        for r in in_scope:
            fh.write(json.dumps({"case_id": r["case_id"], "arm": gmap[r["case_id"]],
                                 "frozen_outcome": r["outcome"], "trajectory": r["trajectory"]["state"],
                                 **{v: percase[r["case_id"]][v] for v in ("primary", "A_only", "B_only")}},
                                sort_keys=True) + "\n")
    with open(os.path.join(OUTDIR, "n2_results.json"), "w") as fh:
        json.dump(results, fh, indent=1, sort_keys=True)
    print("written", OUTDIR)


if __name__ == "__main__":
    main()
