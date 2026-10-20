import argparse, gzip, json, os, random, sys, threading, time, uuid
from concurrent.futures import ThreadPoolExecutor
import requests

SYNC = "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1"
SWAP = "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
V3   = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"

EPS = ["https://ethereum-rpc.publicnode.com", "https://eth.drpc.org",
       "https://eth.merkle.io", "https://cloudflare-eth.com"]

ROOT  = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
CACHE = ROOT + "/cache/receipts"


def _path(h):
    return "%s/%s/%s.json.gz" % (CACHE, h[2:4], h)


def receipt(h, tries=4):
    p = _path(h)
    if os.path.exists(p):
        try:
            with gzip.open(p, "rt") as f:
                return json.load(f)
        except Exception:
            os.remove(p)
    for i in range(tries):
        try:
            r = requests.post(random.choice(EPS), timeout=30, json={
                "jsonrpc": "2.0", "id": 1,
                "method": "eth_getTransactionReceipt", "params": [h]}).json()
            res = r.get("result")
            if res:
                os.makedirs(os.path.dirname(p), exist_ok=True)
                tmp = "%s.tmp.%d.%s" % (p, threading.get_ident(), uuid.uuid4().hex[:8])
                with gzip.open(tmp, "wt") as f:
                    json.dump(res, f)
                os.replace(tmp, p)
                return res
        except Exception:
            pass
        time.sleep(0.4 * (i + 1))
    return None


def u(data, i):
    return int(data[64 * i:64 * (i + 1)], 16)


def swaps_of(rec):
    if not rec:
        return None, 0
    out, last_sync, n_v3 = [], {}, 0
    for lg in rec.get("logs", []):
        t = lg.get("topics") or []
        if not t:
            continue
        a = lg["address"].lower()
        if t[0] == SYNC:
            d = lg["data"][2:]
            last_sync[a] = (u(d, 0), u(d, 1))
        elif t[0] == V3:
            n_v3 += 1
        elif t[0] == SWAP:
            if a not in last_sync:
                continue
            d = lg["data"][2:]
            a0i, a1i, a0o, a1o = u(d, 0), u(d, 1), u(d, 2), u(d, 3)
            r0p, r1p = last_sync[a]
            r0b, r1b = r0p - a0i + a0o, r1p - a1i + a1o
            out.append({"pool": a, "a0in": a0i, "a1in": a1i, "a0out": a0o, "a1out": a1o,
                        "r0_post": r0p, "r1_post": r1p, "r0_pre": r0b, "r1_pre": r1b})
    return out, n_v3


def cpmm(res_in, res_out, amt_in):
    if res_in <= 0 or res_out <= 0 or amt_in <= 0:
        return None
    n = amt_in * 997 * res_out
    return n // (res_in * 1000 + amt_in * 997)


def direction(s):
    if s["a0in"] > 0 and s["a1out"] > 0:
        return s["a0in"], s["r0_pre"], s["r1_pre"], s["a1out"], 0
    if s["a1in"] > 0 and s["a0out"] > 0:
        return s["a1in"], s["r1_pre"], s["r0_pre"], s["a0out"], 1
    return None


def self_test(s):
    d = direction(s)
    if not d:
        return None
    amt_in, ri, ro, actual, _ = d
    pred = cpmm(ri, ro, amt_in)
    if pred is None or actual <= 0:
        return None
    return abs(pred - actual) / actual


def episode(front, victim, back):
    r = {"tier": "undecidable", "verdict": "undecidable", "reason": "",
         "victim_loss_frac": None, "victim_loss_raw": None,
         "attacker_gross": None, "pool": None, "self_err": None}

    recs = {k: receipt(h) for k, h in (("f", front), ("v", victim), ("b", back))}
    if any(v is None for v in recs.values()):
        r["reason"] = "receipt_fetch_failed"
        return r

    sw, v3 = {}, 0
    for k, rec in recs.items():
        s, n = swaps_of(rec)
        sw[k], v3 = s, v3 + n

    if not sw["v"]:
        r["reason"] = "no_v2_swap_in_victim" + ("_v3_present" if v3 else "")
        return r

    pf = {s["pool"] for s in sw["f"]}
    pb = {s["pool"] for s in sw["b"]}
    pv = {s["pool"] for s in sw["v"]}
    shared = sorted(pf & pb & pv)

    if not shared:
        r.update(tier="exact_cpmm", verdict="no_extraction", reason="no_shared_pool",
                 victim_loss_frac=0.0, victim_loss_raw=0)
        return r
    if len(shared) > 1:
        r["reason"] = "ambiguous_shared_pool_%d" % len(shared)
        return r

    P = shared[0]
    r["pool"] = P
    fs = next(s for s in sw["f"] if s["pool"] == P)
    vs = next(s for s in sw["v"] if s["pool"] == P)
    bs = next(s for s in sw["b"] if s["pool"] == P)

    err = self_test(vs)
    r["self_err"] = err
    if err is None:
        r["reason"] = "victim_swap_undirected"
        return r
    if err > 0.01:
        r.update(reason="self_test_fail_%.4f" % err)
        return r

    d = direction(vs)
    amt_in, _, _, actual, side = d

    ri_cf = fs["r0_pre"] if side == 0 else fs["r1_pre"]
    ro_cf = fs["r1_pre"] if side == 0 else fs["r0_pre"]
    out_cf = cpmm(ri_cf, ro_cf, amt_in)
    if out_cf is None or out_cf <= 0:
        r["reason"] = "counterfactual_degenerate"
        return r

    loss = out_cf - actual
    r["victim_loss_raw"] = loss
    r["victim_loss_frac"] = loss / out_cf

    df, db = direction(fs), direction(bs)
    if df and db:
        spent = df[0]
        got = db[3]
        r["attacker_gross"] = got - spent

    r["tier"] = "exact_cpmm"
    r["verdict"] = ("extraction_confirmed"
                    if loss > 0 and (r["attacker_gross"] or 0) > 0 else "no_extraction")
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=ROOT + "/data/h4/h4_dev.parquet")
    ap.add_argument("--out", default=ROOT + "/out/s0_causal_dev.jsonl")
    ap.add_argument("--n", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()

    import pandas as pd
    d = pd.read_parquet(a.data)
    if a.n:
        d = pd.concat([d[d.y == 1].head(a.n // 4), d[d.y == 0].head(a.n)])
    done = set()
    if os.path.exists(a.out):
        for ln in open(a.out):
            try:
                done.add(json.loads(ln)["transaction_id"])
            except Exception:
                pass
    todo = [r for r in d.itertuples() if r.transaction_id not in done]
    print("episodes: %d total, %d cached, %d to do" % (len(d), len(done), len(todo)),
          flush=True)

    fh = open(a.out, "a")
    t0, n = time.time(), 0

    def work(r):
        res = episode(r.front, r.victim, r.back)
        res["transaction_id"] = r.transaction_id
        res["y"] = int(r.y)
        res["block"] = int(r.block)
        return res

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for res in ex.map(work, todo):
            fh.write(json.dumps(res) + "\n")
            n += 1
            if n % 50 == 0:
                fh.flush()
                el = time.time() - t0
                print("  %4d/%4d  %.1f eps/s  eta %.1f min"
                      % (n, len(todo), n / el, (len(todo) - n) / (n / el) / 60), flush=True)
    fh.close()
    print("done in %.1f min" % ((time.time() - t0) / 60), flush=True)


if __name__ == "__main__":
    main()
