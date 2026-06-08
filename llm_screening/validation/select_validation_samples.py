
import pandas as pd
import numpy as np

def select_validation_samples():

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

    print(f"\nRisk Categories:")
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

    print(f"\nValidation samples saved:")
    print(f"  High risk: {len(high_sample)} samples")
    print(f"  Medium risk: {len(medium_sample)} samples")
    print(f"  Low risk: {len(low_sample)} samples")
    print(f"  Total for validation: {len(high_sample) + len(medium_sample) + len(low_sample)}")

    return high_sample, medium_sample, low_sample

if __name__ == "__main__":
    select_validation_samples()
    