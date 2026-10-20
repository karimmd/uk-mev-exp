import os
"""EXPLORATORY DIAGNOSTIC follow-up, 2026-10-05. Quantifies the union of linkage differences for
sandwich and tests the split-route fingerprint for arbitrage."""
import gzip, json, glob, sys, pandas as pd
ROOT=os.environ.get("MEV_ROOT", "."); OUT=ROOT+"/revision/out/diag_20261005"
WETH="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
sys.path.insert(0,ROOT+"/revision/scripts"); from catalog import _economic_actor
s=pd.read_csv(f"{OUT}/sandwich_linkage.csv"); s=s[~s.missing]
s["multi_pool_leg"]=(s.front_pools>=2)|(s.back_pools>=2)
s["amount_mismatch"]=~s.token_amount_within_1pct
s["either"]=s.multi_pool_leg|s.amount_mismatch
s["multi_victim_like"]=s.n_inner>=2
print("SANDWICH: share of brackets with each property, by arm")
print(s.groupby("group")[["multi_pool_leg","amount_mismatch","either","multi_victim_like","victim_adjacent"]].mean().round(4).T)
print("\ncounts, missed arm:"); print(s[s.group=="target_strict_miss"][["multi_pool_leg","amount_mismatch","either"]].sum())
print("\nmissed arm: multi_pool x amount_mismatch"); m=s[s.group=="target_strict_miss"]; print(pd.crosstab(m.multi_pool_leg,m.amount_mismatch))
print("\nrecorded arm: same"); r=s[s.group=="control_detected"]; print(pd.crosstab(r.multi_pool_leg,r.amount_mismatch))
o=pd.read_csv(f"{ROOT}/revision/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv"); o=o[o.in_P2_broad_closure==True]
want=set(o.hash.str.lower()); ev={}
for sh in sorted(glob.glob(f"{ROOT}/local/evidence/benign_sweep/shard-*.jsonl.gz")):
    with gzip.open(sh,"rt") as f:
        for line in f:
            r=json.loads(line)
            if r["hash"].lower() in want: ev[r["hash"].lower()]=r
rows=[]
for r in o.itertuples():
    E=ev[r.hash.lower()]; a=_economic_actor(E)
    buys={}; sells={}; gi={}; go={}
    for tok,frm,to,amt in E["transfers"]:
        amt=int(amt)
        if to==a: buys[tok]=buys.get(tok,0)+1; gi[tok]=gi.get(tok,0)+amt
        if frm==a: sells[tok]=sells.get(tok,0)+1; go[tok]=go.get(tok,0)+amt
    pt=[t for t in set(gi)&set(go) if t!=WETH]
    split=any(buys.get(t,0)>1 or sells.get(t,0)>1 for t in pt)
    weth_split=buys.get(WETH,0)>1 or sells.get(WETH,0)>1
    slack=[(gi[t]-go[t])/max(gi[t],go[t]) for t in pt]
    rows.append(dict(absent=not r.in_records, first=bool(r.first_conjunctive), contested=bool(r.contested),
        split_route=split, weth_split=weth_split, n_pt=len(pt),
        pt_slack_max=max(slack) if slack else None, pt_slack_min=min(slack) if slack else None,
        kept_inventory=any(x>0.001 for x in slack), paid_out=any(x<-0.001 for x in slack),
        exact=all(abs(x)<=1e-12 for x in slack) if slack else False, era=("pre_flashbots" if r.block<11600000 else "flashbots_pre_london" if r.block<12965000 else "post_london")))
a=pd.DataFrame(rows); a.to_csv(f"{OUT}/arbitrage_split.csv",index=False)
print("\nARBITRAGE: by arm (absent=True is record-absent)")
print(a.groupby("absent")[["split_route","weth_split","kept_inventory","paid_out","exact","first"]].mean().round(4).T)
print("\nabsent arm: split_route x first (contested only)"); c=a[a.contested]; print(pd.crosstab([c.absent,c.split_route],c["first"]))
print("\nfirst rate by split_route within each arm (contested):"); print(c.groupby(["absent","split_route"])["first"].agg(["mean","count"]).round(3))
print("\nsplit_route by era and arm:"); print(a.groupby(["era","absent"]).split_route.agg(["mean","count"]).round(3))
print("\nkept_inventory vs paid_out by arm:"); print(pd.crosstab(a.absent,[a.kept_inventory,a.paid_out]))
