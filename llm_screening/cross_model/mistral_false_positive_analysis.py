#!/usr/bin/env python3

import pandas as pd
import numpy as np
import re
from collections import Counter

def analyze_mistral_false_positives():

    print("MISTRAL FALSE POSITIVE & FALSE NEGATIVE ANALYSIS")
    print("=" * 65)

    # Load datasets
    qwen_file = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Results/qwen_arbitrage_100k_20251014_171647.csv"
    mistral_file = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Mistral/Results/Arbitrage/results_arbitrage_100k_20250702_183505.csv"

    qwen_df = pd.read_csv(qwen_file)
    mistral_df = pd.read_csv(mistral_file)

    qwen_unknown = qwen_df[qwen_df['llm_classification'] == 'UNKNOWN']
    mistral_unknown = mistral_df[mistral_df['llm_classification'] == 'UNKNOWN']
    mistral_known = mistral_df[mistral_df['llm_classification'] == 'KNOWN']

    print(f"Dataset Overview:")
    print(f"  Mistral unknown: {len(mistral_unknown):,} patterns")
    print(f"  Mistral known: {len(mistral_known):,} patterns")
    print(f"  Qwen unknown: {len(qwen_unknown):,} patterns (for reference)")

    # 1. ANALYZE MISTRAL'S "UNKNOWN" PATTERNS FOR FALSE POSITIVES
    print(f"\nMISTRAL UNKNOWN PATTERN ANALYSIS")
    print("=" * 45)

    print(f"Examining Mistral's 65 'Unknown' Classifications:")

    # Look at all Mistral unknown patterns
    print(f"\nComplete list of Mistral unknown patterns:")
    for idx, row in mistral_unknown.iterrows():
        desc = row['description'][:100] + "..." if len(row['description']) > 100 else row['description']
        profit = row['profit_eth']
        swaps = row['num_swaps']
        print(f"  {idx:2d}. [{swaps} swaps] {desc} | Profit: {profit:.6f} ETH")

    # Analyze patterns
    def extract_key_features(desc):
        # Check for standard tokens
        standard_tokens = ['Wrapped Ether', 'WETH', 'ETH', 'USDC', 'USDT', 'DAI', 'WBTC']
        has_standard = any(token in desc for token in standard_tokens)

        # Check for standard flow patterns
        standard_flow = 'Wrapped Ether →' in desc and '→ Wrapped Ether' in desc

        return has_standard, standard_flow

    mistral_standard_count = 0
    mistral_standard_flow_count = 0
    mistral_profitable_count = 0

    for _, row in mistral_unknown.iterrows():
        has_standard, standard_flow = extract_key_features(row['description'])
        if has_standard:
            mistral_standard_count += 1
        if standard_flow:
            mistral_standard_flow_count += 1
        if row['profit_eth'] > 0:
            mistral_profitable_count += 1

    print(f"\nMistral Unknown Pattern Characteristics:")
    print(f"  Patterns with standard tokens: {mistral_standard_count}/{len(mistral_unknown)} ({mistral_standard_count/len(mistral_unknown)*100:.1f}%)")
    print(f"  Standard WETH flow patterns: {mistral_standard_flow_count}/{len(mistral_unknown)} ({mistral_standard_flow_count/len(mistral_unknown)*100:.1f}%)")
    print(f"  Profitable patterns: {mistral_profitable_count}/{len(mistral_unknown)} ({mistral_profitable_count/len(mistral_unknown)*100:.1f}%)")

    # Check for potential false positives in Mistral
    print(f"\nPOTENTIAL MISTRAL FALSE POSITIVES:")

    # Patterns that look like standard arbitrage
    potential_mistral_fp = mistral_unknown[
        mistral_unknown['description'].str.contains('Wrapped Ether → .* → Wrapped Ether', na=False, regex=True)
    ]

    print(f"Standard WETH arbitrage patterns marked as unknown:")
    for idx, row in potential_mistral_fp.iterrows():
        print(f"  • {row['description']}")

    # 2. ANALYZE MISTRAL'S "KNOWN" PATTERNS FOR FALSE NEGATIVES
    print(f"\nMISTRAL FALSE NEGATIVE ANALYSIS")
    print("=" * 40)

    # Sample some "known" patterns that might actually be unknown
    print(f"Examining potential false negatives in Mistral's 'Known' classifications:")

    # Look for complex patterns marked as "known"
    complex_known = mistral_known[mistral_known['num_swaps'] >= 5]
    print(f"\nComplex patterns (5+ swaps) marked as KNOWN:")
    print(f"Count: {len(complex_known):,}")

    if len(complex_known) > 0:
        print("Sample complex 'known' patterns:")
        for idx, row in complex_known.head(10).iterrows():
            desc = row['description'][:100] + "..." if len(row['description']) > 100 else row['description']
            print(f"  • [{row['num_swaps']} swaps] {desc}")

    # Look for highly profitable patterns marked as "known" (might be novel strategies)
    high_profit_known = mistral_known[mistral_known['profit_eth'] > 1.0]  # >1 ETH profit
    print(f"\nHigh-profit patterns (>1 ETH) marked as KNOWN:")
    print(f"Count: {len(high_profit_known):,}")

    if len(high_profit_known) > 0:
        print("Sample high-profit 'known' patterns:")
        for idx, row in high_profit_known.head(10).iterrows():
            desc = row['description'][:100] + "..." if len(row['description']) > 100 else row['description']
            print(f"  • {row['profit_eth']:.3f} ETH: {desc}")

    # 3. CROSS-MODEL COMPARISON
    print(f"\nCROSS-MODEL PATTERN COMPARISON")
    print("=" * 45)

    # Find patterns that Qwen marked unknown but Mistral marked known
    # This requires matching similar patterns (challenging without exact overlap)

    # Analyze distribution differences
    qwen_swap_dist = qwen_unknown['num_swaps'].value_counts().sort_index()
    mistral_swap_dist = mistral_unknown['num_swaps'].value_counts().sort_index()

    print(f"Swap complexity comparison:")
    print(f"{'Swaps':<6} {'Qwen Unknown':<12} {'Mistral Unknown':<15} {'Difference':<10}")
    print("-" * 50)

    all_swaps = set(qwen_swap_dist.index) | set(mistral_swap_dist.index)
    for swaps in sorted(all_swaps):
        qwen_count = qwen_swap_dist.get(swaps, 0)
        mistral_count = mistral_swap_dist.get(swaps, 0)
        diff = qwen_count - mistral_count
        print(f"{swaps:<6} {qwen_count:<12} {mistral_count:<15} {diff:+d}")

    # 4. TOKEN DIVERSITY ANALYSIS
    print(f"\nTOKEN DIVERSITY ANALYSIS")
    print("=" * 35)

    def extract_tokens(descriptions):
        all_tokens = []
        for desc in descriptions:
            # Simple token extraction (can be improved)
            tokens = re.findall(r'([A-Za-z][A-Za-z0-9\s\.]+?)(?:\s→|\s\|)', str(desc))
            all_tokens.extend([token.strip() for token in tokens if len(token.strip()) > 1])
        return Counter(all_tokens)

    mistral_unknown_tokens = extract_tokens(mistral_unknown['description'])
    mistral_known_tokens = extract_tokens(mistral_known['description'].head(1000))  # Sample for performance

    print(f"Mistral Token Analysis:")
    print(f"  Unknown patterns - unique tokens: {len(mistral_unknown_tokens)}")
    print(f"  Known patterns (sample) - unique tokens: {len(mistral_known_tokens)}")

    print(f"\nTop tokens in Mistral unknown patterns:")
    for token, count in mistral_unknown_tokens.most_common(10):
        print(f"    {token}: {count}")

    # Check if Mistral unknown tokens are actually common
    common_defi_tokens = ['Wrapped Ether', 'USDC', 'USDT', 'DAI', 'WBTC', 'UNI', 'LINK', 'AAVE']
    mistral_common_unknown = sum(mistral_unknown_tokens[token] for token in common_defi_tokens if token in mistral_unknown_tokens)
    mistral_total_unknown_tokens = sum(mistral_unknown_tokens.values())

    print(f"\nCommon DeFi tokens in Mistral unknown patterns:")
    print(f"  {mistral_common_unknown}/{mistral_total_unknown_tokens} ({mistral_common_unknown/mistral_total_unknown_tokens*100:.1f}%)")

    # 5. MISTRAL FALSE POSITIVE ASSESSMENT
    print(f"\nMISTRAL FALSE POSITIVE RISK ASSESSMENT")
    print("=" * 50)

    mistral_fp_risk_factors = []

    # Check if many patterns are just WETH arbitrage
    weth_arbitrage_count = len(mistral_unknown[
        mistral_unknown['description'].str.contains('Wrapped Ether → .* → Wrapped Ether', na=False, regex=True)
    ])
    weth_arbitrage_rate = weth_arbitrage_count / len(mistral_unknown) * 100

    if weth_arbitrage_rate > 60:
        mistral_fp_risk_factors.append(f"High WETH arbitrage rate ({weth_arbitrage_rate:.1f}%)")

    # Check if patterns are overly profitable (might be data errors)
    very_profitable = len(mistral_unknown[mistral_unknown['profit_eth'] > 10])
    if very_profitable > 0:
        mistral_fp_risk_factors.append(f"{very_profitable} extremely profitable patterns (>10 ETH)")

    # Check for simple patterns
    simple_patterns = len(mistral_unknown[mistral_unknown['num_swaps'] <= 3])
    simple_rate = simple_patterns / len(mistral_unknown) * 100
    if simple_rate > 80:
        mistral_fp_risk_factors.append(f"High simple pattern rate ({simple_rate:.1f}%)")

    print(f"Mistral Risk Factors:")
    if mistral_fp_risk_factors:
        for factor in mistral_fp_risk_factors:
            print(f"   • {factor}")
    else:
        print(f"   No major risk factors detected")

    # 6. MISTRAL FALSE NEGATIVE ASSESSMENT
    print(f"\nMISTRAL FALSE NEGATIVE RISK ASSESSMENT")
    print("=" * 50)

    # Estimate false negatives by looking at complex patterns marked as known
    complex_known_count = len(mistral_known[mistral_known['num_swaps'] >= 6])
    very_profitable_known = len(mistral_known[mistral_known['profit_eth'] > 5])

    print(f"Potential False Negative Indicators:")
    print(f"  Complex patterns (6+ swaps) marked KNOWN: {complex_known_count:,}")
    print(f"  Very profitable patterns (>5 ETH) marked KNOWN: {very_profitable_known:,}")

    # Compare with Qwen's findings
    qwen_complex = len(qwen_unknown[qwen_unknown['num_swaps'] >= 6])
    print(f"  Qwen found {qwen_complex:,} complex unknowns vs Mistral's {len(mistral_unknown):,} total unknowns")

    if complex_known_count > len(mistral_unknown) * 5:
        print(f"  WARNING: Many complex patterns marked as known - potential false negatives")

    # 7. BALANCED ASSESSMENT
    print(f"\nBALANCED MISTRAL ASSESSMENT")
    print("=" * 40)

    # Estimate Mistral's classification quality
    mistral_fp_estimate = 0
    mistral_fn_estimate = 0

    # False positive estimation
    if weth_arbitrage_rate > 70:
        mistral_fp_estimate += 20  # Standard WETH arbitrage shouldn't be unknown
    if simple_rate > 85:
        mistral_fp_estimate += 15  # Very simple patterns likely known

    # False negative estimation
    if complex_known_count > len(mistral_unknown) * 10:
        mistral_fn_estimate += 40  # Missing many complex patterns

    mistral_fn_estimate = min(mistral_fn_estimate, 70)  # Cap at 70%

    print(f"MISTRAL CLASSIFICATION ASSESSMENT:")
    print(f"   Estimated False Positive Rate: {mistral_fp_estimate}%")
    print(f"   Estimated False Negative Rate: {mistral_fn_estimate}%")

    if mistral_fp_estimate < 20 and mistral_fn_estimate < 30:
        mistral_quality = "HIGH PRECISION, MODERATE RECALL"
    elif mistral_fp_estimate < 30:
        mistral_quality = "GOOD PRECISION, LOW RECALL"
    else:
        mistral_quality = "MODERATE PRECISION, LOW RECALL"

    print(f"   Overall Assessment: {mistral_quality}")

    # Adjusted estimates
    mistral_true_unknowns = len(mistral_unknown) * (100 - mistral_fp_estimate) / 100
    print(f"\nADJUSTED MISTRAL ESTIMATES:")
    print(f"   Raw unknowns: {len(mistral_unknown):,}")
    print(f"   Estimated false positives: {len(mistral_unknown) - int(mistral_true_unknowns):,}")
    print(f"   Estimated true unknowns: {int(mistral_true_unknowns):,}")

    return {
        'mistral_fp_rate': mistral_fp_estimate,
        'mistral_fn_rate': mistral_fn_estimate,
        'mistral_true_unknowns': int(mistral_true_unknowns),
        'quality_assessment': mistral_quality
    }

def compare_balanced_assessment():

    print(f"\nBALANCED COMPARISON: BOTH MODELS ANALYZED")
    print("=" * 55)

    # Previous Qwen estimates (from earlier analysis)
    qwen_fp_rate = 30  # From previous analysis
    qwen_raw_unknowns = 1531
    qwen_true_unknowns = int(qwen_raw_unknowns * (100 - qwen_fp_rate) / 100)

    # Run Mistral analysis
    mistral_results = analyze_mistral_false_positives()

    print(f"\nSIDE-BY-SIDE COMPARISON:")
    print(f"{'Metric':<25} {'Qwen':<15} {'Mistral':<15} {'Notes'}")
    print("-" * 70)
    print(f"{'Raw Unknowns':<25} {qwen_raw_unknowns:<15} {65:<15} {'23.6x difference'}")
    print(f"{'Est. FP Rate':<25} {qwen_fp_rate}%{'':<10} {mistral_results['mistral_fp_rate']}%{'':<10} {'Both have issues'}")
    print(f"{'Est. True Unknowns':<25} {qwen_true_unknowns:<15} {mistral_results['mistral_true_unknowns']:<15} {'After FP correction'}")
    print(f"{'True Improvement':<25} {qwen_true_unknowns/mistral_results['mistral_true_unknowns']:.1f}x{'':<10} {'Baseline':<15} {'Realistic comparison'}")

    print(f"\nBALANCED CONCLUSIONS:")
    print(f"  • Qwen: High recall, moderate precision (30% FP rate)")
    print(f"  • Mistral: High precision, low recall (conservative)")
    print(f"  • True improvement: {qwen_true_unknowns/mistral_results['mistral_true_unknowns']:.1f}x (substantial but realistic)")
    print(f"  • Both models need validation for research use")

if __name__ == "__main__":
    compare_balanced_assessment()