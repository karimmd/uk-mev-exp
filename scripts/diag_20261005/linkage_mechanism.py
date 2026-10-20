import gzip, json, glob, os, sys, time
import pandas as pd
ROOT=os.environ.get("MEV_ROOT", ".")
WETH="0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
OUT=ROOT+"/revision/out/diag_20261005"

def load_store(name, want):
    idx={}
    shards=sorted(glob.glob(f"{ROOT}/local/evidence/{name}/shard-*.jsonl.gz"))
    t=time.time(); first=True
    for s in shards:
        with gzip.open(s,"rt") as f:
            for line in f:
                r=json.loads(line)
                if first:
                    print(name,"record keys:",sorted(r.keys()),flush=True); first=False
                h=(r.get("hash") or r.get("tx_hash") or "").lower()
                if h in want: idx[h]=r
    print(name,"loaded",len(idx),"of",len(want),"wanted in",round(time.time()-t),"s",flush=True)
    return idx

def deltas(ev,addr):
    d={}
    for tok,frm,to,amt in ev["transfers"]:
        a=int(amt)
        if frm==addr: d[tok]=d.get(tok,0)-a
        if to==addr: d[tok]=d.get(tok,0)+a
    return d
def gross(ev,addr):
    gi,go={},{}
    for tok,frm,to,amt in ev["transfers"]:
        a=int(amt)
        if to==addr: gi[tok]=gi.get(tok,0)+a
        if frm==addr: go[tok]=go.get(tok,0)+a
    return gi,go

sys.path.insert(0,ROOT+"/revision/scripts")
from catalog import _economic_actor

coh=[]
for g in ["target_strict_miss","control_detected"]:
    c=pd.read_csv(f"{ROOT}/revision/out/s0val/cohort_{g}_v2.csv"); c["group"]=g; coh.append(c)
coh=pd.concat(coh,ignore_index=True)
want=set(coh.front.str.lower())|set(coh.back.str.lower())|set(coh.victim.str.lower())
ev=load_store("benign_sweep_rep",want)
rows=[]
for r in coh.itertuples():
    F=ev.get(r.front.lower()); B=ev.get(r.back.lower()); V=ev.get(r.victim.lower())
    if not (F and B and V): rows.append(dict(group=r.group,episode_id=r.episode_id,missing=True)); continue
    aF,aB=_economic_actor(F),_economic_actor(B)
    dF,dB=deltas(F,aF),deltas(B,aB)
    tok=[t for t in set(dF)|set(dB) if t!=WETH and dF.get(t,0)>0 and dB.get(t,0)<0]
    same_amt=any(dF[t]==-dB[t] for t in tok)
    close_amt=any(abs(dF[t]+dB[t])<=0.01*dF[t] for t in tok)
    rows.append(dict(group=r.group,episode_id=r.episode_id,missing=False,
        same_sender=F["from"].lower()==B["from"].lower(),
        same_to=(F.get("to") or "").lower()==(B.get("to") or "").lower(),
        same_token_amount=same_amt, token_amount_within_1pct=close_amt,
        actor_is_sender_F=aF==F["from"].lower(), actor_is_to_F=aF==(F.get("to") or "").lower(),
        victim_adjacent=(V["index"]==F["index"]+1 and B["index"]==V["index"]+1),
        n_inner=B["index"]-F["index"]-1,
        front_pools=len(F["pools"]), back_pools=len(B["pools"]),
        shared_pools=len(set(F["pools"])&set(V["pools"])&set(B["pools"])),
        front_has_weth=WETH in dF, back_has_weth=WETH in dB,
        victim_to=(V.get("to") or "").lower()))
s=pd.DataFrame(rows); s.to_csv(f"{OUT}/sandwich_linkage.csv",index=False)
print("\nSANDWICH missing evidence:",s.missing.sum())
s=s[~s.missing]
for col in ["same_sender","same_to","same_token_amount","token_amount_within_1pct","victim_adjacent","actor_is_sender_F","actor_is_to_F","front_has_weth","back_has_weth"]:
    print(f"{col:28s}", s.groupby("group")[col].mean().round(4).to_dict())
s["any_link"]=s.same_sender|s.same_to|s.same_token_amount
print("any of (same_sender, same_to, same_token_amount):", s.groupby("group").any_link.mean().round(4).to_dict())
print("n_inner distribution by group:"); print(pd.crosstab(s.group,s.n_inner.clip(upper=5)))
print("front pools by group:"); print(pd.crosstab(s.group,s.front_pools.clip(upper=4)))
del ev

o=pd.read_csv(f"{ROOT}/revision/data/arbitrage_finalization/ordering_v1/ordering_case_rows.csv")
o=o[o.in_P2_broad_closure==True]
want=set(o.hash.str.lower())
ev=load_store("benign_sweep",want)
rows=[]
for r in o.itertuples():
    E=ev.get(r.hash.lower())
    if not E: rows.append(dict(absent=not r.in_records,missing=True)); continue
    a=_economic_actor(E); d=deltas(E,a); gi,go=gross(E,a)
    pt=[t for t in set(gi)&set(go)]
    exact=[t for t in pt if gi[t]==go[t]]
    near=[t for t in pt if abs(gi[t]-go[t])<=0.001*max(gi[t],go[t])]
    gained=[t for t,v in d.items() if v>0]
    rows.append(dict(absent=not r.in_records,missing=False,first=r.first_conjunctive,contested=r.contested,
        actor_is_sender=a==E["from"].lower(), actor_is_to=a==(E.get("to") or "").lower(),
        n_passthrough=len(pt), all_passthrough_exact=len(pt)>0 and len(exact)==len(pt),
        all_passthrough_within_0p1pct=len(pt)>0 and len(near)==len(pt),
        profit_token_weth=(gained==[WETH]), n_transfers=len(E["transfers"]), n_pools=len(E["pools"]),
        n_distinct_tokens=len({t for t,_,_,_ in E["transfers"]}), tx_value_nonzero=int(E.get("value") or 0)>0 if "value" in E else None))
a=pd.DataFrame(rows); a.to_csv(f"{OUT}/arbitrage_chaining.csv",index=False)
print("\nARBITRAGE missing evidence:",a.missing.sum()); a=a[~a.missing]
for col in ["actor_is_sender","actor_is_to","all_passthrough_exact","all_passthrough_within_0p1pct","profit_token_weth","first"]:
    print(f"{col:32s}", a.groupby("absent")[col].mean().round(4).to_dict())
print("n_transfers median by arm:", a.groupby("absent").n_transfers.median().to_dict())
print("n_distinct_tokens by arm:"); print(pd.crosstab(a.absent,a.n_distinct_tokens.clip(upper=6)))
print("exact chaining x first, absent arm:"); print(pd.crosstab([a.absent,a.all_passthrough_exact],a.first))
