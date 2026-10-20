import json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from state2 import rpc, RpcError
import witness2 as W

ROOT = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
EXCL = os.path.join(ROOT, "data/trace_validation/01_feasibility/manifest_hashes_excluded.txt")
OUT = os.path.join(ROOT, "out/trace_validation/counterfactual/v2")
V2_SWAP = "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
V3_SWAP = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"
excluded = {l.strip().lower() for l in open(EXCL)} if os.path.exists(EXCL) else set()

KNOWN = [
    {"block": 12027856, "opening_index": 3,  "victim_index": 183},
    {"block": 11597573, "opening_index": 13, "victim_index": 101},
    {"block": 10652463, "opening_index": 43, "victim_index": 124},
    {"block": 10381484, "opening_index": 2,  "victim_index": 75},
]

mode = sys.argv[1] if len(sys.argv) > 1 else "positive"
N = int(sys.argv[2]) if len(sys.argv) > 2 else 4


def same_pool_pairs(rnd, want):
    found, tried = [], 0
    while len(found) < want and tried < 80:
        tried += 1
        b = rnd.randrange(10_000_000, 14_400_000)
        try:
            rcs, _ = rpc("eth_getBlockReceipts", [hex(b)])
        except RpcError:
            continue
        if not isinstance(rcs, list) or len(rcs) < 8:
            continue
        if any((r.get("transactionHash") or "").lower() in excluded for r in rcs):
            continue
        pools = {}
        for r in rcs:
            idx = int(r["transactionIndex"], 16)
            for lg in (r.get("logs") or []):
                t = (lg.get("topics") or [None])[0]
                if t in (V2_SWAP, V3_SWAP):
                    pools.setdefault((lg["address"] or "").lower(), set()).add(idx)
        for pool, idxs in pools.items():
            if len(idxs) >= 2:
                s = sorted(idxs)
                found.append({"block": b, "opening_index": s[0], "victim_index": s[1], "pool": pool})
                break
    return found


def random_pairs(rnd, want):
    found, tried = [], 0
    while len(found) < want and tried < 80:
        tried += 1
        b = rnd.randrange(10_000_000, 14_400_000)
        try:
            rcs, _ = rpc("eth_getBlockReceipts", [hex(b)])
        except RpcError:
            continue
        if not isinstance(rcs, list) or len(rcs) < 12:
            continue
        if any((r.get("transactionHash") or "").lower() in excluded for r in rcs):
            continue
        i, j = sorted(rnd.sample(range(len(rcs)), 2))
        if j - i > 6 or j == i:
            continue
        found.append({"block": b, "opening_index": i, "victim_index": j})
    return found


rnd = random.Random(20260920)
cases = KNOWN[:N] if mode == "positive" else random_pairs(rnd, N)
if mode == "positive" and N > len(KNOWN):
    cases = KNOWN + same_pool_pairs(rnd, N - len(KNOWN))

res = []
for c in cases:
    t0 = time.time()
    try:
        r = W.evaluate(dict(c))
    except Exception as e:
        r = {"state": "ERROR", "reason": str(e)[:200], "metrics": {}}
    r["case"] = c
    r["seconds"] = round(time.time() - t0, 2)
    res.append(r)
    m = r.get("metrics", {})
    print(f"blk {c['block']} oi={c['opening_index']} vi={c['victim_index']} "
          f"-> {r['state']:22s} {r['reason'][:46]:46s} "
          f"gasΔ={m.get('gas_delta')} reprod={m.get('actual_reproduces_gas')} "
          f"tokΔ={m.get('token_output_differs')} reex={m.get('intervening_reexecuted')} "
          f"{r['seconds']}s", flush=True)

summary = {
    "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"), "mode": mode, "n": len(res),
    "actual_reproduced": sum(1 for r in res if r["metrics"].get("actual_reproduces_gas")
                             and r["metrics"].get("actual_reproduces_token_output")),
    "positive": sum(1 for r in res if r["state"] == "positive"),
    "negative": sum(1 for r in res if r["state"] == "negative"),
    "undecidable": sum(1 for r in res if r["state"] == "undecidable"),
    "technical_unavailable": sum(1 for r in res if r["state"] == "technical_unavailable"),
    "results": res,
}
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "control_%s.json" % mode), "w") as f:
    json.dump(summary, f, indent=1, sort_keys=True)
print(json.dumps({k: v for k, v in summary.items() if k != "results"}, indent=1))
