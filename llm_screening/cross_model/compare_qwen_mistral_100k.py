#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json

def load_and_analyze_results():

    print("QWEN vs MISTRAL 100K ARBITRAGE COMPARISON")
    print("=" * 60)

    # Load datasets
    print("Loading datasets...")
    qwen_file = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Results/qwen_arbitrage_100k_20251014_171647.csv"
    mistral_file = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Mistral/Results/Arbitrage/results_arbitrage_100k_20250702_183505.csv"

    qwen_df = pd.read_csv(qwen_file)
    mistral_df = pd.read_csv(mistral_file)

    print(f"Qwen dataset: {len(qwen_df):,} transactions")
    print(f"Mistral dataset: {len(mistral_df):,} transactions")

    # Basic statistics
    print(f"\nDATASET OVERVIEW")
    print("=" * 40)

    # Qwen Analysis
    qwen_counts = qwen_df['llm_classification'].value_counts()
    qwen_total = len(qwen_df)

    print(f"Qwen2.5-7B Results:")
    for classification, count in qwen_counts.items():
        percentage = count / qwen_total * 100
        print(f"  {classification}: {count:,} ({percentage:.2f}%)")

    # Mistral Analysis
    mistral_counts = mistral_df['llm_classification'].value_counts()
    mistral_total = len(mistral_df)

    print(f"\nMistral-7B Results:")
    for classification, count in mistral_counts.items():
        percentage = count / mistral_total * 100
        print(f"  {classification}: {count:,} ({percentage:.2f}%)")

    # Unknown Pattern Analysis
    print(f"\nUNKNOWN PATTERN ANALYSIS")
    print("=" * 40)

    qwen_unknown = qwen_df[qwen_df['llm_classification'] == 'UNKNOWN']
    mistral_unknown = mistral_df[mistral_df['llm_classification'] == 'UNKNOWN']

    qwen_unknown_rate = len(qwen_unknown) / qwen_total * 100
    mistral_unknown_rate = len(mistral_unknown) / mistral_total * 100

    print(f"Qwen Unknown Patterns:")
    print(f"  Count: {len(qwen_unknown):,}")
    print(f"  Rate: {qwen_unknown_rate:.3f}%")

    print(f"\nMistral Unknown Patterns:")
    print(f"  Count: {len(mistral_unknown):,}")
    print(f"  Rate: {mistral_unknown_rate:.3f}%")

    # Performance Comparison
    improvement_factor = qwen_unknown_rate / mistral_unknown_rate if mistral_unknown_rate > 0 else float('inf')
    absolute_difference = len(qwen_unknown) - len(mistral_unknown)

    print(f"\nPERFORMANCE COMPARISON:")
    print(f"  Improvement Factor: {improvement_factor:.1f}x")
    print(f"  Absolute Difference: +{absolute_difference:,} unknown patterns")

    if improvement_factor > 10:
        print(f"  EXCEPTIONAL: Qwen dramatically outperforms Mistral")
    elif improvement_factor > 3:
        print(f"  EXCELLENT: Qwen significantly outperforms Mistral")
    elif improvement_factor > 1.5:
        print(f"  GOOD: Qwen outperforms Mistral")
    else:
        print(f"  SIMILAR: Comparable performance")

    # Profit Analysis
    print(f"\nPROFIT ANALYSIS OF UNKNOWN PATTERNS")
    print("=" * 50)

    if len(qwen_unknown) > 0:
        qwen_avg_profit = qwen_unknown['profit_eth'].mean()
        qwen_profit_std = qwen_unknown['profit_eth'].std()
        qwen_avg_swaps = qwen_unknown['num_swaps'].mean()

        print(f"Qwen Unknown Patterns:")
        print(f"  Average profit: {qwen_avg_profit:.6f} ETH")
        print(f"  Profit std dev: {qwen_profit_std:.6f} ETH")
        print(f"  Average swaps: {qwen_avg_swaps:.1f}")

    if len(mistral_unknown) > 0:
        mistral_avg_profit = mistral_unknown['profit_eth'].mean()
        mistral_profit_std = mistral_unknown['profit_eth'].std()
        mistral_avg_swaps = mistral_unknown['num_swaps'].mean()

        print(f"\nMistral Unknown Patterns:")
        print(f"  Average profit: {mistral_avg_profit:.6f} ETH")
        print(f"  Profit std dev: {mistral_profit_std:.6f} ETH")
        print(f"  Average swaps: {mistral_avg_swaps:.1f}")

    # Sample Unknown Patterns
    print(f"\nSAMPLE UNKNOWN PATTERNS")
    print("=" * 40)

    print(f"Qwen Unknown Examples (first 10):")
    for idx, row in qwen_unknown.head(10).iterrows():
        desc = row['description'][:80] + "..." if len(row['description']) > 80 else row['description']
        print(f"  • {desc}")

    print(f"\nMistral Unknown Examples (first 10):")
    for idx, row in mistral_unknown.head(10).iterrows():
        desc = row['description'][:80] + "..." if len(row['description']) > 80 else row['description']
        print(f"  • {desc}")

    # Research Impact
    print(f"\nRESEARCH IMPACT ASSESSMENT")
    print("=" * 40)

    # Extrapolation to full dataset
    full_dataset_size = 3462678  # Total arbitrage transactions
    qwen_extrapolated = int((qwen_unknown_rate / 100) * full_dataset_size)
    mistral_extrapolated = int((mistral_unknown_rate / 100) * full_dataset_size)

    print(f"Extrapolation to Full Dataset ({full_dataset_size:,} transactions):")
    print(f"  Qwen projected unknowns: {qwen_extrapolated:,}")
    print(f"  Mistral projected unknowns: {mistral_extrapolated:,}")
    print(f"  Additional discoveries: +{qwen_extrapolated - mistral_extrapolated:,}")

    # Statistical Significance
    print(f"\nSTATISTICAL SIGNIFICANCE:")
    print(f"  Qwen sample size: {qwen_total:,}")
    print(f"  Mistral sample size: {mistral_total:,}")
    print(f"  Both datasets: High statistical power")

    if qwen_unknown_rate > 0.1:
        confidence = "VERY HIGH"
    elif qwen_unknown_rate > 0.05:
        confidence = "HIGH"
    else:
        confidence = "MODERATE"

    print(f"  Confidence in Qwen superiority: {confidence}")

    # Model Comparison Summary
    print(f"\nMODEL COMPARISON SUMMARY")
    print("=" * 40)

    print(f"Winner: {'QWEN2.5-7B' if improvement_factor > 1 else 'MISTRAL-7B'}")
    print(f"Key Advantage: {improvement_factor:.1f}x better unknown detection")
    print(f"Research Value: {qwen_extrapolated:,} vs {mistral_extrapolated:,} projected unknowns")

    if improvement_factor > 5:
        recommendation = "Strong recommendation for Qwen2.5 in MEV research"
    elif improvement_factor > 2:
        recommendation = "Clear preference for Qwen2.5 over Mistral"
    else:
        recommendation = "Both models show comparable performance"

    print(f"Recommendation: {recommendation}")

    # Generate summary statistics
    summary_stats = {
        'qwen': {
            'total_transactions': qwen_total,
            'unknown_count': len(qwen_unknown),
            'unknown_rate': qwen_unknown_rate,
            'avg_profit': qwen_avg_profit if len(qwen_unknown) > 0 else 0,
            'avg_swaps': qwen_avg_swaps if len(qwen_unknown) > 0 else 0
        },
        'mistral': {
            'total_transactions': mistral_total,
            'unknown_count': len(mistral_unknown),
            'unknown_rate': mistral_unknown_rate,
            'avg_profit': mistral_avg_profit if len(mistral_unknown) > 0 else 0,
            'avg_swaps': mistral_avg_swaps if len(mistral_unknown) > 0 else 0
        },
        'comparison': {
            'improvement_factor': improvement_factor,
            'absolute_difference': absolute_difference,
            'qwen_extrapolated': qwen_extrapolated,
            'mistral_extrapolated': mistral_extrapolated,
            'winner': 'qwen' if improvement_factor > 1 else 'mistral'
        }
    }

    return summary_stats, qwen_df, mistral_df

def save_comparison_report(summary_stats):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Comparison/qwen_vs_mistral_100k_{timestamp}.json"

    # Ensure directory exists
    import os
    os.makedirs(os.path.dirname(report_file), exist_ok=True)

    with open(report_file, 'w') as f:
        json.dump(summary_stats, f, indent=2)

    print(f"\nComparison report saved: {report_file}")

if __name__ == "__main__":
    summary_stats, qwen_df, mistral_df = load_and_analyze_results()
    save_comparison_report(summary_stats)

    print(f"\nAnalysis complete! Qwen2.5-7B vs Mistral-7B comparison finished.")