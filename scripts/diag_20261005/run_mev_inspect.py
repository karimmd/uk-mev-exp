import asyncio, json, os, random, sys, time
REPO = os.path.join(os.environ.get("MEV_ROOT", "."), "revision/external/mev-inspect-py")
sys.path.insert(0, REPO)
from web3 import AsyncHTTPProvider, Web3
from web3.eth import AsyncEth
from mev_inspect.methods import get_block_receipts, trace_block
AsyncEth.trace_block = trace_block
AsyncEth.get_block_receipts = get_block_receipts
from mev_inspect.retry import http_retry_with_backoff_request_middleware
from mev_inspect.block import create_from_block_number
from mev_inspect.classifiers.trace import TraceClassifier
from mev_inspect.swaps import get_swaps
from mev_inspect.arbitrages import get_arbitrages
from mev_inspect.sandwiches import get_sandwiches
from mev_inspect.liquidations import get_liquidations

RPCS = ["https://eth.drpc.org"]
PACE = 0.25
HEADERS = {"User-Agent": "Mozilla/5.0 (research; mev-inspect replication)", "Content-Type": "application/json"}


async def hexify_and_pace_middleware(make_request, web3):
    lock = asyncio.Lock()
    async def mw(method, params):
        if method in ("eth_getBlockReceipts", "trace_block") and params and isinstance(params[0], int):
            params = (hex(params[0]),) + tuple(params[1:])
        async with lock:
            await asyncio.sleep(PACE)
        return await make_request(method, params)
    return mw


def make_w3(rpc):
    p = AsyncHTTPProvider(rpc, request_kwargs={"timeout": 120, "headers": HEADERS})
    p.middlewares += (http_retry_with_backoff_request_middleware, hexify_and_pace_middleware)
    return Web3(p, modules={"eth": (AsyncEth,)}, middlewares=[])


def ser_swap(s):
    return {"hash": s.transaction_hash, "pool": s.contract_address, "from": s.from_address, "to": s.to_address,
            "token_in": s.token_in_address, "amount_in": str(s.token_in_amount), "token_out": s.token_out_address,
            "amount_out": str(s.token_out_amount), "pos": s.transaction_position, "protocol": str(getattr(s, "protocol", ""))}


async def do_block(w3s, tc, b):
    w3 = random.choice(w3s)
    block = await create_from_block_number(w3, b, None)
    ct = tc.classify(block.traces)
    swaps = get_swaps(ct)
    arbs = get_arbitrages(swaps)
    sands = get_sandwiches(swaps)
    try:
        liqs = get_liquidations(ct)
    except Exception as e:
        liqs = []; liq_err = str(e)[:120]
    else:
        liq_err = None
    return {"block": b, "n_traces": len(block.traces), "n_swaps": len(swaps),
            "sandwiches": [{"front": s.frontrun_swap.transaction_hash, "back": s.backrun_swap.transaction_hash,
                            "victims": [v.transaction_hash for v in s.sandwiched_swaps], "pool": s.frontrun_swap.contract_address,
                            "sandwicher": s.sandwicher_address, "profit_token": s.profit_token_address, "profit_amount": str(s.profit_amount)}
                           for s in sands],
            "arbitrages": [{"hash": a.transaction_hash, "account": a.account_address, "profit_token": a.profit_token_address,
                            "profit_amount": str(a.profit_amount), "n_swaps": len(a.swaps), "pools": sorted({x.contract_address for x in a.swaps}),
                            "error": a.error} for a in arbs],
            "liquidations": [{k: (str(getattr(l, k)) if getattr(l, k, None) is not None else None)
                              for k in ("transaction_hash", "protocol", "liquidated_user", "liquidator_user", "debt_token_address", "received_token_address")}
                             for l in liqs],
            "liq_error": liq_err}


async def main(blocklist, out, concurrency):
    blocks = [int(x.strip()) for x in open(blocklist) if x.strip() and not x.startswith("block")]
    done = set()
    if os.path.exists(out):
        for l in open(out):
            try: done.add(json.loads(l)["block"])
            except Exception: pass
    todo = [b for b in blocks if b not in done]
    print("blocks", len(blocks), "done", len(done), "todo", len(todo), flush=True)
    w3s = [make_w3(r) for r in RPCS]; tc = TraceClassifier()
    sem = asyncio.Semaphore(concurrency); fh = open(out, "a"); t0 = time.time(); n = 0; fails = 0

    async def one(b):
        nonlocal n, fails
        async with sem:
            for attempt in range(4):
                try:
                    r = await do_block(w3s, tc, b); break
                except Exception as e:
                    err = "%s: %s" % (type(e).__name__, str(e)[:160]); await asyncio.sleep(2 * (attempt + 1) + random.random())
            else:
                r = {"block": b, "error": err}; fails += 1
            fh.write(json.dumps(r) + "\n"); fh.flush(); n += 1
            if n % 50 == 0:
                print("%d/%d blocks, %.1f s/block, fails %d" % (n, len(todo), (time.time() - t0) / n, fails), flush=True)
    await asyncio.gather(*(one(b) for b in todo))
    print("finished", n, "blocks, fails", fails, "in %.0f s" % (time.time() - t0), flush=True)


if __name__ == "__main__":
    bl, out = sys.argv[1], sys.argv[2]
    conc = int(sys.argv[sys.argv.index("--concurrency") + 1]) if "--concurrency" in sys.argv else 2
    asyncio.run(main(bl, out, conc))
