import json, os, sys, threading, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from acquire_tx import BASE, MANIFEST, BATCH_FOR, PRIMARY, SECONDARY, post, write_raw
import hashlib

RAW = os.path.join(BASE, "revision/data/trace_validation/value_flow_v2/raw/block_headers_raw.jsonl")
_lock = threading.Lock()


def manifest_blocks():
    import csv
    seen, order = set(), []
    with open(MANIFEST) as fh:
        for row in csv.DictReader(fh):
            b = int(row["block"])
            if b not in seen:
                seen.add(b)
                order.append(b)
    return order


def already_success(path):
    done = set()
    if not os.path.exists(path):
        return done
    with open(path) as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("state") == "success":
                done |= set(rec.get("resolved") or [])
    return done


def acquire_batch(fh, endpoint, blocks, attempt_budget=5):
    calls = [{"jsonrpc": "2.0", "id": i, "method": "eth_getBlockByNumber",
              "params": [hex(b), False]} for i, b in enumerate(blocks)]
    body = json.dumps(calls)
    for attempt in range(1, attempt_budget + 1):
        text = post(endpoint, body)
        digest = hashlib.sha256(text.encode()).hexdigest()
        stamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        try:
            parsed = json.loads(text)
        except ValueError as e:
            write_raw(fh, {"endpoint": endpoint, "method": "eth_getBlockByNumber",
                           "requested": blocks, "resolved": [], "state": "failed",
                           "attempt": attempt, "retrieved_at": stamp,
                           "response_sha256": digest, "reason": "unparseable: %s" % str(e)[:60],
                           "body": text[:4000]})
            time.sleep(2.0 * attempt)
            continue
        if not isinstance(parsed, list):
            write_raw(fh, {"endpoint": endpoint, "method": "eth_getBlockByNumber",
                           "requested": blocks, "resolved": [], "state": "failed",
                           "attempt": attempt, "retrieved_at": stamp,
                           "response_sha256": digest, "reason": "not a batch list",
                           "body": text[:4000]})
            time.sleep(2.0 * attempt)
            continue
        by_id, errors, resolved = {}, [], []
        for el in parsed:
            if isinstance(el, dict) and "id" in el:
                by_id[el["id"]] = el
        for i, b in enumerate(blocks):
            el = by_id.get(i)
            if el is None or "error" in el or not isinstance(el.get("result"), dict):
                errors.append("%d: %s" % (b, str((el or {}).get("error"))[:80]))
                continue
            res = el["result"]
            if int(res.get("number"), 16) != b or not res.get("miner"):
                errors.append("%d: body reports number %s" % (b, res.get("number")))
                continue
            resolved.append(b)
        state = "success" if (not errors and resolved) else ("partial" if resolved else "failed")
        write_raw(fh, {"endpoint": endpoint, "method": "eth_getBlockByNumber",
                       "requested": blocks, "resolved": resolved, "errors": errors,
                       "state": state, "attempt": attempt, "retrieved_at": stamp,
                       "response_sha256": digest, "response_bytes": len(text),
                       "body": text})
        if state == "success":
            return len(resolved), 0
        if state == "partial":
            missing = [b for b in blocks if b not in set(resolved)]
            if attempt < attempt_budget and missing:
                time.sleep(1.5 * attempt)
                s, f = acquire_batch(fh, endpoint, missing, attempt_budget - attempt)
                return len(resolved) + s, f
            return len(resolved), len(errors)
        time.sleep(2.0 * attempt)
    return 0, len(blocks)


def run(endpoint=PRIMARY, workers=6, limit=None, shard=None, of=None):
    os.makedirs(os.path.dirname(RAW), exist_ok=True)
    want = manifest_blocks()
    done = already_success(RAW)
    todo = [b for b in want if b not in done]
    if of:
        todo = [b for i, b in enumerate(todo) if i % of == shard]
    if limit:
        todo = todo[:limit]
    print("blocks=%d already=%d todo=%d endpoint=%s shard=%s/%s"
          % (len(want), len(done), len(todo), endpoint, shard, of), flush=True)
    if not todo:
        return
    bsz = BATCH_FOR.get(endpoint, 10)
    batches = [todo[i:i + bsz] for i in range(0, len(todo), bsz)]
    counters = {"ok": 0, "fail": 0, "n": 0}
    fh = open(RAW, "a")
    t0 = time.time()

    def worker(queue):
        while True:
            with _lock:
                if not queue:
                    return
                b = queue.pop()
            s, f = acquire_batch(fh, endpoint, b)
            with _lock:
                counters["ok"] += s; counters["fail"] += f; counters["n"] += 1
                if counters["n"] % 20 == 0:
                    print("  %d/%d batches ok=%d fail=%d %.1fs"
                          % (counters["n"], len(batches), counters["ok"], counters["fail"],
                             time.time() - t0), flush=True)

    ts = [threading.Thread(target=worker, args=(batches,)) for _ in range(workers)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    fh.close()
    print("DONE ok=%d fail=%d elapsed=%.1fs"
          % (counters["ok"], counters["fail"], time.time() - t0), flush=True)


if __name__ == "__main__":
    ep, workers, limit, shard, of = PRIMARY, 6, None, None, None
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--secondary":
            ep = SECONDARY
        elif a == "--endpoint":
            ep = args[i + 1]
        elif a == "--workers":
            workers = int(args[i + 1])
        elif a == "--limit":
            limit = int(args[i + 1])
        elif a == "--shard":
            shard = int(args[i + 1])
        elif a == "--of":
            of = int(args[i + 1])
    run(ep, workers, limit, shard, of)
