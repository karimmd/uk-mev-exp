import csv, os, sys, math, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib as mpl, matplotlib.pyplot as plt
EDGE = "#222222"
EDGE_LW = 0.6
mpl.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "Nimbus Roman", "Liberation Serif", "DejaVu Serif"], "mathtext.fontset": "stix",
    "font.size": 8, "axes.titlesize": 8, "axes.labelsize": 8, "xtick.labelsize": 7, "ytick.labelsize": 7, "legend.fontsize": 7, "legend.frameon": False,
    "legend.handlelength": 1.4, "legend.handletextpad": 0.4, "legend.columnspacing": 1.0, "axes.linewidth": 0.7, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.linewidth": 0.4, "grid.color": "#cccccc", "grid.linestyle": ":", "axes.axisbelow": True, "xtick.direction": "out", "ytick.direction": "out",
    "xtick.major.size": 2.5, "ytick.major.size": 2.5, "xtick.major.width": 0.7, "ytick.major.width": 0.7, "figure.dpi": 200, "savefig.dpi": 600, "savefig.bbox": "tight",
    "savefig.pad_inches": 0.01, "figure.constrained_layout.use": False, "pdf.fonttype": 42, "ps.fonttype": 42})
_orig_subplots, _orig_figure = plt.subplots, plt.figure
def _acm_width(figsize):
    if not figsize or abs(figsize[0] - 5.48) < 0.01: return figsize
    return (5.48, figsize[1] if figsize[0] >= 6.0 else figsize[1] * 1.15)
def _subplots(*a, **kw):
    if "figsize" in kw: kw["figsize"] = _acm_width(kw["figsize"])
    return _orig_subplots(*a, **kw)
def _figure(*a, **kw):
    if "figsize" in kw: kw["figsize"] = _acm_width(kw["figsize"])
    return _orig_figure(*a, **kw)
plt.subplots, plt.figure = _subplots, _figure
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
VERSION = sys.argv[1] if len(sys.argv) > 1 else "v2"
OUTDIR = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "latex")
TAB = os.path.join(OUTDIR, "tables"); os.makedirs(TAB, exist_ok=True)
SRC = os.path.join(ROOT, "server/revision/out/explorer_verification_api" + ("_v2" if VERSION == "v2" else ""), "multi_reader", "cards_long.csv")
GRID = "#e6e6e6"
READERS = ["sonnet", "opus55", "deepseek"]
RCOL = {"sonnet": "#1f77b4", "opus55": "#e6550d", "deepseek": "#6a3d9a"}
RHATCH = {"sonnet": "", "opus55": "////", "deepseek": "...."}
RLAB = {"sonnet": "Sonnet 5.5", "opus55": "Opus 5.5", "deepseek": "DeepSeek-V4.1-Flash"}
SETS = [("f1b", "missed", "missed\n(100)"), ("f1b", "reported", "reported\n(50)"), ("f1b", "comparison", "comparison\ncases (50)"),
        ("sym100", "missed", "added by\nS5$'$ (100)"), ("rej53", "missed", "rejected\n53 (53)"), ("arb106", "missed", "arbitrage,\ncanonical (100)")]
SETTEX = {("f1b", "missed"): ("Sealed pack", "missed"), ("f1b", "reported"): ("", "reported"), ("f1b", "comparison"): ("", "comparison"),
          ("sym100", "missed"): ("Added by S5$'$", "missed"), ("rej53", "missed"): ("Rejected 53", "missed"), ("arb106", "missed"): ("Arbitrage, canonical", "missed")}

def rows(p):
    with open(p, newline="") as f: return list(csv.DictReader(f))
def wilson(k, n, z=1.96):
    if n == 0: return (0, 0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (100 * (c - h) / d, 100 * (c + h) / d)
def kappa(a, b):
    cats = sorted(set(a) | set(b)); n = len(a)
    if n == 0: return float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((sum(x == c for x in a) / n) * (sum(y == c for y in b) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")
def tidy(ax, xgrid=True):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_linewidth(EDGE_LW)
    ax.grid(axis="x" if xgrid else "y", color=GRID, linewidth=0.5); ax.set_axisbelow(True); ax.tick_params(length=2, width=0.5)
def save(fig, name):
    p = os.path.join(OUTDIR, name + ".pdf"); fig.savefig(p, bbox_inches="tight"); plt.close(fig); print("wrote", p)
def tex(name, body):
    p = os.path.join(TAB, name + ".tex"); open(p, "w").write(body); print("wrote", p)
def f(v):
    try: return float(v)
    except Exception: return None

cards = rows(SRC)
top6 = {r["card"] for r in cards if r["sample"] == "arb106" and r["card"] in {"arb106_052", "arb106_006", "arb106_014", "arb106_087", "arb106_073", "arb106_065"}}
def sub(s, arm, rd): return [r for r in cards if r["sample"] == s and r["arm"] == arm and r["reader"] == rd and not (s == "arb106" and r["card"] in top6)]
def stats_of(s, arm, rd):
    g = sub(s, arm, rd); n = len(g)
    if n == 0: return None
    q1 = sum(r["Q1"] == "yes" for r in g); sup = sum(r["verdict"] == "structurally_supported" for r in g)
    d = dict(n=n, q1=q1, sup=sup, actor=sum(r["actor_match"] == "True" for r in g))
    if s != "arb106":
        d["agree"] = sum(r["verdict"] == r["n2_outcome"] for r in g); d["kappa"] = kappa([r["n2_outcome"] for r in g], [r["verdict"] for r in g])
        w2 = [r for r in g if r["w2_outcome"]]; d["agree_w2"] = sum(r["verdict"] == r["w2_outcome"] for r in w2); d["n_w2"] = len(w2)
    return d
def all_three(s, arm):
    by = collections.defaultdict(dict)
    for rd in READERS:
        for r in sub(s, arm, rd): by[r["card"]][rd] = r["verdict"]
    full = [v for v in by.values() if len(v) == 3]
    return sum(1 for v in full if len(set(v.values())) == 1), len(full)

SETY = ["missed (100)", "reported (50)", "comparison cases (50)", "added by S5$'$ (100)", "rejected 53", "arbitrage, canonical (100)"]
def fig_validator():
    fig, axes = plt.subplots(1, 3, figsize=(7.16, 2.7), gridspec_kw={"width_ratios": [1.35, 0.95, 0.85]}); fig.subplots_adjust(wspace=0.55)
    y = np.arange(len(SETS))[::-1]
    ax = axes[0]; h = 0.25
    for j, rd in enumerate(READERS):
        vals = []; cis = []
        for s, arm, _ in SETS:
            d = stats_of(s, arm, rd); v = 100 * d["q1"] / d["n"] if d else 0; vals.append(v); cis.append(wilson(d["q1"], d["n"]) if d else (0, 0))
        yy = y - (j - 1) * (h + 0.02)
        ax.barh(yy, vals, h, color=RCOL[rd], edgecolor="white", linewidth=0.5, hatch=RHATCH[rd], label=RLAB[rd])
        ax.errorbar(vals, yy, xerr=[[max(v - lo, 0) for v, (lo, hi) in zip(vals, cis)], [max(hi - v, 0) for v, (lo, hi) in zip(vals, cis)]], fmt="none", ecolor=EDGE, elinewidth=0.6, capsize=1.3)
    ax.set_yticks(y); ax.set_yticklabels(SETY, fontsize=7.5); ax.tick_params(axis="x", labelsize=7.5); ax.set_xlabel("called MEV (%)", fontsize=8); ax.set_xlim(0, 108); ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_title("(a) Called MEV, by set and validator", fontsize=8.5, loc="left"); tidy(ax)
    hh, ll = ax.get_legend_handles_labels(); fig.legend(hh, ll, fontsize=7.5, frameon=False, loc="lower center", bbox_to_anchor=(0.42, -0.12), ncol=3, handlelength=1.4, columnspacing=1.2)
    ax = axes[1]; vals = []; cis = []
    for s, arm, _ in SETS:
        k, m = all_three(s, arm); vals.append(100 * k / m if m else 0); cis.append(wilson(k, m) if m else (0, 0))
    ax.barh(y, vals, 0.6, color="#737373", edgecolor="none")
    ax.errorbar(vals, y, xerr=[[max(v - lo, 0) for v, (lo, hi) in zip(vals, cis)], [max(hi - v, 0) for v, (lo, hi) in zip(vals, cis)]], fmt="none", ecolor=EDGE, elinewidth=0.6, capsize=1.3)
    for yi, v, (lo, hi) in zip(y, vals, cis): ax.text(hi + 1.5, yi, "%.0f" % v, ha="left", va="center", fontsize=7.5, color="#333333")
    ax.set_yticks(y); ax.set_yticklabels([""] * len(y)); ax.tick_params(axis="x", labelsize=7.5); ax.set_xlabel("all three agree (%)", fontsize=8); ax.set_xlim(0, 118); ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_title("(b) Between validators", fontsize=8.5, loc="left"); tidy(ax)
    ax = axes[2]; x3 = np.arange(3); w = 0.36; out = {}
    for j, (key, col, lab) in enumerate((("n2_outcome", "#b8c4d6", "original witness"), ("w2_outcome", "#1f77b4", "revised witness (W2)"))):
        v = []; cnts = []
        for rd in READERS:
            g = [r for r in cards if r["reader"] == rd and r["sample"] != "arb106" and r[key]]; k = sum(1 for r in g if r[key] == r["verdict"]); v.append(100 * k / len(g) if g else 0); cnts.append((k, len(g)))
        out[key] = cnts; ax.bar(x3 + (j - 0.5) * (w + 0.04), v, w, color=col, edgecolor="none", label=lab)
        for xi, vi, (k, m) in zip(x3 + (j - 0.5) * (w + 0.04), v, cnts): ax.text(xi, vi + 1, "%d/\n%d" % (k, m), ha="center", va="bottom", fontsize=6.8, color="#333333")
    ax.set_xticks(x3); ax.set_xticklabels(["Sonnet\n5.5", "Opus\n5.5", "DeepSeek-\nV4.1-\nFlash"], fontsize=6.8); ax.tick_params(axis="y", labelsize=7.5); ax.set_ylabel("agreement with REFEREE (%)", fontsize=8); ax.set_ylim(0, 150); ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_title("(c) With REFEREE", fontsize=8.5, loc="left"); ax.legend(fontsize=7.2, frameon=False, loc="upper left", bbox_to_anchor=(-0.04, 1.0), ncol=1, handlelength=1.2, labelspacing=0.3, borderaxespad=0.1); tidy(ax, xgrid=False)
    save(fig, "llm_validator")
    return out

def fig_values():
    pts = {rd: [(f(r["ledger_after_cost"]), f(r["validator_after_gas"])) for r in cards if r["reader"] == rd and r["sample"] != "arb106"] for rd in READERS}
    pts = {rd: [p for p in v if p[0] is not None and p[1] is not None] for rd, v in pts.items()}
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 2.7)); fig.subplots_adjust(wspace=0.35)
    ax = axes[0]
    for rd in READERS:
        ax.scatter([p[0] for p in pts[rd]], [p[1] for p in pts[rd]], s=9, color=RCOL[rd], alpha=0.6, edgecolors="none", label="%s (n = %d)" % (RLAB[rd], len(pts[rd])))
    lim = (-0.3, 6); ax.plot(lim, lim, color="#111111", linewidth=0.6, linestyle="--"); ax.set_xscale("symlog", linthresh=0.01); ax.set_yscale("symlog", linthresh=0.01); ax.set_xlim(lim); ax.set_ylim(lim)
    ax.set_xlabel("REFEREE ledger after observable cost (ETH)", fontsize=8.5); ax.set_ylabel("validator's profit after gas (ETH)", fontsize=8.5); ax.tick_params(labelsize=7.5)
    ax.set_title("(a) Profit per card and validator", fontsize=9, loc="left"); ax.legend(fontsize=7.2, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.28), ncol=3, handletextpad=0.2, columnspacing=0.8); tidy(ax, xgrid=False)
    ax = axes[1]; edges = [0, 0.001, 0.01, 0.1, 1.0, 100]; labels = ["< 0.001", "0.001\nto 0.01", "0.01\nto 0.1", "0.1\nto 1", "> 1"]; x = np.arange(5); w = 0.26; res = {}
    for j, rd in enumerate(READERS):
        d = np.array([abs(p[0] - p[1]) for p in pts[rd]]); cnts = [int(((d >= lo) & (d < hi)).sum()) for lo, hi in zip(edges[:-1], edges[1:])]; res[rd] = dict(n=len(d), bins=cnts, median=float(np.median(d)) if len(d) else None, within_001=int((d < 0.01).sum()))
        ax.bar(x + (j - 1) * (w + 0.02), [100 * c / len(d) if len(d) else 0 for c in cnts], w, color=RCOL[rd], edgecolor="white", linewidth=0.5, hatch=RHATCH[rd], label=RLAB[rd])
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=7.5); ax.tick_params(axis="y", labelsize=7.5); ax.set_xlabel("absolute difference from the ledger (ETH)", fontsize=8.5); ax.set_ylabel("share of cards (%)", fontsize=8.5); ax.set_ylim(0, 100)
    ax.set_title("(b) Agreement on the profit figure", fontsize=9, loc="left"); ax.legend(fontsize=7.5, frameon=False); tidy(ax, xgrid=False)
    save(fig, "validator_values")
    return res

def tab_samples(pm):
    def trio(fn): return " / ".join(fn(rd) for rd in READERS)
    L = [r"\begin{table}[!t]", r"\centering", r"\caption{Validation on Public Explorers by Three Validators}", r"\label{tab:explorer_samples}", r"\scriptsize", r"\setlength\tabcolsep{2.5pt}",
         r"\begin{threeparttable}", r"\begin{tabular}{>{\raggedright\arraybackslash}p{1.9cm}lrccccc}", r"\toprule",
         r"\textbf{Sample} & \textbf{Set} & \textbf{Cards} & \textbf{Called MEV (\%)} & \textbf{Positive (\%)} & \textbf{Agree. (\%)} & $\kappa$ & \textbf{All agree (\%)} \\", r"\midrule"]
    first = True
    for s, arm, _ in SETS:
        d = {rd: stats_of(s, arm, rd) for rd in READERS}
        if any(v is None for v in d.values()): continue
        lab, setlab = SETTEX[(s, arm)]; k3, m3 = all_three(s, arm)
        n0 = d["sonnet"]["n"]
        row = [(r"\multirow{3}{*}{Sealed pack}" if first and s == "f1b" else lab), setlab, str(n0),
               trio(lambda rd: "%d" % round(100 * d[rd]["q1"] / d[rd]["n"])), trio(lambda rd: "%d" % round(100 * d[rd]["sup"] / d[rd]["n"])),
               trio(lambda rd: "%d" % round(100 * d[rd]["agree"] / d[rd]["n"])) if s != "arb106" else "---",
               trio(lambda rd: ("%.2f" % d[rd]["kappa"]).replace("-", "$-$")) if s != "arb106" else "---",
               "%d" % round(100 * k3 / m3) if m3 else "---"]
        if s == "f1b": first = False
        L.append(" & ".join(row) + r" \\")
    L += [r"\bottomrule", r"\end{tabular}", r"\begin{tablenotes}", r"\footnotesize",
          r"\item[] \emph{Note:} Each cell with three values gives Sonnet 5.5 / Opus 5.5 / DeepSeek-V4.1-Flash. ``Called MEV'' is the share of cards the validator calls a sandwich attack (or an arbitrage); ``positive'' the share it also finds positive after observable cost; Agree.\ and $\kappa$ are against the evidence state under the original witness; ``all agree'' is the share of cards on which the three validators return the same verdict. Wilson 95\% intervals for every share, and the share of cards on which each validator's attacker address matches the economic actor, are in the supplementary document.",
          r"\end{tablenotes}", r"\end{threeparttable}", r"\end{table}", ""]
    tex("tab_explorer_samples", "\n".join(L))
    L = [r"\begin{table}[!t]", r"\centering", r"\caption{Validation on Public Explorers, per Validator with Wilson Intervals}", r"\label{tab:explorer_samples_full}", r"\scriptsize", r"\setlength\tabcolsep{2pt}",
         r"\begin{threeparttable}", r"\begin{tabular}{llrllrrr}", r"\toprule",
         r"\textbf{Sample, set} & \textbf{Validator} & \textbf{Cards} & \textbf{Called MEV} & \textbf{Positive} & \textbf{Agree.} & \textbf{Agree., W2} & \textbf{Actor} \\", r"\midrule"]
    for s, arm, _ in SETS:
        lab, setlab = SETTEX[(s, arm)]; lab = (lab or "Sealed pack") + ", " + setlab
        for rd in READERS:
            d = stats_of(s, arm, rd)
            if d is None: continue
            ci = lambda k, n: "%d\\%% [%.1f, %.1f]" % (round(100 * k / n), *wilson(k, n))
            L.append(r"%s & %s & %d & %s & %s & %s & %s & %d/%d \\" % (lab if rd == "sonnet" else "", RLAB[rd], d["n"], ci(d["q1"], d["n"]), ci(d["sup"], d["n"]),
                     ("%.1f\\%%" % (100 * d["agree"] / d["n"])) if s != "arb106" else "---", ("%.1f\\%%" % (100 * d["agree_w2"] / d["n_w2"])) if s != "arb106" and d["n_w2"] else "---", d["actor"], d["n"]))
    L += [r"\bottomrule", r"\end{tabular}", r"\begin{tablenotes}", r"\footnotesize",
          r"\item[] \emph{Note:} Brackets are Wilson 95\% intervals. Agree.\ is agreement with the evidence state under the original witness and Agree., W2 under the revised witness; both over the cards with a state.",
          r"\end{tablenotes}", r"\end{threeparttable}", r"\end{table}", ""]
    tex("tab_explorer_samples_full", "\n".join(L))

EX = os.path.join(ROOT, "server/revision/out/exhibits")
STATE = {"structurally_supported": "supported", "rejected": "rejected", "undecidable": "inconclusive"}
def majority(byrd):
    c = collections.Counter(byrd[rd] for rd in READERS if rd in byrd); top, k = c.most_common(1)[0]
    return top if k >= 2 and len(c) and sum(c.values()) == 3 else ("split" if sum(c.values()) == 3 else None)
def by_card():
    d = collections.defaultdict(dict)
    for r in cards: d[(r["sample"], r["card"])][r["reader"]] = r
    return d

def tab_disagreements():
    samples = [("f1b", "Sealed pack"), ("sym100", "Added by S5$'$"), ("rej53", "Rejected 53")]
    def key(m, st, led, q2no):
        if st == m: return None
        if st == "rejected":
            if m == "structurally_supported": return ("rejected", "ledger positive, validators support" if led == "positive" else "ledger inconclusive, validators support" if led == "undecidable" else "ledger negative, validators support")
            return ("rejected", "validators cannot tell")
        if st == "undecidable": return ("undecidable", "validators support" if m == "structurally_supported" else "validators reject")
        if m == "rejected": return ("supported", "validators reject: position not positive after cost" if q2no else "validators reject: not a sandwich attack")
        return ("supported", "validators cannot tell")
    cnt = collections.Counter(); w2sup = collections.Counter(); tot = collections.Counter(); per = {rd: collections.Counter() for rd in READERS}; split = collections.Counter()
    for (s, c), byrd in by_card().items():
        if s == "arb106" or len(byrd) < 3: continue
        tot[s] += 1; any_r = next(iter(byrd.values())); st = any_r["n2_outcome"]; led = any_r["value_flow_state"]
        for rd in READERS: per[rd][s] += byrd[rd]["verdict"] != st
        m = majority({rd: byrd[rd]["verdict"] for rd in READERS})
        if m == "split": split[s] += 1; continue
        k = key(m, st, led, sum(byrd[rd]["Q2"] == "no" for rd in READERS) >= 2)
        if k: cnt[(s, k)] += 1; w2sup[(s, k)] += any_r["w2_outcome"] == "structurally_supported"
    groups = [("rejected", "REFEREE rejected (trajectory negative)"), ("undecidable", "REFEREE inconclusive (residual token or cost unpriced)"), ("supported", "REFEREE supported")]
    L = [r"\begin{table}[!t]", r"\centering", r"\caption{Disagreements Between the Validators' Majority Verdict and REFEREE}", r"\label{tab:disagreements}", r"\footnotesize", r"\setlength\tabcolsep{4pt}",
         r"\begin{threeparttable}", r"\begin{tabular}{lrrrr}", r"\toprule",
         r"\textbf{Disagreement} & " + " & ".join(r"\textbf{%s}" % lab for _, lab in samples) + r" & \textbf{W2 supports} \\", r"\midrule"]
    for g, glab in groups:
        ks = sorted({k for (_, k) in cnt if k[0] == g}, key=lambda k: -sum(cnt[(s_, k)] for s_, _ in samples))
        if not ks: continue
        L.append(r"\multicolumn{5}{l}{\textit{%s}} \\" % glab)
        for k in ks:
            L.append(r"\quad %s & " % k[1] + " & ".join(str(cnt[(s_, k)]) if cnt[(s_, k)] else "---" for s_, _ in samples) + " & %d of %d" % (sum(w2sup[(s_, k)] for s_, _ in samples), sum(cnt[(s_, k)] for s_, _ in samples)) + r" \\")
    L.append(r"\midrule")
    L.append("All disagreements, majority verdict & " + " & ".join(str(sum(cnt[(s_, k)] for k in {k for (_, k) in cnt})) for s_, _ in samples) + " & %d of %d" % (sum(w2sup.values()), sum(cnt.values())) + r" \\")
    for rd in READERS: L.append("\\quad %s alone & " % RLAB[rd] + " & ".join(str(per[rd][s_]) for s_, _ in samples) + r" & \\")
    L.append("Cards in the sample & " + " & ".join(str(tot[s_]) for s_, _ in samples) + r" & \\")
    L += [r"\bottomrule", r"\end{tabular}", r"\begin{tablenotes}", r"\footnotesize",
          r"\item[] \emph{Note:} Disagreements under the original witness between the majority verdict of the three validators and the evidence state, grouped by the evidence state, with the number of those cards that the revised witness W2 moves to supported; %s. The three rows below the total count each validator's own disagreements. Agreements are the remainder of each sample." % ("no card is split three ways" if not sum(split.values()) else "%d cards on which the three validators return three different verdicts are excluded" % sum(split.values())),
          r"\end{tablenotes}", r"\end{threeparttable}", r"\end{table}", ""]
    tex("tab_disagreements", "\n".join(L))
    return cnt, per

def tab_rej53():
    rj = {r["card"]: r for r in rows(os.path.join(EX, "rej53_table.csv"))}
    bc = by_card(); groups = collections.defaultdict(lambda: collections.defaultdict(list))
    vmed = {}
    for (s, c), byrd in bc.items():
        if s != "rej53" or len(byrd) < 3: continue
        r = rj[c]; led = r["n2_reason"].split("ledger ")[-1]; traj = "negative" if "trajectory negative" in r["n2_reason"] else "positive"
        m = majority({rd: byrd[rd]["verdict"] for rd in READERS})
        vals = [f(byrd[rd]["validator_after_gas"]) for rd in READERS if f(byrd[rd]["validator_after_gas"]) is not None]
        vmed[c] = (f(byrd["sonnet"]["ledger_after_cost"]), statistics.median(vals) if vals else None)
        groups[(traj, led)][(STATE.get(r["w2_outcome"], r["w2_outcome"]), r["in_M"] == "True", {"structurally_supported": "support", "rejected": "reject", "undecidable": "cannot tell", "split": "split"}[m])].append(c)
    glab = {("negative", "positive"): "Trajectory negative, ledger positive", ("negative", "undecidable"): "Trajectory negative, ledger inconclusive", ("negative", "negative"): "Trajectory and ledger negative", ("positive", "negative"): "Trajectory positive, ledger negative", ("positive", "undecidable"): "Trajectory positive, ledger inconclusive"}
    L = [r"\begin{table}[!t]", r"\centering", r"\caption{The 53 Missed Attacks the Original Witness Rejects}", r"\label{tab:rej53}", r"\footnotesize", r"\setlength\tabcolsep{4pt}",
         r"\begin{threeparttable}", r"\begin{tabular}{lccrrr}", r"\toprule",
         r"\textbf{Under W2} & \textbf{mev-inspect detects} & \textbf{Validators} & \textbf{Cases} & \textbf{REFEREE (ETH)} & \textbf{Validators (ETH)} \\", r"\midrule"]
    for gk, sub_ in sorted(groups.items(), key=lambda x: -sum(len(v) for v in x[1].values())):
        L.append(r"\multicolumn{6}{l}{\textit{%s (%d)}} \\" % (glab.get(gk, "%s / %s" % gk), sum(len(v) for v in sub_.values())))
        for (w2o, inm, rd), cs in sorted(sub_.items(), key=lambda x: -len(x[1])):
            lv = [vmed[c][0] for c in cs if vmed[c][0] is not None]; pv = [vmed[c][1] for c in cs if vmed[c][1] is not None]
            L.append(r"\quad %s & %s & %s & %d & %s & %s \\" % (w2o, "yes" if inm else "no", rd, len(cs), ("%.3f" % statistics.median(lv)) if lv else "---", ("%.3f" % statistics.median(pv)) if pv else "---"))
    L += [r"\midrule", r"All & & & 53 & & \\", r"\bottomrule", r"\end{tabular}", r"\begin{tablenotes}", r"\footnotesize",
          r"\item[] \emph{Note:} Grouped by the reason for the rejection, with the state under the revised witness W2, whether mev-inspect also detects the attack, the majority verdict of the three validators, and the median profit of the group in ETH as REFEREE's ledger after observable cost and as the validators computed it after gas (the median of the three validators per card).",
          r"\end{tablenotes}", r"\end{threeparttable}", r"\end{table}", ""]
    tex("tab_rej53", "\n".join(L))

def tab_arb_top6():
    ar = sorted(rows(os.path.join(EX, "arb_top6.csv")), key=lambda r: -float(r["profit_eth"]))
    kinds = {"0x46c8": "mints cETH and issues a leveraged token", "0x184e": "ETH paid into ibETH, minted IBETH sold through LINK", "0xa28a": "flash loan returned, no cycle", "0x47b0": "flash swap returned in full", "0x04ff": "ETH paid into ibETH, minted IBETH sold", "0x48ba": "flash swap of USDC, FEI bought and returned"}
    bc = by_card()
    L = [r"\begin{table}[!t]", r"\centering", r"\caption{The Six Largest Missed Arbitrage Transactions}", r"\label{tab:arb_top6}", r"\footnotesize", r"\setlength\tabcolsep{3pt}",
         r"\begin{threeparttable}", r"\begin{tabular}{lrrccp{3.2cm}}", r"\toprule",
         r"\textbf{Transaction} & \textbf{Rule (ETH)} & \textbf{Validators (ETH)} & \textbf{Inflow} & \textbf{Arbitrage} & \textbf{What the validators saw} \\", r"\midrule"]
    q1map = {"yes": "yes", "no": "no", "cannot tell": "unclear"}
    for r in ar:
        inflow = "mint" if r["mint_in"] == "True" else ("non-pool" if r["nonpool_in"] == "True" else "pool")
        byrd = bc[("arb106", r["case_id"])]
        q1 = " / ".join(q1map.get(byrd[rd]["Q1"], byrd[rd]["Q1"]) if rd in byrd else "---" for rd in READERS)
        vals = [f(byrd[rd]["validator_after_gas"]) if rd in byrd else None for rd in READERS]
        given = [v for v in vals if v is not None]
        vp = ("%.2f" % statistics.median(given)) if given and max(given) - min(given) < 0.01 else " / ".join(("%.2f" % v) if v is not None else "---" for v in vals)
        L.append(r"\texttt{%s\ldots} & %.1f & %s & %s & %s & %s \\" % (r["hash"][:10], float(r["profit_eth"]), vp, inflow, q1, kinds.get(r["hash"][:6], "")))
    L += [r"\bottomrule", r"\end{tabular}", r"\begin{tablenotes}", r"\footnotesize",
          r"\item[] \emph{Note:} Ordered by the rule's apparent profit and read by the three validators under the arbitrage protocol; Arbitrage gives Sonnet 5.5 / Opus 5.5 / DeepSeek-V4.1-Flash. Validators (ETH) is the profit after gas as the validators computed it, one figure where the three agree within 0.01 ETH and otherwise each validator's figure in the same order; where DeepSeek-V4.1-Flash reports a figure near the rule's, its note describes a routed sale and gives the WETH received without netting the stablecoin sold. None has canonical flow. Token symbols: cETH and ibETH (written IBETH by the validators) are interest-bearing ETH tokens, LINK is the Chainlink token, USDC is USD Coin and FEI is the Fei USD stablecoin.",
          r"\end{tablenotes}", r"\end{threeparttable}", r"\end{table}", ""]
    tex("tab_arb_top6", "\n".join(L))

if __name__ == "__main__":
    a = fig_validator(); b = fig_values(); tab_samples(b); tab_disagreements(); tab_rej53(); tab_arb_top6()
    print("agreement by witness", a); print("profit", {k: (v["n"], v["within_001"], v["median"]) for k, v in b.items()})
