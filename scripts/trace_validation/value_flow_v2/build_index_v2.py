import collections, json, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evidence import Evidence, BASE, TX_RAW, BLK_RAW, sha256_file

MANIFEST = os.path.join(BASE, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
OUTDIR = os.path.join(BASE, "revision/data/trace_validation/value_flow_v2/index")
INDEX = os.path.join(OUTDIR, "transaction_body_index.jsonl")
SUMMARY = os.path.join(OUTDIR, "index_summary.json")

COMPARED = ["hash", "blockNumber", "transactionIndex", "from", "to"]


def _lc(x):
    return x.lower() if isinstance(x, str) else x


def _hexint(x):
    try:
        return int(x, 16) if isinstance(x, str) else x
    except (TypeError, ValueError):
        return None


def agreement(tx, receipt):
    diffs = []
    if _lc(tx.get("hash")) != _lc(receipt.get("transactionHash")):
        diffs.append("hash")
    for k in ("blockNumber", "transactionIndex"):
        if _hexint(tx.get(k)) != _hexint(receipt.get(k)):
            diffs.append(k)
    if _lc(tx.get("from")) != _lc(receipt.get("from")):
        diffs.append("from")
    rt, tt = _lc(receipt.get("to")), _lc(tx.get("to"))
    if rt is not None and tt is not None and rt != tt:
        diffs.append("to")
    return diffs


def main():
    import csv
    ev = Evidence()
    rows = list(csv.DictReader(open(MANIFEST)))
    os.makedirs(OUTDIR, exist_ok=True)
    tally = collections.Counter()
    mirrored = 0
    top_level_nonzero = 0
    out = open(INDEX + ".tmp", "w")
    for row in rows:
        block = int(row["block"])
        ben = ev.beneficiary(block)
        tally["beneficiary_resolved" if ben else "beneficiary_missing"] += 1
        for role, col in (("opening", "front"), ("closing", "back")):
            h = row[col].lower()
            rc_rec = ev.record("receipts", h)
            in_rec = ev.record("internal", h)
            rc, rc_state = ev.receipt(h)
            rows_int, in_state = ev.internal(h)
            tx, tx_state = ev.body(h)
            meta = ev.body_meta(h) or {}
            tally["tx_" + tx_state] += 1
            tally["receipt_" + rc_state] += 1
            tally["internal_" + in_state] += 1

            agree, diffs = None, []
            if tx and rc:
                diffs = agreement(tx, rc)
                agree = "agree" if not diffs else "disagree"
                tally["body_receipt_" + agree] += 1
                v = _hexint(tx.get("value")) or 0
                if v > 0:
                    top_level_nonzero += 1
                    frm, to = _lc(tx.get("from")), _lc(tx.get("to"))
                    for r in (rows_int or []):
                        try:
                            rv = int(r.get("value") or 0)
                        except (TypeError, ValueError):
                            continue
                        if rv == v and _lc(r.get("from")) == frm and _lc(r.get("to")) == to:
                            mirrored += 1
                            break
            out.write(json.dumps({
                "case_id": row["case_id"], "transaction_hash": h, "role": role,
                "block": block,
                "transaction": {"state": tx_state,
                                "endpoint": meta.get("endpoint"),
                                "response_sha256": meta.get("response_sha256"),
                                "retrieved_at": meta.get("retrieved_at"),
                                "reason": None if tx_state == "success"
                                else "no successful eth_getTransactionByHash response stored"},
                "receipt": {"state": rc_state,
                            "response_sha256": (rc_rec or {}).get("response_sha256")},
                "internal_transfers": {"state": in_state,
                                       "response_sha256": (in_rec or {}).get("response_sha256")},
                "body_receipt_agreement": {"state": agree, "fields_compared": COMPARED,
                                           "differences": diffs},
                "block_fee_recipient": {"state": "success" if ben else "missing",
                                        "address": ben},
            }, sort_keys=True) + "\n")
            tally["rows"] += 1
    out.close()
    os.replace(INDEX + ".tmp", INDEX)

    summary = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "cases": len(rows),
        "expected_rows": 2 * len(rows),
        "rows": tally["rows"],
        "tally": dict(tally),
        "top_level_value_nonzero_legs": top_level_nonzero,
        "top_level_mirrored_by_internal_record": mirrored,
        "raw": {
            "tx_bodies_raw.jsonl": sha256_file(TX_RAW) if os.path.exists(TX_RAW) else None,
            "block_headers_raw.jsonl": sha256_file(BLK_RAW) if os.path.exists(BLK_RAW) else None,
        },
        "index_sha256": sha256_file(INDEX),
    }
    with open(SUMMARY, "w") as fh:
        json.dump(summary, fh, indent=1, sort_keys=True)
    print(json.dumps(summary, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
