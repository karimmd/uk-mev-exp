import json, subprocess, time

PRIMARY = "https://eth.drpc.org"
SECONDARY = "https://eth.merkle.io"
ZERO32 = "0x" + "00" * 32
ZERO_ADDR = "0x" + "00" * 20
XFER = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"


class RpcError(Exception):
    pass


class ReconstructionError(Exception):
    pass


def rpc(method, params, endpoint=PRIMARY, timeout=120, attempts=4):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params})
    last = None
    for i in range(attempts):
        t0 = time.time()
        p = subprocess.run(["curl", "-s", "-m", str(timeout), "-X", "POST", endpoint,
                            "-H", "content-type: application/json", "--data-binary", "@-"],
                           input=body, capture_output=True, text=True)
        try:
            d = json.loads(p.stdout)
        except Exception as e:
            last = "unparseable response: %s" % str(e)[:80]
            time.sleep(1.5 * (i + 1)); continue
        if "error" in d:
            last = str(d["error"])[:120]
            time.sleep(1.5 * (i + 1)); continue
        return d["result"], time.time() - t0
    raise RpcError("%s failed after %d attempts: %s" % (method, attempts, last))


def _valid_inner(d):
    return isinstance(d, dict) and isinstance(d.get("pre"), dict) and isinstance(d.get("post"), dict)


def normalize_tier1(raw, n_expected):
    if not isinstance(raw, list):
        raise RpcError("tier1 returned a non-list")
    if len(raw) != n_expected:
        raise RpcError("tier1 cardinality %d != %d" % (len(raw), n_expected))
    out = []
    for i, e in enumerate(raw):
        inner = e.get("result") if isinstance(e, dict) and "result" in e else e
        if not _valid_inner(inner):
            raise RpcError("tier1 entry %d malformed: keys=%s" % (i, list((inner or {}).keys())[:6]))
        out.append(inner)
    return out


def block_diffs(block, endpoint=PRIMARY):
    blk, _ = rpc("eth_getBlockByNumber", [hex(block), False], endpoint=endpoint)
    txs = [t.lower() for t in blk["transactions"]]
    try:
        raw, _ = rpc("debug_traceBlockByNumber",
                     [hex(block), {"tracer": "prestateTracer", "tracerConfig": {"diffMode": True}}],
                     endpoint=endpoint)
        return normalize_tier1(raw, len(txs)), txs, 1
    except RpcError:
        out = []
        for h in txs:
            d, _ = rpc("debug_traceTransaction",
                       [h, {"tracer": "prestateTracer", "tracerConfig": {"diffMode": True}}],
                       endpoint=endpoint)
            if not _valid_inner(d):
                raise RpcError("tier2 entry malformed for %s" % h)
            out.append(d)
        return out, txs, 2


def zeroed_slots(d):
    pre, post = (d or {}).get("pre") or {}, (d or {}).get("post") or {}
    out = {}
    for a, pv in pre.items():
        a = a.lower()
        pres = {k.lower() for k in (pv.get("storage") or {})}
        if not pres:
            continue
        pa = post.get(a) or post.get(a.lower()) or {}
        posts = {k.lower() for k in (pa.get("storage") or {})}
        gone = pres - posts
        if gone:
            out[a] = gone
    return out


def accumulate(diffs):
    ov = {}
    for d in diffs:
        for a, v in ((d or {}).get("post") or {}).items():
            a = a.lower()
            cur = ov.setdefault(a, {})
            for k in ("balance", "nonce", "code"):
                if k in v:
                    cur[k] = v[k]
            if v.get("storage"):
                cur.setdefault("stateDiff", {}).update(
                    {s.lower(): val for s, val in v["storage"].items()})
        for a, slots in zeroed_slots(d).items():
            ov.setdefault(a, {}).setdefault("stateDiff", {}).update({s: ZERO32 for s in slots})
    return ov


def prefix_changes_state(diffs):
    return any(((d or {}).get("post") or {}) for d in diffs)


def assert_overrides_sound(diffs, ov):
    if prefix_changes_state(diffs) and not ov:
        raise ReconstructionError(
            "prefix of %d entries changes state but produced an empty override map" % len(diffs))
    return True


def block_context(blk):
    if not blk.get("timestamp"):
        raise ReconstructionError("block has no timestamp; context cannot be completed")
    bov = {"number": blk["number"], "time": blk["timestamp"]}
    for src, dst in (("baseFeePerGas", "baseFee"), ("gasLimit", "gasLimit"),
                     ("miner", "feeRecipient"), ("difficulty", "difficulty")):
        if blk.get(src):
            bov[dst] = blk[src]
    return bov


def call_from_tx(t):
    c = {"from": t["from"], "gas": t["gas"]}
    for k in ("to", "value", "input", "nonce", "accessList"):
        if t.get(k):
            c[k] = t[k]
    if t.get("maxFeePerGas") or t.get("maxPriorityFeePerGas"):
        for k in ("maxFeePerGas", "maxPriorityFeePerGas"):
            if t.get(k):
                c[k] = t[k]
    elif t.get("gasPrice"):
        c["gasPrice"] = t["gasPrice"]
    return c


def flat_logs(node, out=None):
    out = [] if out is None else out
    for l in (node.get("logs") or []):
        out.append((( l.get("address") or "").lower(), tuple(l.get("topics") or []), l.get("data") or ""))
    for c in (node.get("calls") or []):
        flat_logs(c, out)
    return out


def receipt_logs(rc):
    return [((l["address"] or "").lower(), tuple(l["topics"]), l.get("data") or "")
            for l in (rc.get("logs") or [])]


def token_deltas(logs, actor):
    a = (actor or "").lower()
    pos = {}
    for addr, topics, data in logs:
        if not topics or topics[0] != XFER or len(topics) < 3:
            continue
        frm = "0x" + topics[1][-40:]
        to = "0x" + topics[2][-40:]
        try:
            amt = int(data[:66], 16) if data and data != "0x" else 0
        except ValueError:
            continue
        if frm.lower() == a:
            pos[addr] = pos.get(addr, 0) - amt
        if to.lower() == a:
            pos[addr] = pos.get(addr, 0) + amt
    return {k: v for k, v in pos.items() if v != 0}


def storage_keys(state):
    return {(a.lower(), s.lower())
            for a, v in (state or {}).items() for s in (v.get("storage") or {})}


def account_keys(state):
    return {a.lower() for a in (state or {})}


def contaminated_contract_balances(diff, fee_recipient=None, code_accounts=None):
    fr = (fee_recipient or "").lower()
    out = set()
    post, pre = (diff or {}).get("post") or {}, (diff or {}).get("pre") or {}
    for a, v in post.items():
        a = a.lower()
        if a == fr or "balance" not in v:
            continue
        if (pre.get(a) or {}).get("balance") == v.get("balance"):
            continue
        has_code = bool((v.get("code") or (pre.get(a) or {}).get("code")))
        if code_accounts is not None:
            has_code = has_code or a in code_accounts
        if has_code:
            out.add(a)
    return out


def merge_post(slots, accounts, diff):
    post = (diff or {}).get("post") or {}
    slots |= storage_keys(post)
    accounts |= account_keys(post)
    for a, gone in zeroed_slots(diff).items():
        slots |= {(a, s) for s in gone}
    return slots, accounts


def accessed_state(txhash, endpoint=PRIMARY):
    d, _ = rpc("debug_traceTransaction", [txhash, {"tracer": "prestateTracer"}], endpoint=endpoint)
    return d or {}


def intersects(accessed, slots, accounts):
    a_slots = storage_keys(accessed)
    return bool(a_slots & slots) or bool(account_keys(accessed) & accounts)


def balance_uncertain(accessed, contaminated):
    return bool(account_keys(accessed) & set(contaminated))


def apply_diff(ov, d):
    for a, v in ((d or {}).get("post") or {}).items():
        a = a.lower()
        cur = ov.setdefault(a, {})
        for k in ("balance", "nonce", "code"):
            if k in v:
                cur[k] = v[k]
        if v.get("storage"):
            cur.setdefault("stateDiff", {}).update({s.lower(): x for s, x in v["storage"].items()})
    for a, slots in zeroed_slots(d).items():
        ov.setdefault(a, {}).setdefault("stateDiff", {}).update({s: ZERO32 for s in slots})
    return ov


def transfer_multiset(logs):
    out = []
    for addr, topics, data in logs:
        if not topics or topics[0] != XFER or len(topics) < 3:
            continue
        try:
            amt = int(data[:66], 16) if data and data != "0x" else 0
        except ValueError:
            amt = None
        out.append((addr, "0x" + topics[1][-40:].lower(), "0x" + topics[2][-40:].lower(), amt))
    return sorted(out)


WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
V2_SWAP_TOPIC = "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
V3_SWAP_TOPIC = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"


def swap_pools(logs):
    return {a for a, t, _ in logs if t and t[0] in (V2_SWAP_TOPIC, V3_SWAP_TOPIC)}


def economic_actor(logs, pools=None):
    pools = {p.lower() for p in (pools or set())}
    if not pools:
        return None
    tokens = {a for a, _, _ in logs}
    excluded = tokens | {ZERO_ADDR} | pools
    cands = {}
    for addr, topics, data in logs:
        if not topics or topics[0] != XFER or len(topics) < 3:
            continue
        try:
            amt = int(data[:66], 16) if data and data != "0x" else 0
        except ValueError:
            continue
        frm, to = "0x" + topics[1][-40:].lower(), "0x" + topics[2][-40:].lower()
        if frm not in pools and to not in pools:
            continue
        for who, sign in ((frm, -1), (to, 1)):
            if who in excluded:
                continue
            cands.setdefault(who, {})
            cands[who][addr] = cands[who].get(addr, 0) + sign * amt
    def key(who):
        pos = {k: v for k, v in cands[who].items() if v != 0}
        non_weth = [k for k in pos if k != WETH]
        return (len(non_weth), len(pos), abs(pos.get(WETH, 0)))
    ranked = sorted(cands, key=key, reverse=True)
    if not ranked or key(ranked[0]) == (0, 0, 0):
        return None
    if len(ranked) > 1 and key(ranked[0]) == key(ranked[1]):
        return None
    return ranked[0]


def victim_output(logs, pools=None):
    a = economic_actor(logs, pools)
    if a is None:
        return None, None
    pl = {p.lower() for p in (pools or set())}
    pos = {}
    for addr, topics, data in logs:
        if not topics or topics[0] != XFER or len(topics) < 3:
            continue
        try:
            amt = int(data[:66], 16) if data and data != "0x" else 0
        except ValueError:
            continue
        frm, to = "0x" + topics[1][-40:].lower(), "0x" + topics[2][-40:].lower()
        if frm not in pl and to not in pl:
            continue
        if frm == a:
            pos[addr] = pos.get(addr, 0) - amt
        if to == a:
            pos[addr] = pos.get(addr, 0) + amt
    return a, {k: v for k, v in pos.items() if v != 0}


def _u256(word):
    return int(word, 16)


def _i256(word):
    v = int(word, 16)
    return v - (1 << 256) if v >= (1 << 255) else v


def _words(data):
    h = (data or "0x")[2:]
    return ["0x" + h[i:i + 64] for i in range(0, len(h) - len(h) % 64, 64)]


def decode_swap_vector(logs, pools):
    pl = {p.lower() for p in (pools or set())}
    if not pl:
        return None, "no_shared_pool"
    seq = []
    for idx, (addr, topics, data) in enumerate(logs):
        if addr not in pl or not topics:
            continue
        t0 = topics[0]
        if t0 == V2_SWAP_TOPIC:
            w = _words(data)
            if len(w) < 4:
                return None, "malformed_v2_swap_data"
            seq.append({"pool": addr, "order": idx, "venue": "v2",
                        "amounts": [_u256(w[0]), _u256(w[1]), _u256(w[2]), _u256(w[3])]})
        elif t0 == V3_SWAP_TOPIC:
            w = _words(data)
            if len(w) < 2:
                return None, "malformed_v3_swap_data"
            seq.append({"pool": addr, "order": idx, "venue": "v3",
                        "amounts": [_i256(w[0]), _i256(w[1])]})
    if not seq:
        return None, "no_swap_event_on_shared_pool"
    seq.sort(key=lambda e: (e["pool"], e["order"]))
    return seq, None


def vectors_comparable(a, b):
    if a is None or b is None or len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x["pool"] != y["pool"] or x["venue"] != y["venue"]:
            return False
        if len(x["amounts"]) != len(y["amounts"]):
            return False
    return True


def vector_changes(a, b):
    out = []
    for x, y in zip(a, b):
        d = [yy - xx for xx, yy in zip(x["amounts"], y["amounts"])]
        if any(d):
            out.append({"pool": x["pool"], "venue": x["venue"], "order": x["order"],
                        "actual": [str(v) for v in x["amounts"]],
                        "counterfactual": [str(v) for v in y["amounts"]],
                        "delta": [str(v) for v in d]})
    return out


def swap_pools_of(logs):
    return {a for a, t, _ in logs if t and t[0] in (V2_SWAP_TOPIC, V3_SWAP_TOPIC)}
