import hashlib, json, os, subprocess, sys, threading, time

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
MANIFEST = os.path.join(BASE, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
OUT = os.path.join(BASE, "revision/data/trace_validation/value_flow_v2")
RAW = os.path.join(OUT, "raw/tx_bodies_raw.jsonl")

PRIMARY = "https://cloudflare-eth.com"
SECONDARY = "https://eth.drpc.org"
BATCH_FOR = {"https://cloudflare-eth.com": 10, "https://eth.drpc.org": 3,
             "https://rpc.mevblocker.io": 10, "https://eth-pokt.nodies.app": 10,
             "https://eth.merkle.io": 1}
BATCH = 10

_lock = threading.Lock()


def leg_hashes():
    import csv
    seen, order = set(), []
    with open(MANIFEST) as fh:
        for row in csv.DictReader(fh):
            for col in ("front", "back"):
                h = row[col].lower()
                if h not in seen:
                    seen.add(h)
                    order.append(h)
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
            if rec.get("state") != "success":
                continue
            for h in rec.get("resolved") or []:
                done.add(h)
    return done


def post(endpoint, body, timeout=120):
    p = subprocess.run(["curl", "-s", "-m", str(timeout), "-X", "POST", endpoint,
                        "-H", "content-type: application/json", "--data-binary", "@-"],
                       input=body, capture_output=True, text=True)
    return p.stdout


def write_raw(fh, rec):
    with _lock:
        fh.write(json.dumps(rec, sort_keys=True) + "\n")
        fh.flush()


def acquire_batch(fh, endpoint, hashes, attempt_budget=5):
    calls = [{"jsonrpc": "2.0", "id": i, "method": "eth_getTransactionByHash",
              "params": [h]} for i, h in enumerate(hashes)]
    body = json.dumps(calls)
    last = None
    for attempt in range(1, attempt_budget + 1):
        text = post(endpoint, body)
        digest = hashlib.sha256(text.encode()).hexdigest()
        stamp = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        try:
            parsed = json.loads(text)
        except ValueError as e:
            last = "unparseable: %s" % str(e)[:60]
            write_raw(fh, {"endpoint": endpoint, "method": "eth_getTransactionByHash",
                           "requested": hashes, "resolved": [], "state": "failed",
                           "attempt": attempt, "retrieved_at": stamp,
                           "response_sha256": digest, "reason": last,
                           "body": text[:4000]})
            time.sleep(2.0 * attempt)
            continue
        if not isinstance(parsed, list):
            last = "batch response was not a list: %s" % str(parsed)[:120]
            write_raw(fh, {"endpoint": endpoint, "method": "eth_getTransactionByHash",
                           "requested": hashes, "resolved": [], "state": "failed",
                           "attempt": attempt, "retrieved_at": stamp,
                           "response_sha256": digest, "reason": last, "body": text[:4000]})
            time.sleep(2.0 * attempt)
            continue

        by_id, errors, empties, resolved = {}, [], [], []
        for el in parsed:
            if not isinstance(el, dict) or "id" not in el:
                errors.append("element without id")
                continue
            by_id[el["id"]] = el
        for i, h in enumerate(hashes):
            el = by_id.get(i)
            if el is None:
                errors.append("%s: no element for id %d" % (h, i))
            elif "error" in el:
                errors.append("%s: %s" % (h, str(el["error"])[:80]))
            elif el.get("result") is None:
                empties.append(h)
            elif (el["result"].get("hash") or "").lower() != h:
                errors.append("%s: body reports hash %s" % (h, el["result"].get("hash")))
            else:
                resolved.append(h)

        state = "success" if (not errors and resolved and not empties) else (
            "partial" if resolved else "failed")
        write_raw(fh, {"endpoint": endpoint, "method": "eth_getTransactionByHash",
                       "requested": hashes, "resolved": resolved, "empty": empties,
                       "errors": errors, "state": state, "attempt": attempt,
                       "retrieved_at": stamp, "response_sha256": digest, "body": text})
        if state == "success":
            return len(resolved), 0, 0
        if state == "partial":
            missing = [h for h in hashes if h not in set(resolved)]
            if attempt < attempt_budget and missing:
                time.sleep(1.5 * attempt)
                s, e, f = acquire_batch(fh, endpoint, missing, attempt_budget - attempt)
                return len(resolved) + s, e, f
            return len(resolved), len(empties), len(errors)
        last = "; ".join(errors[:3]) or "empty batch"
        time.sleep(2.0 * attempt)
    return 0, 0, len(hashes)


def run(endpoint, workers, limit=None, only=None, shard=None, of=None):
    os.makedirs(os.path.dirname(RAW), exist_ok=True)
    want = only if only is not None else leg_hashes()
    done = already_success(RAW)
    todo = [h for h in want if h not in done]
    if of:
        todo = [h for h in todo if int(h[-4:], 16) % of == shard]
    if limit:
        todo = todo[:limit]
    print("legs=%d already=%d todo=%d endpoint=%s workers=%d shard=%s/%s"
          % (len(want), len(done), len(todo), endpoint, workers, shard, of), flush=True)
    if not todo:
        return
    bsz = BATCH_FOR.get(endpoint, BATCH)
    batches = [todo[i:i + bsz] for i in range(0, len(todo), bsz)]
    counters = {"ok": 0, "empty": 0, "fail": 0, "batches": 0}
    fh = open(RAW, "a")
    t0 = time.time()

    def worker(queue):
        while True:
            with _lock:
                if not queue:
                    return
                b = queue.pop()
            s, e, f = acquire_batch(fh, endpoint, b)
            with _lock:
                counters["ok"] += s; counters["empty"] += e; counters["fail"] += f
                counters["batches"] += 1
                if counters["batches"] % 10 == 0:
                    print("  %d/%d batches  ok=%d empty=%d fail=%d  %.1fs"
                          % (counters["batches"], len(batches), counters["ok"],
                             counters["empty"], counters["fail"], time.time() - t0), flush=True)

    ts = [threading.Thread(target=worker, args=(batches,)) for _ in range(workers)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    fh.close()
    print("DONE ok=%d empty=%d fail=%d elapsed=%.1fs"
          % (counters["ok"], counters["empty"], counters["fail"], time.time() - t0), flush=True)


if __name__ == "__main__":
    ep = PRIMARY
    workers, limit, shard, of = 4, None, None, None
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--secondary":
            ep = SECONDARY
        elif a == "--workers":
            workers = int(args[i + 1])
        elif a == "--limit":
            limit = int(args[i + 1])
        elif a == "--endpoint":
            ep = args[i + 1]
        elif a == "--shard":
            shard = int(args[i + 1])
        elif a == "--of":
            of = int(args[i + 1])
    run(ep, workers, limit, None, shard, of)
