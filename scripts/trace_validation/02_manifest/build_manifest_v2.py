import csv, gzip, hashlib, json, os, re, sys, time
from collections import Counter

ROOT = os.environ.get("MEV_ROOT", ".")
csv.field_size_limit(10 ** 9)

S0 = os.path.join(ROOT, "revision/out/s0val")
RCACHE = os.path.join(ROOT, "revision/cache/receipts")
FIX = os.path.join(ROOT, "revision/data/trace_validation/01_feasibility")
V1_MANI = os.path.join(ROOT, "revision/data/trace_validation/manifests/v1")
V1_GRP = os.path.join(ROOT, "revision/data/trace_validation/group_map/v1")
V2_MANI = os.path.join(ROOT, "revision/data/trace_validation/manifests/v2")
V2_GRP = os.path.join(ROOT, "revision/data/trace_validation/group_map/v2")
NOTES = os.path.join(ROOT, "revision/notes/trace_validation/02_manifest_v2")
for d in (V2_MANI, V2_GRP, NOTES):
    os.makedirs(d, exist_ok=True)

V2_SWAP = "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
V3_SWAP = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"
LONDON, FLASHBOTS = 12_965_000, 11_600_000
ADDR = re.compile(r"^0x[0-9a-f]{40}$")

COHORTS = [
    ("cohort_target_strict_miss_v2.csv", "target_strict_miss"),
    ("cohort_control_detected_v2.csv", "control_detected"),
    ("cohort_control_nearmiss_v2.csv", "control_nearmiss"),
]
FORBIDDEN = {"group", "profit_eth", "n_in_mined", "missed", "fully_mined",
             "covered", "profitable", "has_evidence", "failed", "episode_id"}


def log(m):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), m), flush=True)


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def normalize_pools(raw):
    parts = re.split(r"[|;]", raw or "")
    pools, rejected, seen = [], [], set()
    for p in parts:
        p = p.strip().lower()
        if not p:
            continue
        if not ADDR.match(p):
            rejected.append(p)
            continue
        if p in seen:
            continue
        seen.add(p)
        pools.append(p)
    return pools, rejected


def receipt(h):
    p = os.path.join(RCACHE, h[2:4], h + ".json.gz")
    if not os.path.exists(p):
        return None
    try:
        return json.load(gzip.open(p, "rt"))
    except Exception:
        return None


def era_of(b):
    return "pre_flashbots" if b < FLASHBOTS else (
        "flashbots_pre_london" if b < LONDON else "post_london")


def main():
    log("reading cohorts")
    episodes, seen_eid = [], set()
    for fn, group in COHORTS:
        rows = list(csv.DictReader(open(os.path.join(S0, fn))))
        log("  %-38s %d rows" % (fn, len(rows)))
        for r in rows:
            eid = r["episode_id"]
            if eid in seen_eid:
                raise SystemExit("duplicate episode_id: %s" % eid)
            seen_eid.add(eid)
            episodes.append({"src_episode_id": eid, "group": group,
                             "block": int(r["block"]), "front": r["front"].lower(),
                             "victim": r["victim"].lower(), "back": r["back"].lower(),
                             "pools_raw": r.get("pools_all") or ""})
    log("episodes: %d" % len(episodes))

    n_target = sum(1 for e in episodes if e["group"] == "target_strict_miss")
    if n_target != 258:
        raise SystemExit("258 did not reproduce: %d" % n_target)
    log("target_strict_miss: %d" % n_target)

    fixture_hashes = set()
    fp = os.path.join(FIX, "fixtures.json")
    if os.path.exists(fp):
        def harvest(o):
            if isinstance(o, str) and o.startswith("0x") and len(o) == 66:
                fixture_hashes.add(o.lower())
            elif isinstance(o, dict):
                [harvest(v) for v in o.values()]
            elif isinstance(o, list):
                [harvest(v) for v in o]
        harvest(json.load(open(fp)))

    log("building v2 rows with the corrected pool parse")
    out, ineligible, rejected_total = [], [], Counter()
    for e in episodes:
        legs = [e["front"], e["victim"], e["back"]]
        recs = {h: receipt(h) for h in legs}
        if any(recs[h] is None for h in legs):
            ineligible.append({**e, "reason": "receipt_not_cached"})
            continue

        pools, rejected = normalize_pools(e["pools_raw"])
        for r in rejected:
            rejected_total[r] += 1

        topics, gps, n_swaps = set(), [], 0
        for h in legs:
            rc = recs[h]
            gp = rc.get("effectiveGasPrice")
            gps.append(int(gp, 16) if isinstance(gp, str) else None)
            for lg in (rc.get("logs") or []):
                t = (lg.get("topics") or [None])[0]
                if t in (V2_SWAP, V3_SWAP):
                    topics.add(t)
                    n_swaps += 1
        hv2, hv3 = V2_SWAP in topics, V3_SWAP in topics
        amm = ("mixed_v2_v3" if hv2 and hv3 else "v2_only" if hv2
               else "v3_only" if hv3 else "no_uniswap_swap_event")

        out.append({
            "case_id": "case_" + hashlib.sha256("|".join(legs).encode()).hexdigest()[:20],
            "block": e["block"], "front": e["front"], "victim": e["victim"],
            "back": e["back"],
            "n_pools": len(pools),
            "pools_all": ";".join(pools),
            "era": era_of(e["block"]), "amm_design": amm,
            "observable_gas_price_zero": any(g == 0 for g in gps if g is not None),
            "route_complexity_swap_events": n_swaps,
            "_group": e["group"], "_src_episode_id": e["src_episode_id"],
            "_fixture_overlap": any(h in fixture_hashes for h in legs),
        })

    log("eligible %d ; ineligible %d ; rejected pool tokens %d"
        % (len(out), len(ineligible), sum(rejected_total.values())))
    if rejected_total:
        raise SystemExit("pool addresses failed validation: %s"
                         % list(rejected_total)[:5])

    cids = [r["case_id"] for r in out]
    if len(set(cids)) != len(cids):
        raise SystemExit("case_id collision")

    BLIND = ["case_id", "block", "front", "victim", "back", "n_pools", "pools_all",
             "era", "amm_design", "observable_gas_price_zero",
             "route_complexity_swap_events"]
    assert not (set(BLIND) & FORBIDDEN)
    out.sort(key=lambda r: r["case_id"])

    bp = os.path.join(V2_MANI, "cases_blinded.csv")
    with open(bp, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=BLIND)
        w.writeheader()
        for r in out:
            w.writerow({k: r[k] for k in BLIND})
    log("wrote %s (%d rows)" % (bp, len(out)))

    gp_path = os.path.join(V2_GRP, "case_group_map.csv")
    with open(gp_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["case_id", "group"])
        for r in out:
            w.writerow([r["case_id"], r["_group"]])

    ip = os.path.join(V2_MANI, "cases_ineligible.csv")
    with open(ip, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["src_episode_id", "group", "block", "front", "victim", "back", "reason"])
        for e in ineligible:
            w.writerow([e["src_episode_id"], e["group"], e["block"], e["front"],
                        e["victim"], e["back"], e["reason"]])

    log("proving v1/v2 identity on every non-pool field")
    v1 = {r["case_id"]: r for r in csv.DictReader(
        open(os.path.join(V1_MANI, "cases_blinded.csv")))}
    v2 = {r["case_id"]: r for r in csv.DictReader(open(bp))}
    v1g = {r["case_id"]: r["group"] for r in csv.DictReader(
        open(os.path.join(V1_GRP, "case_group_map.csv")))}
    v2g = {r["case_id"]: r["group"] for r in csv.DictReader(open(gp_path))}

    SAME = ["block", "front", "victim", "back", "era", "amm_design",
            "observable_gas_price_zero", "route_complexity_swap_events"]
    diff = {"case_id_sets_equal": set(v1) == set(v2),
            "n_v1": len(v1), "n_v2": len(v2),
            "group_map_equal": v1g == v2g,
            "fields_required_identical": SAME,
            "mismatches": {}}
    for f in SAME:
        bad = [c for c in v2 if v1[c][f] != v2[c][f]]
        diff["mismatches"][f] = len(bad)
    v1_tx = set()
    v2_tx = set()
    for c in v1:
        for k in ("front", "victim", "back"):
            v1_tx.add(v1[c][k])
            v2_tx.add(v2[c][k])
    diff["unique_transaction_hashes_v1"] = len(v1_tx)
    diff["unique_transaction_hashes_v2"] = len(v2_tx)
    diff["transaction_hash_sets_equal"] = v1_tx == v2_tx
    diff["n_pools_changed"] = sum(1 for c in v2 if v1[c]["n_pools"] != v2[c]["n_pools"])
    diff["pools_all_changed"] = sum(1 for c in v2 if v1[c]["pools_all"] != v2[c]["pools_all"])
    diff["only_pool_fields_differ"] = all(v == 0 for v in diff["mismatches"].values())
    json.dump(diff, open(os.path.join(NOTES, "V1_V2_IDENTITY_DIFF.json"), "w"),
              indent=2, sort_keys=True)
    log("identity: case_ids_equal=%s group_equal=%s txhashes_equal=%s only_pool_fields_differ=%s"
        % (diff["case_id_sets_equal"], diff["group_map_equal"],
           diff["transaction_hash_sets_equal"], diff["only_pool_fields_differ"]))
    if not (diff["case_id_sets_equal"] and diff["group_map_equal"]
            and diff["transaction_hash_sets_equal"] and diff["only_pool_fields_differ"]):
        raise SystemExit("identity assertion failed; see V1_V2_IDENTITY_DIFF.json")

    tgt = [r for r in out if r["_group"] == "target_strict_miss"]
    dist = {
        "all_cases": {str(k): v for k, v in sorted(Counter(r["n_pools"] for r in out).items())},
        "target_strict_miss": {str(k): v for k, v in
                               sorted(Counter(r["n_pools"] for r in tgt).items())},
        "by_group": {g: {str(k): v for k, v in sorted(Counter(
            r["n_pools"] for r in out if r["_group"] == g).items())}
            for g in sorted({r["_group"] for r in out})},
        "multi_pool_cases_all": sum(1 for r in out if r["n_pools"] > 1),
        "multi_pool_cases_target": sum(1 for r in tgt if r["n_pools"] > 1),
        "distinct_pool_addresses": len({p for r in out for p in r["pools_all"].split(";") if p}),
    }
    json.dump(dist, open(os.path.join(NOTES, "POOL_COUNT_DISTRIBUTION.json"), "w"),
              indent=2, sort_keys=True)
    log("pool counts all=%s" % dist["all_cases"])
    log("pool counts 258=%s" % dist["target_strict_miss"])

    header = open(bp).readline().strip().split(",")
    body = open(bp).read()
    acc = {
        "task": "R2-02_repair_manifest_v2",
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "counts": {"episodes_read": len(episodes), "target_strict_miss": n_target,
                   "eligible": len(out), "ineligible": len(ineligible),
                   "every_episode_accounted_once":
                       len(out) + len(ineligible) == len(episodes),
                   "eligible_by_group": {k: v for k, v in sorted(
                       Counter(r["_group"] for r in out).items())}},
        "pool_repair": {"source_delimiter": "|",
                        "v1_delimiter_used": ";",
                        "canonical_output_delimiter": ";",
                        "addresses_rejected": sum(rejected_total.values()),
                        "n_pools_rows_changed": diff["n_pools_changed"],
                        "pools_all_rows_changed": diff["pools_all_changed"]},
        "identity_vs_v1": diff,
        "pool_count_distribution": dist,
        "blinding": {"blinded_columns": BLIND,
                     "forbidden_columns_in_blinded_file":
                         sorted(set(header) & FORBIDDEN),
                     "group_label_strings_found": [g for _f, g in COHORTS if g in body],
                     "group_map_is_separate_directory":
                         os.path.dirname(gp_path) != os.path.dirname(bp)},
        "development_fixture_overlap": sum(1 for r in out if r["_fixture_overlap"]),
    }
    ap = os.path.join(V2_MANI, "manifest_accounting.json")
    json.dump(acc, open(ap, "w"), indent=2, sort_keys=True)

    for p in (bp, ip, ap, gp_path):
        log("sha256 %s  %s" % (sha256_file(p), os.path.basename(p)))
    log("done")


if __name__ == "__main__":
    main()
