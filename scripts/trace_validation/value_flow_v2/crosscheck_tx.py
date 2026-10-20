import hashlib, json, os, random, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from acquire_tx import BASE, BATCH_FOR, SECONDARY, leg_hashes, post
from evidence import Evidence

RAW = os.path.join(BASE,
                   "revision/data/trace_validation/value_flow_v2/raw/tx_bodies_crosscheck_raw.jsonl")
OUT = os.path.join(BASE, "revision/out/trace_validation/value_flow_v2/provider_agreement.json")
SEED = 20260920
FIELDS = ["hash", "from", "to", "value", "nonce", "blockNumber", "transactionIndex", "input"]


def _lc(x):
    return x.lower() if isinstance(x, str) else x


def _norm(v):
    if isinstance(v, str) and v.startswith("0x") and len(v) <= 34:
        try:
            return int(v, 16)
        except ValueError:
            return _lc(v)
    return _lc(v)


def main(n=600):
    ev = Evidence()
    have = [h for h in leg_hashes() if h in ev.tx]
    rnd = random.Random(SEED)
    sample = sorted(rnd.sample(have, min(n, len(have))))
    bsz = BATCH_FOR.get(SECONDARY, 3)
    os.makedirs(os.path.dirname(RAW), exist_ok=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    checked = agree = 0
    unavailable = 0
    differences = []
    with open(RAW, "a") as fh:
        for i in range(0, len(sample), bsz):
            batch = sample[i:i + bsz]
            calls = [{"jsonrpc": "2.0", "id": j, "method": "eth_getTransactionByHash",
                      "params": [h]} for j, h in enumerate(batch)]
            text = post(SECONDARY, json.dumps(calls))
            rec = {"endpoint": SECONDARY, "requested": batch,
                   "retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                   "response_sha256": hashlib.sha256(text.encode()).hexdigest(), "body": text}
            try:
                parsed = json.loads(text)
                assert isinstance(parsed, list)
            except (ValueError, AssertionError):
                rec["state"] = "failed"
                fh.write(json.dumps(rec, sort_keys=True) + "\n")
                unavailable += len(batch)
                time.sleep(0.5)
                continue
            rec["state"] = "success"
            fh.write(json.dumps(rec, sort_keys=True) + "\n")
            by_id = {e.get("id"): e for e in parsed if isinstance(e, dict)}
            for j, h in enumerate(batch):
                el = by_id.get(j) or {}
                second = el.get("result")
                if not isinstance(second, dict):
                    unavailable += 1
                    continue
                first = ev.tx[h]["body"]
                d = [f for f in FIELDS if _norm(first.get(f)) != _norm(second.get(f))]
                checked += 1
                if d:
                    differences.append({"hash": h, "fields": d})
                else:
                    agree += 1
            time.sleep(0.15)

    summary = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
               "primary": ev.tx[sample[0]]["endpoint"], "secondary": SECONDARY,
               "seed": SEED, "sampled": len(sample), "checked": checked, "agree": agree,
               "second_provider_unavailable": unavailable,
               "fields_compared": FIELDS, "differences": differences,
               "tolerance": "T4 provider agreement, exact"}
    with open(OUT, "w") as fh:
        json.dump(summary, fh, indent=1, sort_keys=True)
    print(json.dumps({k: v for k, v in summary.items() if k != "differences"}, indent=1,
                     sort_keys=True))
    print("differences: %d" % len(differences))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 600)
