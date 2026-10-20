import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib as mpl, matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "latex")
CACHE = os.path.join(ROOT, "analysis/fresh_manuscript/data")
LABELS = ["blk_num", "blk_ts", "eth_usd", "cost_e", "cost_u", "gain_e", "gain_u", "prof_e", "prof_u"]

def corr_matrices():
    corrs = [pd.read_csv(os.path.join(CACHE, "corr_%s.csv" % k), index_col=0) for k in ("arbitrage", "sandwich")]
    fig = plt.figure(figsize=(5.48, 2.75), constrained_layout=True)
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 0.05], wspace=0.05)
    for i, (corr, label) in enumerate(zip(corrs, ("Arbitrage", "Sandwich"))):
        ax = fig.add_subplot(gs[i])
        ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1, aspect="equal")
        ax.set_xticks(np.arange(9)); ax.set_xticklabels(LABELS, fontsize=7.5, rotation=90); ax.set_yticks(np.arange(9))
        ax.set_yticklabels(LABELS if i == 0 else [""] * 9, fontsize=7.5, rotation=0)
        ax.set_xticks(np.arange(-0.5, 9, 1), minor=True); ax.set_yticks(np.arange(-0.5, 9, 1), minor=True); ax.grid(False); ax.grid(which="minor", color="#dddddd", linestyle="-", linewidth=0.25); ax.tick_params(which="minor", length=0)
        for sp in ax.spines.values(): sp.set_visible(False)
        ax.set_title("(%s) %s" % ("ab"[i], label), fontsize=8.5, fontweight="bold", pad=3); ax.tick_params(length=1.2, pad=1.0)
    cax = fig.add_subplot(gs[2]); sm = mpl.cm.ScalarMappable(cmap="RdBu_r", norm=mpl.colors.Normalize(vmin=-1, vmax=1)); sm.set_array([])
    cb = fig.colorbar(sm, cax=cax); cb.ax.tick_params(labelsize=7, length=1.2, pad=1.0); cb.set_label("r", size=8)
    p = os.path.join(OUT, "shared_correlation_matrices.pdf"); fig.savefig(p, bbox_inches=None); plt.close(fig); print("wrote", p)

def miner_heatmap():
    miners = ["0xEA67...8ec8", "0x5A0b...9c4c", "0x829B...A830", "0x0466...8F7F", "0x52bc...E3b5", "0x1aD9...5836"]
    data = np.array([[792_512, 216_086], [763_690, 219_642], [365_985, 127_592], [165_279, 44_657], [150_550, 38_232], [128_446, 39_787]], dtype=float)
    fig, ax = plt.subplots(figsize=(3.5, 2.6))
    im = ax.imshow(data, cmap="YlOrRd", aspect="auto")
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, format(int(data[i, j]), ","), ha="center", va="center", fontsize=8, color="white" if data[i, j] > 0.6 * data.max() else "#111111")
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Arbitrage", "Sandwich"], fontsize=8); ax.set_yticks(range(6)); ax.set_yticklabels(miners, fontsize=8)
    ax.set_xticks([-0.5, 0.5, 1.5], minor=True); ax.set_yticks(np.arange(-0.5, 6, 1), minor=True); ax.grid(False); ax.grid(which="minor", color="#cccccc", linestyle="-", linewidth=0.3); ax.tick_params(which="minor", length=0); ax.tick_params(which="major", length=2)
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.set_xlabel("MEV type", fontsize=8.5); ax.set_ylabel("Miner address", fontsize=8.5)
    cb = fig.colorbar(im, ax=ax, shrink=0.85); cb.ax.tick_params(labelsize=7.5); cb.set_label("Tx count", size=8)
    fig.tight_layout(pad=0.3)
    p = os.path.join(OUT, "miner_mev_heatmap.pdf"); fig.savefig(p); plt.close(fig); print("wrote", p)

if __name__ == "__main__":
    corr_matrices(); miner_heatmap()
