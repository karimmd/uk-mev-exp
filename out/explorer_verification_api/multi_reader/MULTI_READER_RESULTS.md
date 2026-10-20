# Multi-reader explorer validation, protocol v1, scored 2026-10-19T20:11:34+0800

Plan: MULTI_READER_PLAN.md (hashes in MULTI_READER_REGISTRATION.txt). Readers:
- cc_sonnet: claude-sonnet-5-5 (Claude Code, earlier reading); judgments 459 of 459; refusals 0; tokens in 0, out 0, 11.95 USD as recorded
- sonnet: claude-sonnet-5-5 (API); judgments 459 of 459; refusals 0; tokens in 1455253, out 410661, about 7.02 USD at list prices
- opus55: claude-opus-5-5 (API); judgments 459 of 459; refusals 0; tokens in 1455253, out 371188, about 13.24 USD at list prices
- deepseek: DeepSeek-V4.1-Flash (API); judgments 450 of 459; refusals 0; tokens in 1127988, out 3589710

Coverage per sample (judgments / cards): f1b 200/200/200/198 of 200; sym100 100/100/100/100 of 100; rej53 53/53/53/53 of 53; arb106 106/106/106/99 of 106

## 1. Per reader and per sample: called MEV (Q1 yes), supported (Q1 yes and Q2 yes), agreement with REFEREE (original witness), actor

| sample | set | reader | n | Q1 yes | supported | agree N2 | kappa N2 | agree W2 | actor match |
|---|---|---|---:|---|---|---|---:|---|---|
| f1b | missed | cc_sonnet | 100 | 98/100 = 98.0% [93.0, 99.4] | 81/100 = 81.0% [72.2, 87.5] | 60.0% (60) | -0.01 | 75.0% (75 of 100) | 98/100 |
| f1b | missed | sonnet | 100 | 98/100 = 98.0% [93.0, 99.4] | 83/100 = 83.0% [74.5, 89.1] | 62.0% (62) | 0.01 | 77.0% (77 of 100) | 98/100 |
| f1b | missed | opus55 | 100 | 98/100 = 98.0% [93.0, 99.4] | 85/100 = 85.0% [76.7, 90.7] | 64.0% (64) | 0.03 | 79.0% (79 of 100) | 98/100 |
| f1b | missed | deepseek | 100 | 98/100 = 98.0% [93.0, 99.4] | 90/100 = 90.0% [82.6, 94.5] | 66.0% (66) | 0.01 | 81.0% (81 of 100) | 98/100 |
| f1b | reported | cc_sonnet | 50 | 50/50 = 100.0% [92.9, 100.0] | 46/50 = 92.0% [81.2, 96.8] | 90.0% (45) | 0.34 | 90.0% (45 of 50) | 50/50 |
| f1b | reported | sonnet | 50 | 50/50 = 100.0% [92.9, 100.0] | 46/50 = 92.0% [81.2, 96.8] | 90.0% (45) | 0.34 | 90.0% (45 of 50) | 50/50 |
| f1b | reported | opus55 | 50 | 50/50 = 100.0% [92.9, 100.0] | 46/50 = 92.0% [81.2, 96.8] | 90.0% (45) | 0.34 | 90.0% (45 of 50) | 50/50 |
| f1b | reported | deepseek | 50 | 50/50 = 100.0% [92.9, 100.0] | 48/50 = 96.0% [86.5, 98.9] | 90.0% (45) | 0.13 | 90.0% (45 of 50) | 50/50 |
| f1b | comparison | cc_sonnet | 50 | 15/50 = 30.0% [19.1, 43.8] | 13/50 = 26.0% [15.9, 39.6] | 94.0% (47) | 0.85 | 94.0% (47 of 50) | 24/50 |
| f1b | comparison | sonnet | 50 | 14/50 = 28.0% [17.5, 41.7] | 11/50 = 22.0% [12.8, 35.2] | 94.0% (47) | 0.85 | 94.0% (47 of 50) | 20/50 |
| f1b | comparison | opus55 | 50 | 15/50 = 30.0% [19.1, 43.8] | 13/50 = 26.0% [15.9, 39.6] | 94.0% (47) | 0.85 | 94.0% (47 of 50) | 29/50 |
| f1b | comparison | deepseek | 48 | 3/48 = 6.2% [2.1, 16.8] | 3/48 = 6.2% [2.1, 16.8] | 79.2% (38) | 0.31 | 79.2% (38 of 48) | 25/48 |
| sym100 | missed | cc_sonnet | 100 | 93/100 = 93.0% [86.3, 96.6] | 90/100 = 90.0% [82.6, 94.5] | 88.0% (88) | 0.44 | 89.0% (89 of 100) | 99/100 |
| sym100 | missed | sonnet | 100 | 94/100 = 94.0% [87.5, 97.2] | 91/100 = 91.0% [83.8, 95.2] | 88.0% (88) | 0.42 | 89.0% (89 of 100) | 99/100 |
| sym100 | missed | opus55 | 100 | 90/100 = 90.0% [82.6, 94.5] | 87/100 = 87.0% [79.0, 92.2] | 86.0% (86) | 0.41 | 87.0% (87 of 100) | 99/100 |
| sym100 | missed | deepseek | 100 | 34/100 = 34.0% [25.5, 43.7] | 33/100 = 33.0% [24.6, 42.7] | 39.0% (39) | 0.06 | 40.0% (40 of 100) | 99/100 |
| rej53 | missed | cc_sonnet | 53 | 51/53 = 96.2% [87.2, 99.0] | 44/53 = 83.0% [70.8, 90.8] | 13.2% (7) | 0.00 | 79.2% (42 of 53) | 52/53 |
| rej53 | missed | sonnet | 53 | 51/53 = 96.2% [87.2, 99.0] | 44/53 = 83.0% [70.8, 90.8] | 11.3% (6) | 0.00 | 77.4% (41 of 53) | 52/53 |
| rej53 | missed | opus55 | 53 | 52/53 = 98.1% [90.1, 99.7] | 44/53 = 83.0% [70.8, 90.8] | 11.3% (6) | 0.00 | 77.4% (41 of 53) | 52/53 |
| rej53 | missed | deepseek | 53 | 52/53 = 98.1% [90.1, 99.7] | 44/53 = 83.0% [70.8, 90.8] | 11.3% (6) | 0.00 | 73.6% (39 of 53) | 52/53 |
| arb106 | missed | cc_sonnet | 100 | 100/100 = 100.0% [96.3, 100.0] | 96/100 = 96.0% [90.2, 98.4] | --- | --- | --- | 100/100 |
| arb106 | missed | sonnet | 100 | 99/100 = 99.0% [94.6, 99.8] | 95/100 = 95.0% [88.8, 97.8] | --- | --- | --- | 100/100 |
| arb106 | missed | opus55 | 100 | 99/100 = 99.0% [94.6, 99.8] | 95/100 = 95.0% [88.8, 97.8] | --- | --- | --- | 100/100 |
| arb106 | missed | deepseek | 96 | 92/96 = 95.8% [89.8, 98.4] | 88/96 = 91.7% [84.4, 95.7] | --- | --- | --- | 96/96 |

Sealed pack, all 200 cards: agreement with REFEREE and kappa per reader
- cc_sonnet: n 200, agree 76.0% (152), kappa 0.492; mean confidence 4.04; confidence 4 or 5 on 88%
- sonnet: n 200, agree 77.0% (154), kappa 0.512; mean confidence 3.96; confidence 4 or 5 on 87%
- opus55: n 200, agree 78.0% (156), kappa 0.523; mean confidence 4.36; confidence 4 or 5 on 95%
- deepseek: n 198, agree 75.3% (149), kappa 0.467; mean confidence 4.93; confidence 4 or 5 on 100%

## 2. Profit agreement with the ledger: cards with both values, within 0.01 ETH, median absolute difference (sandwich samples)

- cc_sonnet: 323 cards, within 0.01 ETH 274 (84.8%), within 0.001 ETH 204, median abs diff 7.27e-07 ETH, above 0.1 ETH 16
- sonnet: 316 cards, within 0.01 ETH 261 (82.6%), within 0.001 ETH 194, median abs diff 7.28e-07 ETH, above 0.1 ETH 21
- opus55: 323 cards, within 0.01 ETH 121 (37.5%), within 0.001 ETH 79, median abs diff 1.74e-02 ETH, above 0.1 ETH 35
- deepseek: 320 cards, within 0.01 ETH 106 (33.1%), within 0.001 ETH 54, median abs diff 2.10e-02 ETH, above 0.1 ETH 50

## 3. Between readers (API readers): pairwise agreement and Cohen's kappa on the three-state verdict; Fleiss' kappa over the three

| sample | pair | n | agree | kappa |
|---|---|---:|---|---:|
| f1b | sonnet vs opus55 | 200 | 196/200 = 98.0% [95.0, 99.2] | 0.952 |
| f1b | sonnet vs deepseek | 198 | 178/198 = 89.9% [84.9, 93.4] | 0.761 |
| f1b | opus55 vs deepseek | 198 | 177/198 = 89.4% [84.3, 93.0] | 0.741 |
| f1b | Fleiss, three readers | 198 | all agree 176/198 = 88.9% [83.8, 92.5] | 0.818 |
| sym100 | sonnet vs opus55 | 100 | 96/100 = 96.0% [90.2, 98.4] | 0.797 |
| sym100 | sonnet vs deepseek | 100 | 42/100 = 42.0% [32.8, 51.8] | 0.093 |
| sym100 | opus55 vs deepseek | 100 | 46/100 = 46.0% [36.6, 55.7] | 0.137 |
| sym100 | Fleiss, three readers | 100 | all agree 42/100 = 42.0% [32.8, 51.8] | 0.073 |
| rej53 | sonnet vs opus55 | 53 | 53/53 = 100.0% [93.2, 100.0] | 1.000 |
| rej53 | sonnet vs deepseek | 53 | 51/53 = 96.2% [87.2, 99.0] | 0.872 |
| rej53 | opus55 vs deepseek | 53 | 51/53 = 96.2% [87.2, 99.0] | 0.872 |
| rej53 | Fleiss, three readers | 53 | all agree 51/53 = 96.2% [87.2, 99.0] | 0.915 |
| arb106 | sonnet vs opus55 | 106 | 105/106 = 99.1% [94.8, 99.8] | 0.937 |
| arb106 | sonnet vs deepseek | 99 | 93/99 = 93.9% [87.4, 97.2] | 0.597 |
| arb106 | opus55 vs deepseek | 99 | 93/99 = 93.9% [87.4, 97.2] | 0.597 |
| arb106 | Fleiss, three readers | 99 | all agree 93/99 = 93.9% [87.4, 97.2] | 0.693 |
| pooled | sonnet vs opus55 | 459 | 450/459 = 98.0% [96.3, 99.0] | 0.937 |
| pooled | sonnet vs deepseek | 450 | 364/450 = 80.9% [77.0, 84.3] | 0.513 |
| pooled | opus55 vs deepseek | 450 | 367/450 = 81.6% [77.7, 84.9] | 0.527 |
| pooled | Fleiss, three readers | 450 | all agree 362/450 = 80.4% [76.5, 83.8] | 0.633 |

Run-to-run, claude-sonnet-5-5 earlier reading against the API reading: n 459, verdict agreement 450/459 = 98.0% [96.3, 99.0], kappa 0.937; Q1 agreement 451/459 = 98.3% [96.6, 99.1]; Q2 agreement 426/459 = 92.8% [90.1, 94.8]

## 4. Majority verdict of the three API readers (secondary summary)

| sample | set | n (all three answered) | majority supported | split | agree N2 | kappa N2 | agree W2 |
|---|---|---:|---|---:|---|---:|---|
| f1b | missed | 100 | 84/100 = 84.0% [75.6, 89.9] | 0 | 63.0% (63 of 100) | 0.02 | 78.0% (78 of 100) |
| f1b | reported | 50 | 46/50 = 92.0% [81.2, 96.8] | 0 | 90.0% (45 of 50) | 0.34 | 90.0% (45 of 50) |
| f1b | comparison | 48 | 10/48 = 20.8% [11.7, 34.3] | 1 | 95.7% (45 of 47) | 0.88 | 95.7% (45 of 47) |
| sym100 | missed | 100 | 87/100 = 87.0% [79.0, 92.2] | 0 | 86.0% (86 of 100) | 0.41 | 87.0% (87 of 100) |
| rej53 | missed | 53 | 44/53 = 83.0% [70.8, 90.8] | 0 | 11.3% (6 of 53) | 0.00 | 77.4% (41 of 53) |
| arb106 | missed | 96 | 92/96 = 95.8% [89.8, 98.4] | 0 | --- | --- | --- |

## 5. The six largest missed arbitrage transactions, per reader

| case | hash | rule profit (ETH) | cc_sonnet | sonnet | opus55 | deepseek |
|---|---|---:|---|---|---|---|
| arb106_052 | 0x46c8f3e9... | 88.9 | no (other), Q2 no, -0.19 ETH | no (other), Q2 cannot tell, 0.01 ETH | yes (arbitrage), Q2 yes, 0.01 ETH | --- |
| arb106_006 | 0x184e2077... | 56.6 | yes (arbitrage), Q2 yes, 0.05 ETH | yes (arbitrage), Q2 yes, 0.05 ETH | yes (arbitrage), Q2 yes, -0.95 ETH | no (minted token sale), Q2 yes, 0.05 ETH |
| arb106_014 | 0xa28aa478... | 46.6 | no (flash loan only), Q2 no, -0.07 ETH | no (other), Q2 no, -0.07 ETH | no (other), Q2 no, -0.13 ETH | no (flash loan only), Q2 no, -0.07 ETH |
| arb106_087 | 0x47b0d92d... | 30.0 | cannot tell (unclear), Q2 no, -0.07 ETH | no (other), Q2 no, -0.07 ETH | no (routed sale), Q2 cannot tell, 30.00 ETH | --- |
| arb106_073 | 0x04ff20fe... | 29.7 | yes (arbitrage), Q2 yes, -0.25 ETH | yes (arbitrage), Q2 yes, 0.01 ETH | yes (arbitrage), Q2 yes, -0.25 ETH | no (minted token sale), Q2 yes, -0.25 ETH |
| arb106_065 | 0x48ba14c7... | 29.0 | no (flash loan only), Q2 no, -0.04 ETH | no (other), Q2 no, -0.01 ETH | no (routed sale), Q2 cannot tell, 28.97 ETH | --- |
Validator profit: under v2, profit_after_gas as the reader states it; under v1, net_eth minus gas_eth, which double-counts gas for a reader that states net_eth after gas (check the note before quoting).

## 6. Cards on which the three API readers do not all agree (verdict, Q1/Q2, confidence), with REFEREE's states

| sample | card | set | N2 | W2 | sonnet | opus55 | deepseek |
|---|---|---|---|---|---|---|---|
| arb106 | arb106_006 | missed | no answer | no answer | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| arb106 | arb106_023 | missed | no answer | no answer | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| arb106 | arb106_033 | missed | no answer | no answer | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| arb106 | arb106_044 | missed | no answer | no answer | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| arb106 | arb106_050 | missed | no answer | no answer | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| arb106 | arb106_073 | missed | no answer | no answer | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| f1b | pack_007 | comparison | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| f1b | pack_021 | reported | rejected | rejected | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_024 | comparison | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| f1b | pack_030 | missed | rejected | rejected | cannot tell (yes/cannot tell, c3) | cannot tell (yes/cannot tell, c3) | supported (yes/yes, c4) |
| f1b | pack_035 | comparison | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| f1b | pack_046 | missed | supported | supported | cannot tell (yes/cannot tell, c3) | supported (yes/yes, c4) | supported (yes/yes, c5) |
| f1b | pack_048 | missed | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_060 | missed | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_065 | comparison | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c3) | rejected (no/yes, c5) |
| f1b | pack_074 | comparison | rejected | rejected | rejected (no/yes, c3) | supported (yes/yes, c3) | rejected (no/yes, c5) |
| f1b | pack_077 | missed | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_079 | comparison | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| f1b | pack_084 | comparison | supported | supported | cannot tell (yes/cannot tell, c3) | supported (yes/yes, c4) | rejected (no/cannot tell, c5) |
| f1b | pack_089 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (yes/no, c5) |
| f1b | pack_094 | missed | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_113 | reported | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c4) | cannot tell (yes/cannot tell, c5) |
| f1b | pack_132 | reported | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_141 | missed | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_160 | missed | rejected | rejected | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_161 | comparison | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| f1b | pack_164 | comparison | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c3) | rejected (no/yes, c4) |
| f1b | pack_186 | missed | supported | supported | cannot tell (yes/cannot tell, c3) | supported (yes/yes, c3) | cannot tell (yes/cannot tell, c4) |
| rej53 | rej53_028 | missed | rejected | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (yes/no, c5) |
| rej53 | rej53_050 | missed | rejected | rejected | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| sym100 | sym100_001 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_002 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_004 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_005 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_008 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c3) | rejected (no/yes, c4) |
| sym100 | sym100_009 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_011 | missed | cannot tell | cannot tell | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_013 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_014 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c5) | rejected (no/yes, c5) |
| sym100 | sym100_017 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_018 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_019 | missed | cannot tell | cannot tell | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_020 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_022 | missed | rejected | rejected | supported (yes/yes, c2) | rejected (no/yes, c3) | rejected (no/yes, c5) |
| sym100 | sym100_023 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_027 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_028 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_030 | missed | rejected | rejected | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_031 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_033 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c5) | rejected (no/yes, c4) |
| sym100 | sym100_035 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_041 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_042 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_045 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c3) | rejected (no/yes, c5) |
| sym100 | sym100_048 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_050 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_051 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_052 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c5) | rejected (no/yes, c5) |
| sym100 | sym100_054 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_055 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c3) | rejected (no/yes, c4) |
| sym100 | sym100_057 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_058 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_059 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c5) | rejected (no/yes, c4) |
| sym100 | sym100_060 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c5) | rejected (no/yes, c4) |
| sym100 | sym100_061 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_062 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c3) | rejected (no/yes, c4) |
| sym100 | sym100_063 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c5) | rejected (no/yes, c4) |
| sym100 | sym100_065 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_066 | missed | supported | supported | supported (yes/yes, c3) | rejected (no/yes, c3) | rejected (no/yes, c4) |
| sym100 | sym100_067 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_068 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_070 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_071 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_075 | missed | supported | supported | supported (yes/yes, c3) | rejected (no/yes, c3) | rejected (no/yes, c5) |
| sym100 | sym100_078 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_081 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c3) | rejected (no/yes, c4) |
| sym100 | sym100_082 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_083 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_085 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_087 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_088 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_090 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| sym100 | sym100_091 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_092 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c5) | rejected (no/yes, c5) |
| sym100 | sym100_096 | missed | cannot tell | cannot tell | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| sym100 | sym100_097 | missed | rejected | rejected | supported (yes/yes, c4) | supported (yes/yes, c3) | rejected (no/yes, c5) |
| sym100 | sym100_099 | missed | supported | supported | supported (yes/yes, c3) | rejected (no/yes, c3) | rejected (no/yes, c4) |
| sym100 | sym100_100 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c5) |

Notes of the disagreeing readers are in cards_long.csv.
