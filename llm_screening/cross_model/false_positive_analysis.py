#!/usr/bin/env python3

import pandas as pd
import numpy as np
import re
from collections import Counter

def analyze_false_positives():

    print("FALSE POSITIVE ANALYSIS: Qwen vs Mistral Unknown Classifications")
    print("=" * 75)

    # Load datasets
    qwen_file = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Results/qwen_arbitrage_100k_20251014_171647.csv"
    mistral_file = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Mistral/Results/Arbitrage/results_arbitrage_100k_20250702_183505.csv"

    qwen_df = pd.read_csv(qwen_file)
    mistral_df = pd.read_csv(mistral_file)

    qwen_unknown = qwen_df[qwen_df['llm_classification'] == 'UNKNOWN']
    mistral_unknown = mistral_df[mistral_df['llm_classification'] == 'UNKNOWN']

    print(f"Dataset Overview:")
    print(f"  Qwen unknown: {len(qwen_unknown):,} patterns")
    print(f"  Mistral unknown: {len(mistral_unknown):,} patterns")
    print(f"  Ratio: {len(qwen_unknown)/len(mistral_unknown):.1f}x more")

    # 1. ANALYZE TOKEN PATTERNS
    print(f"\nTOKEN PATTERN ANALYSIS")
    print("=" * 50)

    def extract_tokens_from_description(desc):
        # Match token names in format "Token Name → Another Token"
        tokens = re.findall(r'([A-Za-z][A-Za-z0-9\s\.]+?)(?:\s→|\s\|)', desc)
        return [token.strip() for token in tokens if len(token.strip()) > 1]

    # Analyze token diversity
    qwen_tokens = []
    mistral_tokens = []

    for desc in qwen_unknown['description']:
        qwen_tokens.extend(extract_tokens_from_description(str(desc)))

    for desc in mistral_unknown['description']:
        mistral_tokens.extend(extract_tokens_from_description(str(desc)))

    qwen_token_counts = Counter(qwen_tokens)
    mistral_token_counts = Counter(mistral_tokens)

    print(f"Qwen Token Analysis:")
    print(f"  Unique tokens: {len(qwen_token_counts)}")
    print(f"  Most common tokens:")
    for token, count in qwen_token_counts.most_common(10):
        print(f"    {token}: {count} times")

    print(f"\nMistral Token Analysis:")
    print(f"  Unique tokens: {len(mistral_token_counts)}")
    print(f"  Most common tokens:")
    for token, count in mistral_token_counts.most_common(10):
        print(f"    {token}: {count} times")

    # 2. COMMON TOKENS ANALYSIS (Potential False Positives)
    print(f"\nPOTENTIAL FALSE POSITIVE INDICATORS")
    print("=" * 50)

    common_tokens = ['Wrapped Ether', 'Ether', 'WETH', 'ETH', 'USDC', 'USDT', 'DAI', 'Tether USD', 'USD Coin']

    qwen_common_count = 0
    qwen_total_unknown = len(qwen_unknown)

    for desc in qwen_unknown['description']:
        if any(token in str(desc) for token in common_tokens):
            qwen_common_count += 1

    mistral_common_count = 0
    mistral_total_unknown = len(mistral_unknown)

    for desc in mistral_unknown['description']:
        if any(token in str(desc) for token in common_tokens):
            mistral_common_count += 1

    qwen_common_rate = qwen_common_count / qwen_total_unknown * 100
    mistral_common_rate = mistral_common_count / mistral_total_unknown * 100

    print(f"Qwen patterns with common tokens:")
    print(f"  Count: {qwen_common_count:,}/{qwen_total_unknown:,} ({qwen_common_rate:.1f}%)")

    print(f"Mistral patterns with common tokens:")
    print(f"  Count: {mistral_common_count:,}/{mistral_total_unknown:,} ({mistral_common_rate:.1f}%)")

    if qwen_common_rate > mistral_common_rate * 2:
        print(f"  WARNING: Qwen may be over-classifying common token patterns as unknown")

    # 3. SWAP COMPLEXITY ANALYSIS
    print(f"\nSWAP COMPLEXITY ANALYSIS")
    print("=" * 40)

    qwen_swap_dist = qwen_unknown['num_swaps'].value_counts().sort_index()
    mistral_swap_dist = mistral_unknown['num_swaps'].value_counts().sort_index()

    print(f"Qwen swap distribution:")
    for swaps, count in qwen_swap_dist.items():
        percentage = count / len(qwen_unknown) * 100
        print(f"  {swaps} swaps: {count:,} ({percentage:.1f}%)")

    print(f"Mistral swap distribution:")
    for swaps, count in mistral_swap_dist.items():
        percentage = count / len(mistral_unknown) * 100
        print(f"  {swaps} swaps: {count:,} ({percentage:.1f}%)")

    # Check if Qwen is marking simple 2-3 swap patterns as unknown
    qwen_simple = len(qwen_unknown[qwen_unknown['num_swaps'] <= 3])
    qwen_simple_rate = qwen_simple / len(qwen_unknown) * 100

    mistral_simple = len(mistral_unknown[mistral_unknown['num_swaps'] <= 3])
    mistral_simple_rate = mistral_simple / len(mistral_unknown) * 100

    print(f"\nSimple patterns (≤3 swaps) marked as unknown:")
    print(f"  Qwen: {qwen_simple:,} ({qwen_simple_rate:.1f}%)")
    print(f"  Mistral: {mistral_simple:,} ({mistral_simple_rate:.1f}%)")

    if qwen_simple_rate > 70:
        print(f"  WARNING: High rate of simple patterns marked as unknown by Qwen")

    # 4. PROFIT PATTERN ANALYSIS
    print(f"\nPROFIT PATTERN ANALYSIS")
    print("=" * 40)

    # Check for patterns that are clearly standard arbitrage based on profit behavior
    qwen_profitable = len(qwen_unknown[qwen_unknown['profit_eth'] > 0])
    qwen_profitable_rate = qwen_profitable / len(qwen_unknown) * 100

    mistral_profitable = len(mistral_unknown[mistral_unknown['profit_eth'] > 0])
    mistral_profitable_rate = mistral_profitable / len(mistral_unknown) * 100

    print(f"Qwen profitable unknown patterns:")
    print(f"  Count: {qwen_profitable:,}/{len(qwen_unknown):,} ({qwen_profitable_rate:.1f}%)")

    print(f"Mistral profitable unknown patterns:")
    print(f"  Count: {mistral_profitable:,}/{len(mistral_unknown):,} ({mistral_profitable_rate:.1f}%)")

    # 5. DESCRIPTION PATTERN ANALYSIS
    print(f"\nDESCRIPTION PATTERN ANALYSIS")
    print("=" * 45)

    # Check for repetitive or standard-looking patterns
    def analyze_description_patterns(df, model_name):
        descriptions = df['description'].tolist()

        # Common arbitrage indicators
        standard_indicators = [
            'Wrapped Ether →',
            'USDC →',
            'DAI →',
            'USDT →',
            '→ Wrapped Ether',
            '→ USDC',
            '→ DAI'
        ]

        standard_count = 0
        for desc in descriptions:
            if any(indicator in str(desc) for indicator in standard_indicators):
                standard_count += 1

        standard_rate = standard_count / len(descriptions) * 100

        print(f"  {model_name} patterns with standard arbitrage indicators:")
        print(f"    Count: {standard_count:,}/{len(descriptions):,} ({standard_rate:.1f}%)")

        return standard_rate

    qwen_standard_rate = analyze_description_patterns(qwen_unknown, "Qwen")
    mistral_standard_rate = analyze_description_patterns(mistral_unknown, "Mistral")

    # 6. SAMPLE ANALYSIS FOR MANUAL VALIDATION
    print(f"\nSAMPLE ANALYSIS FOR MANUAL VALIDATION")
    print("=" * 55)

    print(f"Qwen patterns that might be FALSE POSITIVES (standard arbitrage):")
    print(f"   (Simple swaps with common tokens)")

    # Filter for potentially standard patterns
    potential_fp = qwen_unknown[
        (qwen_unknown['num_swaps'] <= 3) &
        (qwen_unknown['description'].str.contains('Wrapped Ether|USDC|DAI|USDT', na=False))
    ].head(10)

    for idx, row in potential_fp.iterrows():
        print(f"   • {row['description'][:100]}...")

    print(f"\nQwen patterns that might be TRUE UNKNOWNS (novel arbitrage):")
    print(f"   (Complex swaps with obscure tokens)")

    # Filter for genuinely novel patterns
    potential_unknown = qwen_unknown[
        (qwen_unknown['num_swaps'] >= 4) &
        (~qwen_unknown['description'].str.contains('Wrapped Ether|USDC|DAI|USDT', na=False))
    ].head(10)

    for idx, row in potential_unknown.iterrows():
        print(f"   • {row['description'][:100]}...")

    # 7. FALSE POSITIVE RISK ASSESSMENT
    print(f"\nFALSE POSITIVE RISK ASSESSMENT")
    print("=" * 50)

    risk_factors = []

    if qwen_common_rate > mistral_common_rate * 2:
        risk_factors.append("High rate of common token patterns")

    if qwen_simple_rate > 70:
        risk_factors.append("Many simple 2-3 swap patterns marked unknown")

    if qwen_standard_rate > 50:
        risk_factors.append("High rate of standard arbitrage indicators")

    if len(qwen_unknown) > len(mistral_unknown) * 20:
        risk_factors.append("Extremely high detection rate vs baseline")

    print(f"Risk Factors Identified:")
    if risk_factors:
        for factor in risk_factors:
            print(f"   • {factor}")
    else:
        print(f"   No major risk factors detected")

    # Calculate estimated false positive rate
    estimated_fp_rate = 0

    if qwen_common_rate > 40:
        estimated_fp_rate += 30
    if qwen_simple_rate > 60:
        estimated_fp_rate += 25
    if qwen_standard_rate > 50:
        estimated_fp_rate += 20

    estimated_fp_rate = min(estimated_fp_rate, 80)  # Cap at 80%

    print(f"\nESTIMATED FALSE POSITIVE RATE:")
    print(f"   Estimated FP rate: {estimated_fp_rate}%")

    if estimated_fp_rate > 50:
        confidence = "LOW - High false positive risk"
    elif estimated_fp_rate > 25:
        confidence = "MODERATE - Some false positives likely"
    else:
        confidence = "HIGH - Low false positive risk"

    print(f"   Confidence in results: {confidence}")

    # 8. RECOMMENDATIONS
    print(f"\nRECOMMENDATIONS")
    print("=" * 25)

    print(f"Validation Strategy:")
    print(f"   1. Manual review of 100-200 Qwen 'unknown' patterns")
    print(f"   2. Focus on simple (≤3 swap) patterns with common tokens")
    print(f"   3. Compare with known arbitrage databases")
    print(f"   4. Expert MEV researcher validation")

    print(f"\nQuality Improvement:")
    print(f"   1. Refine Qwen classification prompt for higher precision")
    print(f"   2. Add explicit criteria for 'known' arbitrage patterns")
    print(f"   3. Implement confidence scoring for classifications")
    print(f"   4. Cross-validate with multiple models")

    true_unknown_estimate = len(qwen_unknown) * (100 - estimated_fp_rate) / 100
    print(f"\nADJUSTED ESTIMATES:")
    print(f"   Raw Qwen unknowns: {len(qwen_unknown):,}")
    print(f"   Estimated false positives: {len(qwen_unknown) - int(true_unknown_estimate):,}")
    print(f"   Estimated true unknowns: {int(true_unknown_estimate):,}")
    print(f"   Adjusted advantage over Mistral: {true_unknown_estimate/len(mistral_unknown):.1f}x")

if __name__ == "__main__":
    analyze_false_positives()