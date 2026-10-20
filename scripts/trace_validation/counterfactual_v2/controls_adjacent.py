import json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from state2 import rpc, RpcError
import witness2 as W

ROOT = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
EXCL = os.path.join(ROOT, "data/trace_validation/01_feasibility/manifest_hashes_excluded.txt")
OUT = os.path.join(ROOT, "out/trace_validation/counterfactual/v2")
V2_SWAP = "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
V3_SWAP = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"
excluded = {l.strip().lower() for l in open(EXCL)} if os.path.exists(EXCL) else set()

mode = sys.argv[1] if len(sys.argv) > 1 else "positive_adjacent"
N = int(sys.argv[2]) if len(sys.argv) > 2 else 6
rnd = random.Random(int(sys.argv[3]) if len(sys.argv) > 3 else 20260920)

def scan(want, adjacent_same_pool):
    found, tried = [], 0
    while len(found) < want and tried < 600:
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
        if adjacent_same_pool:
            pools = {}
            for r in rcs:
                idx = int(r["transactionIndex"], 16)
                if r.get("status") != "0x1":
                    continue
                for lg in (r.get("logs") or []):
                    t = (lg.get("topics") or [None])[0]
                    if t in (V2_SWAP, V3_SWAP):
                        pools.setdefault((lg["address"] or "").lower(), set()).add(idx)
            for pool, idxs in pools.items():
                s = sorted(idxs)
                for a, c in zip(s, s[1:]):
                    if c == a + 1:
                        found.append({"block": b, "opening_index": a, "victim_index": c,
                                      "pool": pool})
                        break
                else:
                    continue
                break
        else:
            ok = [int(r["transactionIndex"], 16) for r in rcs if r.get("status") == "0x1"]
            if len(ok) < 2:
                continue
            i = rnd.choice(ok[:-1])
            if i + 1 in ok:
                found.append({"block": b, "opening_index": i, "victim_index": i + 1})
    return found

cases = scan(N, mode == "positive_adjacent")
print(f"found {len(cases)} {mode} cases", flush=True)
res = []
for c in cases:
    t0 = time.time()
    try:
        r = W.evaluate({k: c[k] for k in ("block", "opening_index", "victim_index")})
    except Exception as e:
        r = {"state": "ERROR", "reason": str(e)[:200], "metrics": {}}
    r["case"] = c; r["seconds"] = round(time.time() - t0, 2)
    res.append(r); m = r.get("metrics", {})
    print(f"blk {c['block']} oi={c['opening_index']} vi={c['victim_index']} pool={c.get('pool','-')[:10]} "
          f"-> {r['state']:22s} {r['reason'][:44]:44s} gasD={m.get('gas_delta')} "
          f"reprod={m.get('actual_reproduces_gas')} tokD={m.get('token_output_differs')} "
          f"{r['seconds']}s", flush=True)

summ = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"), "mode": mode, "n": len(res),
        "actual_reproduced": sum(1 for r in res if r["metrics"].get("actual_reproduces_gas")
                                 and r["metrics"].get("actual_reproduces_token_output")),
        "positive": sum(1 for r in res if r["state"] == "positive"),
        "negative": sum(1 for r in res if r["state"] == "negative"),
        "undecidable": sum(1 for r in res if r["state"] == "undecidable"),
        "technical_unavailable": sum(1 for r in res if r["state"] == "technical_unavailable"),
        "results": res}
os.makedirs(OUT, exist_ok=True)
json.dump(summ, open(os.path.join(OUT, "control_%s.json" % mode), "w"), indent=1, sort_keys=True)
print(json.dumps({k: v for k, v in summ.items() if k != "results"}, indent=1))
