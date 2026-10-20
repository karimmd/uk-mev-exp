import os
"""Second record: Frontrunner Jones (Torres et al., USENIX Security 2021) insertion attacks, joined to
the rule-accepted brackets on the replication lattice (residue 6). FJ rows carry block, attacker and
whale ADDRESSES (not hashes), exchange, token. Join key: block + victim sender address."""
import json, glob, gzip, collections
import pandas as pd
ROOT = os.environ.get("MEV_ROOT", "."); REV = ROOT + "/revision"
fj = pd.read_csv(REV + "/data/external/frontrunner_jones/insertion_attacks.csv")
fj["block"] = fj["Block Number"].astype(float).astype(int)
fj = fj[(fj.block >= 10000000) & (fj.block % 88 == 6)].copy()
fj["whale"] = fj["Whale"].str.lower(); fj["first"] = fj["First Attacker"].str.lower(); fj["second"] = fj["Second Attacker"].str.lower()
print("FJ insertion attacks on lattice, block>=10M:", len(fj), "blocks", fj.block.min(), "to", fj.block.max())
br = pd.read_csv(REV + "/out/h3_brackets_rep.csv")
br = br[br.block <= fj.block.max()].copy()
print("rule brackets on lattice up to FJ end block:", len(br), "fully recorded", int(br.fully_mined.sum()), "absent", int(br.missed.sum()))
want = set(br.front.str.lower()) | set(br.victim.str.lower()) | set(br.back.str.lower())
store = {}
for s in sorted(glob.glob(ROOT + "/local/evidence/benign_sweep_rep/shard-*.jsonl.gz")):
    with gzip.open(s, "rt") as f:
        for line in f:
            x = json.loads(line)
            if x["hash"].lower() in want: store[x["hash"].lower()] = x
br["victim_from"] = [store[h.lower()]["from"].lower() if h.lower() in store else None for h in br.victim]
br["front_from"] = [store[h.lower()]["from"].lower() if h.lower() in store else None for h in br.front]
fjkeys = set(zip(fj.block, fj.whale)); fjkeys_f = set(zip(fj.block, fj["first"]))
br["in_fj"] = [((b, v) in fjkeys) for b, v in zip(br.block, br.victim_from)]
br["in_fj_front"] = [((b, f) in fjkeys_f) for b, f in zip(br.block, br.front_from)]
print("\nrule brackets found in FJ by (block, victim sender):", int(br.in_fj.sum()), "of", len(br), "= %.1f%%" % (100 * br.in_fj.mean()))
print(pd.crosstab(br.fully_mined.map({True: "recorded_in_Weintraub", False: "not_fully_recorded"}), br.in_fj.map({True: "in_FJ", False: "not_in_FJ"})))
print("\nstrict absent (Weintraub) brackets in this era:", int(br.missed.sum()), "of which in FJ:", int(br[br.missed].in_fj.sum()))
brkeys = set(zip(br.block, br.victim_from))
fj["in_rule"] = [((b, w) in brkeys) for b, w in zip(fj.block, fj.whale)]
print("\nFJ attacks reproduced by a rule bracket (block, whale):", int(fj.in_rule.sum()), "of", len(fj), "= %.1f%%" % (100 * fj.in_rule.mean()))
print("FJ not in rule, by exchange:"); print(fj[~fj.in_rule].Exchange.value_counts().head())
br.to_csv(REV + "/out/diag_20261005/fj_join_brackets.csv", index=False); fj.to_csv(REV + "/out/diag_20261005/fj_join_fj.csv", index=False)
