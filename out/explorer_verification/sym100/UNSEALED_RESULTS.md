# sym100 explorer verification (100 brackets added by the direction-symmetric rule), unsealed 2026-10-13T22:39:00+08:00

Reader claude-sonnet-5-5 headless, PROTOCOL.md sha256 e95442c2…6395, 100 cards, mapping sha256 bc6773bc…

## 1. Reader verdicts

- Q1 sandwich yes: 93/100 = 93.0% [86.3, 96.6]
- Q2 positive after cost yes: 95/100 = 95.0% [88.8, 97.8]
- reader supported (Q1 yes and Q2 yes): 90/100 = 90.0% [82.6, 94.5]
- reader rejected: 10; undecidable: 0

## 2. Agreement with the adjudicator (N2)

| n2_outcome             |   rejected |   structurally_supported |   All |
|:-----------------------|-----------:|-------------------------:|------:|
| rejected               |          6 |                        4 |    10 |
| structurally_supported |          4 |                       82 |    86 |
| undecidable            |          0 |                        4 |     4 |
| All                    |         10 |                       90 |   100 |

Agreement 88.0% (88 of 100), kappa 0.444

## 3. By direction pattern (the new brackets the symmetric rule admits)

| pattern | n | reader Q1 yes | reader supported | adjudicator supported | called by mev-inspect |
|---|---:|---|---|---|---|
| sell_first | 81 | 76/81 = 93.8% [86.4, 97.3] | 74/81 = 91.4% [83.2, 95.8] | 69/81 = 85.2% [75.9, 91.3] | 80 |
| weth_only | 19 | 17/19 = 89.5% [68.6, 97.1] | 16/19 = 84.2% [62.4, 94.5] | 17/19 = 89.5% [68.6, 97.1] | 14 |

Reader Q1 yes among brackets mev-inspect calls: 89/94 = 94.7% [88.1, 97.7]; among those it does not: 4/6 = 66.7% [30.0, 90.3]

## Actor identification

Reader actor equals the rule's actor in 99 of 100

## Disagreements, itemised

| case | adjudicator | reader | Q1 | Q2 | conf | note |
|---|---|---|---|---|---|---|
| sym100_011 | undecidable | structurally_supported | yes | yes | 4 | The same contract trades MOD/WETH on the same pool in the front and back legs, with the victim's MOD sale between them. The front leg sells 10453.15 MOD for 18.219 WETH, the back leg buys back exactly 10453.15 MOD for 16.988879 WETH, so the MOD position is flat. Net WETH is +1.230121, and after 0.20 |
| sym100_016 | rejected | structurally_supported | yes | yes | 4 | The actor contract sells 1809529318417.167725 BDT to the pool for 0.760486 WETH in the front leg. The victim sells BDT into the same pool. The back leg buys back exactly the same BDT amount for 0.639761 WETH, so the actor ends with no BDT residual. WETH net is +0.120725. After 0.007195 ETH of gas, t |
| sym100_019 | undecidable | structurally_supported | yes | yes | 4 | The actor contract sells 22542.862174 PKF into the pool for 15.563 WETH before the victim's PKF sale on the same pool, then buys back exactly 22542.862174 PKF for 14.90956 WETH, so PKF nets to zero. WETH gain of 0.65344 minus 0.392697 ETH gas (front 0.356005 + back 0.036692) leaves about +0.2607 ETH |
| sym100_030 | rejected | structurally_supported | yes | yes | 4 | The sender EOA sells 1242.795971 API3 for 2.850253 WETH in the front leg, the victim sells API3 into the same pool in between, and the back leg buys back exactly 1242.795971 API3 for 2.681226 WETH, so no API3 is left over. Net WETH is +0.169027 before gas and about +0.142 after the 0.026996 ETH of c |
| sym100_047 | undecidable | structurally_supported | yes | yes | 3 | The actor's contract runs a V3-to-V2 LOOKS round trip in each leg. It sells LOOKS into the V2 pool before the victim sells there and buys LOOKS back from that pool afterwards, so the V2 pool is the shared pool (the victim also trades the V3 pool). Net WETH is -1.084465 in the front and +2.029713 in  |
| sym100_053 | structurally_supported | rejected | yes | no | 3 | The actor contract sold 1,980,461.84 wOMI into the pool before the victim's wOMI sale (front) and bought exactly that amount back after it (back). This is a reverse-direction bracket on the same pool. The wOMI nets to zero, but the front leg starts from existing inventory, so the 'opens a position'  |
| sym100_056 | structurally_supported | rejected | yes | no | 3 | The actor sells CGG into the V3 pool in the front leg (10.226 WETH in, CGG sourced from the V2 pool 0xc8ca), the victim sells CGG on that V3 pool, and the back leg buys the CGG back from V3 for exactly 10.226 WETH and routes it to V2. That is a sandwich bracket on V3. Gross WETH is -2.0617 on the fr |
| sym100_074 | structurally_supported | rejected | no | no | 3 | Each leg is an atomic V3<->V2 round trip: the ICE goes straight from the V3 pool to the V2 pool (front) and back (back), so the actor never holds ICE between legs. The WETH nets to -0.291278 in the front and +0.467195 in the back, about +0.175917 in total, which matches the 0.175918 ETH of gas, so t |
| sym100_077 | structurally_supported | rejected | yes | no | 3 | The same contract (0xc1dfd...) sells 61547.897140 SMINU into the pool in the front leg, in the same direction as the victim's sale. It buys exactly that amount back in the back leg, on the same pool and with the victim in between. The WETH nets +0.972757 - 0.922246 = +0.050511, and front plus back g |
| sym100_094 | rejected | structurally_supported | yes | yes | 4 | The actor contract sold 6608.905755 INFI for 1.850367 WETH in the front leg. It bought back exactly 6608.905755 INFI for 1.703883 WETH in the back leg. The victim sold INFI on the same pool between the two legs, in the same direction as the front leg. Net WETH is +0.146484. After gas of 0.016492 ETH |
| sym100_096 | undecidable | structurally_supported | yes | yes | 4 | The contract 0x09dd... (called by 0xd38b...) sells 12160.41 CVR into the pool for 5.921007 WETH before the victim's CVR->WETH swap on the same pool, then buys the same 12160.41 CVR back for 5.707798 WETH right after. WETH net is +0.213209, and after 0.027306 ETH of gas it is about +0.1859 ETH with n |
| sym100_097 | rejected | structurally_supported | yes | yes | 3 | The actor contract sells 30590.96 NCT for 1.509 WETH in the front leg. In the back leg it buys exactly 30590.96 NCT back for 1.396588 WETH, so no NCT is left over. The victim trades WETH to NCT on the same pool (0x9f4a...) in between. The WETH gain of 0.112412 less 0.101725 ETH gas leaves about +0.0 |
