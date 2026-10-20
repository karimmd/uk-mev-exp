import csv, glob, json, os, re, subprocess, sys, time

protocol, cards_dir, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "claude-sonnet-5-5"
jd = os.path.join(out_dir, "judgments"); os.makedirs(jd, exist_ok=True)
proto = open(protocol).read()
claude = os.path.expanduser("~/.local/bin/claude")

def ask(card):
    prompt = proto + "\n\n---\n\n# Card\n\n" + card + "\n\nAnswer with the JSON object only."
    for i in range(3):
        p = subprocess.run([claude, "-p", "--output-format", "json", "--model", model, "--tools", ""],
                           input=prompt, capture_output=True, text=True, timeout=600)
        try:
            j = json.loads(p.stdout)
            text = j.get("result", "")
            m = re.search(r"\{.*\}", text, re.S)
            ans = json.loads(m.group(0))
            ans["_model"] = model; ans["_cost_usd"] = j.get("total_cost_usd"); ans["_session"] = j.get("session_id")
            return ans, text
        except Exception as e:
            err = "%s | stdout: %s | stderr: %s" % (e, p.stdout[:300], p.stderr[:300])
            time.sleep(5 + 10 * i)
    return None, err

cards = sorted(glob.glob(os.path.join(cards_dir, "*.md")))
n = 0
for path in cards:
    cid = os.path.basename(path)[:-3]
    jp = os.path.join(jd, cid + ".json")
    if os.path.exists(jp):
        n += 1; continue
    ans, text = ask(open(path).read())
    if ans is None:
        print("%s %s FAILED %s" % (time.strftime("%H:%M:%S"), cid, text), flush=True); continue
    ans["_raw"] = text; ans["case_id"] = cid; ans["_time"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    json.dump(ans, open(jp, "w"), indent=1)
    n += 1
    print("%s %s %d/%d Q1=%s Q2=%s conf=%s" % (time.strftime("%H:%M:%S"), cid, n, len(cards), ans.get("Q1"), ans.get("Q2"), ans.get("confidence")), flush=True)

with open(os.path.join(out_dir, "sheet.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["case_id", "scorer", "Q1_sandwich", "Q2_positive_after_cost", "confidence_1to5", "actor", "note"])
    for jp in sorted(glob.glob(os.path.join(jd, "*.json"))):
        a = json.load(open(jp))
        w.writerow([a["case_id"], a.get("_model"), a.get("Q1"), a.get("Q2"), a.get("confidence"), a.get("actor"), (a.get("note") or "").replace("\n", " ")])
print("judge complete", n, "of", len(cards), flush=True)
