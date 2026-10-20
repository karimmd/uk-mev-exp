import csv, json, os, sys, math, collections
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
EX = os.path.join(ROOT, "server/revision/out/exhibits"); DG = os.path.join(ROOT, "server/revision/out/diag_20261005")
LAT = os.path.join(ROOT, "latex"); TAB = os.path.join(LAT, "tables"); os.makedirs(TAB, exist_ok=True)
SUP, REJ, UND, MUTED, ACCENT, GRID = "#1f77b4", "#d62728", "#737373", "#b8c4d6", "#1f77b4", "#e6e6e6"
PAT = {"buy_first": "#1f77b4", "sell_first": "#ff7f0e", "weth_only": "#2ca02c"}
PATLAB = {"buy_first": "buy-first (pre-specified rule)", "sell_first": "sell-first (added by S5$'$)", "weth_only": "WETH-side (added by S5$'$)"}
IN, OUT, NEAR = "reported", "missed", "comparison cases"
SETLAB = {"absent_258": "missed, pre-specified rule", "absent_new": "missed, added by S5$'$", "absent_1642": "missed, under S5$'$", "recorded": "reported", "comparison": "comparison cases"}
def rows(p):
    with open(p, newline="") as f: return list(csv.DictReader(f))
def J(p): return json.load(open(p))
def wilson(k, n, z=1.96):
    if n == 0: return (0, 0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (100 * (c - h) / d, 100 * (c + h) / d)
def tidy(ax, xgrid=True):
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_linewidth(EDGE_LW)
    ax.grid(axis="x" if xgrid else "y", color=GRID, linewidth=0.5); ax.set_axisbelow(True); ax.tick_params(length=2, width=0.5)
def save(fig, name):
    p = os.path.join(LAT, name + ".pdf"); fig.savefig(p, bbox_inches="tight"); plt.close(fig); print("wrote", p)
def tex(name, body):
    p = os.path.join(TAB, name + ".tex"); open(p, "w").write(body); print("wrote", p)
def n(x): return format(int(round(float(x))), ",")
ERA = [("pre_flashbots", "pre-Flashbots"), ("flashbots_pre_london", "Flashbots, pre-London"), ("post_london", "post-London")]
SAMPLAB = {"f1b": "sealed pack", "sym100": "added by S5$'$", "rej53": "rejected 53"}
STATE = {"structurally_supported": "supported", "rejected": "rejected", "undecidable": "inconclusive"}

COV = [("sandwich", "accepted by $\\Phi_S$", 1498, 14383, 0), ("sandwich", "pools the dataset covers", 1138, 14023, 0),
       ("sandwich", "profitable after gas\n(pre-specified rule)", 258, 11287, 1), ("sandwich", "the same, under S5$'$", 1642, 12671, 1),
       ("arbitrage", "closure-qualified", 440, 12482, 0), ("arbitrage", "profitable after gas", 255, 11068, 1),
       ("arbitrage", "canonical flow", 230, 11682, 1), ("arbitrage", "non-canonical flow", 210, 800, 0),
       ("liquidation", "liquidation event,\nsupported protocols", 0, 392, 0), ("liquidation", "accepted by $\\Phi_L$", 0, 238, 1)]
def fig_coverage():
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 2.4)); fig.subplots_adjust(wspace=1.05)
    for ax, typ, title in zip(axes, ("sandwich", "arbitrage"), ("(a) Sandwich attacks", "(b) Arbitrage")):
        rr = [r for r in COV if r[0] == typ]; y = np.arange(len(rr))[::-1]
        for yi, (_, lab, k, m, hl) in zip(y, rr):
            v = 100 * k / m; lo, hi = wilson(k, m)
            ax.barh(yi, v, height=0.62, color=ACCENT if hl else MUTED, edgecolor="none")
            ax.errorbar(v, yi, xerr=[[max(v - lo, 0)], [max(hi - v, 0)]], fmt="none", ecolor=EDGE, elinewidth=0.7, capsize=1.6, capthick=0.7)
            ax.text(hi + 0.4, yi, "%s / %s" % (n(k), n(m)), va="center", ha="left", fontsize=7.5, color="#333333")
        ax.set_yticks(y); ax.set_yticklabels([r[1] for r in rr], fontsize=8); ax.tick_params(axis="x", labelsize=7.5)
        ax.set_xlabel("missed by the existing dataset (%)", fontsize=8.5); ax.set_title(title, fontsize=9, loc="left", pad=3)
        ax.set_xlim(0, max(wilson(r[2], r[3])[1] for r in rr) * 1.5 + 0.5); tidy(ax)
    save(fig, "coverage_by_type")

ERA_DEN_SYM = {"pre_flashbots": 2631, "flashbots_pre_london": 5934, "post_london": 3376}
ERA_PRE = {"pre_flashbots": (13, 2491), "flashbots_pre_london": (120, 5082), "post_london": (125, 2984)}
MI_BY_PAT = [("buy_first", 249, 258), ("sell_first", 1011, 1022), ("weth_only", 249, 362)]
MI_IN = (10151, 10299)
def fig_misses():
    wc = rows(os.path.join(DG, "witness_rejection_cases.csv"))
    newb = {r["episode_id"]: r["pattern"] for r in rows(os.path.join(DG, "symmetric_rule_new_brackets.csv")) if r["covered"] == "True" and r["profitable"] == "True"}
    cnt = collections.Counter(); design = collections.Counter()
    for r in wc:
        if r["arm"] == "absent_258": cnt[(r["era"], "buy_first")] += 1; design[("out", r["amm_design"])] += 1
        elif r["cohort"] == "control_nearmiss" and r["episode_id"] in newb: cnt[(r["era"], newb[r["episode_id"]])] += 1; design[("out", r["amm_design"])] += 1
        elif r["arm"] == "recorded": design[("in", r["amm_design"])] += 1
    fig, axes = plt.subplots(1, 3, figsize=(7.16, 2.6), gridspec_kw={"width_ratios": [1.15, 0.9, 1.3]}); fig.subplots_adjust(wspace=0.62)
    ax = axes[0]; x = np.arange(3); w = 0.55; bottom = np.zeros(3)
    for pat in ("buy_first", "sell_first", "weth_only"):
        v = np.array([100 * cnt[(e, pat)] / ERA_DEN_SYM[e] for e, _ in ERA])
        ax.bar(x, v, w, bottom=bottom, color=PAT[pat], edgecolor="white", linewidth=0.8, label=PATLAB[pat]); bottom += v
    tot = np.array([sum(cnt[(e, p)] for p in PAT) for e, _ in ERA]); den = np.array([ERA_DEN_SYM[e] for e, _ in ERA])
    for xi, t, d, b in zip(x, tot, den, bottom):
        lo, hi = wilson(t, d); ax.errorbar(xi, b, yerr=[[max(b - lo, 0)], [max(hi - b, 0)]], fmt="none", ecolor=EDGE, elinewidth=0.7, capsize=2)
        ax.text(xi, hi + 0.5, "%.1f%%" % (100 * t / d), ha="center", va="bottom", fontsize=7.5, color="#333333")
    ax.scatter(x, [100 * ERA_PRE[e][0] / ERA_PRE[e][1] for e, _ in ERA], marker="_", s=240, color="#111111", linewidths=1.4, zorder=5)
    ax.plot([], [], color="#111111", linewidth=1.4, label="pre-specified rule alone")
    ax.set_xticks(x); ax.set_xticklabels(["pre-\nFlashbots", "Flashbots,\npre-London", "post-\nLondon"], fontsize=6.8); ax.tick_params(axis="y", labelsize=7.5); ax.set_ylabel("missed by the existing dataset (%)", fontsize=8.5); ax.set_ylim(0, 36)
    ax.set_title("(a) By era and pattern", fontsize=8.5, loc="left"); ax.legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(-0.02, 1.0), ncol=1, handlelength=1.4, labelspacing=0.3, borderaxespad=0.1); tidy(ax, xgrid=False)
    ax = axes[1]; des = [("v2_only", "V2\nonly"), ("v3_only", "V3\nonly"), ("mixed_v2_v3", "V2 and\nV3")]
    x = np.arange(3); vals = []
    for xi, (k, lab) in zip(x, des):
        o, i = design[("out", k)], design[("in", k)]; v = 100 * o / (o + i); lo, hi = wilson(o, o + i); vals.append(v)
        ax.bar(xi, v, 0.55, color=ACCENT, edgecolor="none"); ax.errorbar(xi, v, yerr=[[max(v - lo, 0)], [max(hi - v, 0)]], fmt="none", ecolor=EDGE, elinewidth=0.7, capsize=2)
        ax.text(xi, hi + 0.5, "%s /\n%s" % (n(o), n(o + i)), ha="center", va="bottom", fontsize=7, color="#333333")
    ax.set_xticks(x); ax.set_xticklabels([l for _, l in des], fontsize=7.2); ax.tick_params(axis="y", labelsize=7.5); ax.set_ylabel("missed by the existing dataset (%)", fontsize=8.5); ax.set_ylim(0, 40); ax.set_xlim(-0.6, 2.6)
    ax.set_title("(b) By pool design (S5$'$)", fontsize=8.5, loc="left"); tidy(ax, xgrid=False)
    ax = axes[2]; items = [("reported", MI_IN[0], MI_IN[1], MUTED), ("missed\nbuy-\nfirst", 249, 258, PAT["buy_first"]), ("missed\nsell-\nfirst", 1011, 1022, PAT["sell_first"]), ("missed\nWETH-\nside", 249, 362, PAT["weth_only"])]
    x = np.arange(len(items))
    for xi, (lab, k, m, col) in zip(x, items):
        v = 100 * k / m; lo, hi = wilson(k, m); ax.bar(xi, v, 0.55, color=col, edgecolor="none")
        ax.errorbar(xi, v, yerr=[[max(v - lo, 0)], [max(hi - v, 0)]], fmt="none", ecolor=EDGE, elinewidth=0.7, capsize=2); ax.text(xi, hi + 1.5, "%s /\n%s" % (n(k), n(m)), ha="center", va="bottom", fontsize=7, color="#333333")
    ax.set_xticks(x); ax.set_xticklabels([i[0] for i in items], fontsize=6.4); ax.tick_params(axis="y", labelsize=7.5); ax.set_ylabel("also detected by mev-inspect (%)", fontsize=8.5); ax.set_ylim(0, 132); ax.set_yticks([0, 25, 50, 75, 100]); ax.set_xlim(-0.6, 3.6)
    ax.set_title("(c) mev-inspect agreement", fontsize=8.5, loc="left"); tidy(ax, xgrid=False)
    save(fig, "misses_by_era_design_detector")
    return {"era_pattern": {"%s|%s" % k: v for k, v in cnt.items()}, "design": {"%s|%s" % k: v for k, v in design.items()}}

def fig_outcomes():
    r = rows(os.path.join(HERE, "data", "outcomes_by_arm_referee.csv"))
    lab = {"Recorded": "reported", "Record-absent (pre-specified)": "missed,\npre-specified rule", "Record-absent (symmetric)": "missed,\nunder S5$'$", "Comparison": "comparison cases"}
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 2.1), sharey=True); fig.subplots_adjust(wspace=0.12)
    sizes = {}
    for x in r: sizes.setdefault(x["arm"], set()).add(x["n"])
    assert all(len(v) == 1 for v in sizes.values()), sizes
    for ax, w, title in zip(axes, ("N2 (registered)", "W2 (revised)"), ("(a) Original witness", "(b) Revised witness (W2)")):
        rr = [x for x in r if x["witness"] == w]; y = np.arange(len(rr))[::-1]
        for yi, x in zip(y, rr):
            m = int(x["n"]); parts = [(int(x["supported"]), SUP, ""), (int(x["rejected"]), REJ, ""), (int(x["undecidable"]), UND, "////")]; left = 0.0
            for k, col, hatch in parts:
                v = 100 * k / m; ax.barh(yi, v, left=left, height=0.62, color=col, edgecolor="white", linewidth=0.9, hatch=hatch)
                if v >= 9 and hatch == "": ax.text(left + v / 2, yi, "%.1f" % v, va="center", ha="center", fontsize=8 if v >= 15 else 7, color="white")
                elif v >= 6: ax.text(left + v / 2, yi, "%.1f" % v, va="center", ha="center", fontsize=6.5, color="#111111", bbox=dict(boxstyle="square,pad=0.06", facecolor="white", edgecolor="none"))
                left += v
        ax.set_yticks(y); ax.set_yticklabels(["%s\n(n = %s)" % (lab.get(x["arm"], x["arm"]), n(x["n"])) for x in rr], fontsize=7.5); ax.set_xlim(0, 100); ax.set_xticks([0, 25, 50, 75, 100]); ax.tick_params(axis="x", labelsize=7.5)
        ax.set_xlabel("share of attacks (%)", fontsize=8.5); ax.set_title(title, fontsize=9, loc="left", pad=3); tidy(ax)
    h = [plt.Rectangle((0, 0), 1, 1, color=SUP), plt.Rectangle((0, 0), 1, 1, color=REJ), plt.Rectangle((0, 0), 1, 1, facecolor=UND, hatch="////", edgecolor="white")]
    fig.legend(h, ["supported", "rejected", "inconclusive"], loc="lower center", bbox_to_anchor=(0.56, -0.13), ncol=3, fontsize=7.5, frameon=False, handlelength=1.2, columnspacing=1.2)
    save(fig, "outcomes_by_set")

def fig_reversal():
    rm = rows(os.path.join(EX, "reversal_metrics.csv"))
    def f(v):
        try: return float(v)
        except: return None
    pos = [f(r["reversal_fraction"]) for r in rm if r["traj_w2"] == "positive" and f(r["reversal_fraction"]) is not None]
    neg = [f(r["reversal_fraction"]) for r in rm if r["traj_w2"] == "negative" and f(r["reversal_fraction"]) is not None]
    defect = lambda r: r["traj_frozen"] == "negative" and r["traj_w2"] == "positive"
    eps = [f(r["opening_move_rel"]) for r in rm if defect(r) and f(r["opening_move_rel"]) not in (None, 0)]
    oth = [f(r["opening_move_rel"]) for r in rm if not defect(r) and f(r["opening_move_rel"]) not in (None, 0)]
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 2.4)); fig.subplots_adjust(wspace=0.3)
    ax = axes[0]; bins = np.linspace(-0.5, 2.5, 61)
    ax.hist(np.clip(pos, -0.5, 2.5), bins=bins, weights=100 * np.ones(len(pos)) / len(pos), color=SUP, alpha=0.85, label="witness positive (n = %s)" % n(len(pos)))
    ax.hist(np.clip(neg, -0.5, 2.5), bins=bins, weights=100 * np.ones(len(neg)) / len(neg), color=REJ, alpha=0.65, label="witness negative (n = %s)" % n(len(neg)))
    ax.axvline(0.10, color="#111111", linewidth=0.8, linestyle="--"); ax.text(0.14, ax.get_ylim()[1] * 0.55, r"$\eta = 0.10$", fontsize=7.5)
    ax.set_xlabel("reversal fraction (T4) under W2, clipped to [$-$0.5, 2.5]", fontsize=8.5); ax.set_ylabel("share of attacks (%)", fontsize=8.5); ax.tick_params(labelsize=7.5); ax.set_title("(a) Closing reversal by verdict", fontsize=9, loc="left"); ax.legend(fontsize=7.5, frameon=False, loc="upper right"); tidy(ax, xgrid=False)
    ax = axes[1]; lb = np.logspace(-5, 0, 51)
    ax.hist(oth, bins=lb, weights=100 * np.ones(len(oth)) / len(oth), color=MUTED, label="other attacks\n(n = %s)" % n(len(oth)))
    ax.hist(eps, bins=lb, weights=100 * np.ones(len(eps)) / len(eps), color=REJ, alpha=0.8, label="read as no move by\nthe original witness\n(n = %s)" % n(len(eps)))
    ax.set_xscale("log"); ax.set_xlabel("relative price move of the front-run (T3)", fontsize=8.5); ax.set_ylabel("share of attacks (%)", fontsize=8.5); ax.tick_params(labelsize=7.5)
    ax.set_title("(b) The absolute-floor defect", fontsize=9, loc="left"); ax.legend(fontsize=7.5, frameon=False, loc="upper left"); tidy(ax, xgrid=False)
    save(fig, "trajectory_metrics")
    return dict(pos=len(pos), neg=len(neg), eps=len(eps), eps_median=float(np.median(eps)), eps_p10=float(np.percentile(eps, 10)), eps_p90=float(np.percentile(eps, 90)))

def fig_arb_index():
    ar = rows(os.path.join(EX, "arb_tx_index.csv")); con = [r for r in ar if r["contested"] == "True"]
    ab = np.array([int(r["tx_index"]) for r in con if r["in_records"] != "True"]); rc = np.array([int(r["tx_index"]) for r in con if r["in_records"] == "True"])
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 2.4)); fig.subplots_adjust(wspace=0.3)
    ax = axes[0]
    for v, col, lab in ((rc, MUTED, "reported (n = %s)" % n(len(rc))), (ab, ACCENT, "missed (n = %s)" % n(len(ab)))):
        xs = np.sort(v); ax.step(xs, 100 * np.arange(1, len(xs) + 1) / len(xs), where="post", color=col, linewidth=1.3, label=lab)
    ax.set_xscale("symlog", linthresh=10); ax.set_xlabel("index of the transaction in its block", fontsize=8.5); ax.set_ylabel("cumulative share (%)", fontsize=8.5); ax.tick_params(labelsize=7.5)
    ax.set_title("(a) Block index of contested arbitrage", fontsize=9, loc="left"); ax.legend(fontsize=7.5, frameon=False, loc="lower right"); tidy(ax, xgrid=False)
    ax.text(0.02, 0.95, "median %d against %d" % (np.median(ab), np.median(rc)), transform=ax.transAxes, fontsize=7.5, va="top")
    ax = axes[1]; x = np.arange(3); w = 0.36; out = {}
    for j, (key, col, lab) in enumerate((("recorded", MUTED, "reported"), ("absent", ACCENT, "missed"))):
        v = []; cnts = []
        for e, _ in ERA:
            s = [r for r in con if r["era"] == e and ((r["in_records"] == "True") == (key == "recorded"))]
            k = sum(1 for r in s if r["first_conjunctive"] == "True"); v.append(100 * k / len(s) if s else 0); cnts.append((k, len(s)))
        out[key] = cnts; ax.bar(x + (j - 0.5) * (w + 0.04), v, w, color=col, edgecolor="none", label=lab)
        for xi, vi, (k, m) in zip(x + (j - 0.5) * (w + 0.04), v, cnts): ax.text(xi, vi + 1, "%.0f%%\n%d/%d" % (vi, k, m), ha="center", va="bottom", fontsize=7.2, color="#333333")
    ax.set_xticks(x); ax.set_xticklabels(["pre-\nFlashbots", "Flashbots,\npre-London", "post-\nLondon"], fontsize=7.5); ax.tick_params(axis="y", labelsize=7.5); ax.set_ylabel("first on every pool used (%)", fontsize=8.5); ax.set_ylim(0, 95)
    ax.set_title("(b) First on every pool, by era", fontsize=9, loc="left"); ax.legend(fontsize=7.5, frameon=False, loc="upper right"); tidy(ax, xgrid=False)
    save(fig, "arbitrage_position")
    return dict(median_absent=float(np.median(ab)), median_recorded=float(np.median(rc)), n_absent=len(ab), n_recorded=len(rc), by_era=out)

def fig_victim_actor():
    vl = rows(os.path.join(EX, "victim_loss_states.csv"))
    def lam(r):
        try: return float(r["victim_loss_frac"])
        except: return None
    sets = (("absent_258", "missed, pre-specified rule", ACCENT, "-", 1.2), ("absent_new", "missed, added by S5$'$", "#ff7f0e", "-", 1.2), ("recorded", "reported", MUTED, "-", 1.2), ("comparison", "comparison cases", "#111111", ":", 0.8))
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 2.5)); fig.subplots_adjust(wspace=0.3)
    ax = axes[0];
    above = min(lam(r) for r in vl if r["exceeds_T"] == "True" and lam(r) is not None); below = max(lam(r) for r in vl if r["exceeds_T"] == "False" and lam(r) is not None)
    assert below < 0.14821 <= above, (below, above); T = 0.14821
    for key, lab, col, ls, lw in sets:
        v = np.array([lam(r) for r in vl if r["arm"] == key and lam(r) is not None]); xs = np.sort(v)
        ax.step(xs, 100 * np.arange(1, len(xs) + 1) / len(xs), where="post", color=col, linewidth=lw, linestyle=ls, label="%s (n = %s)" % (lab, n(len(v))))
    ax.axvline(T, color="#111111", linewidth=0.7, linestyle="--"); ax.text(T * 1.1, 8, "$T$ = %.3f" % T, fontsize=7.5)
    ax.set_xscale("log"); ax.set_xlim(1e-4, 1.2); ax.set_xlabel(r"victim loss fraction $\lambda$ (replay-eligible attacks)", fontsize=8.5); ax.set_ylabel("cumulative share (%)", fontsize=8.5); ax.tick_params(labelsize=7.5)
    ax.set_title(r"(a) Distribution of $\lambda$", fontsize=9, loc="left"); ax.legend(fontsize=6.8, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.3), ncol=2, handlelength=1.3, columnspacing=0.8); tidy(ax, xgrid=False)
    ax = axes[1]; groups = [("absent_258", False), ("absent_258", True), ("absent_new", False), ("absent_new", True), ("recorded", False), ("recorded", True)]
    labels = ["missed,\npre-spec.\n$\\lambda < T$", "missed,\npre-spec.\n$\\lambda \\geq T$", "missed,\nadded\n$\\lambda < T$", "missed,\nadded\n$\\lambda \\geq T$", "reported\n$\\lambda < T$", "reported\n$\\lambda \\geq T$"]
    x = np.arange(len(groups)); out = {}
    for xi, (key, hi) in zip(x, groups):
        s = [r for r in vl if r["arm"] == key and (r["exceeds_T"] == "True") == hi]; m = len(s) or 1
        parts = [(sum(1 for r in s if r["w2_outcome"] == "structurally_supported"), SUP, ""), (sum(1 for r in s if r["w2_outcome"] == "rejected"), REJ, ""), (sum(1 for r in s if r["w2_outcome"] == "undecidable"), UND, "////")]
        out[(key, hi)] = (len(s), parts[0][0], parts[1][0], parts[2][0]); left = 0
        for k, col, h in parts:
            v = 100 * k / m; ax.bar(xi, v, 0.62, bottom=left, color=col, edgecolor="white", linewidth=0.8, hatch=h)
            if v >= 12: ax.text(xi, left + v / 2, "%d" % k, ha="center", va="center", fontsize=7.2, color="white" if h == "" else "#111111", bbox=None if h == "" else dict(boxstyle="square,pad=0.1", facecolor="white", edgecolor="none"))
            left += v
        ax.text(xi, 102, "n = %d" % len(s), ha="center", va="bottom", fontsize=7)
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=6.2); ax.tick_params(axis="y", labelsize=7.5); ax.set_ylabel("share of attacks (%)", fontsize=8.5); ax.set_ylim(0, 115); ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_title("(b) Actor-side state (W2) by victim loss", fontsize=9, loc="left"); tidy(ax, xgrid=False)
    h = [plt.Rectangle((0, 0), 1, 1, color=SUP), plt.Rectangle((0, 0), 1, 1, color=REJ), plt.Rectangle((0, 0), 1, 1, facecolor=UND, hatch="////", edgecolor="white")]
    ax.legend(h, ["supported", "rejected", "inconclusive"], fontsize=7.2, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.36), ncol=3)
    save(fig, "victim_actor")
    return dict(T=T, groups={"%s_%s" % k: v for k, v in out.items()})

def fig_llm():
    cards = rows(os.path.join(EX, "explorer_cards.csv"))
    fig, axes = plt.subplots(1, 3, figsize=(7.16, 2.4)); fig.subplots_adjust(wspace=0.5)
    ax = axes[0]; st = ["structurally_supported", "undecidable", "rejected"]; M = np.zeros((3, 3))
    for r in cards:
        if r["sample"] == "f1b": M[st.index(r["n2_outcome"]), st.index(r["reader"])] += 1
    ax.imshow(M, cmap="Blues", vmin=0, vmax=M.max() * 1.15, aspect="auto")
    for i in range(3):
        for j in range(3): ax.text(j, i, "%d" % M[i, j], ha="center", va="center", fontsize=8.5, color="white" if M[i, j] > M.max() * 0.55 else "#111111")
    ax.grid(False); ax.set_xticks(range(3)); ax.set_xticklabels(["supported", "cannot\ntell", "rejected"], fontsize=7); ax.set_yticks(range(3)); ax.set_yticklabels(["supported", "inconclusive", "rejected"], fontsize=7)
    ax.set_xlabel("LLM validator", fontsize=7.5); ax.set_ylabel("REFEREE, original witness", fontsize=7.5); ax.set_title("(a) Sealed pack, 200 cards", fontsize=8, loc="left")
    for s_ in ("top", "right", "left", "bottom"): ax.spines[s_].set_visible(False)
    ax.tick_params(length=0)
    ax = axes[1]; samples = ["f1b", "sym100", "rej53"]; x = np.arange(3); w = 0.6; bottom = np.zeros(3); cols = {"2": "#c6dbef", "3": "#9ecae1", "4": "#4292c6", "5": "#08519c"}
    for lvl in ("2", "3", "4", "5"):
        v = np.array([100 * sum(1 for r in cards if r["sample"] == s and r["confidence"] == lvl) / sum(1 for r in cards if r["sample"] == s) for s in samples])
        ax.bar(x, v, w, bottom=bottom, color=cols[lvl], edgecolor="white", linewidth=0.8, label="confidence %s" % lvl)
        for xi, vi, b in zip(x, v, bottom):
            if vi >= 8: ax.text(xi, b + vi / 2, "%.0f" % vi, ha="center", va="center", fontsize=7, color="white" if lvl in ("4", "5") else "#111111")
        bottom += v
    ax.set_xticks(x); ax.set_xticklabels(["sealed\npack\n(n = 200)", "added\nby S5$'$\n(n = 100)", "rejected\n53\n(n = 53)"], fontsize=6.8); ax.set_ylabel("share of cards (%)", fontsize=7.5); ax.set_ylim(0, 100)
    ax.set_title("(b) Self-reported confidence", fontsize=8, loc="left"); ax.legend(fontsize=6.3, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.36), ncol=2, handlelength=1.0); tidy(ax, xgrid=False)
    ax = axes[2]; lv = ["3", "4", "5"]; x = np.arange(3); w = 0.36; out = {}
    for j, (key, col, lab) in enumerate((("n2_outcome", MUTED, "original witness"), ("w2_outcome", ACCENT, "revised witness (W2)"))):
        v = []; cnts = []
        for l in lv:
            s = [r for r in cards if r["confidence"] == l and r[key]]; k = sum(1 for r in s if r[key] == r["reader"]); v.append(100 * k / len(s) if s else 0); cnts.append((k, len(s)))
        out[key] = cnts; ax.bar(x + (j - 0.5) * (w + 0.04), v, w, color=col, edgecolor="none", label=lab)
        for xi, vi, (k, m) in zip(x + (j - 0.5) * (w + 0.04), v, cnts): ax.text(xi, vi + 1, "%d/\n%d" % (k, m), ha="center", va="bottom", fontsize=6.2, color="#333333")
    ax.set_xticks(x); ax.set_xticklabels(["conf. 3", "conf. 4", "conf. 5"], fontsize=7); ax.set_ylabel("agreement with REFEREE (%)", fontsize=7.5); ax.set_ylim(0, 110); ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_title("(c) Agreement by confidence, 353 cards", fontsize=8, loc="left"); ax.legend(fontsize=6.5, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=1); tidy(ax, xgrid=False)
    save(fig, "llm_validator")
    return dict(matrix=M.tolist(), agreement_by_conf=out)


def fig_values():
    vv = rows(os.path.join(HERE, "data", "validator_values.csv"))
    def f(v):
        try: return float(v)
        except: return None
    pts = [(f(r["ledger_after_cost"]), f(r["validator_after_gas"]), r["n2_outcome"], r["sample"]) for r in vv]
    pts = [p for p in pts if p[0] is not None and p[1] is not None]
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 2.4), gridspec_kw={"width_ratios": [1.0, 1.0]}); fig.subplots_adjust(wspace=0.35)
    ax = axes[0]; cols = {"structurally_supported": SUP, "rejected": REJ, "undecidable": UND}; labs = {"structurally_supported": "supported", "rejected": "rejected", "undecidable": "inconclusive"}
    for st in ("structurally_supported", "undecidable", "rejected"):
        xs = [p[0] for p in pts if p[2] == st]; ys = [p[1] for p in pts if p[2] == st]
        ax.scatter(xs, ys, s=11, color=cols[st], alpha=0.75, edgecolors="none", label="%s (n = %d)" % (labs[st], len(xs)))
    lim = (-0.3, 6); ax.plot(lim, lim, color="#111111", linewidth=0.6, linestyle="--"); ax.set_xscale("symlog", linthresh=0.01); ax.set_yscale("symlog", linthresh=0.01); ax.set_xlim(lim); ax.set_ylim(lim)
    ax.set_xlabel("REFEREE ledger after observable cost (ETH)", fontsize=7.5); ax.set_ylabel("LLM validator profit after gas (ETH)", fontsize=7.5)
    ax.set_title("(a) Profit per card, 323 cards with both values", fontsize=8, loc="left"); ax.legend(fontsize=6.5, frameon=False, loc="upper left", title="REFEREE state", title_fontsize=6.5, alignment="left", handletextpad=0.2); tidy(ax, xgrid=False)
    ax = axes[1]; d = np.array([abs(p[0] - p[1]) for p in pts]); edges = [0, 0.001, 0.01, 0.1, 1.0, 100]; labels = ["< 0.001", "0.001\nto 0.01", "0.01\nto 0.1", "0.1\nto 1", "> 1"]
    cnts = [int(((d >= lo) & (d < hi)).sum()) for lo, hi in zip(edges[:-1], edges[1:])]
    ax.bar(np.arange(5), [100 * c / len(d) for c in cnts], 0.6, color=ACCENT, edgecolor="none")
    for xi, c in enumerate(cnts): ax.text(xi, 100 * c / len(d) + 1.5, "%d" % c, ha="center", va="bottom", fontsize=7, color="#333333")
    ax.set_xticks(np.arange(5)); ax.set_xticklabels(labels, fontsize=7); ax.set_xlabel("absolute difference, validator against ledger (ETH)", fontsize=7.5); ax.set_ylabel("share of cards (%)", fontsize=7.5); ax.set_ylim(0, 100)
    ax.set_title("(b) Agreement on the profit figure", fontsize=8, loc="left"); tidy(ax, xgrid=False)
    save(fig, "validator_values")
    within = {smp: (sum(1 for p in pts if p[3] == smp and abs(p[0] - p[1]) < 0.01), sum(1 for p in pts if p[3] == smp)) for smp in ("f1b", "sym100", "rej53")}
    return dict(n=len(pts), bins=dict(zip(labels, cnts)), median_abs=float(np.median(d)), within_001=within)

def tab_populations():
    body = r"""\begin{table}[!t]
\centering
\caption{Populations. Sandwich counts are attacks on the replication sweep after each successive filter; arbitrage and liquidation counts are transactions. "Reported" means every transaction of the attack is in the existing public MEV dataset~\cite{aflashbotinthepan}, "missed" means none is, "partially" means one or two of its transactions are. Every count is a sampled count on the 1-in-88 block lattice.}
\label{tab:populations}
\footnotesize
\setlength\tabcolsep{4pt}
\begin{tabular}{llrrrr}
\toprule
\textbf{Type} & \textbf{Successive filter} & \textbf{Count} & \textbf{Reported} & \textbf{Missed} & \textbf{Partially reported} \\
\midrule
Sandwich & accepted by $\Phi_S$ & 14{,}383 & & 1{,}498 & \\
 & on DEX pools the dataset covers & 14{,}023 & & 1{,}138 & \\
 & profitable after gas, pre-specified rule & 11{,}287 & 10{,}299 & 258 & 730 \\
 & the same population under S5$'$ & 12{,}671 & 10{,}299 & 1{,}642 & 730 \\
 & comparison cases (fail only S5) & 7{,}080 & & & \\
\midrule
Arbitrage & closure-qualified (A1 to A4) & 12{,}482 & 12{,}042 & 440 & \\
 & profitable after observable gas & 11{,}068 & 10{,}813 & 255 & \\
 & canonical flow & 11{,}682 & 11{,}452 & 230 & \\
 & contested (another transaction shares a pool) & 8{,}166 & 7{,}994 & 172 & \\
\midrule
Liquidation & liquidation event, supported protocols & 392 & 392 & 0 & \\
 & accepted by $\Phi_L$ & 238 & 238 & 0 & \\
\bottomrule
\end{tabular}
\\[2pt]\footnotesize The 17{,}637 adjudicated sandwich attacks are the 258 missed, the 10{,}299 reported and the 7{,}080 comparison cases. Canonical flow (11{,}682) and non-canonical flow (800) partition the closure-qualified arbitrage population.
\end{table}
"""
    tex("tab_populations", body)

def tab_contrast():
    c2 = J(os.path.join(DG, "symmetric_arm_contrast.json")); cw = J(os.path.join(DG, "symmetric_arm_contrast_w2.json"))
    keys = [("original_258", "pre-specified rule (258)"), ("new_1384_only", "added by S5$'$ (1{,}384)"), ("symmetric_1642", "under S5$'$ (1{,}642)")]
    L = [r"\begin{table}[!t]", r"\centering",
         r"\caption{Support for the missed sandwich attacks against the 10{,}299 reported ones, of which 85.2\% are supported under the original witness (8{,}772) and 87.8\% under the revised witness W2 (9{,}045). The difference in support share carries a 95\% confidence interval (Newcombe method); the adjusted difference is directly standardized over the 21 pre-specified strata (era, pool design, pool count, route complexity, zero gas price) with its 95\% permutation band and $p$ from 20{,}000 within-stratum relabelings. Percentage points.}",
         r"\label{tab:contrast}", r"\footnotesize", r"\setlength\tabcolsep{2.6pt}", r"\begin{tabular}{llrrrr}", r"\toprule",
         r"\textbf{Missed attacks} & \textbf{Witness} & \textbf{Supported} & \textbf{Difference [95\% CI]} & \textbf{Adjusted [perm.\ band]} & $p$ \\", r"\midrule"]
    R = [r"\begin{table}[!t]", r"\centering", r"\caption{Robustness of the adjusted difference of the manuscript's contrast table: 95\% bootstrap intervals resampling blocks and resampling economic actors, and the range over leaving one stratum out. Percentage points.}", r"\label{tab:contrast_robustness}", r"\footnotesize", r"\setlength\tabcolsep{5pt}", r"\begin{tabular}{llrrr}", r"\toprule", r"\textbf{Missed attacks} & \textbf{Witness} & \textbf{Resampling blocks} & \textbf{Resampling actors} & \textbf{Leave one stratum out} \\", r"\midrule"]
    for k, lab in keys:
        for wname, d in (("original", c2[k]), ("revised", cw[k])):
            L.append(r"%s & %s & %.1f\%% (%s/%s) & $%+.1f$ [%+.1f, %+.1f] & $%+.1f$ [%+.1f, %+.1f] & %s \\" % (
                lab if wname == "original" else "", wname, 100 * d["sup_missed"] / d["n_missed"], n(d["sup_missed"]), n(d["n_missed"]),
                d["unadj_pp"], d["newcombe"][0], d["newcombe"][1], d["standardized_pp"], d["perm_band"][0], d["perm_band"][1], ("%.4f" % d["perm_p"]) if d["perm_p"] >= 0.0001 else "$<$0.0001"))
            R.append(r"%s & %s & [%+.1f, %+.1f] & [%+.1f, %+.1f] & [%+.1f, %+.1f] \\" % (lab if wname == "original" else "", wname, d["block_boot"][0], d["block_boot"][1], d["actor_boot"][0], d["actor_boot"][1], d["loo_range"][0], d["loo_range"][1]))
        L.append(r"\addlinespace[2pt]"); R.append(r"\addlinespace[2pt]")
    L += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]; R += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex("tab_contrast", "\n".join(L)); tex("tab_contrast_robustness", "\n".join(R))

def tab_mechanism():
    m = {r["arm"]: r for r in rows(os.path.join(EX, "mechanism_by_arm.csv"))}; a, r = m["absent_258"], m["recorded"]
    def cell(d, k): return "%s (%s\\%%)" % (n(d[k]), d[k + "_pct"]) if d.get(k) not in (None, "") else "---"
    L = [r"\begin{table}[!t]", r"\centering",
         r"\caption{Why a sandwich attack was missed: linkage properties of the 258 missed attacks under the pre-specified rule against the 10{,}299 reported ones. A two-pool leg routes the front-run or the back-run through a second pool; an amount mismatch is a front and back token amount that differ by more than 1\%; a routed attack reaches the shared pool through an intermediate token. Counts with the share of the set.}",
         r"\label{tab:mechanism}", r"\footnotesize", r"\setlength\tabcolsep{5pt}", r"\begin{tabular}{lrr}", r"\toprule",
         r"\textbf{Property of the attack} & \textbf{Missed (258)} & \textbf{Reported (10{,}299)} \\", r"\midrule",
         r"Two-pool front-run or back-run & %s & %s \\" % (cell(a, "two_pool_leg"), cell(r, "two_pool_leg")),
         r"Front and back amounts differ by more than 1\%% & %s & %s \\" % (cell(a, "amount_mismatch"), cell(r, "amount_mismatch")),
         r"Either of the two & %s & %s \\" % (cell(a, "either"), cell(r, "either")),
         r"Routed through an intermediate token & %s & %s \\" % (cell(a, "routed"), cell(r, "routed")),
         r"Victim adjacent to both legs & %s & %s \\" % (cell(a, "victim_adjacent"), cell(r, "victim_adjacent")),
         r"Front-run and back-run sent by the same address & %s & %s \\" % (cell(a, "same_sender"), cell(r, "same_sender")),
         r"Economic actor is the sender of the front-run & %s & %s \\" % (cell(a, "actor_is_sender_F"), cell(r, "actor_is_sender_F")),
         r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex("tab_mechanism", "\n".join(L))

def tab_magnitudes():
    m2 = J(os.path.join(DG, "symmetric_arm_magnitudes.json")); mw = J(os.path.join(DG, "symmetric_arm_magnitudes_w2.json"))
    L = [r"\begin{table}[!t]", r"\centering",
         r"\caption{Economic magnitudes by set. Attacker profit is the signed ledger over supported attacks; victim loss is the replay-eligible subset priced at the pool's own post-victim reserves, with honeypot-style cases ($\lambda \geq 0.9$ or a single loss above 50 ETH) excluded from totals. Per 1{,}000 blocks divides the 50{,}000-block sweep total by 50.}",
         r"\label{tab:magnitudes}", r"\footnotesize", r"\setlength\tabcolsep{3.5pt}", r"\begin{tabular}{lp{3.9cm}rrrrr}", r"\toprule",
         r"\textbf{Quantity} & \textbf{Set of attacks} & \textbf{Cases} & \textbf{Total ETH} & \textbf{Median} & \textbf{p90} & \textbf{Per 1{,}000 bl.} \\", r"\midrule"]
    sets = [("absent_258", SETLAB["absent_258"]), ("absent_new_all", SETLAB["absent_new"]), ("absent_1642", SETLAB["absent_1642"]), ("recorded", SETLAB["recorded"])]
    for wname, m in (("original witness", m2), ("revised witness (W2)", mw)):
        L.append(r"\multicolumn{7}{l}{\textit{Attacker profit, supported attacks, %s}} \\" % wname)
        for k, lab in sets:
            d = m[k]; L.append(r" & %s & %s & %.2f & %.3f & %.3f & %.2f \\" % (lab, n(d["n"]), d["total_eth"], d["median"], d["p90"], d["per_1000_blocks"]))
    L.append(r"\midrule"); L.append(r"\multicolumn{7}{l}{\textit{Victim loss, replay-eligible and priced, after the honeypot exclusion}} \\")
    for k, lab in (("victim_loss_absent_258", SETLAB["absent_258"]), ("victim_loss_absent_new", SETLAB["absent_new"]), ("victim_loss_absent_1642", SETLAB["absent_1642"]), ("victim_loss_recorded", SETLAB["recorded"])):
        d = m2[k]; L.append(r" & %s & %s of %s & %.2f & %.3f & --- & %.2f \\" % (lab, n(d["kept"]), n(d["n"]), d["total_eth"], d["median"], d["per_1000_blocks"]))
    L += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex("tab_magnitudes", "\n".join(L))

def tab_arb_twoway():
    cc = J(os.path.join(DG, "arbitrage_cross_check.json")); mo = J(os.path.join(DG, "arbitrage_m_only_breakdown.json"))
    def c(k): a, b = cc[k]; return "%s / %s (%.1f\\%%)" % (n(a), n(b), 100 * a / b)
    fp = cc["first_position_within_M_called_canonical_contested"]
    L = [r"\begin{table}[!t]", r"\centering",
         r"\caption{Arbitrage on the same 50{,}000 blocks: REFEREE's rule against mev-inspect. Upper part: of the transactions the rule accepts, reported or missed by the existing dataset, the number mev-inspect also detects over all (with the share), by flow class, and the first-on-every-pool share among contested transactions both detect. Lower part: the 18{,}108 decodable transactions mev-inspect detects and the rule does not, by the conjunct they fail.}",
         r"\label{tab:arb_twoway}", r"\footnotesize", r"\setlength\tabcolsep{4pt}", r"\begin{tabular}{p{6.4cm}rr}", r"\toprule",
         r"\textbf{Accepted by REFEREE's rule} & \textbf{Reported} & \textbf{Missed} \\", r"\midrule",
         r"Closure-qualified (A1 to A4) & %s & %s \\" % (c("P2_recorded_in_M"), c("P2_absent_in_M")),
         r"\quad canonical flow & %s & %s \\" % (c("P2_canonical_recorded_in_M"), c("P2_canonical_absent_in_M")),
         r"\quad non-canonical flow & %s & %s \\" % (c("P2_noncanonical_recorded_in_M"), c("P2_noncanonical_absent_in_M")),
         r"Profitable after observable gas & %s & %s \\" % (c("P4_recorded_in_M"), c("P4_absent_in_M")),
         r"First on every pool, contested, detected by both & %s / %s (%.1f\%%) & %s / %s (%.1f\%%) \\" % (n(fp["recorded"][0]), n(fp["recorded"][1]), 100 * fp["recorded"][0] / fp["recorded"][1], n(fp["absent"][0]), n(fp["absent"][1]), 100 * fp["absent"][0] / fp["absent"][1]),
         r"\midrule", r"\textbf{Detected by mev-inspect only (%s decodable of %s)} & \textbf{Count} & \textbf{Share} \\" % (n(mo["in_store"]), n(mo["M_only"]))]
    v = mo["verdicts"]; tot = sum(v.values())
    names = {"fail:cyclic": "fails A2 (closure) only", "fail:multi_venue,cyclic": "fails A1 and A2", "fail:single_profit_asset": "fails A3 (single profit asset) only", "fail:multi_venue,single_profit_asset": "fails A1 and A3", "fail:cyclic,single_profit_asset": "fails A2 and A3", "fail:multi_venue": "fails A1 only", "fail:multi_venue,cyclic,single_profit_asset": "fails A1, A2 and A3"}
    for k, cnt in sorted(v.items(), key=lambda x: -x[1]): L.append(r"%s & %s & %.1f\%% \\" % (names[k], n(cnt), 100 * cnt / tot))
    L.append(r"\quad of those failing A2: cyclic at $\theta = 0.10$ & %s & %.1f\%% of %s \\" % (n(mo["loose_tolerance"]["cyclic at 10%"]), 100 * mo["loose_tolerance"]["cyclic at 10%"] / (mo["loose_tolerance"]["cyclic at 10%"] + mo["loose_tolerance"]["still not cyclic at 10%"]), n(mo["loose_tolerance"]["cyclic at 10%"] + mo["loose_tolerance"]["still not cyclic at 10%"])))
    L += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex("tab_arb_twoway", "\n".join(L))

def tab_eligibility():
    el = rows(os.path.join(EX, "eligibility_by_arm.csv"))
    cls = {"licensed": "Replay-eligible", "intervening_shared_pool_swap": "Intervening swap on the shared pool", "undecidable_mixed_v2_v3": "Concentrated-liquidity or mixed path", "undecidable_v3_only": "Concentrated-liquidity or mixed path",
           "multiple_or_zero_swaps_on_pool_in_back": "Degenerate swap count on the pool", "multiple_or_zero_swaps_on_pool_in_victim": "Degenerate swap count on the pool", "multiple_or_zero_swaps_on_pool_in_front": "Degenerate swap count on the pool",
           "oracle_ambiguous_shared_pool_2": "Ambiguous shared pool", "oracle_ambiguous_shared_pool_3": "Ambiguous shared pool", "oracle_ambiguous_shared_pool_4": "Ambiguous shared pool"}
    sets = [("absent_258", "Missed, pre-spec."), ("absent_new", "Missed, added"), ("recorded", "Reported"), ("comparison", "Comparison")]
    cnt = collections.Counter(); tot = collections.Counter()
    for r in el: cnt[(r["arm"], cls[r["license_reason"]])] += int(r["n"]); tot[r["arm"]] += int(r["n"])
    order = ["Replay-eligible", "Concentrated-liquidity or mixed path", "Intervening swap on the shared pool", "Degenerate swap count on the pool", "Ambiguous shared pool"]
    L = [r"\begin{table}[!t]", r"\centering", r"\caption{Replay eligibility by set, with the cause of exclusion. The eligibility requirement registered for the missed attacks was 80\%.}",
         r"\label{tab:eligibility}", r"\footnotesize", r"\setlength\tabcolsep{4pt}", r"\begin{tabular}{l" + "r" * len(sets) + "}", r"\toprule",
         r"\textbf{Status} & " + " & ".join(r"\textbf{%s}" % a[1] for a in sets) + r" \\", r"\midrule"]
    for o in order:
        L.append(o + " & " + " & ".join("%s (%.1f\\%%)" % (n(cnt[(a, o)]), 100 * cnt[(a, o)] / tot[a]) for a, _ in sets) + r" \\")
        if o == "Replay-eligible": L.append(r"\midrule")
    L.append(r"\midrule"); L.append("All & " + " & ".join(n(tot[a]) for a, _ in sets) + r" \\")
    L += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex("tab_eligibility", "\n".join(L))

def tab_explorer_samples(pm):
    body = r"""\begin{table}[!t]
\centering
\caption{LLM validation on public explorers: four samples read blind by the LLM validator under the released protocols. "Called MEV" means the validator calls the card a sandwich attack (or an arbitrage); "positive" means it also finds the attacker position positive after observable cost. Agreement and $\kappa$ are against REFEREE's state under the original witness; actor match is the validator's attacker address against the economic-actor rule; profit match is the share of cards whose validator profit after gas lies within 0.01 ETH of REFEREE's ledger. Wilson 95\% intervals.}
\label{tab:explorer_samples}
\footnotesize
\setlength\tabcolsep{2.5pt}
\begin{tabular}{p{2.2cm}lrp{1.9cm}p{1.9cm}rrrr}
\toprule
\textbf{Sample} & \textbf{Set} & \textbf{Cards} & \textbf{Called MEV} & \textbf{Positive} & \textbf{Agree.} & $\kappa$ & \textbf{Actor} & \textbf{Profit} \\
\midrule
\multirow{3}{*}{Sealed pack} & missed & 100 & 98\% [93.0, 99.4] & 81\% [72.2, 87.5] & 60.0\% & $-0.01$ & 98/100 & PM_F1B \\
 & reported & 50 & 100\% [92.9, 100] & 92\% [81.2, 96.8] & 90.0\% & 0.34 & 50/50 & \\
 & comparison & 50 & 30\% [19.1, 43.8] & 26\% [15.9, 39.6] & 94.0\% & 0.85 & 24/50 & \\
Added by S5$'$ & missed & 100 & 93\% [86.3, 96.6] & 90\% [82.6, 94.5] & 88.0\% & 0.44 & 99/100 & PM_SYM \\
Rejected 53 & missed & 53 & 96\% [87.2, 99.0] & 83\% [70.8, 90.8] & 13.2\% & 0.00 & --- & PM_REJ \\
Arbitrage, canonical & missed & 100 & 100\% [96.3, 100] & 96\% [90.2, 98.4] & --- & --- & 100/100 & --- \\
Arbitrage, six largest & missed & 6 & 2 of 6 & 2 of 6 & --- & --- & --- & --- \\
\midrule
\multicolumn{9}{p{12.8cm}}{LLM validator: headless session, tools disabled, protocols hashed before the run; 459 cards; total cost 11.95 USD; mean confidence 4.0 of 5 on the sealed pack.} \\
\bottomrule
\end{tabular}
\end{table}
"""
    for key, smp in (("PM_F1B", "f1b"), ("PM_SYM", "sym100"), ("PM_REJ", "rej53")):
        k, m = pm[smp]; body = body.replace(key, "%d/%d" % (k, m))
    tex("tab_explorer_samples", body)

def tab_disagreements():
    cards = rows(os.path.join(EX, "explorer_cards.csv"))
    samples = [("f1b", "Sealed pack"), ("sym100", "Added by S5$'$"), ("rej53", "Rejected 53")]
    def key(r):
        if r["n2_outcome"] == r["reader"]: return None
        st, led, rd = r["n2_outcome"], r["value_flow_state"], r["reader"]
        if st == "rejected":
            if rd == "structurally_supported": return ("rejected", "ledger positive, validator supports" if led == "positive" else "ledger undecidable, validator supports" if led == "undecidable" else "ledger negative, validator supports")
            return ("rejected", "validator cannot tell")
        if st == "undecidable": return ("undecidable", "validator supports" if rd == "structurally_supported" else "validator rejects")
        if rd == "rejected": return ("supported", "validator rejects: position not positive after cost" if r["Q2"] == "no" else "validator rejects: not a sandwich attack")
        return ("supported", "validator cannot tell")
    cnt = collections.Counter(); w2sup = collections.Counter(); tot = collections.Counter()
    for r in cards:
        tot[r["sample"]] += 1; k = key(r)
        if k: cnt[(r["sample"], k)] += 1; w2sup[(r["sample"], k)] += r["w2_outcome"] == "structurally_supported"
    groups = [("rejected", "REFEREE rejected (trajectory negative)"), ("undecidable", "REFEREE undecidable (residual token or cost unpriced)"), ("supported", "REFEREE supported")]
    L = [r"\begin{table}[!t]", r"\centering",
         r"\caption{Disagreements between the LLM validator and REFEREE under the original witness, grouped by REFEREE's state, with the number of those cards that the revised witness W2 moves to supported. Agreements are the remainder of each sample.}",
         r"\label{tab:disagreements}", r"\footnotesize", r"\setlength\tabcolsep{4pt}", r"\begin{tabular}{lrrrr}", r"\toprule",
         r"\textbf{Disagreement} & " + " & ".join(r"\textbf{%s}" % lab for _, lab in samples) + r" & \textbf{W2 supports} \\", r"\midrule"]
    for g, glab in groups:
        ks = sorted({k for (_, k) in cnt if k[0] == g}, key=lambda k: -sum(cnt[(s_, k)] for s_, _ in samples))
        if not ks: continue
        L.append(r"\multicolumn{5}{l}{\textit{%s}} \\" % glab)
        for k in ks:
            L.append(r"\quad %s & " % k[1] + " & ".join(str(cnt[(s_, k)]) if cnt[(s_, k)] else "---" for s_, _ in samples) + " & %d of %d" % (sum(w2sup[(s_, k)] for s_, _ in samples), sum(cnt[(s_, k)] for s_, _ in samples)) + r" \\")
    L.append(r"\midrule"); L.append("All disagreements & " + " & ".join(str(sum(cnt[(s_, k)] for k in {k for (_, k) in cnt})) for s_, _ in samples) + " & %d of %d" % (sum(w2sup.values()), sum(cnt.values())) + r" \\")
    L.append("Cards in the sample & " + " & ".join(str(tot[s_]) for s_, _ in samples) + r" & \\")
    L += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex("tab_disagreements", "\n".join(L))
    return cnt

def tab_arb_top6():
    ar = sorted(rows(os.path.join(EX, "arb_top6.csv")), key=lambda r: -float(r["profit_eth"]))
    kinds = {"0x46c8": "mints cETH and issues a leveraged token", "0x184e": "ETH paid into ibETH, minted IBETH sold through LINK", "0xa28a": "flash loan returned, no cycle", "0x47b0": "flash swap returned in full", "0x04ff": "ETH paid into ibETH, minted IBETH sold", "0x48ba": "flash swap of USDC, FEI bought and returned"}
    jud = {}
    AFTER_GAS = {"arb106_073"}
    for fjson in __import__("glob").glob(os.path.join(ROOT, "server/revision/out/explorer_verification/arb106/judgments/*.json")):
        try: j = json.load(open(fjson)); jud[j.get("case_id")] = j
        except Exception: pass
    L = [r"\begin{table}[!t]", r"\centering",
         r"\caption{The six largest missed arbitrage transactions by the rule's apparent profit, read blind by the LLM validator; profits in ETH, the validator's after gas. None has canonical flow, and the validator's profit after gas for the two it calls arbitrage is below 0.05 ETH against the rule's 56.6 and 29.7 ETH, which is why no ETH total for missed arbitrage is reported.}",
         r"\label{tab:arb_top6}", r"\footnotesize", r"\setlength\tabcolsep{3pt}", r"\begin{tabular}{lrrccp{3.4cm}}", r"\toprule",
         r"\textbf{Transaction} & \textbf{Rule (ETH)} & \textbf{Validator (ETH)} & \textbf{Inflow} & \textbf{Arbitrage} & \textbf{What the validator saw} \\", r"\midrule"]
    for r in ar:
        inflow = "mint" if r["mint_in"] == "True" else ("non-pool" if r["nonpool_in"] == "True" else "pool")
        q1 = {"yes": "yes", "no": "no", "cannot tell": "unclear"}[r["Q1"]]
        j = jud.get(r["case_id"], {}); vp = "%.2f" % (float(j["net_eth"]) - (0.0 if r["case_id"] in AFTER_GAS else float(j["gas_eth"]))) if j.get("net_eth") is not None and j.get("gas_eth") is not None else "---"
        L.append(r"\texttt{%s\ldots} & %.1f & %s & %s & %s & %s \\" % (r["hash"][:10], float(r["profit_eth"]), vp, inflow, q1, kinds.get(r["hash"][:6], "")))
    L += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex("tab_arb_top6", "\n".join(L))

def tab_rej53():
    rj = rows(os.path.join(EX, "rej53_table.csv")); vv = {r["card"]: r for r in rows(os.path.join(HERE, "data", "validator_values.csv")) if r["sample"] == "rej53"}
    def f(v):
        try: return float(v)
        except: return None
    groups = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rj:
        led = r["n2_reason"].split("ledger ")[-1]; traj = "negative" if "trajectory negative" in r["n2_reason"] else "positive"
        groups[(traj, led)][(STATE.get(r["w2_outcome"], r["w2_outcome"]), r["in_M"] == "True", {"structurally_supported": "supports", "rejected": "rejects", "undecidable": "cannot tell"}.get(r["reader"], r["reader"]))].append(r["card"])
    glab = {("negative", "positive"): "Trajectory negative, ledger positive", ("negative", "undecidable"): "Trajectory negative, ledger undecidable", ("negative", "negative"): "Trajectory and ledger negative", ("positive", "negative"): "Trajectory positive, ledger negative", ("positive", "undecidable"): "Trajectory positive, ledger undecidable"}
    L = [r"\begin{table}[!t]", r"\centering",
         r"\caption{The 53 missed sandwich attacks that the original witness rejects, grouped by the reason for the rejection, with the state under the revised witness W2, whether mev-inspect also detects the attack, the LLM validator's verdict, and the median profit of the group in ETH as REFEREE's ledger after observable cost and as the validator computed it after gas.}",
         r"\label{tab:rej53}", r"\footnotesize", r"\setlength\tabcolsep{4pt}", r"\begin{tabular}{lccrrr}", r"\toprule",
         r"\textbf{Under W2} & \textbf{mev-inspect detects} & \textbf{Validator} & \textbf{Cases} & \textbf{REFEREE (ETH)} & \textbf{Validator (ETH)} \\", r"\midrule"]
    for gk, sub in sorted(groups.items(), key=lambda x: -sum(len(v) for v in x[1].values())):
        L.append(r"\multicolumn{6}{l}{\textit{%s (%d)}} \\" % (glab.get(gk, "%s / %s" % gk), sum(len(v) for v in sub.values())))
        for (w2o, inm, rd), cards in sorted(sub.items(), key=lambda x: -len(x[1])):
            lv = [f(vv[c]["ledger_after_cost"]) for c in cards if c in vv and f(vv[c]["ledger_after_cost"]) is not None]
            pv = [f(vv[c]["validator_after_gas"]) for c in cards if c in vv and f(vv[c]["validator_after_gas"]) is not None]
            L.append(r"\quad %s & %s & %s & %d & %s & %s \\" % (w2o, "yes" if inm else "no", rd, len(cards), ("%.3f" % float(np.median(lv))) if lv else "---", ("%.3f" % float(np.median(pv))) if pv else "---"))
    L += [r"\midrule", r"All & & & 53 & & \\", r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    tex("tab_rej53", "\n".join(L))

def tab_systematization():
    body = r"""\begin{table}[!t]
\centering
\caption{Detection methods compared on what they decide. The first four are the heuristics of the cited papers and Flashbots' open-source detector mev-inspect; the public dataset audited in this paper~\cite{aflashbotinthepan} was built by applying the sandwich heuristics of Torres et al.~\cite{torres2021frontrunner} and the arbitrage heuristics of Qin et al.~\cite{qin2022quantifying}, and mev-inspect is the second detector audited. A filled circle marks a property the method states, a half circle one it states in part, an open circle one it does not have, and a dash a property that does not apply.}
\label{tab:systematization}
\footnotesize
\setlength\tabcolsep{3pt}
\begin{tabular}{p{4.3cm}>{\centering\arraybackslash}p{1.55cm}>{\centering\arraybackslash}p{1.55cm}>{\centering\arraybackslash}p{1.6cm}>{\centering\arraybackslash}p{1.55cm}>{\centering\arraybackslash}p{1.3cm}}
\toprule
\textbf{Property} & \textbf{Torres et al.~\cite{torres2021frontrunner}} & \textbf{Qin et al.~\cite{qin2022quantifying}} & \textbf{McLaughlin et al.~\cite{mclaughlin2023large}} & \textbf{mev-inspect~\cite{flashbots2021mevinspect}} & \textbf{REFEREE} \\
\midrule
Nature & heuristics & heuristics & heuristics & open-source tool & this paper \\
MEV types covered & sandwich & sandwich, arbitrage, liquidation & arbitrage & sandwich, arbitrage, liquidation & sandwich, arbitrage, liquidation \\
\midrule
Sell-first sandwich attacks admitted & \Circle & \CIRCLE & --- & \CIRCLE & \CIRCLE \\
Attacker identified beyond the transaction sender & \LEFTcircle & \LEFTcircle & \LEFTcircle & \LEFTcircle & \CIRCLE \\
Pool-price test of the attack & \Circle & \Circle & --- & \Circle & \CIRCLE \\
Payments to the block producer charged as cost & \Circle & \LEFTcircle & \LEFTcircle & \CIRCLE & \CIRCLE \\
Residual token position priced by a stated rule & \Circle & \Circle & \Circle & \LEFTcircle & \CIRCLE \\
Undecidable state reported & \Circle & \Circle & \Circle & \Circle & \CIRCLE \\
Per-case reason codes & \Circle & \Circle & \Circle & \LEFTcircle & \CIRCLE \\
Rules frozen and hashed before scoring & \Circle & \Circle & \Circle & \Circle & \CIRCLE \\
Replay of the victim's swap & \Circle & \CIRCLE & \Circle & \Circle & \LEFTcircle \\
Manual validation on a sample & \CIRCLE & \CIRCLE & \CIRCLE & \Circle & \Circle \\
LLM validation on public explorers, reports released & \Circle & \Circle & \Circle & \Circle & \CIRCLE \\
Audits existing public datasets & \Circle & \Circle & \Circle & \Circle & \CIRCLE \\
\bottomrule
\end{tabular}
\end{table}
"""
    tex("tab_systematization", body)

if __name__ == "__main__":
    out = {}
    fig_coverage(); out["misses"] = fig_misses(); fig_outcomes(); out["reversal"] = fig_reversal(); out["arb_index"] = fig_arb_index(); out["victim_actor"] = fig_victim_actor()
    tab_populations(); tab_contrast(); tab_mechanism(); tab_magnitudes(); tab_arb_twoway(); tab_eligibility(); tab_systematization()
    json.dump(out, open(os.path.join(HERE, "data", "exhibit_numbers.json"), "w"), indent=1); print("numbers written")
