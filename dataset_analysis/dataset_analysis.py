#!/usr/bin/env python3
import ast
import warnings
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# Point these at the local raw CSVs (see datasets/README.md).
DATA_DIR = Path("<PROJECT_ROOT>/large")
ARBITRAGE_CSV = DATA_DIR / "arbitrage_results.csv"
SANDWICH_CSV = DATA_DIR / "sandwich_results.csv"
LIQUIDATION_CSV = DATA_DIR / "liquidation_results.csv"

# Nine numeric features shared across all three MEV types.
COMMON_FEATURES = [
    "block_number", "block_timestamp", "eth_usd_price",
    "cost_eth", "cost_usd", "gain_eth", "gain_usd",
    "profit_eth", "profit_usd",
]


def load_sample(csv_path, sample_size):
    total = sum(1 for _ in open(csv_path)) - 1
    if total > sample_size:
        skip = sorted(np.random.choice(range(1, total + 1),
                                       total - sample_size, replace=False))
        df = pd.read_csv(csv_path, skiprows=skip, low_memory=False)
    else:
        df = pd.read_csv(csv_path, low_memory=False)
    return df, total


def analyze_miner_concentration(chunk_size=50000, top_n=10):
    print("\n[1] Miner concentration")
    files = [("Arbitrage", ARBITRAGE_CSV),
             ("Sandwich", SANDWICH_CSV),
             ("Liquidation", LIQUIDATION_CSV)]
    counts = defaultdict(lambda: defaultdict(int))
    sizes = {}
    for mev_type, path in files:
        processed = 0
        for chunk in pd.read_csv(path, chunksize=chunk_size, low_memory=False,
                                 usecols=lambda c: c == "miner"):
            for miner in chunk["miner"].dropna():
                counts[miner][mev_type] += 1
            processed += len(chunk)
        sizes[mev_type] = processed
        print(f"  {mev_type}: {processed:,} transactions")

    rows = []
    for miner, c in counts.items():
        rows.append({"miner": miner,
                     "Arbitrage": c.get("Arbitrage", 0),
                     "Sandwich": c.get("Sandwich", 0),
                     "Liquidation": c.get("Liquidation", 0)})
    pivot = pd.DataFrame(rows).set_index("miner")
    pivot["total"] = pivot.sum(axis=1)
    pivot = pivot.sort_values("total", ascending=False)
    print(f"  Unique miners: {len(pivot):,}")

    arb_total = sizes.get("Arbitrage", 0)
    top2_arb = pivot["Arbitrage"].head(2).sum()
    if arb_total:
        print(f"  Top-2 miners account for {top2_arb:,} arbitrage txs "
              f"({top2_arb / arb_total:.1%} of {arb_total:,})")
    print(f"  Top {top_n} miners by total volume:")
    for miner, r in pivot.head(top_n).iterrows():
        short = f"{miner[:6]}...{miner[-4:]}"
        print(f"    {short}: total {int(r['total']):,} "
              f"(A:{int(r['Arbitrage']):,} S:{int(r['Sandwich']):,} L:{int(r['Liquidation']):,})")
    return pivot


def correlation_for(csv_path, label, sample_size=100000):
    df, total = load_sample(csv_path, sample_size)
    cols = [c for c in COMMON_FEATURES if c in df.columns]
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    corr_df = df[cols].dropna(thresh=max(3, len(cols) // 2))
    corr = corr_df.corr()
    print(f"  {label}: {len(corr_df):,} rows sampled from {total:,}; "
          f"{len(cols)} features")
    pairs = []
    cs = corr.columns
    for i in range(len(cs)):
        for j in range(i + 1, len(cs)):
            v = corr.iloc[i, j]
            if not pd.isna(v) and abs(v) > 0.7:
                pairs.append((cs[i], cs[j], v))
    pairs.sort(key=lambda x: abs(x[2]), reverse=True)
    for a, b, v in pairs[:8]:
        print(f"    {a} <-> {b}: {v:+.3f}")
    return corr


def analyze_feature_correlations(sample_size=100000):
    print("\n[2] Feature correlations")
    correlation_for(ARBITRAGE_CSV, "Arbitrage", sample_size)
    correlation_for(SANDWICH_CSV, "Sandwich", sample_size)
    correlation_for(LIQUIDATION_CSV, "Liquidation", sample_size)


def analyze_gas_strategy(sample_size=50000):
    print("\n[3] Sandwich gas strategy")
    df, total = load_sample(SANDWICH_CSV, sample_size)
    rows = []
    for _, row in df.iterrows():
        try:
            first = ast.literal_eval(row["first_transaction"]) if pd.notna(row["first_transaction"]) else {}
            second = ast.literal_eval(row["second_transaction"]) if pd.notna(row["second_transaction"]) else {}
            whale = ast.literal_eval(row["whale_transaction"]) if pd.notna(row["whale_transaction"]) else {}
            rows.append({
                "profit_eth": pd.to_numeric(row["profit_eth"], errors="coerce"),
                "front": pd.to_numeric(first.get("gasPrice", 0), errors="coerce") / 1e9,
                "back": pd.to_numeric(second.get("gasPrice", 0), errors="coerce") / 1e9,
                "victim": pd.to_numeric(whale.get("gasPrice", 0), errors="coerce") / 1e9,
            })
        except Exception:
            continue
    g = pd.DataFrame(rows)
    g["front_ratio"] = (g["front"] / g["victim"]).replace([np.inf, -np.inf], np.nan)
    g["back_ratio"] = (g["back"] / g["victim"]).replace([np.inf, -np.inf], np.nan)
    prof = g[(g["profit_eth"] > 0.01) &
             (g["front_ratio"].between(0.5, 5)) &
             (g["back_ratio"].between(0.5, 5))]
    print(f"  Parsed {len(g):,} of {total:,}; {len(prof):,} profitable in range")
    if len(prof):
        print(f"  Front-run median ratio: {prof['front_ratio'].median():.3f}x victim gas")
        print(f"  Back-run  median ratio: {prof['back_ratio'].median():.3f}x victim gas")
        print(f"  Front-run ratio vs profit corr: {prof['front_ratio'].corr(prof['profit_eth']):+.3f}")
        print(f"  Back-run  ratio vs profit corr: {prof['back_ratio'].corr(prof['profit_eth']):+.3f}")
        print(f"  Front-run gas > victim: {(prof['front_ratio'] > 1).mean():.1%} of profitable attacks")
        print(f"  Back-run  gas > victim: {(prof['back_ratio'] > 1).mean():.1%} of profitable attacks")
    return prof


DEX_ADDRESSES = {
    "0xa478c2975ab1ea89e8196811f51a7b7ade33eb11": "Uniswap V2",
    "0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc": "Uniswap V2",
    "0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852": "Uniswap V2",
    "0x397ff1542f962076d0bfe58ea045ffa2d347aca0": "SushiSwap",
    "0xce84867c3c02b05dc570d0135103d3fb9cc19433": "SushiSwap",
    "0x59a19d8c652fa0284f44113d0ff9aba70bd46fb4": "Balancer",
    "0xa5407eae9ba41422680e2e00537571bcc53efbfd": "Curve",
    "0x1811a719a05d20b6447ca556a54f00f9c14578be": "Bancor",
}


def _dex_stats(records):
    out = {}
    for dex, vals in records.items():
        if len(vals) >= 30:
            profits = [v for v in vals]
            out[dex] = {
                "count": len(profits),
                "avg_profit": float(np.mean(profits)),
                "success_rate": float(np.mean([p > 0 for p in profits]) * 100),
            }
    return out


def analyze_dex_mapping(nrows=15000):
    print("\n[4] DEX mapping")
    dex = defaultdict(lambda: defaultdict(list))

    arb = pd.read_csv(ARBITRAGE_CSV, nrows=nrows, low_memory=False)
    for _, row in arb.iterrows():
        try:
            if pd.isna(row["swaps"]) or pd.isna(row["profit_eth"]):
                continue
            swaps = ast.literal_eval(row["swaps"])
            if not isinstance(swaps, list):
                continue
            for swap in swaps:
                if not isinstance(swap, dict):
                    continue
                name = swap.get("exchange_name") or DEX_ADDRESSES.get(swap.get("exchange"))
                if name:
                    p = pd.to_numeric(row["profit_eth"], errors="coerce")
                    if p is not None and -10 < p < 10:
                        dex[name]["Arbitrage"].append(p)
                    break
        except Exception:
            continue

    san = pd.read_csv(SANDWICH_CSV, nrows=nrows, low_memory=False)
    san = san[san["exchange_name"].notna() & san["profit_eth"].notna()]
    san["profit_eth"] = pd.to_numeric(san["profit_eth"], errors="coerce")
    for exch in san["exchange_name"].dropna().unique():
        sub = san[san["exchange_name"] == exch]["profit_eth"].dropna()
        for p in sub:
            dex[exch]["Sandwich"].append(float(p))

    for name in sorted(dex):
        arb_stats = _dex_stats({name: dex[name]["Arbitrage"]}).get(name)
        san_stats = _dex_stats({name: dex[name]["Sandwich"]}).get(name)
        if not arb_stats and not san_stats:
            continue
        print(f"  {name}:")
        if arb_stats:
            print(f"    Arbitrage: {arb_stats['count']:,} txs, "
                  f"avg {arb_stats['avg_profit']:.4f} ETH, "
                  f"{arb_stats['success_rate']:.1f}% profitable")
        if san_stats:
            print(f"    Sandwich:  {san_stats['count']:,} txs, "
                  f"avg {san_stats['avg_profit']:.4f} ETH, "
                  f"{san_stats['success_rate']:.1f}% profitable")


def main():
    analyze_miner_concentration()
    analyze_feature_correlations()
    analyze_gas_strategy()
    analyze_dex_mapping()


if __name__ == "__main__":
    main()
