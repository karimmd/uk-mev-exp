import csv, json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from state2 import (rpc, RpcError, block_diffs, merge_post, accessed_state, intersects,
                    contaminated_contract_balances, balance_uncertain)

ROOT = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
MAN = os.path.join(ROOT, "data/trace_validation/manifests/v2/cases_blinded.csv")
OUT = os.path.join(ROOT, "out/trace_validation/counterfactual/v2")
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30
FORBIDDEN = {"group", "arm", "label", "is_sandwich", "treatment", "outcome"}

rows = list(csv.DictReader(open(MAN)))
assert not (FORBIDDEN & set(rows[0].keys())), "manifest carries a label column; refusing to read"
rnd = random.Random(20260920)
sample = rnd.sample(rows, min(N, len(rows)))

res = []
for i, r in enumerate(sample):
    b = int(r["block"]); front = r["front"].lower(); victim = r["victim"].lower()
    rec = {"case_id": r["case_id"], "block": b, "era": r.get("era"),
           "amm_design": r.get("amm_design"), "n_pools": r.get("n_pools")}
    t0 = time.time()
    try:
        diffs, txs, tier = block_diffs(b)
        if front not in txs or victim not in txs:
            rec["skip"] = "hash_not_in_block"; res.append(rec); continue
        oi, vi = txs.index(front), txs.index(victim)
        rec.update({"opening_index": oi, "victim_index": vi, "diff_tier": tier,
                    "adjacent": vi == oi + 1, "intervening": max(0, vi - oi - 1)})
        blk, _ = rpc("eth_getBlockByNumber", [hex(b), False])
        slots, accts = merge_post(set(), set(), diffs[oi])
        blkf, _ = rpc("eth_getBlockByNumber", [hex(b), True])
        fee = (blkf.get("miner") or "").lower()
        cbal = contaminated_contract_balances(diffs[oi], fee)
        rec["opening_tainted_slots"] = len(slots)
        rec["opening_tainted_contract_balances"] = len(cbal)
        tainted = reexec = 0; uncertain = False
        for k in range(oi + 1, vi):
            try:
                acc = accessed_state(txs[k])
            except RpcError:
                rec["read_set_failures"] = rec.get("read_set_failures", 0) + 1; continue
            if balance_uncertain(acc, cbal):
                uncertain = True; break
            if intersects(acc, slots, accts):
                tainted += 1; reexec += 1
                slots, accts = merge_post(slots, accts, diffs[k])
        rec.update({"tainted_intervening": tainted, "would_reexecute": reexec,
                    "balance_uncertain": uncertain})
    except Exception as e:
        rec["error"] = str(e)[:160]
    rec["seconds"] = round(time.time() - t0, 2)
    res.append(rec); print(json.dumps(rec), flush=True)

ok = [r for r in res if "intervening" in r and "error" not in r]
adj = [r for r in ok if r["adjacent"]]
nonadj = [r for r in ok if not r["adjacent"]]
summ = {
    "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"), "sampled": len(sample), "usable": len(ok),
    "adjacent": len(adj), "non_adjacent": len(nonadj),
    "mean_intervening": round(sum(r["intervening"] for r in ok) / max(1, len(ok)), 2),
    "mean_intervening_nonadjacent": round(sum(r["intervening"] for r in nonadj) / max(1, len(nonadj)), 2),
    "total_intervening": sum(r["intervening"] for r in ok),
    "total_tainted": sum(r.get("tainted_intervening", 0) for r in ok),
    "taint_rate": round(sum(r.get("tainted_intervening", 0) for r in ok)
                        / max(1, sum(r["intervening"] for r in ok)), 4),
    "balance_uncertain_cases": sum(1 for r in ok if r.get("balance_uncertain")),
    "mean_seconds_per_case": round(sum(r["seconds"] for r in ok) / max(1, len(ok)), 1),
    "cases": res,
}
os.makedirs(OUT, exist_ok=True)
json.dump(summ, open(os.path.join(OUT, "manifest_rates.json"), "w"), indent=1, sort_keys=True)
print(json.dumps({k: v for k, v in summ.items() if k != "cases"}, indent=1))
