import json, csv, collections, random, sys, os
REV=os.path.join(os.environ.get("MEV_ROOT", "."), "revision")
sys.path.insert(0, REV+"/scripts/trace_validation/08_analysis")
import run_task08 as T8
rows=[json.loads(l) for l in open(REV+"/out/trace_validation/07_execution/task07_outcomes.jsonl")]
pc={}
for l in open(REV+"/out/trace_validation/n2_valuation/n2_per_case.jsonl"):
    r=json.loads(l); pc[r["case_id"]]=r["primary"]["outcome"]
man={r["case_id"]:r for r in csv.DictReader(open(REV+"/data/trace_validation/manifests/v2/cases_blinded.csv"))}
gmap={r["case_id"]:r["group"] for r in csv.DictReader(open(REV+"/data/trace_validation/group_map/v2/case_group_map.csv"))}
MIN_CELL=20
recs=[]
for r in rows:
    g=gmap[r["case_id"]]
    if g not in ("target_strict_miss","control_detected"): continue
    out=pc.get(r["case_id"], r["outcome"])
    actor=(r["value_flow"].get("metrics") or {}).get("actor") or ("na_"+r["case_id"])
    recs.append(dict(lab="missed" if g=="target_strict_miss" else "recorded", sup=1 if out=="structurally_supported" else 0,
                     st=T8.stratum(r["covariates"]), block=man[r["case_id"]]["block"], actor=actor))
strata_all=[T8.stratum(r["covariates"]) for r in rows]
size=collections.Counter(strata_all)
per=collections.defaultdict(collections.Counter)
for x in recs: per[x["st"]][x["lab"]]+=1
included={st for st in size if size[st]>=MIN_CELL and per[st]["missed"]>0 and per[st]["recorded"]>0}
other=("other",)*5
pooled={st for st in size if st not in included}
for x in recs:
    if x["st"] in pooled: x["st"]=other
size2=collections.Counter(other if st in pooled else st for st in strata_all)
per=collections.defaultdict(collections.Counter)
for x in recs: per[x["st"]][x["lab"]]+=1
if size2[other]>=MIN_CELL and per[other]["missed"]>0 and per[other]["recorded"]>0: included.add(other)
inc=sorted(included); weights={st:size2[st] for st in inc}
def sdiff(sample, inc_set):
    num=collections.defaultdict(lambda:[0,0]); den=collections.defaultdict(lambda:[0,0])
    for x in sample:
        if x["st"] not in inc_set: continue
        t=num[x["st"]] if x["lab"]=="missed" else den[x["st"]]; t[0]+=x["sup"]; t[1]+=1
    wm=wr=tot=0.0
    for st in sorted(inc_set):
        m,r=num[st],den[st]
        if m[1]==0 or r[1]==0: continue
        w=weights[st]; wm+=w*m[0]/m[1]; wr+=w*r[0]/r[1]; tot+=w
    return 100*(wm/tot-wr/tot) if tot else None
full=sdiff(recs,set(inc)); print("N2 primary standardized diff:",round(full,4),"strata",len(inc))
print("leave-one-stratum-out:")
for st in inc:
    d=sdiff(recs,set(inc)-{st}); print("  drop",st,"missed n=",per[st]["missed"],"->",round(d,3))
def cboot(key,B=2000,seed=20260920):
    groups=collections.defaultdict(list)
    for x in recs: groups[x[key]].append(x)
    keys=list(groups); rnd=random.Random(seed); out=[]
    for _ in range(B):
        s=[]; 
        for k in rnd.choices(keys,k=len(keys)): s.extend(groups[k])
        d=sdiff(s,set(inc)); 
        if d is not None: out.append(d)
    out.sort(); return out[int(.025*len(out))],out[int(.975*len(out))],len(out)
print("block-clustered bootstrap 95%:",cboot("block"))
print("actor-clustered bootstrap 95%:",cboot("actor"))
print("distinct blocks",len({x["block"] for x in recs}),"distinct actors",len({x["actor"] for x in recs}))
