import json, os, random, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
BASE = os.path.abspath(os.path.join(HERE, "../../../.."))
EXCL = os.path.join(BASE, "revision/data/trace_validation/01_feasibility/manifest_hashes_excluded.txt")
MANIFEST = os.path.join(BASE, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
TOKEN = os.path.join(BASE, ".etherscan_token")
OUT = os.path.join(BASE, "revision/out/trace_validation/value_flow_v2/native_ledger_control.json")
RPC = "https://eth.drpc.org"
ES = "https://api.etherscan.io/v2/api"
DEPOSIT = "0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c"
WITHDRAWAL = "0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65"


def rpc(method, params, timeout=180, attempts=4):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params})
    last = None
    for i in range(attempts):
        p = subprocess.run(["curl", "-s", "-m", str(timeout), "-X", "POST", RPC,
                            "-H", "content-type: application/json", "--data-binary", "@-"],
                           input=body, capture_output=True, text=True)
        try:
            d = json.loads(p.stdout)
        except ValueError:
            last = "unparseable"
            time.sleep(1.5 * (i + 1)); continue
        if "error" in d:
            last = str(d["error"])[:120]
            time.sleep(1.5 * (i + 1)); continue
        return d["result"]
    raise RuntimeError("%s failed: %s" % (method, last))


def etherscan_internal(txhash):
    with open(TOKEN) as fh:
        key = fh.read().strip()
    url = ("%s?chainid=1&module=account&action=txlistinternal&txhash=%s&apikey=%s"
           % (ES, txhash, key))
    p = subprocess.run(["curl", "-s", "-m", "60", url], capture_output=True, text=True)
    try:
        d = json.loads(p.stdout)
    except ValueError:
        return None, "failed"
    res = d.get("result")
    if d.get("status") == "1" and isinstance(res, list):
        return res, "success"
    if isinstance(res, list) and not res:
        return [], "empty"
    if isinstance(res, str) and "No transactions found" in res:
        return [], "empty"
    return None, "failed"


def _int(x, default=None):
    try:
        return int(x, 16) if isinstance(x, str) else (x if x is not None else default)
    except (TypeError, ValueError):
        return default


def predicted_deltas(tx, receipt, internal_rows):
    d = {}

    def add(a, v):
        if a:
            d[a.lower()] = d.get(a.lower(), 0) + v

    for r in internal_rows or []:
        if str(r.get("isError", "0")) not in ("0", "False", "false"):
            continue
        try:
            v = int(r.get("value") or 0)
        except (TypeError, ValueError):
            continue
        if v <= 0:
            continue
        to = (r.get("to") or "").lower()
        if not to and (r.get("type") or "").lower() in ("create", "create2"):
            to = (r.get("contractAddress") or "").lower()
        add(r.get("from"), -v)
        add(to, v)
    v = _int(tx.get("value"), 0) or 0
    if v:
        add(tx.get("from"), -v)
        add(tx.get("to") or receipt.get("contractAddress"), v)
    gas = (_int(receipt.get("gasUsed"), 0) or 0) * (_int(receipt.get("effectiveGasPrice"), 0) or 0)
    add(tx.get("from"), -gas)
    return d


def actual_deltas(trace):
    pre, post = trace.get("pre") or {}, trace.get("post") or {}
    out = {}
    for a in set(pre) | set(post):
        pb, qb = (pre.get(a) or {}).get("balance"), (post.get(a) or {}).get("balance")
        if pb is None and qb is None:
            continue
        if qb is None:
            continue
        out[a.lower()] = _int(qb, 0) - _int(pb, 0)
    return out


def main(n=20, seed=20260920):
    excluded = {l.strip().lower() for l in open(EXCL)} if os.path.exists(EXCL) else set()
    import csv
    for row in csv.DictReader(open(MANIFEST)):
        for c in ("front", "victim", "back"):
            excluded.add(row[c].lower())
    rnd = random.Random(seed)
    plain_seen = [0]
    results, tried = [], 0
    while len(results) < n and tried < 400:
        tried += 1
        blk = rnd.randrange(10_000_000, 14_400_000)
        try:
            rcs = rpc("eth_getBlockReceipts", [hex(blk)])
        except RuntimeError:
            continue
        if not isinstance(rcs, list) or len(rcs) < 5:
            continue
        blkinfo = rpc("eth_getBlockByNumber", [hex(blk), False])
        fee_recipient = (blkinfo.get("miner") or "").lower()
        cands = [r for r in rcs
                 if (r.get("transactionHash") or "").lower() not in excluded
                 and r.get("status") == "0x1" and (r.get("logs") or [])]
        if not cands:
            continue
        def interest(r):
            tops = {(lg.get("topics") or [None])[0] for lg in (r.get("logs") or [])}
            return ((DEPOSIT in tops or WITHDRAWAL in tops), len(r.get("logs") or []))
        cands.sort(key=interest, reverse=True)
        rc, rows, state, h = None, None, None, None
        for cand in cands[:4]:
            hh = cand["transactionHash"]
            rr, st = etherscan_internal(hh)
            time.sleep(0.25)
            if st == "failed":
                continue
            if rr or (plain_seen[0] >= 2 and st == "empty"):
                rc, rows, state, h = cand, rr, st, hh
                break
            if st == "empty" and plain_seen[0] < 2:
                rc, rows, state, h = cand, rr, st, hh
                plain_seen[0] += 1
                break
        if rc is None:
            continue
        try:
            tx = rpc("eth_getTransactionByHash", [h])
            tr = rpc("debug_traceTransaction",
                     [h, {"tracer": "prestateTracer",
                          "tracerConfig": {"diffMode": True}}])
        except RuntimeError:
            continue
        if not isinstance(tr, dict) or "pre" not in tr:
            continue
        pred, act = predicted_deltas(tx, rc, rows), actual_deltas(tr)
        addrs = (set(pred) | set(act)) - {fee_recipient}
        mismatches = []
        for a in sorted(addrs):
            p, q = pred.get(a, 0), act.get(a, 0)
            if p != q:
                mismatches.append({"address": a, "predicted": str(p), "actual": str(q),
                                   "difference": str(q - p)})
        results.append({"block": blk, "tx": h, "internal_state": state,
                        "internal_rows": len(rows or []),
                        "top_level_value": tx.get("value"),
                        "addresses_compared": len(addrs),
                        "mismatches": mismatches})
        print("%d %s rows=%d addrs=%d mismatch=%d"
              % (blk, h[:12], len(rows or []), len(addrs), len(mismatches)), flush=True)
        time.sleep(0.3)

    total = sum(r["addresses_compared"] for r in results)
    bad = sum(len(r["mismatches"]) for r in results)
    summary = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
               "seed": seed, "transactions": len(results),
               "addresses_compared": total, "exact_matches": total - bad,
               "mismatched_addresses": bad,
               "excluded_from_comparison": "block fee recipient; balance unchanged in diffMode",
               "tolerance": "exact integer wei, zero slack",
               "cases": results}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(summary, fh, indent=1, sort_keys=True)
    print(json.dumps({k: v for k, v in summary.items() if k != "cases"}, indent=1, sort_keys=True))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20)
