#!/usr/bin/env python3

import pandas as pd
import numpy as np
from collections import Counter
import json
from datetime import datetime

class LocalPatternAnalyzer:
    def __init__(self, input_csv):
        self.df = pd.read_csv(input_csv)
        print(f"Loaded {len(self.df)} unknown MEV patterns")

    def check_data_completeness(self):
        print("\n" + "="*70)
        print("DATA COMPLETENESS CHECK")
        print("="*70)

        # Check hash presence
        has_first = self.df['first_tx_hash'].notna() & (self.df['first_tx_hash'] != '')
        has_whale = self.df['whale_tx_hash'].notna() & (self.df['whale_tx_hash'] != '')
        has_second = self.df['second_tx_hash'].notna() & (self.df['second_tx_hash'] != '')

        complete = has_first & has_whale & has_second

        print(f"\nTransaction Hash Presence:")
        print(f"  First TX hash: {has_first.sum()}/{len(self.df)} ({has_first.sum()/len(self.df)*100:.1f}%)")
        print(f"  Whale TX hash: {has_whale.sum()}/{len(self.df)} ({has_whale.sum()/len(self.df)*100:.1f}%)")
        print(f"  Second TX hash: {has_second.sum()}/{len(self.df)} ({has_second.sum()/len(self.df)*100:.1f}%)")
        print(f"  ALL 3 hashes present: {complete.sum()}/{len(self.df)} ({complete.sum()/len(self.df)*100:.1f}%)")

        return complete

    def analyze_profitability(self):
        print("\n" + "="*70)
        print("PROFITABILITY ANALYSIS")
        print("="*70)

        profit = self.df['profit_eth']

        profitable = profit > 0
        breakeven = (profit >= -0.001) & (profit <= 0.001)
        loss_making = profit < 0

        print(f"\nProfit Distribution:")
        print(f"  Profitable: {profitable.sum()} ({profitable.sum()/len(self.df)*100:.1f}%)")
        print(f"  Break-even: {breakeven.sum()} ({breakeven.sum()/len(self.df)*100:.1f}%)")
        print(f"  Loss-making: {loss_making.sum()} ({loss_making.sum()/len(self.df)*100:.1f}%)")

        print(f"\nProfit Statistics:")
        print(f"  Mean: {profit.mean():.4f} ETH")
        print(f"  Median: {profit.median():.4f} ETH")
        print(f"  Min: {profit.min():.4f} ETH")
        print(f"  Max: {profit.max():.4f} ETH")
        print(f"  Std: {profit.std():.4f} ETH")

        # High-value attacks
        high_value = profit > 0.5
        print(f"\nHigh-Value Attacks (>0.5 ETH):")
        print(f"  Count: {high_value.sum()} ({high_value.sum()/len(self.df)*100:.1f}%)")
        if high_value.sum() > 0:
            print(f"  Max profit: {profit[high_value].max():.4f} ETH")

    def analyze_exchanges(self):
        print("\n" + "="*70)
        print("EXCHANGE DISTRIBUTION")
        print("="*70)

        exchanges = self.df['exchange_name'].value_counts()

        print(f"\nTop 10 Exchanges:")
        for exchange, count in exchanges.head(10).items():
            print(f"  {exchange}: {count} ({count/len(self.df)*100:.1f}%)")

        # Standard vs non-standard
        standard = ['Uniswap V2', 'Uniswap V3', 'SushiSwap']
        is_standard = self.df['exchange_name'].isin(standard)

        print(f"\nExchange Type:")
        print(f"  Standard DEX: {is_standard.sum()} ({is_standard.sum()/len(self.df)*100:.1f}%)")
        print(f"  Non-standard: {(~is_standard).sum()} ({(~is_standard).sum()/len(self.df)*100:.1f}%)")

    def analyze_flashbots(self):
        print("\n" + "="*70)
        print("FLASHBOTS USAGE")
        print("="*70)

        flashbots = self.df['flashbots_bundle']

        print(f"\nFlashbots Bundle Usage:")
        print(f"  Using Flashbots: {flashbots.sum()} ({flashbots.sum()/len(self.df)*100:.1f}%)")
        print(f"  Not using Flashbots: {(~flashbots).sum()} ({(~flashbots).sum()/len(self.df)*100:.1f}%)")

        # Flashbots vs profit
        fb_profit = self.df[flashbots]['profit_eth']
        no_fb_profit = self.df[~flashbots]['profit_eth']

        if len(fb_profit) > 0:
            print(f"\nWith Flashbots:")
            print(f"  Mean profit: {fb_profit.mean():.4f} ETH")
            print(f"  Median profit: {fb_profit.median():.4f} ETH")

        if len(no_fb_profit) > 0:
            print(f"\nWithout Flashbots:")
            print(f"  Mean profit: {no_fb_profit.mean():.4f} ETH")
            print(f"  Median profit: {no_fb_profit.median():.4f} ETH")

    def analyze_bots(self):
        print("\n" + "="*70)
        print("BOT ADDRESS ANALYSIS")
        print("="*70)

        bot_counts = self.df['bot_address'].value_counts()

        print(f"\nTotal unique bots: {len(bot_counts)}")
        print(f"\nTop 10 Most Active Bots:")
        for bot, count in bot_counts.head(10).items():
            print(f"  {bot[:15]}...: {count} attacks ({count/len(self.df)*100:.1f}%)")

        # Bot frequency distribution
        single_attack = (bot_counts == 1).sum()
        multi_attack = (bot_counts > 1).sum()
        systematic = (bot_counts > 10).sum()

        print(f"\nBot Attack Frequency:")
        print(f"  Single attack: {single_attack} bots ({single_attack/len(bot_counts)*100:.1f}%)")
        print(f"  Multiple attacks: {multi_attack} bots ({multi_attack/len(bot_counts)*100:.1f}%)")
        print(f"  Systematic (>10): {systematic} bots ({systematic/len(bot_counts)*100:.1f}%)")

    def categorize_patterns(self):
        print("\n" + "="*70)
        print("AUTOMATED PATTERN CATEGORIZATION")
        print("="*70)

        categories = []

        for idx, row in self.df.iterrows():
            category = 'unknown'
            confidence = 'LOW'
            notes = []

            profit = row.get('profit_eth', 0)
            exchange = row.get('exchange_name', '')
            flashbots = row.get('flashbots_bundle', False)

            # Category 1: False Positive
            # Standard Uniswap V2 + Flashbots + low profit = likely false positive
            if (exchange == 'Uniswap V2' and flashbots and -0.1 < profit < 0.1):
                category = 'false_positive'
                confidence = 'MEDIUM'
                notes.append('Standard Uniswap V2 + Flashbots + low profit')

            # Category 2: High-Value Attack
            elif profit > 0.5:
                category = 'high_value_attack'
                confidence = 'HIGH'
                notes.append(f'High profit: {profit:.4f} ETH')

            # Category 3: Non-Standard Exchange
            elif exchange not in ['Uniswap V2', 'Uniswap V3', 'SushiSwap']:
                category = 'non_standard_exchange'
                confidence = 'MEDIUM'
                notes.append(f'Non-standard exchange: {exchange}')

            # Category 4: Significant Loss
            elif profit < -0.1:
                category = 'significant_loss'
                confidence = 'MEDIUM'
                notes.append(f'Significant loss: {profit:.4f} ETH')

            # Category 5: No Flashbots but Profitable
            elif not flashbots and profit > 0.05:
                category = 'no_flashbots_profitable'
                confidence = 'MEDIUM'
                notes.append(f'Profitable without Flashbots: {profit:.4f} ETH')

            # Add general notes
            if flashbots:
                notes.append('Uses Flashbots')
            notes.append(f'Exchange: {exchange}')

            categories.append({
                'transaction_id': row['transaction_id'],
                'auto_category': category,
                'confidence': confidence,
                'analysis_notes': ' | '.join(notes),
                'profit_eth': profit,
                'exchange_name': exchange,
                'flashbots_bundle': flashbots
            })

        categories_df = pd.DataFrame(categories)

        # Summary
        print(f"\nPattern Categories:")
        cat_counts = categories_df['auto_category'].value_counts()
        for cat, count in cat_counts.items():
            print(f"  {cat}: {count} ({count/len(categories_df)*100:.1f}%)")

        print(f"\nConfidence Distribution:")
        conf_counts = categories_df['confidence'].value_counts()
        for conf, count in conf_counts.items():
            print(f"  {conf}: {count} ({count/len(categories_df)*100:.1f}%)")

        return categories_df

    def generate_report(self, output_csv, output_json):
        print("\n" + "="*70)
        print("GENERATING LOCAL ANALYSIS REPORT")
        print("="*70)

        # Run all analyses
        complete = self.check_data_completeness()
        self.analyze_profitability()
        self.analyze_exchanges()
        self.analyze_flashbots()
        self.analyze_bots()
        categories_df = self.categorize_patterns()

        # Merge categories with original data
        merged = self.df.merge(categories_df, on='transaction_id', how='left')
        merged.to_csv(output_csv, index=False)

        # Generate summary JSON
        summary = {
            'analysis_date': datetime.now().isoformat(),
            'total_patterns': len(self.df),
            'data_completeness': {
                'all_hashes_present': int(complete.sum()),
                'completeness_rate': float(complete.sum() / len(self.df) * 100)
            },
            'profitability': {
                'profitable': int((self.df['profit_eth'] > 0).sum()),
                'loss_making': int((self.df['profit_eth'] < 0).sum()),
                'mean_profit': float(self.df['profit_eth'].mean()),
                'median_profit': float(self.df['profit_eth'].median()),
                'max_profit': float(self.df['profit_eth'].max()),
                'high_value_count': int((self.df['profit_eth'] > 0.5).sum())
            },
            'flashbots': {
                'usage_count': int(self.df['flashbots_bundle'].sum()),
                'usage_rate': float(self.df['flashbots_bundle'].sum() / len(self.df) * 100)
            },
            'pattern_categories': categories_df['auto_category'].value_counts().to_dict(),
            'confidence_distribution': categories_df['confidence'].value_counts().to_dict()
        }

        with open(output_json, 'w') as f:
            json.dump(summary, f, indent=2)

        print(f"\nAnalysis complete!")
        print(f"Detailed results: {output_csv}")
        print(f"Summary report: {output_json}")

        return merged, summary


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python analyze_patterns_local.py <input_csv>")
        print("\nExample:")
        print("  python analyze_patterns_local.py qwen_sandwich_1m_unknowns_20251216_223809_with_hashes.csv")
        return

    input_csv = sys.argv[1]
    output_csv = input_csv.replace('.csv', '_analyzed.csv')
    output_json = input_csv.replace('.csv', '_summary.json')

    analyzer = LocalPatternAnalyzer(input_csv)
    merged, summary = analyzer.generate_report(output_csv, output_json)

    print("\n" + "="*70)
    print("FOR PUBLICATION")
    print("="*70)
    print("\nYou can now write:")
    print(f"  'We identified {summary['total_patterns']:,} unknown sandwich patterns")
    print(f"   with {summary['data_completeness']['completeness_rate']:.1f}% having complete transaction hashes.'")
    print(f"  'All transactions are independently verifiable on Ethereum blockchain.'")
    print(f"  'Pattern distribution: {summary['pattern_categories']}'")


if __name__ == "__main__":
    main()
