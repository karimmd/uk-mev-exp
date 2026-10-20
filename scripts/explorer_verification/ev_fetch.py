import csv, json, os, sys, time
import requests

BS = "https://eth.blockscout.com/api/v2"
ES = "https://api.etherscan.io/v2/api"
KEY = os.environ.get("ETHERSCAN_API_KEY", "")
if not KEY:
    sys.exit("ETHERSCAN_API_KEY not set")

TOPICS = {
    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef": "Transfer",
    "0xe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c": "WETH Deposit",
    "0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65": "WETH Withdrawal",
    "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822": "UniswapV2 Swap",
    "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1": "UniswapV2 Sync",
    "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67": "UniswapV3 Swap",
    "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925": "Approval",
}
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"

S = requests.Session()
S.headers["User-Agent"] = "uk-mev explorer verification"

def get(url, params=None, tries=5):
    for i in range(tries):
        try:
            r = S.get(url, params=params, timeout=30)
            if r.status_code == 200:
                return r.json()
            if r.status_code == 429:
                time.sleep(3 + 3 * i); continue
        except Exception:
            pass
        time.sleep(1 + i)
    return None

def bs_tx(h):
    time.sleep(0.35)
    return get(f"{BS}/transactions/{h}")

def bs_transfers(h):
    items, params = [], None
    while True:
        time.sleep(0.35)
        j = get(f"{BS}/transactions/{h}/token-transfers", params)
        if not j: break
        items += j.get("items", [])
        params = j.get("next_page_params")
        if not params: break
    return items

def es_receipt(h):
    time.sleep(0.25)
    j = get(ES, {"chainid": 1, "module": "proxy", "action": "eth_getTransactionReceipt", "txhash": h, "apikey": KEY})
    return (j or {}).get("result")

def es_internal(h):
    time.sleep(0.25)
    j = get(ES, {"chainid": 1, "module": "account", "action": "txlistinternal", "txhash": h, "apikey": KEY})
    return (j or {}).get("result") if (j or {}).get("status") == "1" else []

def eth(wei):
    return "%.6f" % (int(wei) / 1e18)

def amount(item):
    tot = item.get("total") or {}
    val = tot.get("value"); dec = tot.get("decimals") or (item.get("token") or {}).get("decimals")
    try:
        d = int(dec) if dec not in (None, "") else None
        v = int(val)
        return ("%.6f" % (v / 10 ** d)) if d is not None else f"{v} (raw units)"
    except Exception:
        return f"{val} (raw units)"

def addr(x):
    if isinstance(x, dict): return (x.get("hash") or "").lower()
    return (x or "").lower()

def render_leg(name, h, tx, transfers, receipt, internal, tags):
    L = [f"### {name} leg: `{h}`"]
    if tx:
        gp = tx.get("gas_price"); gu = tx.get("gas_used")
        fee = (tx.get("fee") or {}).get("value")
        L.append("- block %s, position %s, result %s, from `%s`, to `%s`, value %s ETH, gas used %s at %s gwei, fee %s ETH" % (
            tx.get("block_number") or tx.get("block"), tx.get("position"), tx.get("result") or tx.get("status"),
            addr(tx.get("from")), addr(tx.get("to")), eth(tx.get("value") or 0), gu,
            ("%.1f" % (int(gp) / 1e9)) if gp else "?", eth(fee) if fee else "?"))
        for side in ("from", "to"):
            a = tx.get(side) or {}
            for t in (a.get("metadata") or {}).get("tags") or []:
                tags.append({"hash": h, "address": addr(a), "tag": t.get("name")})
            if a.get("name"): tags.append({"hash": h, "address": addr(a), "tag": a.get("name")})
    else:
        L.append("- Blockscout transaction record unavailable")
    L.append("- token transfers (Blockscout, decoded):")
    if transfers:
        for it in transfers:
            tok = it.get("token") or {}
            sym = tok.get("symbol") or "?"
            ta = (tok.get("address") or tok.get("address_hash") or "").lower()
            for side in ("from", "to"):
                a = it.get(side) or {}
                for t in (a.get("metadata") or {}).get("tags") or []:
                    tags.append({"hash": h, "address": addr(a), "tag": t.get("name")})
            L.append("  - %s %s (`%s`): `%s` -> `%s`" % (amount(it), sym, ta[:10], addr(it.get("from")), addr(it.get("to"))))
    else:
        L.append("  - none")
    L.append("- internal ETH transfers (Etherscan):")
    shown = 0
    for it in internal or []:
        if int(it.get("value") or 0) == 0 and it.get("type") != "self-destruct": continue
        L.append("  - %s ETH: `%s` -> `%s` [%s%s]" % (eth(it.get("value") or 0), it.get("from"), it.get("to"), it.get("type"), ", error" if it.get("isError") == "1" else ""))
        shown += 1
    if not shown: L.append("  - none with value")
    L.append("- events in the receipt (Etherscan), by emitting contract:")
    if receipt and receipt.get("logs"):
        for lg in receipt["logs"]:
            t0 = (lg.get("topics") or [""])[0]
            nm = TOPICS.get(t0, "other")
            a = lg["address"].lower()
            extra = ""
            if a == WETH and nm in ("WETH Deposit", "WETH Withdrawal"):
                who = "0x" + lg["topics"][1][-40:]
                extra = " %s ETH for `%s`" % (eth(int(lg["data"], 16)), who)
            L.append("  - `%s` %s%s" % (a, nm, extra))
        L.append("- receipt status %s, index %d" % (int(receipt.get("status", "0x0"), 16), int(receipt.get("transactionIndex", "0x0"), 16)))
    else:
        L.append("  - receipt unavailable")
    return "\n".join(L)

def main():
    cases_csv, out_dir = sys.argv[1], sys.argv[2]
    cards = os.path.join(out_dir, "cards"); raw = os.path.join(out_dir, "raw")
    os.makedirs(cards, exist_ok=True); os.makedirs(raw, exist_ok=True)
    rows = list(csv.DictReader(open(cases_csv)))
    single = rows and "tx" in rows[0] and "front" not in rows[0]
    done = 0
    for r in rows:
        cid = r["case_id"]
        card_path = os.path.join(cards, cid + ".md")
        if os.path.exists(card_path):
            done += 1; continue
        tags = []
        if single:
            legs = [("Transaction", r["tx"])]
            parts = ["# %s" % cid, "", "Block %s. One transaction. Evidence is what two public explorers return for its hash." % r["block"], ""]
        else:
            legs = [("Front", r["front"]), ("Victim", r["victim"]), ("Back", r["back"])]
            parts = ["# %s" % cid, "", "Block %s. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash." % r["block"], ""]
        rawd = {}
        for name, h in legs:
            tx = bs_tx(h); tr = bs_transfers(h); rc = es_receipt(h); it = es_internal(h)
            rawd[name.lower()] = {"hash": h, "blockscout_tx": tx, "blockscout_transfers": tr, "etherscan_receipt": rc, "etherscan_internal": it}
            parts.append(render_leg(name, h, tx, tr, rc, it, tags)); parts.append("")
        os.makedirs(os.path.join(raw, cid), exist_ok=True)
        json.dump(rawd, open(os.path.join(raw, cid, "explorer.json"), "w"))
        json.dump(tags, open(os.path.join(raw, cid, "tags.json"), "w"), indent=1)
        open(card_path, "w").write("\n".join(parts))
        done += 1
        print("%s card %d/%d" % (time.strftime("%H:%M:%S"), done, len(rows)), flush=True)
    print("fetch complete", done, "cards", flush=True)

if __name__ == "__main__":
    main()
