import csv, glob, os, re, sys

pack_dir, out_csv = sys.argv[1], sys.argv[2]
rows = []
for path in sorted(glob.glob(os.path.join(pack_dir, "episodes", "pack_*.md"))):
    text = open(path).read()
    pid = os.path.basename(path)[:-3]
    block = int(re.search(r"^Block (\d+)\.", text, re.M).group(1))
    hashes = {}
    for leg in ("Front", "Victim", "Back"):
        m = re.search(r"### %s leg: `(0x[0-9a-f]{64})`" % leg, text)
        hashes[leg.lower()] = m.group(1)
    rows.append([pid, block, hashes["front"], hashes["victim"], hashes["back"]])
os.makedirs(os.path.dirname(out_csv), exist_ok=True)
with open(out_csv, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["case_id", "block", "front", "victim", "back"])
    w.writerows(rows)
print("cases", len(rows), "->", out_csv)
