# Multi-reader explorer validation, amendment 1: protocol version 2 (registered before the v2 run)

## Why

The version 1 run under MULTI_READER_PLAN.md (claude-sonnet-5-5 and claude-opus-5-5 complete on all 459
cards; DeepSeek-V4.1-Flash on 240 at the time of writing) located two wording defects in the version 1
protocols. Neither is a disagreement about the transactions.

1. Q1 of PROTOCOL.md presupposes a buy-first bracket: "opens a position in a non-WETH token in the front leg
   and closes it in the back leg". On sell-first brackets (the sample added by S5' and the comparison cases)
   DeepSeek-V4.1-Flash reads this literally and answers "no" while its note records that the actor sells
   first, buys back after the victim and profits. The two Claude readers treat a short position as a
   position. Called a sandwich attack on the S5' sample so far: 94%, 90% and 40%.
2. The answer fields net_eth and gas_eth do not state whether net_eth is before or after gas. Sonnet reports
   it before gas, Opus 5.5 after gas on most cards, DeepSeek a mixture. Scored as net minus gas, Opus 5.5 lies
   within 0.01 ETH of REFEREE's ledger on 37% of cards; read as already after gas, on 80%.

## What changes

PROTOCOL_v2.md and PROTOCOL_ARBITRAGE_v2.md differ from version 1 in exactly these places (diff recorded in
MULTI_READER_REGISTRATION.txt):

- Q1 (sandwich only): "opens a position in a non-WETH token in the front leg, long by buying it or short by
  selling it, and closes that position in the back leg".
- Answer fields (both protocols): net_eth and gas_eth are replaced by net_eth_before_gas, gas_eth and
  profit_after_gas, each with a one-line definition.
- The output limit per reading rises from 16,000 to 32,000 tokens, because two DeepSeek readings in the
  version 1 run exceeded 16,000 tokens of reasoning and were recorded as no answer.

Nothing else changes: readers, effort, prompt form, cards, verdict rule, no-answer rule and the reported
statistics are those of MULTI_READER_PLAN.md. Outputs go to out/explorer_verification_api_v2/<reader>/<sample>/.

## How it is reported

The version 2 readings are the validation reported in the manuscript. The version 1 readings are kept and
reported beside them as the run that located the two defects, in the same way the manuscript reports the
original witness beside W2. Profit agreement with the ledger uses profit_after_gas as each reader states it.
