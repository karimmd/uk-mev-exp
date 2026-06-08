#!/usr/bin/env python3

def create_improved_classification_prompt():

    return """You are an expert blockchain analyst specializing in MEV (Maximal Extractible Value) detection.

Analyze Ethereum transactions and classify them as:
1. KNOWN MEV - Clear, identifiable MEV patterns (including failed attempts)
2. UNKNOWN MEV - Genuinely novel patterns you cannot categorize as known strategies
3. NORMAL - Regular transactions without MEV characteristics

CRITICAL: Use VERY STRICT criteria for UNKNOWN classification. Only mark as UNKNOWN if 90%+ confident it represents a genuinely novel strategy.

=== KNOWN ARBITRAGE PATTERNS (Comprehensive List) ===

STANDARD TOKEN ARBITRAGE:
- ANY patterns involving WETH, ETH, USDC, USDT, DAI, WBTC, LINK, UNI
- Cross-DEX arbitrage between Uniswap, SushiSwap, Balancer, Curve
- Multi-hop swaps following established routing (A→B→C→A)
- Flash loan arbitrage using Aave, dYdX, Compound
- Failed arbitrage attempts using standard methods
- Profitable OR unprofitable execution of known token pair strategies

ESTABLISHED DEFI PROTOCOLS:
- Bancor Network Token arbitrage (well-established)
- Synthetix network arbitrage
- Yearn Finance vault arbitrage
- Compound/Aave lending arbitrage
- Standard governance token arbitrage

COMMON ALTCOIN ARBITRAGE:
- Established altcoins with known liquidity pools
- Standard ERC-20 token swaps
- Gaming tokens with established DEX presence
- Stablecoin arbitrage between different protocols

TYPICAL COMPLEXITY PATTERNS:
- 2-3 swap arbitrage (almost always known)
- Simple profitable/unprofitable cross-DEX trades
- Standard MEV bot behavior patterns

=== UNKNOWN ARBITRAGE CRITERIA (Very Selective) ===

ONLY mark as UNKNOWN if ALL of the following apply:
1. Involves completely novel protocol combinations NOT seen in standard arbitrage
2. Uses cutting-edge/experimental tokens launched in last 6 months
3. Demonstrates unclear or revolutionary profit extraction mechanisms
4. Shows sophisticated multi-protocol coordination (6+ unique protocols)
5. Employs genuinely new DeFi primitives or mechanisms

EXAMPLES OF TRUE UNKNOWNS:
- Novel NFT-DeFi arbitrage bridges
- Experimental layer-2 cross-chain arbitrage
- Brand new protocol mechanisms not documented
- Revolutionary multi-dimensional arbitrage strategies
- Sophisticated social token arbitrage with new mechanisms

=== CLASSIFICATION GUIDELINES ===

ASK YOURSELF:
- "Have I seen this type of arbitrage strategy before in MEV literature?"
- "Are these token pairs commonly arbitraged?"
- "Is this a standard profit extraction method?"
- "Would an experienced MEV researcher recognize this pattern?"

IF YES to any of the above → Classify as KNOWN

PROFIT/LOSS IRRELEVANT:
- Failed known strategies are still KNOWN
- Successful novel strategies might be UNKNOWN
- Profit amount does not determine classification

COMPLEXITY THRESHOLD:
- 2-3 swaps: Almost certainly KNOWN unless revolutionary tokens
- 4-5 swaps: Likely KNOWN unless novel protocol combination
- 6+ swaps: Examine closely for genuine novelty

CONFIDENCE REQUIREMENT:
- Only mark UNKNOWN if 90%+ confident it's genuinely novel
- When in doubt, classify as KNOWN
- Better to miss a few unknowns than create false positives

Respond with ONLY: KNOWN, UNKNOWN, or NORMAL

REMEMBER: Most arbitrage (99%+) should be classified as KNOWN. Unknown patterns are exceptionally rare."""

def create_validation_sample_selector():

    validation_script = '''
import pandas as pd
import numpy as np

def select_validation_samples():
    """Select strategic samples for manual validation"""

    # Load Qwen results
    qwen_file = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Qwen/Results/qwen_arbitrage_100k_20251014_171647.csv"
    df = pd.read_csv(qwen_file)
    unknown_df = df[df['llm_classification'] == 'UNKNOWN']

    print(f"VALIDATION SAMPLE SELECTION")
    print(f"Total unknown patterns: {len(unknown_df):,}")

    # HIGH RISK samples (likely false positives)
    high_risk = unknown_df[
        (unknown_df['num_swaps'] <= 3) &
        (unknown_df['description'].str.contains('Wrapped Ether|WETH|USDC|USDT|DAI', na=False, case=False))
    ]

    # MEDIUM RISK samples
    medium_risk = unknown_df[
        (unknown_df['num_swaps'].between(4, 5)) &
        (unknown_df['description'].str.contains('Bancor|Synthetix|Compound|Uniswap', na=False, case=False))
    ]

    # LOW RISK samples (likely true unknowns)
    low_risk = unknown_df[
        (unknown_df['num_swaps'] >= 6) &
        (~unknown_df['description'].str.contains('Wrapped Ether|WETH|USDC|USDT|DAI|Bancor', na=False, case=False))
    ]

    print(f"\\nRisk Categories:")
    print(f"  High risk (likely FP): {len(high_risk):,}")
    print(f"  Medium risk: {len(medium_risk):,}")
    print(f"  Low risk (likely true): {len(low_risk):,}")

    # Select samples
    high_sample = high_risk.sample(min(200, len(high_risk)), random_state=42)
    medium_sample = medium_risk.sample(min(100, len(medium_risk)), random_state=42)
    low_sample = low_risk.sample(min(50, len(low_risk)), random_state=42)

    # Save validation samples
    validation_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Validation/"
    import os
    os.makedirs(validation_dir, exist_ok=True)

    high_sample.to_csv(f"{validation_dir}high_risk_validation_sample.csv", index=False)
    medium_sample.to_csv(f"{validation_dir}medium_risk_validation_sample.csv", index=False)
    low_sample.to_csv(f"{validation_dir}low_risk_validation_sample.csv", index=False)

    print(f"\\nValidation samples saved:")
    print(f"  High risk: {len(high_sample)} samples")
    print(f"  Medium risk: {len(medium_sample)} samples")
    print(f"  Low risk: {len(low_sample)} samples")
    print(f"  Total for validation: {len(high_sample) + len(medium_sample) + len(low_sample)}")

    return high_sample, medium_sample, low_sample

if __name__ == "__main__":
    select_validation_samples()
    '''

    return validation_script

def create_expert_validation_template():

    template = '''
# MEV Pattern Validation Template

## Instructions
For each pattern, please assess:
1. **Known/Unknown**: Is this a known MEV strategy?
2. **Confidence**: How confident are you (1-5 scale)?
3. **Category**: What type of strategy is this?
4. **Comments**: Any additional observations

## Validation Criteria

### KNOWN Indicators:
- Uses standard token pairs (WETH, USDC, USDT, DAI, etc.)
- Follows established arbitrage routes
- Uses well-known DeFi protocols
- Matches documented MEV strategies
- Simple 2-3 swap patterns

### UNKNOWN Indicators:
- Novel token combinations never seen before
- New protocol mechanisms
- Revolutionary arbitrage strategies
- Experimental cross-chain techniques
- Sophisticated 6+ protocol coordination

## Sample Pattern Analysis

**Pattern ID**: [AUTO_FILLED]
**Description**: [AUTO_FILLED]
**Swaps**: [AUTO_FILLED]
**Profit**: [AUTO_FILLED]

### Assessment:
- [ ] KNOWN - This is a recognized MEV strategy
- [ ] UNKNOWN - This represents a novel approach
- [ ] UNCERTAIN - Requires further investigation

**Confidence** (1=unsure, 5=certain): ___/5

**Category**:
- [ ] Standard cross-DEX arbitrage
- [ ] Flash loan arbitrage
- [ ] Multi-hop token arbitrage
- [ ] Protocol-specific arbitrage
- [ ] Novel arbitrage mechanism
- [ ] Failed arbitrage attempt
- [ ] Other: _______________

**Comments**:
_______________________________________________________
_______________________________________________________

**Validator**: _________________ **Date**: _____________
'''

    return template

def main():

    print("IMPROVED QWEN CLASSIFICATION FRAMEWORK")
    print("=" * 55)

    # Save improved prompt
    with open("<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Prompts/improved_qwen_prompt.txt", "w") as f:
        f.write(create_improved_classification_prompt())

    # Save validation sample selector
    with open("<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Validation/select_validation_samples.py", "w") as f:
        f.write(create_validation_sample_selector())

    # Save expert validation template
    with open("<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments/Validation/expert_validation_template.md", "w") as f:
        f.write(create_expert_validation_template())

    print("Framework components created:")
    print("   1. Improved classification prompt")
    print("   2. Validation sample selector")
    print("   3. Expert validation template")

    print("\\nNext Steps:")
    print("   1. Re-run Qwen with improved prompt")
    print("   2. Select validation samples")
    print("   3. Conduct expert validation")
    print("   4. Calculate actual false positive rate")
    print("   5. Publish validated results")

if __name__ == "__main__":
    main()