import csv, hashlib, json, os, re, sys

ROOT = os.environ.get("MEV_ROOT", ".")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
csv.field_size_limit(10 ** 9)
from build_manifest_v2 import normalize_pools

V1 = os.path.join(ROOT, "revision/data/trace_validation/manifests/v1/cases_blinded.csv")
V2 = os.path.join(ROOT, "revision/data/trace_validation/manifests/v2/cases_blinded.csv")
G1 = os.path.join(ROOT, "revision/data/trace_validation/group_map/v1/case_group_map.csv")
G2 = os.path.join(ROOT, "revision/data/trace_validation/group_map/v2/case_group_map.csv")
RAW = os.path.join(ROOT, "revision/data/trace_validation/etherscan/v1/raw/etherscan_raw.jsonl")

A = "0x" + "a" * 40
B = "0x" + "b" * 40
FAILS = []


def check(name, cond, detail=""):
    print(("  PASS  " if cond else "  FAIL  ") + name + ("  " + str(detail) if detail and not cond else ""))
    if not cond:
        FAILS.append(name)


print("\n1. normalizer fixtures")
check("pipe-delimited pair parses to two pools", normalize_pools(A + "|" + B)[0] == [A, B])
check("semicolon-delimited pair also parses", normalize_pools(A + ";" + B)[0] == [A, B])
check("single address parses to one", normalize_pools(A)[0] == [A])
check("empty string yields no pools", normalize_pools("")[0] == [])
check("mixed case is lowercased", normalize_pools(A.upper().replace("0X", "0x"))[0] == [A])
check("duplicates collapse", normalize_pools(A + "|" + A)[0] == [A])
check("empty segments dropped", normalize_pools(A + "||" + B + "|")[0] == [A, B])
check("order is first-seen", normalize_pools(B + "|" + A)[0] == [B, A])
pools, rej = normalize_pools(A + "|0xdeadbeef|" + B)
check("short address is rejected, not silently kept", pools == [A, B] and rej == ["0xdeadbeef"], (pools, rej))
pools, rej = normalize_pools("notanaddress")
check("non-address rejected", pools == [] and rej == ["notanaddress"], (pools, rej))

print("\n2. the v1 defect is real and reproduced")
v1 = {r["case_id"]: r for r in csv.DictReader(open(V1))}
v2 = {r["case_id"]: r for r in csv.DictReader(open(V2))}
check("v1 froze n_pools at 1 for every case",
      {r["n_pools"] for r in v1.values()} == {"1"})
check("v1 pools_all still holds the raw pipe data (no information lost)",
      sum(1 for r in v1.values() if "|" in r["pools_all"]) == 5755)
check("v2 no longer has a constant pool count", len({r["n_pools"] for r in v2.values()}) > 1)

print("\n3. v1/v2 identity")
check("same case_id set", set(v1) == set(v2))
check("17,637 cases", len(v2) == 17637)
for f in ("block", "front", "victim", "back", "era", "amm_design",
          "observable_gas_price_zero", "route_complexity_swap_events"):
    check("field identical: %s" % f, all(v1[c][f] == v2[c][f] for c in v2))
tx1 = {v1[c][k] for c in v1 for k in ("front", "victim", "back")}
tx2 = {v2[c][k] for c in v2 for k in ("front", "victim", "back")}
check("39,448 unique transaction hashes, unchanged", tx1 == tx2 and len(tx2) == 39448, len(tx2))
g1 = {r["case_id"]: r["group"] for r in csv.DictReader(open(G1))}
g2 = {r["case_id"]: r["group"] for r in csv.DictReader(open(G2))}
check("group mapping unchanged", g1 == g2)
check("258 targets in v2", sum(1 for v in g2.values() if v == "target_strict_miss") == 258)

print("\n4. v2 pool fields are well formed")
ADDR = re.compile(r"^0x[0-9a-f]{40}$")
bad = [c for c in v2 if any(not ADDR.match(p) for p in v2[c]["pools_all"].split(";") if p)]
check("every pool address validates", not bad, bad[:3])
mismatch = [c for c in v2 if int(v2[c]["n_pools"]) !=
            len([p for p in v2[c]["pools_all"].split(";") if p])]
check("n_pools equals the parsed list length", not mismatch, mismatch[:3])
check("no pipe survives in v2", not any("|" in v2[c]["pools_all"] for c in v2))
check("multi-pool cases present", sum(1 for c in v2 if int(v2[c]["n_pools"]) > 1) == 5755,
      sum(1 for c in v2 if int(v2[c]["n_pools"]) > 1))

print("\n5. blinding preserved in v2")
hdr = open(V2).readline().strip().split(",")
forb = {"group", "profit_eth", "n_in_mined", "missed", "fully_mined", "covered",
        "profitable", "has_evidence", "failed", "episode_id"}
check("no forbidden column", not (set(hdr) & forb), sorted(set(hdr) & forb))
body = open(V2).read()
check("no group label string in the blinded file",
      not any(g in body for g in ("target_strict_miss", "control_detected", "control_nearmiss")))

print("\n6. the Etherscan raw cache is untouched by this repair")
check("raw cache exists", os.path.exists(RAW))
n = sum(1 for _ in open(RAW))
check("raw cache is non-empty and append-only", n > 0, n)
keys = set()
with open(RAW) as fh:
    for line in fh:
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get("endpoint") == "account/txlistinternal":
            keys.add((r.get("params") or {}).get("txhash", "").lower())
check("every cached internal-transfer key is a v2 manifest transaction",
      keys <= tx2, len(keys - tx2))

print("\n%s" % ("ALL TESTS PASSED" if not FAILS else "FAILURES: %s" % FAILS))
sys.exit(1 if FAILS else 0)
