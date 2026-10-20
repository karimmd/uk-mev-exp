V2_SWAP = "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
V2_SYNC = "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1"
V3_SWAP = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"
Q96 = 1 << 96


def _words(data):
    h = data[2:] if data.startswith("0x") else data
    return [int(h[i:i + 64], 16) for i in range(0, len(h) - len(h) % 64, 64)]


def _signed(u, bits=256):
    return u - (1 << bits) if u >= (1 << (bits - 1)) else u


def decode_v2_swap(log):
    w = _words(log["data"])
    if len(w) < 4:
        return None
    return {"kind": "v2_swap", "pool": log["address"].lower(),
            "amount0In": w[0], "amount1In": w[1],
            "amount0Out": w[2], "amount1Out": w[3],
            "delta0": w[0] - w[2], "delta1": w[1] - w[3]}


def decode_v2_sync(log):
    w = _words(log["data"])
    if len(w) < 2:
        return None
    return {"kind": "v2_sync", "pool": log["address"].lower(),
            "reserve0": w[0], "reserve1": w[1]}


def decode_v3_swap(log):
    w = _words(log["data"])
    if len(w) < 5:
        return None
    return {"kind": "v3_swap", "pool": log["address"].lower(),
            "delta0": _signed(w[0]), "delta1": _signed(w[1]),
            "sqrtPriceX96": w[2], "liquidity": w[3],
            "tick": _signed(w[4], 24) if len(w) > 4 else None}


def decode_pool_events(receipt, pool):
    out = []
    for lg in (receipt.get("logs") or []):
        if (lg.get("address") or "").lower() != pool:
            continue
        t = (lg.get("topics") or [None])[0]
        d = None
        if t == V2_SWAP:
            d = decode_v2_swap(lg)
        elif t == V2_SYNC:
            d = decode_v2_sync(lg)
        elif t == V3_SWAP:
            d = decode_v3_swap(lg)
        if d:
            out.append(d)
    return out


def price_v2(reserve0, reserve1):
    if reserve0 <= 0 or reserve1 <= 0:
        return None
    return reserve1 / reserve0


def price_v3(sqrtPriceX96):
    if not sqrtPriceX96:
        return None
    r = sqrtPriceX96 / Q96
    return r * r


def v2_reserves_before(sync, swaps):
    r0, r1 = sync["reserve0"], sync["reserve1"]
    for s in reversed(swaps):
        r0 -= s["delta0"]
        r1 -= s["delta1"]
    if r0 <= 0 or r1 <= 0:
        return None
    return r0, r1


def net_direction(events):
    d0 = d1 = 0
    seen = False
    for e in events:
        if e["kind"] in ("v2_swap", "v3_swap"):
            d0 += e["delta0"]
            d1 += e["delta1"]
            seen = True
    return (d0, d1) if seen else None
