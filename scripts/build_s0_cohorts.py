import collections, csv, glob, gzip, itertools, json, os, sys
import pandas as pd

R = os.environ.get("MEV_ROOT", ".")
OUT = R + "/revision/out/s0val"
csv.field_size_limit(10 ** 9)
sys.path.insert(0, R + "/revision/scripts")
from catalog import match_sandwich, _economic_actor

os.makedirs(OUT, exist_ok=True)

print("loading exchange set from the deployed heuristic's corpus…", flush=True)
ex = set()
with open(R + "/previous/large/sandwich_results.csv", newline="", errors="replace") as f:
    rd = csv.reader(l.replace("\0", "") for l in f)
    hdr = next(rd); i = hdr.index("exchange_address")
    for row in rd:
        if i < len(row) and str(row[i]).startswith("0x"):
            ex.add(row[i].lower())
print("  %d distinct covered venues" % len(ex), flush=True)

print("loading mined hashes…", flush=True)
mined = set()
with gzip.open(R + "/revision/data/mined_hashes_all.txt.gz", "rt") as fh:
    for l in fh:
        if l.startswith("0x"):
            mined.add(l.strip())
print("  %d mined hashes" % len(mined), flush=True)

print("loading REPLICATION evidence (benign_sweep_rep)…", flush=True)
ev, by_block = {}, collections.defaultdict(list)
for fn in sorted(glob.glob(R + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(fn, "rt") as fh:
        for line in fh:
            r = json.loads(line)
            ev[r["hash"]] = r
            by_block[r["block"]].append(r)
print("  %d transactions across %d blocks" % (len(ev), len(by_block)), flush=True)

d = pd.read_csv(R + "/revision/out/h3_brackets_rep.csv")
print("  %d catalog-matched brackets in h3_brackets_rep.csv" % len(d), flush=True)


def pools_of(row):
    pl = set()
    for h in (row.front, row.victim, row.back):
        e = ev.get(h)
        if e:
            pl |= set(e["pools"])
    return pl


def enrich(df):
    pl = [pools_of(r) for r in df.itertuples()]
    df = df.copy()
    df["pools_all"] = ["|".join(sorted(p)) for p in pl]
    df["pools_covered"] = ["|".join(sorted(p & ex)) for p in pl]
    df["covered"] = [bool(p & ex) for p in pl]
    df["profitable"] = pd.to_numeric(df.profit_eth, errors="coerce") > 0
    df["has_evidence"] = [all(h in ev for h in (r.front, r.victim, r.back))
                          for r in df.itertuples()]
    return df


d = enrich(d)

print("\n=== INCLUSION FLOW (target cohort) ===", flush=True)
flow = [("catalog-matched brackets (offset-14 sweep)", len(d))]
s = d[d.covered];                       flow.append(("+ venue covered by the heuristic", len(s)))
s = s[s.profitable];                    flow.append(("+ realised profit after gas > 0", len(s)))
s = s[s.missed.astype(bool)];           flow.append(("+ no leg in the mined corpus (STRICT MISS)", len(s)))
for lab, n in flow:
    print("  %-52s %6d" % (lab, n), flush=True)
target = s
EXPECTED = 258
print("\n  reproduced strict-miss count : %d   expected : %d   %s"
      % (len(target), EXPECTED, "MATCH" if len(target) == EXPECTED else "*** MISMATCH ***"),
      flush=True)
if len(target) != EXPECTED:
    print("\nSTOP: expected count did not reproduce. Criteria are NOT being adjusted.",
          flush=True)
    print("Reporting the discrepancy and writing no manifest.", flush=True)
    sys.exit(2)

detected = d[d.covered & d.profitable & d.fully_mined.astype(bool)]
print("\n=== CONTROL 1 — detected-positive (all three legs in the mined corpus) ===", flush=True)
print("  %d brackets" % len(detected), flush=True)

print("\n=== CONTROL 2 — near-miss negatives (fail ONLY `reversal`) ===", flush=True)
negrows, tested = [], 0
for blk, txs in by_block.items():
    if len(txs) < 3:
        continue
    txs.sort(key=lambda r: r["index"])
    act = {}
    for r in txs:
        try:
            act[r["hash"]] = _economic_actor(r)
        except Exception:
            act[r["hash"]] = None
    ba = collections.defaultdict(list)
    for r in txs:
        if act[r["hash"]]:
            ba[act[r["hash"]]].append(r)
    for a, legs in ba.items():
        if len(legs) < 2:
            continue
        if len(legs) > 12:
            legs = legs[:12]
        for f, b in itertools.combinations(legs, 2):
            if f["index"] >= b["index"]:
                continue
            fp = set(f["pools"]) & set(b["pools"])
            if not fp:
                continue
            for v in txs:
                if not (f["index"] < v["index"] < b["index"]):
                    continue
                if v["hash"] in (f["hash"], b["hash"]):
                    continue
                if not (fp & set(v["pools"])):
                    continue
                tested += 1
                m = match_sandwich(f, v, b)
                if m.get("matched"):
                    continue
                failed = m.get("failed", [])
                if failed != ["reversal"]:
                    continue
                hs = (f["hash"], v["hash"], b["hash"])
                if any(h in mined for h in hs):
                    continue
                pl = set(f["pools"]) | set(v["pools"]) | set(b["pools"])
                if not (pl & ex):
                    continue
                negrows.append({"block": blk, "front": hs[0], "victim": hs[1],
                                "back": hs[2], "actor": a,
                                "pools_all": "|".join(sorted(pl)),
                                "pools_covered": "|".join(sorted(pl & ex)),
                                "failed": ",".join(failed)})
neg = pd.DataFrame(negrows)
print("  brackets enumerated: %d   near-miss negatives kept: %d" % (tested, len(neg)), flush=True)

cols = ["block", "front", "victim", "back", "actor", "profit_eth",
        "n_in_mined", "missed", "fully_mined", "covered", "profitable",
        "has_evidence", "pools_all", "pools_covered"]
target[cols].to_csv(OUT + "/cohort_target_strict_miss.csv", index=False)
detected[cols].to_csv(OUT + "/cohort_control_detected.csv", index=False)
if len(neg):
    neg.to_csv(OUT + "/cohort_control_nearmiss.csv", index=False)

print("\n=== COHORT DESCRIPTIVES (no S0 outcome computed) ===", flush=True)
for name, df in (("target_strict_miss", target), ("control_detected", detected),
                 ("control_nearmiss", neg)):
    if not len(df):
        continue
    pe = pd.to_numeric(df.profit_eth, errors="coerce") if "profit_eth" in df else None
    top = df.actor.value_counts()
    print("  %-20s n=%-6d blocks=%-6d actors=%-5d  top-actor share %.1f%%%s"
          % (name, len(df), df.block.nunique(), df.actor.nunique(),
             100 * top.iloc[0] / len(df),
             ("  profit median %+.4f ETH" % pe.median()) if pe is not None else ""), flush=True)

print("\n=== BLOCK SEPARATION FROM THE H4 (offset-58) POPULATION ===", flush=True)
h4blocks = set(pd.read_parquet(R + "/revision/data/h4/h4_dev.parquet").block.astype(int))
tb = set(target.block.astype(int))
print("  h4_dev blocks: %d   target blocks: %d   INTERSECTION: %d"
      % (len(h4blocks), len(tb), len(h4blocks & tb)), flush=True)
print("  (holdout NOT read: separation established from the offset manifests, "
      "step 88, offsets 58 vs 14)", flush=True)
print("\nwritten to %s" % OUT, flush=True)
