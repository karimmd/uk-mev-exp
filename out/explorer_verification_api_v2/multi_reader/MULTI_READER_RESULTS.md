# Multi-reader explorer validation, protocol v2, scored 2026-10-19T20:11:41+0800

Plan: MULTI_READER_PLAN.md with amendment 1 (protocol version 2) (hashes in MULTI_READER_REGISTRATION.txt). Readers:
- cc_sonnet: claude-sonnet-5-5 (Claude Code, earlier reading); judgments 459 of 459; refusals 0; tokens in 0, out 0, 11.95 USD as recorded
- sonnet: claude-sonnet-5-5 (API); judgments 459 of 459; refusals 0; tokens in 1493666, out 411460, about 7.10 USD at list prices
- opus55: claude-opus-5-5 (API); judgments 459 of 459; refusals 0; tokens in 1493666, out 360672, about 13.19 USD at list prices
- deepseek: DeepSeek-V4.1-Flash (API); judgments 459 of 459; refusals 0; tokens in 1179711, out 3466200

Coverage per sample (judgments / cards): f1b 200/200/200/200 of 200; sym100 100/100/100/100 of 100; rej53 53/53/53/53 of 53; arb106 106/106/106/106 of 106

## 1. Per reader and per sample: called MEV (Q1 yes), supported (Q1 yes and Q2 yes), agreement with REFEREE (original witness), actor

| sample | set | reader | n | Q1 yes | supported | agree N2 | kappa N2 | agree W2 | actor match |
|---|---|---|---:|---|---|---|---:|---|---|
| f1b | missed | cc_sonnet | 100 | 98/100 = 98.0% [93.0, 99.4] | 81/100 = 81.0% [72.2, 87.5] | 60.0% (60) | -0.01 | 75.0% (75 of 100) | 98/100 |
| f1b | missed | sonnet | 100 | 98/100 = 98.0% [93.0, 99.4] | 83/100 = 83.0% [74.5, 89.1] | 62.0% (62) | 0.01 | 77.0% (77 of 100) | 98/100 |
| f1b | missed | opus55 | 100 | 98/100 = 98.0% [93.0, 99.4] | 84/100 = 84.0% [75.6, 89.9] | 63.0% (63) | 0.02 | 78.0% (78 of 100) | 98/100 |
| f1b | missed | deepseek | 100 | 98/100 = 98.0% [93.0, 99.4] | 89/100 = 89.0% [81.4, 93.7] | 66.0% (66) | 0.03 | 81.0% (81 of 100) | 98/100 |
| f1b | reported | cc_sonnet | 50 | 50/50 = 100.0% [92.9, 100.0] | 46/50 = 92.0% [81.2, 96.8] | 90.0% (45) | 0.34 | 90.0% (45 of 50) | 50/50 |
| f1b | reported | sonnet | 50 | 50/50 = 100.0% [92.9, 100.0] | 45/50 = 90.0% [78.6, 95.7] | 88.0% (44) | 0.29 | 88.0% (44 of 50) | 50/50 |
| f1b | reported | opus55 | 50 | 50/50 = 100.0% [92.9, 100.0] | 46/50 = 92.0% [81.2, 96.8] | 90.0% (45) | 0.34 | 90.0% (45 of 50) | 50/50 |
| f1b | reported | deepseek | 50 | 50/50 = 100.0% [92.9, 100.0] | 47/50 = 94.0% [83.8, 97.9] | 88.0% (44) | 0.10 | 88.0% (44 of 50) | 50/50 |
| f1b | comparison | cc_sonnet | 50 | 15/50 = 30.0% [19.1, 43.8] | 13/50 = 26.0% [15.9, 39.6] | 94.0% (47) | 0.85 | 94.0% (47 of 50) | 24/50 |
| f1b | comparison | sonnet | 50 | 15/50 = 30.0% [19.1, 43.8] | 12/50 = 24.0% [14.3, 37.4] | 92.0% (46) | 0.80 | 92.0% (46 of 50) | 23/50 |
| f1b | comparison | opus55 | 50 | 15/50 = 30.0% [19.1, 43.8] | 13/50 = 26.0% [15.9, 39.6] | 94.0% (47) | 0.85 | 94.0% (47 of 50) | 29/50 |
| f1b | comparison | deepseek | 50 | 14/50 = 28.0% [17.5, 41.7] | 10/50 = 20.0% [11.2, 33.0] | 88.0% (44) | 0.69 | 88.0% (44 of 50) | 29/50 |
| sym100 | missed | cc_sonnet | 100 | 93/100 = 93.0% [86.3, 96.6] | 90/100 = 90.0% [82.6, 94.5] | 88.0% (88) | 0.44 | 89.0% (89 of 100) | 99/100 |
| sym100 | missed | sonnet | 100 | 98/100 = 98.0% [93.0, 99.4] | 95/100 = 95.0% [88.8, 97.8] | 85.0% (85) | 0.16 | 86.0% (86 of 100) | 99/100 |
| sym100 | missed | opus55 | 100 | 98/100 = 98.0% [93.0, 99.4] | 95/100 = 95.0% [88.8, 97.8] | 85.0% (85) | 0.16 | 86.0% (86 of 100) | 99/100 |
| sym100 | missed | deepseek | 100 | 96/100 = 96.0% [90.2, 98.4] | 94/100 = 94.0% [87.5, 97.2] | 84.0% (84) | 0.14 | 85.0% (85 of 100) | 99/100 |
| rej53 | missed | cc_sonnet | 53 | 51/53 = 96.2% [87.2, 99.0] | 44/53 = 83.0% [70.8, 90.8] | 13.2% (7) | 0.00 | 79.2% (42 of 53) | 52/53 |
| rej53 | missed | sonnet | 53 | 51/53 = 96.2% [87.2, 99.0] | 46/53 = 86.8% [75.2, 93.5] | 11.3% (6) | 0.00 | 81.1% (43 of 53) | 52/53 |
| rej53 | missed | opus55 | 53 | 50/53 = 94.3% [84.6, 98.1] | 44/53 = 83.0% [70.8, 90.8] | 15.1% (8) | 0.00 | 81.1% (43 of 53) | 52/53 |
| rej53 | missed | deepseek | 53 | 52/53 = 98.1% [90.1, 99.7] | 44/53 = 83.0% [70.8, 90.8] | 11.3% (6) | 0.00 | 73.6% (39 of 53) | 52/53 |
| arb106 | missed | cc_sonnet | 100 | 100/100 = 100.0% [96.3, 100.0] | 96/100 = 96.0% [90.2, 98.4] | --- | --- | --- | 100/100 |
| arb106 | missed | sonnet | 100 | 100/100 = 100.0% [96.3, 100.0] | 95/100 = 95.0% [88.8, 97.8] | --- | --- | --- | 100/100 |
| arb106 | missed | opus55 | 100 | 99/100 = 99.0% [94.6, 99.8] | 95/100 = 95.0% [88.8, 97.8] | --- | --- | --- | 100/100 |
| arb106 | missed | deepseek | 100 | 96/100 = 96.0% [90.2, 98.4] | 92/100 = 92.0% [85.0, 95.9] | --- | --- | --- | 97/100 |

Sealed pack, all 200 cards: agreement with REFEREE and kappa per reader
- cc_sonnet: n 200, agree 76.0% (152), kappa 0.492; mean confidence 4.04; confidence 4 or 5 on 88%
- sonnet: n 200, agree 76.0% (152), kappa 0.491; mean confidence 3.94; confidence 4 or 5 on 85%
- opus55: n 200, agree 77.5% (155), kappa 0.515; mean confidence 4.33; confidence 4 or 5 on 95%
- deepseek: n 200, agree 77.0% (154), kappa 0.499; mean confidence 4.93; confidence 4 or 5 on 100%

## 2. Profit agreement with the ledger: cards with both values, within 0.01 ETH, median absolute difference (sandwich samples)

- cc_sonnet: 323 cards, within 0.01 ETH 274 (84.8%), within 0.001 ETH 204, median abs diff 7.27e-07 ETH, above 0.1 ETH 16
- sonnet: 317 cards, within 0.01 ETH 267 (84.2%), within 0.001 ETH 198, median abs diff 7.21e-07 ETH, above 0.1 ETH 18
- opus55: 323 cards, within 0.01 ETH 275 (85.1%), within 0.001 ETH 207, median abs diff 7.20e-07 ETH, above 0.1 ETH 16
- deepseek: 323 cards, within 0.01 ETH 223 (69.0%), within 0.001 ETH 158, median abs diff 1.36e-03 ETH, above 0.1 ETH 32

## 3. Between readers (API readers): pairwise agreement and Cohen's kappa on the three-state verdict; Fleiss' kappa over the three

| sample | pair | n | agree | kappa |
|---|---|---:|---|---:|
| f1b | sonnet vs opus55 | 200 | 195/200 = 97.5% [94.3, 98.9] | 0.941 |
| f1b | sonnet vs deepseek | 200 | 186/200 = 93.0% [88.6, 95.8] | 0.832 |
| f1b | opus55 vs deepseek | 200 | 189/200 = 94.5% [90.4, 96.9] | 0.865 |
| f1b | Fleiss, three readers | 200 | all agree 185/200 = 92.5% [88.0, 95.4] | 0.880 |
| sym100 | sonnet vs opus55 | 100 | 100/100 = 100.0% [96.3, 100.0] | 1.000 |
| sym100 | sonnet vs deepseek | 100 | 99/100 = 99.0% [94.6, 99.8] | 0.904 |
| sym100 | opus55 vs deepseek | 100 | 99/100 = 99.0% [94.6, 99.8] | 0.904 |
| sym100 | Fleiss, three readers | 100 | all agree 99/100 = 99.0% [94.6, 99.8] | 0.934 |
| rej53 | sonnet vs opus55 | 53 | 50/53 = 94.3% [84.6, 98.1] | 0.784 |
| rej53 | sonnet vs deepseek | 53 | 48/53 = 90.6% [79.7, 95.9] | 0.645 |
| rej53 | opus55 vs deepseek | 53 | 49/53 = 92.5% [82.1, 97.0] | 0.742 |
| rej53 | Fleiss, three readers | 53 | all agree 47/53 = 88.7% [77.4, 94.7] | 0.723 |
| arb106 | sonnet vs opus55 | 106 | 104/106 = 98.1% [93.4, 99.5] | 0.879 |
| arb106 | sonnet vs deepseek | 106 | 99/106 = 93.4% [87.0, 96.8] | 0.661 |
| arb106 | opus55 vs deepseek | 106 | 99/106 = 93.4% [87.0, 96.8] | 0.663 |
| arb106 | Fleiss, three readers | 106 | all agree 98/106 = 92.5% [85.8, 96.1] | 0.723 |
| pooled | sonnet vs opus55 | 459 | 449/459 = 97.8% [96.0, 98.8] | 0.926 |
| pooled | sonnet vs deepseek | 459 | 432/459 = 94.1% [91.6, 95.9] | 0.802 |
| pooled | opus55 vs deepseek | 459 | 436/459 = 95.0% [92.6, 96.6] | 0.831 |
| pooled | Fleiss, three readers | 459 | all agree 429/459 = 93.5% [90.8, 95.4] | 0.852 |

Run-to-run, claude-sonnet-5-5 earlier reading against the API reading: n 459, verdict agreement 445/459 = 96.9% [94.9, 98.2], kappa 0.900; Q1 agreement 452/459 = 98.5% [96.9, 99.3]; Q2 agreement 422/459 = 91.9% [89.1, 94.1]

Version 2 against version 1, per reader (same cards, same reader, protocol wording changed): verdict agreement and kappa; Q1 agreement on buy-first and on other patterns
- sonnet: n 459, verdict agreement 446/459 = 97.2% [95.2, 98.3], kappa 0.907; Q1 agreement buy-first 250/253 = 98.8% [96.6, 99.6], other patterns 96/100 = 96.0% [90.2, 98.4]
- opus55: n 459, verdict agreement 447/459 = 97.4% [95.5, 98.5], kappa 0.913; Q1 agreement buy-first 251/253 = 99.2% [97.2, 99.8], other patterns 92/100 = 92.0% [85.0, 95.9]
- deepseek: n 450, verdict agreement 366/450 = 81.3% [77.5, 84.7], kappa 0.519; Q1 agreement buy-first 239/251 = 95.2% [91.8, 97.2], other patterns 34/100 = 34.0% [25.5, 43.7]

## 4. Majority verdict of the three API readers (secondary summary)

| sample | set | n (all three answered) | majority supported | split | agree N2 | kappa N2 | agree W2 |
|---|---|---:|---|---:|---|---:|---|
| f1b | missed | 100 | 84/100 = 84.0% [75.6, 89.9] | 0 | 63.0% (63 of 100) | 0.02 | 78.0% (78 of 100) |
| f1b | reported | 50 | 46/50 = 92.0% [81.2, 96.8] | 0 | 90.0% (45 of 50) | 0.34 | 90.0% (45 of 50) |
| f1b | comparison | 50 | 12/50 = 24.0% [14.3, 37.4] | 0 | 92.0% (46 of 50) | 0.80 | 92.0% (46 of 50) |
| sym100 | missed | 100 | 95/100 = 95.0% [88.8, 97.8] | 0 | 85.0% (85 of 100) | 0.16 | 86.0% (86 of 100) |
| rej53 | missed | 53 | 44/53 = 83.0% [70.8, 90.8] | 0 | 13.2% (7 of 53) | 0.00 | 79.2% (42 of 53) |
| arb106 | missed | 100 | 96/100 = 96.0% [90.2, 98.4] | 0 | --- | --- | --- |

## 5. The six largest missed arbitrage transactions, per reader

| case | hash | rule profit (ETH) | cc_sonnet | sonnet | opus55 | deepseek |
|---|---|---:|---|---|---|---|
| arb106_052 | 0x46c8f3e9... | 88.9 | no (other), Q2 no, -0.19 ETH | no (other), Q2 yes, 0.01 ETH | no (minted token sale), Q2 yes, 0.01 ETH | no (minted token sale), Q2 yes, 0.01 ETH |
| arb106_006 | 0x184e2077... | 56.6 | yes (arbitrage), Q2 yes, 0.05 ETH | yes (arbitrage), Q2 yes, 0.05 ETH | yes (arbitrage), Q2 yes, 0.05 ETH | no (minted token sale), Q2 yes, 0.05 ETH |
| arb106_014 | 0xa28aa478... | 46.6 | no (flash loan only), Q2 no, -0.07 ETH | no (flash loan only), Q2 no, -0.07 ETH | no (routed sale), Q2 no, -0.07 ETH | no (routed sale), Q2 cannot tell, 46.58 ETH |
| arb106_087 | 0x47b0d92d... | 30.0 | cannot tell (unclear), Q2 no, -0.07 ETH | no (flash loan only), Q2 no, -0.07 ETH | no (routed sale), Q2 cannot tell, ? ETH | no (routed sale), Q2 yes, 30.00 ETH |
| arb106_073 | 0x04ff20fe... | 29.7 | yes (arbitrage), Q2 yes, -0.25 ETH | yes (arbitrage), Q2 yes, 0.01 ETH | yes (arbitrage), Q2 yes, 0.01 ETH | no (minted token sale), Q2 yes, 0.01 ETH |
| arb106_065 | 0x48ba14c7... | 29.0 | no (flash loan only), Q2 no, -0.04 ETH | cannot tell (unclear), Q2 no, -0.01 ETH | cannot tell (unclear), Q2 no, -0.04 ETH | no (routed sale), Q2 cannot tell, 29.01 ETH |
Validator profit: under v2, profit_after_gas as the reader states it; under v1, net_eth minus gas_eth, which double-counts gas for a reader that states net_eth after gas (check the note before quoting).

## 6. Cards on which the three API readers do not all agree (verdict, Q1/Q2, confidence), with REFEREE's states

| sample | card | set | N2 | W2 | sonnet | opus55 | deepseek |
|---|---|---|---|---|---|---|---|
| arb106 | arb106_006 | missed | no answer | no answer | supported (yes/yes, c3) | supported (yes/yes, c3) | rejected (no/yes, c4) |
| arb106 | arb106_008 | missed | no answer | no answer | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| arb106 | arb106_024 | missed | no answer | no answer | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| arb106 | arb106_025 | missed | no answer | no answer | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| arb106 | arb106_049 | missed | no answer | no answer | supported (yes/yes, c4) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| arb106 | arb106_073 | missed | no answer | no answer | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c5) |
| arb106 | arb106_081 | missed | no answer | no answer | supported (yes/yes, c3) | cannot tell (cannot tell/yes, c2) | supported (yes/yes, c4) |
| arb106 | arb106_092 | missed | no answer | no answer | rejected (yes/no, c4) | supported (yes/yes, c4) | supported (yes/yes, c5) |
| f1b | pack_009 | comparison | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (no/yes, c4) |
| f1b | pack_021 | reported | rejected | rejected | rejected (yes/no, c4) | rejected (yes/no, c3) | supported (yes/yes, c5) |
| f1b | pack_040 | missed | supported | supported | cannot tell (yes/cannot tell, c3) | supported (yes/yes, c4) | supported (yes/yes, c5) |
| f1b | pack_046 | missed | supported | supported | cannot tell (yes/cannot tell, c3) | supported (yes/yes, c4) | supported (yes/yes, c5) |
| f1b | pack_048 | missed | supported | supported | rejected (yes/no, c3) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_060 | missed | supported | supported | rejected (yes/no, c3) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_077 | missed | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c4) | supported (yes/yes, c5) |
| f1b | pack_084 | comparison | supported | supported | cannot tell (yes/cannot tell, c3) | supported (yes/yes, c4) | cannot tell (yes/cannot tell, c5) |
| f1b | pack_089 | missed | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (yes/no, c5) |
| f1b | pack_094 | missed | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c3) | supported (yes/yes, c5) |
| f1b | pack_105 | reported | supported | supported | rejected (yes/no, c4) | supported (yes/yes, c5) | supported (yes/yes, c5) |
| f1b | pack_109 | comparison | supported | supported | supported (yes/yes, c3) | supported (yes/yes, c3) | rejected (yes/no, c4) |
| f1b | pack_141 | missed | supported | supported | rejected (yes/no, c4) | rejected (yes/no, c3) | supported (yes/yes, c5) |
| f1b | pack_160 | missed | rejected | rejected | rejected (yes/no, c4) | rejected (yes/no, c3) | supported (yes/yes, c5) |
| f1b | pack_186 | missed | supported | supported | supported (yes/yes, c3) | cannot tell (yes/cannot tell, c3) | cannot tell (yes/cannot tell, c5) |
| rej53 | rej53_007 | missed | rejected | supported | supported (yes/yes, c4) | rejected (yes/no, c5) | rejected (yes/no, c5) |
| rej53 | rej53_026 | missed | rejected | rejected | rejected (no/cannot tell, c2) | rejected (no/cannot tell, c3) | cannot tell (yes/cannot tell, c4) |
| rej53 | rej53_028 | missed | rejected | supported | supported (yes/yes, c3) | supported (yes/yes, c4) | rejected (yes/no, c4) |
| rej53 | rej53_033 | missed | rejected | rejected | cannot tell (yes/cannot tell, c3) | rejected (no/no, c3) | cannot tell (yes/cannot tell, c4) |
| rej53 | rej53_034 | missed | rejected | rejected | supported (yes/yes, c3) | cannot tell (yes/cannot tell, c3) | cannot tell (yes/cannot tell, c4) |
| rej53 | rej53_050 | missed | rejected | rejected | rejected (yes/no, c4) | rejected (yes/no, c3) | supported (yes/yes, c5) |
| sym100 | sym100_038 | missed | supported | supported | supported (yes/yes, c4) | supported (yes/yes, c3) | rejected (no/yes, c5) |

Notes of the disagreeing readers are in cards_long.csv.
