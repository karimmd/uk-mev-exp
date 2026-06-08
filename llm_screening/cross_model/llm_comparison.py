#!/usr/bin/env python3

import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
import logging

class LLMComparisonFramework:
    def __init__(self):
        self.base_dir = "<PROJECT_ROOT>/Part-2_Unknown_Mev/Experiments"
        self.mistral_results_dir = f"{self.base_dir}/Mistral/Results"
        self.qwen_results_dir = f"{self.base_dir}/Qwen/Results"
        self.comparison_dir = f"{self.base_dir}/Comparison"

        # Setup logging
        self.setup_logging()

        # Results storage
        self.mistral_results = None
        self.qwen_results = None
        self.comparison_results = {}

    def setup_logging(self):
        os.makedirs(self.comparison_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"{self.comparison_dir}/comparison_{timestamp}.log"

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger(__name__)
        self.logger.info("Multi-LLM Comparison Framework Initialized")

    def load_results(self, mistral_file=None, qwen_file=None):
        self.logger.info("Loading model results...")

        # Auto-detect latest files if not specified
        if mistral_file is None:
            mistral_files = [f for f in os.listdir(self.mistral_results_dir) if f.startswith('results_arbitrage_20k')]
            if mistral_files:
                mistral_file = max(mistral_files)  # Get latest
                self.logger.info(f"Auto-detected Mistral file: {mistral_file}")

        if qwen_file is None:
            qwen_files = [f for f in os.listdir(self.qwen_results_dir) if f.startswith('qwen_arbitrage_20k')]
            if qwen_files:
                qwen_file = max(qwen_files)  # Get latest
                self.logger.info(f"Auto-detected Qwen file: {qwen_file}")

        # Load Mistral results
        try:
            mistral_path = os.path.join(self.mistral_results_dir, mistral_file)
            self.mistral_results = pd.read_csv(mistral_path)
            self.mistral_results['model'] = 'mistral-7b'
            self.logger.info(f"Loaded Mistral results: {len(self.mistral_results):,} transactions")
        except Exception as e:
            self.logger.error(f"Failed to load Mistral results: {e}")
            return False

        # Load Qwen results
        try:
            qwen_path = os.path.join(self.qwen_results_dir, qwen_file)
            self.qwen_results = pd.read_csv(qwen_path)
            self.qwen_results['model'] = 'qwen2.5-7b'
            self.logger.info(f"Loaded Qwen results: {len(self.qwen_results):,} transactions")
        except Exception as e:
            self.logger.error(f"Failed to load Qwen results: {e}")
            return False

        return True

    def calculate_basic_metrics(self):
        self.logger.info("Calculating basic comparison metrics...")

        results = {}

        for name, df in [("Mistral-7B", self.mistral_results), ("Qwen2.5-7B", self.qwen_results)]:
            total = len(df)
            classification_counts = df['llm_classification'].value_counts()

            unknown_count = classification_counts.get('UNKNOWN', 0)
            known_count = classification_counts.get('KNOWN', 0)
            normal_count = classification_counts.get('NORMAL', 0)
            error_count = classification_counts.get('ERROR', 0)

            results[name] = {
                'total_transactions': total,
                'unknown_count': unknown_count,
                'unknown_rate': (unknown_count / total * 100) if total > 0 else 0,
                'known_count': known_count,
                'known_rate': (known_count / total * 100) if total > 0 else 0,
                'normal_count': normal_count,
                'normal_rate': (normal_count / total * 100) if total > 0 else 0,
                'error_count': error_count,
                'error_rate': (error_count / total * 100) if total > 0 else 0
            }

        self.comparison_results['basic_metrics'] = results
        return results

    def analyze_unknown_patterns(self):
        self.logger.info("Analyzing unknown pattern characteristics...")

        mistral_unknown = self.mistral_results[self.mistral_results['llm_classification'] == 'UNKNOWN']
        qwen_unknown = self.qwen_results[self.qwen_results['llm_classification'] == 'UNKNOWN']

        analysis = {
            'mistral_unknown': {
                'count': len(mistral_unknown),
                'avg_profit': mistral_unknown['profit_eth'].mean() if len(mistral_unknown) > 0 else 0,
                'avg_cost': mistral_unknown['cost_eth'].mean() if len(mistral_unknown) > 0 else 0,
                'avg_swaps': mistral_unknown['num_swaps'].mean() if len(mistral_unknown) > 0 else 0,
                'profit_std': mistral_unknown['profit_eth'].std() if len(mistral_unknown) > 0 else 0
            },
            'qwen_unknown': {
                'count': len(qwen_unknown),
                'avg_profit': qwen_unknown['profit_eth'].mean() if len(qwen_unknown) > 0 else 0,
                'avg_cost': qwen_unknown['cost_eth'].mean() if len(qwen_unknown) > 0 else 0,
                'avg_swaps': qwen_unknown['num_swaps'].mean() if len(qwen_unknown) > 0 else 0,
                'profit_std': qwen_unknown['profit_eth'].std() if len(qwen_unknown) > 0 else 0
            }
        }

        self.comparison_results['unknown_analysis'] = analysis
        return analysis

    def find_overlapping_transactions(self):
        self.logger.info("Finding overlapping and differing classifications...")

        # Merge on transaction identifiers (assuming same dataset)
        merged = pd.merge(
            self.mistral_results[['transaction_id', 'llm_classification', 'profit_eth', 'num_swaps']],
            self.qwen_results[['transaction_id', 'llm_classification', 'profit_eth', 'num_swaps']],
            on='transaction_id',
            suffixes=('_mistral', '_qwen'),
            how='inner'
        )

        # Find disagreements
        disagreements = merged[merged['llm_classification_mistral'] != merged['llm_classification_qwen']]

        # Specific interesting cases
        mistral_unknown_qwen_known = disagreements[
            (disagreements['llm_classification_mistral'] == 'UNKNOWN') &
            (disagreements['llm_classification_qwen'] == 'KNOWN')
        ]

        qwen_unknown_mistral_known = disagreements[
            (disagreements['llm_classification_mistral'] == 'KNOWN') &
            (disagreements['llm_classification_qwen'] == 'UNKNOWN')
        ]

        overlap_analysis = {
            'total_overlap': len(merged),
            'total_disagreements': len(disagreements),
            'disagreement_rate': len(disagreements) / len(merged) * 100 if len(merged) > 0 else 0,
            'mistral_unknown_qwen_known': len(mistral_unknown_qwen_known),
            'qwen_unknown_mistral_known': len(qwen_unknown_mistral_known),
            'interesting_cases': {
                'mistral_only_unknown': mistral_unknown_qwen_known.head(3).to_dict('records'),
                'qwen_only_unknown': qwen_unknown_mistral_known.head(3).to_dict('records')
            }
        }

        self.comparison_results['overlap_analysis'] = overlap_analysis
        return overlap_analysis

    def generate_comparison_report(self):
        self.logger.info("Generating comprehensive comparison report...")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"{self.comparison_dir}/llm_comparison_report_{timestamp}.md"

        basic = self.comparison_results['basic_metrics']
        unknown = self.comparison_results['unknown_analysis']
        overlap = self.comparison_results['overlap_analysis']

        report = f"""# Multi-LLM MEV Detection Comparison Report

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Executive Summary

**Models Compared:**
- Mistral-7B-Instruct-v0.1 (Baseline)
- Qwen2.5-7B-Instruct (New)

**Dataset:** 20K Arbitrage Transactions (same sample, random_state=42)

## Performance Comparison

### Classification Results

| Model | Unknown | Known | Normal | Error |
|-------|---------|-------|--------|-------|
| Mistral-7B | {basic['Mistral-7B']['unknown_count']:,} ({basic['Mistral-7B']['unknown_rate']:.3f}%) | {basic['Mistral-7B']['known_count']:,} ({basic['Mistral-7B']['known_rate']:.1f}%) | {basic['Mistral-7B']['normal_count']:,} ({basic['Mistral-7B']['normal_rate']:.1f}%) | {basic['Mistral-7B']['error_count']:,} ({basic['Mistral-7B']['error_rate']:.2f}%) |
| Qwen2.5-7B | {basic['Qwen2.5-7B']['unknown_count']:,} ({basic['Qwen2.5-7B']['unknown_rate']:.3f}%) | {basic['Qwen2.5-7B']['known_count']:,} ({basic['Qwen2.5-7B']['known_rate']:.1f}%) | {basic['Qwen2.5-7B']['normal_count']:,} ({basic['Qwen2.5-7B']['normal_rate']:.1f}%) | {basic['Qwen2.5-7B']['error_count']:,} ({basic['Qwen2.5-7B']['error_rate']:.2f}%) |

### Unknown Detection Performance

**Mistral-7B:**
- Unknown rate: {basic['Mistral-7B']['unknown_rate']:.3f}%
- Average profit: {unknown['mistral_unknown']['avg_profit']:.6f} ETH
- Average swaps: {unknown['mistral_unknown']['avg_swaps']:.1f}

**Qwen2.5-7B:**
- Unknown rate: {basic['Qwen2.5-7B']['unknown_rate']:.3f}%
- Average profit: {unknown['qwen_unknown']['avg_profit']:.6f} ETH
- Average swaps: {unknown['qwen_unknown']['avg_swaps']:.1f}

### Model Agreement Analysis

- Total overlapping transactions: {overlap['total_overlap']:,}
- Disagreements: {overlap['total_disagreements']:,} ({overlap['disagreement_rate']:.1f}%)
- Mistral found unknown, Qwen found known: {overlap['mistral_unknown_qwen_known']:,}
- Qwen found unknown, Mistral found known: {overlap['qwen_unknown_mistral_known']:,}

## Key Findings

1. **Unknown Detection Rate:**
   {f"- Qwen2.5 outperformed Mistral by {((basic['Qwen2.5-7B']['unknown_rate'] - basic['Mistral-7B']['unknown_rate']) / basic['Mistral-7B']['unknown_rate'] * 100):.1f}%" if basic['Mistral-7B']['unknown_rate'] > 0 and basic['Qwen2.5-7B']['unknown_rate'] > basic['Mistral-7B']['unknown_rate'] else f"- Mistral outperformed Qwen2.5 by {((basic['Mistral-7B']['unknown_rate'] - basic['Qwen2.5-7B']['unknown_rate']) / basic['Mistral-7B']['unknown_rate'] * 100):.1f}%" if basic['Mistral-7B']['unknown_rate'] > 0 else "- Similar performance"}

2. **Pattern Characteristics:**
   - Different models may identify different types of unknown patterns
   - Profit distributions and complexity vary between models

3. **Research Implications:**
   - Multi-model ensemble could improve unknown detection
   - Model-specific biases in pattern recognition

## Recommendations

1. **For Production:** {"Use Qwen2.5-7B for better unknown detection" if basic['Qwen2.5-7B']['unknown_rate'] > basic['Mistral-7B']['unknown_rate'] else "Continue with Mistral-7B as baseline"}
2. **For Research:** Investigate transactions where models disagree
3. **For Scale:** Consider ensemble approach combining both models

## Files Generated

- Comparison results: `{self.comparison_dir}/comparison_results_{timestamp}.json`
- Detailed analysis: `{self.comparison_dir}/detailed_analysis_{timestamp}.csv`

"""

        with open(report_file, 'w') as f:
            f.write(report)

        # Save detailed results as JSON
        results_file = f"{self.comparison_dir}/comparison_results_{timestamp}.json"
        with open(results_file, 'w') as f:
            json.dump(self.comparison_results, f, indent=2, default=str)

        self.logger.info(f"Report saved to: {report_file}")
        self.logger.info(f"Results saved to: {results_file}")

        return report_file, results_file

    def run_full_comparison(self, mistral_file=None, qwen_file=None):
        self.logger.info("Starting full LLM comparison analysis...")

        # Load results
        if not self.load_results(mistral_file, qwen_file):
            self.logger.error("Failed to load results. Aborting comparison.")
            return False

        # Run analyses
        self.calculate_basic_metrics()
        self.analyze_unknown_patterns()
        self.find_overlapping_transactions()

        # Generate report
        report_file, results_file = self.generate_comparison_report()

        # Log summary
        basic = self.comparison_results['basic_metrics']

        self.logger.info("\\nCOMPARISON SUMMARY")
        self.logger.info("=" * 50)
        self.logger.info(f"Mistral-7B unknown rate: {basic['Mistral-7B']['unknown_rate']:.3f}%")
        self.logger.info(f"Qwen2.5-7B unknown rate: {basic['Qwen2.5-7B']['unknown_rate']:.3f}%")

        if basic['Qwen2.5-7B']['unknown_rate'] > basic['Mistral-7B']['unknown_rate']:
            improvement = ((basic['Qwen2.5-7B']['unknown_rate'] - basic['Mistral-7B']['unknown_rate']) / basic['Mistral-7B']['unknown_rate'] * 100) if basic['Mistral-7B']['unknown_rate'] > 0 else 0
            self.logger.info(f"Qwen2.5 outperformed Mistral by {improvement:.1f}%")
        else:
            self.logger.info(f"Mistral performed better or similar to Qwen2.5")

        self.logger.info(f"Full report: {report_file}")
        self.logger.info("Comparison analysis completed!")

        return True

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Multi-LLM MEV Detection Comparison')
    parser.add_argument('--mistral-file', type=str, help='Specific Mistral results file')
    parser.add_argument('--qwen-file', type=str, help='Specific Qwen results file')
    args = parser.parse_args()

    # Run comparison
    framework = LLMComparisonFramework()
    success = framework.run_full_comparison(args.mistral_file, args.qwen_file)

    if not success:
        print("Comparison failed. Check logs for details.")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())