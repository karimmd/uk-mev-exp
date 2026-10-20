import hashlib, json, os

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
ES_RAW = os.path.join(BASE, "revision/data/trace_validation/etherscan/v1/raw/etherscan_raw.jsonl")
V2 = os.path.join(BASE, "revision/data/trace_validation/value_flow_v2")
TX_RAW = os.path.join(V2, "raw/tx_bodies_raw.jsonl")
BLK_RAW = os.path.join(V2, "raw/block_headers_raw.jsonl")
OFFSETS = os.path.join(V2, "index/etherscan_offsets.json")

RECEIPT = "proxy/eth_getTransactionReceipt"
INTERNAL = "account/txlistinternal"


def _stamp(path):
    st = os.stat(path)
    return {"size": st.st_size, "mtime_ns": st.st_mtime_ns}


def build_offsets(force=False):
    if not force and os.path.exists(OFFSETS):
        try:
            d = json.load(open(OFFSETS))
            if d.get("source_stamp") == _stamp(ES_RAW):
                return d
        except (ValueError, OSError):
            pass
    receipts, internal = {}, {}
    with open(ES_RAW, "rb") as fh:
        off = 0
        for raw in fh:
            n = len(raw)
            try:
                rec = json.loads(raw)
            except ValueError:
                off += n
                continue
            ep, state = rec.get("endpoint"), rec.get("state")
            h = (rec.get("params") or {}).get("txhash")
            if h and state in ("success", "empty"):
                if ep == RECEIPT:
                    receipts[h.lower()] = [off, n, state]
                elif ep == INTERNAL:
                    internal[h.lower()] = [off, n, state]
            off += n
    d = {"source_stamp": _stamp(ES_RAW), "receipts": receipts, "internal": internal}
    os.makedirs(os.path.dirname(OFFSETS), exist_ok=True)
    tmp = OFFSETS + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(d, fh)
    os.replace(tmp, OFFSETS)
    return d


class Evidence:

    def __init__(self):
        self.off = build_offsets()
        self._fh = open(ES_RAW, "rb")
        self.tx = self._load_tx_bodies()
        self.blocks = self._load_blocks()

    def record(self, table, h):
        ent = self.off[table].get(h.lower())
        if not ent:
            return None
        off, n, _ = ent
        self._fh.seek(off)
        return json.loads(self._fh.read(n))

    def _read(self, table, h):
        ent = self.off[table].get(h.lower())
        if not ent:
            return None, "missing"
        off, n, state = ent
        self._fh.seek(off)
        rec = json.loads(self._fh.read(n))
        try:
            payload = json.loads(rec["body"])
        except (ValueError, KeyError):
            return None, "failed"
        return payload, state

    def receipt(self, h):
        payload, state = self._read("receipts", h)
        if payload is None:
            return None, state
        r = payload.get("result")
        if not isinstance(r, dict):
            return None, "failed"
        return r, "success"

    def internal(self, h):
        payload, state = self._read("internal", h)
        if payload is None:
            return None, state
        rows = payload.get("result")
        if state == "empty" or rows in (None, "", []):
            return [], "empty"
        if not isinstance(rows, list):
            return None, "failed"
        return rows, "success"

    def _load_tx_bodies(self):
        out = {}
        if not os.path.exists(TX_RAW):
            return out
        with open(TX_RAW) as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if rec.get("state") not in ("success", "partial"):
                    continue
                resolved = set(rec.get("resolved") or [])
                if not resolved:
                    continue
                try:
                    parsed = json.loads(rec["body"])
                except (ValueError, KeyError):
                    continue
                if not isinstance(parsed, list):
                    continue
                for el in parsed:
                    if not isinstance(el, dict):
                        continue
                    res = el.get("result")
                    if not isinstance(res, dict):
                        continue
                    h = (res.get("hash") or "").lower()
                    if h in resolved:
                        out[h] = {"body": res, "response_sha256": rec.get("response_sha256"),
                                  "endpoint": rec.get("endpoint"),
                                  "retrieved_at": rec.get("retrieved_at")}
        return out

    def _load_blocks(self):
        out = {}
        if not os.path.exists(BLK_RAW):
            return out
        with open(BLK_RAW) as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if rec.get("state") not in ("success", "partial"):
                    continue
                try:
                    parsed = json.loads(rec["body"])
                except (ValueError, KeyError):
                    continue
                for el in (parsed if isinstance(parsed, list) else [parsed]):
                    res = (el or {}).get("result")
                    if not isinstance(res, dict) or not res.get("miner"):
                        continue
                    try:
                        out[int(res["number"], 16)] = res["miner"].lower()
                    except (TypeError, ValueError):
                        continue
        return out

    def body(self, h):
        e = self.tx.get(h.lower())
        if not e:
            return None, "missing"
        return e["body"], "success"

    def body_meta(self, h):
        return self.tx.get(h.lower())

    def beneficiary(self, block):
        return self.blocks.get(int(block))

    def leg(self, h):
        rc, rc_state = self.receipt(h)
        rows, in_state = self.internal(h)
        tx, tx_state = self.body(h)
        return {"receipt": rc, "receipt_state": rc_state,
                "internal": rows, "internal_state": in_state,
                "tx": tx, "tx_state": tx_state}


def sha256_file(path):
    d = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            d.update(chunk)
    return d.hexdigest()
