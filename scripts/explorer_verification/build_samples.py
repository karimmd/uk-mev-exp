import csv, hashlib, os, random, subprocess
import pandas as pd
R = os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
OUT = R + "/out/explorer_verification"; SEALED = R + "/data/explorer_verification/sealed"
os.makedirs(SEALED, exist_ok=True)
SEED = 20261013
stamp = subprocess.check_output(["date", "-Is"]).decode().strip()

def write_cases(name, rows, cols, mapping, mcols):
    d = OUT + "/" + name; os.makedirs(d, exist_ok=True)
    rnd = random.Random(SEED); idx = list(range(len(rows))); rnd.shuffle(idx)
    with open(d + "/cases.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["case_id"] + cols)
        for k, i in enumerate(idx): w.writerow(["%s_%03d" % (name, k + 1)] + [rows[i][c] for c in cols])
    mp = SEALED + "/%s_mapping.csv" % name
    with open(mp, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["case_id"] + mcols)
        for k, i in enumerate(idx): w.writerow(["%s_%03d" % (name, k + 1)] + [mapping[i][c] for c in mcols])
    h = hashlib.sha256(open(mp, "rb").read()).hexdigest()
    open(d + "/MAPPING_SHA256.txt", "w").write("sha256 %s sealed %s_mapping.csv\nsealed_at %s (date -Is on the server)\nseed %d\n" % (h, name, stamp, SEED))
    print(name, len(rows), "cases ->", d, "| mapping sealed", h[:12])

new = pd.read_csv(R + "/out/diag_20261005/symmetric_rule_new_brackets.csv")
strict = new[new.covered & new.profitable].reset_index(drop=True); assert len(strict) == 1384
pick = strict.sample(n=100, random_state=SEED).reset_index(drop=True)
rows = pick.to_dict("records")
write_cases("sym100", rows, ["block", "front", "victim", "back"], rows, ["episode_id", "pattern", "n2_outcome", "in_M", "profit_eth"])

j = pd.read_csv(R + "/out/trace_validation/n2_valuation/n2_case_level_join.csv")
coh = pd.read_csv(R + "/out/s0val/cohort_target_strict_miss_v2.csv")
rej = j[(j.cohort == "target_strict_miss") & (j.n2_outcome == "rejected")].merge(coh[["episode_id", "block", "front", "victim", "back", "actor"]], on="episode_id")
assert len(rej) == 53, len(rej)
rows = rej.to_dict("records")
write_cases("rej53", rows, ["block", "front", "victim", "back"], rows, ["episode_id", "case_id", "n2_outcome", "n2_decided_by", "trajectory_state", "value_flow_state", "actor"])

o = pd.read_csv(R + "/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")
p2 = o[o.in_P2_broad_closure == True].reset_index(drop=True)
fl = pd.read_csv(R + "/out/diag_20261005/arbitrage_inflow_sources.csv")
assert len(p2) == len(fl) == 12482, (len(p2), len(fl))
p2 = pd.concat([p2, fl[["canonical_flow", "mint_in", "nonpool_in"]]], axis=1)
assert (p2.in_records.astype(bool) != fl.absent.astype(bool)).all()
h5 = pd.read_csv(R + "/out/h5_arbitrage_missed.csv")[["hash", "profit_eth"]]
pool = p2[(~p2.in_records.astype(bool)) & p2.canonical_flow & (p2.in_P4_profitable_closure == True)]
assert len(pool) == 208, len(pool)
samp = pool.sample(n=100, random_state=SEED)
top6 = ["0x46c8f3e94d5950e59fa9051afc9b5081fd8cf013afb90fac22aebe80ebee005e", "0x184e20773231c902ab015f48c46244dea5044317396f064bc868e3205665f0ff",
        "0xa28aa478c6c54bb89061e54c3ea374e363f555f031b82cf64f8526f4ee50b6e6", "0x47b0d92d4d2fe1cce68ff855dcdfedd245ee6bbf0d712f3544eda53036a51137",
        "0x04ff20fe6d3f23bbfd35fbd30d91137b34ee5d77c3eb04ea6661d1011f64ca0e", "0x48ba14c72cb33edfb866fa052ea540d7d72e85ea3fe913317a98f2f23d997168"]
t6 = p2[p2.hash.str.lower().isin(top6)]
assert len(t6) == 6, len(t6)
arb = pd.concat([samp.assign(top6=False), t6.assign(top6=True)]).drop_duplicates("hash").merge(h5, on="hash", how="left")
arb["tx"] = arb.hash
rows = arb.to_dict("records")
write_cases("arb106", rows, ["block", "tx"], rows, ["hash", "top6", "canonical_flow", "mint_in", "nonpool_in", "first_conjunctive", "contested", "n_pools", "profit_eth", "economic_actor"])
print("sealed at", stamp)
