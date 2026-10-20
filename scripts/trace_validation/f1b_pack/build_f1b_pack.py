import csv, glob, gzip, hashlib, json, os, random, subprocess, sys, time
ROOT = os.environ.get("MEV_ROOT", ".")
REV = ROOT + "/revision"
sys.path.insert(0, REV + "/scripts")
sys.path.insert(0, REV + "/scripts/trace_validation/value_flow_v2")
from catalog import _economic_actor
import flow2 as F
from evidence import Evidence

SEED = 20261005
N = {"target_strict_miss": 100, "control_detected": 50, "control_nearmiss": 50}
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
SYNC = "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1"
V2SWAP = "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822"
V3SWAP = "0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67"
PACK = REV + "/out/f1b/pack"
SEALED = REV + "/data/f1b/sealed"
os.makedirs(PACK + "/episodes", exist_ok=True)
os.makedirs(SEALED, exist_ok=True)

man = {r["case_id"]: r for r in csv.DictReader(open(REV + "/data/trace_validation/manifests/v2/cases_blinded.csv"))}
gmap = {r["case_id"]: r["group"] for r in csv.DictReader(open(REV + "/data/trace_validation/group_map/v2/case_group_map.csv"))}
rnd = random.Random(SEED)
chosen = []
for arm, k in N.items():
    ids = sorted(c for c, g in gmap.items() if g == arm)
    chosen += [(c, arm) for c in rnd.sample(ids, k)]
rnd.shuffle(chosen)
pack_ids = ["pack_%03d" % (i + 1) for i in range(len(chosen))]

with open(SEALED + "/mapping.csv", "w") as fh:
    w = csv.writer(fh); w.writerow(["pack_id", "case_id", "arm"])
    for pid, (cid, arm) in zip(pack_ids, chosen):
        w.writerow([pid, cid, arm])
mh = hashlib.sha256(open(SEALED + "/mapping.csv", "rb").read()).hexdigest()
stamp = subprocess.run(["date", "-Is"], capture_output=True, text=True).stdout.strip()
open(PACK + "/MAPPING_SHA256.txt", "w").write("sha256 %s sealed mapping.csv\nsealed_at %s (date -Is on the server)\nseed %d\n" % (mh, stamp, SEED))

want = set()
for cid, _ in chosen:
    m = man[cid]; want |= {m["front"].lower(), m["victim"].lower(), m["back"].lower()}
store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            r = json.loads(line)
            if r["hash"].lower() in want: store[r["hash"].lower()] = r
ev = Evidence()

TOK = REV + "/data/f1b/token_meta.json"
meta = json.load(open(TOK)) if os.path.exists(TOK) else {}
def rpc_call(to, data):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "eth_call", "params": [{"to": to, "data": data}, "latest"]})
    for url in ("https://eth.drpc.org", "https://ethereum-rpc.publicnode.com", "https://cloudflare-eth.com"):
        try:
            out = subprocess.run(["curl", "-s", "-m", "10", "-H", "Content-Type: application/json", "-H", "User-Agent: Mozilla/5.0", "-d", body, url], capture_output=True, text=True, timeout=15).stdout
            res = json.loads(out).get("result")
            if res and res != "0x": return res
        except Exception:
            pass
    return None
def tokmeta(addr):
    if addr in meta: return meta[addr]
    sym, dec = None, None
    r = rpc_call(addr, "0x95d89b41")
    if r and len(r) >= 130:
        try:
            n = int(r[2 + 64:2 + 128], 16); sym = bytes.fromhex(r[2 + 128:2 + 128 + 2 * n]).decode("utf-8", "replace")
        except Exception: sym = None
    elif r and len(r) == 66:
        try: sym = bytes.fromhex(r[2:]).rstrip(b"\x00").decode("utf-8", "replace")
        except Exception: sym = None
    r = rpc_call(addr, "0x313ce567")
    if r:
        try: dec = int(r, 16)
        except Exception: dec = None
    meta[addr] = {"symbol": sym, "decimals": dec}
    return meta[addr]

def fmt(addr, amt):
    m = tokmeta(addr); d = m.get("decimals"); s = m.get("symbol") or addr[:10]
    if d is not None:
        return "%s %s" % (("%.6f" % (int(amt) / 10 ** d)).rstrip("0").rstrip("."), s)
    return "%s raw %s" % (int(amt), s)

def decode_updates(rc):
    out = []
    for lg in rc.get("logs") or []:
        t = lg.get("topics") or []
        if not t: continue
        a = (lg.get("address") or "").lower(); d = lg.get("data") or "0x"
        if t[0] == SYNC and len(d) >= 130:
            out.append("pool %s Sync reserve0=%d reserve1=%d" % (a, int(d[2:66], 16), int(d[66:130], 16)))
        elif t[0] == V3SWAP and len(d) >= 2 + 64 * 5:
            sq = int(d[2 + 64 * 2:2 + 64 * 3], 16); tick = int(d[2 + 64 * 4:2 + 64 * 5], 16)
            if tick >= 2 ** 255: tick -= 2 ** 256
            out.append("pool %s V3 Swap sqrtPriceX96=%d tick=%d" % (a, sq, tick))
    return out

def leg_block(name, h, rc, pools_shared):
    r = store.get(h.lower())
    lines = ["### %s leg: `%s`" % (name, h)]
    if not r: return lines + ["(evidence record missing)"]
    actor = _economic_actor(r)
    lines.append("- block index %s, status %s, sender `%s`, target `%s`, gas used %s at %s gwei" % (
        r["index"], r["status"], r["from"], r.get("to"), r["gas_used"], round(int(r["gas_price"]) / 1e9, 2)))
    lines.append("- economic actor by the published rule: `%s`" % actor)
    lines.append("- pools touched: " + ", ".join("`%s`%s" % (p, " (shared)" if p in pools_shared else "") for p in r["pools"]))
    lines.append("- ERC-20 transfers:")
    for tok, frm, to, amt in r["transfers"]:
        tag = []
        if frm == actor: tag.append("from actor")
        if to == actor: tag.append("to actor")
        lines.append("  - %s: `%s` -> `%s`%s" % (fmt(tok, amt), frm[:10], to[:10], (" [" + ", ".join(tag) + "]") if tag else ""))
    if rc:
        conv = F.weth_conversion_deltas(rc)
        for a, wad in conv.items():
            lines.append("  - WETH %s %s by `%s`" % ("deposit" if wad > 0 else "withdrawal", fmt(WETH, abs(wad)), a[:10]))
        ups = decode_updates(rc)
        if ups:
            lines.append("- reserve/price updates:")
            lines += ["  - " + u for u in ups]
    d = {}
    for tok, frm, to, amt in r["transfers"]:
        if frm == actor: d[tok] = d.get(tok, 0) - int(amt)
        if to == actor: d[tok] = d.get(tok, 0) + int(amt)
    if rc:
        for a, wad in F.weth_conversion_deltas(rc).items():
            if a == actor: d[WETH] = d.get(WETH, 0) + wad
    lines.append("- actor net position this leg: " + (", ".join("%s%s" % ("+" if v > 0 else "", fmt(t, abs(v)) if v >= 0 else "-" + fmt(t, abs(v))) for t, v in d.items()) or "none"))
    return lines

sheet = []
for pid, (cid, arm) in zip(pack_ids, chosen):
    m = man[cid]
    pools = {p.strip().lower() for p in m["pools_all"].split(";") if p.strip()}
    rf, _ = ev.receipt(m["front"]); rv, _ = ev.receipt(m["victim"]); rb, _ = ev.receipt(m["back"])
    doc = ["# %s" % pid, "", "Block %s. Three transactions in block order: front, victim, back. Evidence is decoded on-chain data only." % m["block"], ""]
    doc += leg_block("Front", m["front"], rf, pools) + [""]
    doc += leg_block("Victim", m["victim"], rv, pools) + [""]
    doc += leg_block("Back", m["back"], rb, pools) + [""]
    fr = store.get(m["front"].lower()); br = store.get(m["back"].lower())
    if fr and br:
        gas = (fr["gas_used"] * int(fr["gas_price"]) + br["gas_used"] * int(br["gas_price"])) / 1e18
        doc.append("Observable gas cost of front plus back: %.6f ETH. Direct payments to the block producer, if any, are not shown here." % gas)
    doc += ["", "## Score", "Q1 Is this a sandwich bracket (same actor opens a non-WETH position in the front leg and closes it in the back leg on a pool the victim trades, victim in between)? yes / no / cannot tell",
            "Q2 Is the actor's position positive after observable cost (ETH plus WETH net across both legs minus gas, with any residual token holdings noted)? yes / no / cannot tell", "Note:"]
    open(PACK + "/episodes/%s.md" % pid, "w").write("\n".join(doc) + "\n")
    sheet.append(pid)
json.dump(meta, open(TOK, "w"), indent=0)
with open(PACK + "/scoring_sheet.csv", "w") as fh:
    w = csv.writer(fh); w.writerow(["pack_id", "scorer", "Q1_sandwich", "Q2_positive_after_cost", "confidence_1to5", "note"])
    for pid in sheet: w.writerow([pid, "", "", "", "", ""])
readme = """# F1b blinded adjudication pack (built %s, seed %d)

200 sandwich episodes drawn at random from three arms of the study, shuffled. The arm of each episode is
sealed in a mapping whose SHA-256 is in MAPPING_SHA256.txt; the mapping itself is not in this folder and
must not be opened until both scorers have returned their sheets.

Each file in episodes/ shows decoded on-chain evidence for one bracket: the three transactions in block
order with sender, target, status, gas, every ERC-20 transfer and WETH wrap/unwrap, pool reserve updates
(Uniswap V2 Sync) and V3 swap prices, and the economic actor chosen by the published rule (the address
with the most non-zero net token positions, non-WETH first; pools and token contracts excluded). Token
symbols and decimals come from the token contracts themselves; where lookup failed, raw units are shown.
Nothing from any MEV record and nothing from the study's own adjudication is included.

## Rubric, decoded evidence only
Q1 Is this a sandwich bracket? Answer yes if, in the same block, one economic actor opens a position in a
   non-WETH token in the front leg and closes it in the back leg on a pool the victim also trades, with the
   victim between them. Answer no if any of these fails. Answer cannot tell if the evidence shown does not
   settle it.
Q2 Is the actor's position positive after observable cost? Net the actor's ETH and WETH across front and
   back (treat ETH and WETH as one asset), subtract the gas shown, and note any residual non-WETH holding.
   Answer yes if positive, no if not, cannot tell if a residual holding or a missing figure prevents a sign.
Confidence 1 (guess) to 5 (certain). Use the note for anything that influenced you.

Scorers work independently and do not discuss episodes until both sheets are returned.
""" % (stamp, SEED)
open(PACK + "/README.md", "w").write(readme)
print("built", len(sheet), "episodes; sealed mapping sha256", mh, "at", stamp, "; tokens looked up", len(meta))
