# Multi-reader explorer validation, analysis plan (registered before the run)

## Purpose

The explorer validation of the manuscript (Section 5.6) is re-read by three language-model readers of two
lineages, each through its vendor's API, so that the validation does not rest on one model, and so that
agreement between independent readers is reported as a statistic. No reading enters any REFEREE state.

## Readers

| reader | model id requested | endpoint | settings |
|---|---|---|---|
| sonnet | claude-sonnet-5-5 | Anthropic Messages API | effort high, adaptive thinking at the default, max_tokens 16000 |
| opus55 | claude-opus-5-5 | Anthropic Messages API | effort high, adaptive thinking at the default, max_tokens 16000 |
| deepseek | deepseek-flash (reported by the endpoint as DeepSeek-V4.1-Flash) | DeepSeek chat completions API | reasoning_effort high, max_tokens 16000 |

claude-opus-5 was tried first and is excluded: its safety classifier declined every smoke-test card with zero
output (stop_reason refusal, category cyber); the refusal records are kept in the smoke-test outputs.

Each card is sent as one user message, the protocol text followed by the card, byte-identical to the prompt the
earlier Claude Code reading received. No system prompt, no tools, one reading per card. The model id the
endpoint reports, the settings, the token usage and the request id are stored in every judgement file.

## Inputs

The same 459 cards as the earlier reading, unchanged: f1b (200, sealed pack), sym100 (100), rej53 (53),
arb106 (106). Sandwich cards use PROTOCOL.md (sha256 e95442c2...6395); arbitrage cards use
PROTOCOL_ARBITRAGE.md (sha256 b20e6fd0...6156). The sealed mappings are not read by the runner.

Runner: scripts/explorer_verification/ev_judge_api.py. Outputs: out/explorer_verification_api/<reader>/<sample>/.

## Reader verdict

As before: supported = Q1 yes and Q2 yes; rejected = Q1 no or Q2 no; undecidable otherwise. A card the
endpoint declines (refusal) or that fails after six attempts is "no answer": it is counted and reported, and
it is excluded from the denominator of the shares below, with the count stated beside each share.

## Reported, per reader and per sample

1. Share of cards called a sandwich attack (arbitrage for arb106), Q1 yes, with a Wilson 95% interval.
2. Share supported (Q1 yes and Q2 yes), with a Wilson 95% interval.
3. Agreement with REFEREE's state (N2 outcome for sandwich samples): percentage and Cohen's kappa over the
   three states; the full cross-tabulation.
4. Actor identification: share of cards where the reader's actor equals the rule's economic actor.
5. The six largest arbitrage transactions, itemised per reader.

## Reported, between readers

6. Pairwise percentage agreement and Cohen's kappa on the three-state verdict, for the three pairs, and
   Fleiss' kappa across the three readers, per sample and pooled.
7. A majority verdict (the state two or three readers give; "split" if all three differ) as a secondary
   summary, with its agreement with REFEREE's state.
8. Disagreement table: every card on which the readers do not all agree, with each reader's Q1, Q2,
   confidence and note, and REFEREE's state.

## Relation to the earlier reading

The earlier reading (claude-sonnet-5-5 through Claude Code in headless mode, tools disabled) stays in the
record as the reading that located the W2 implementation error. The manuscript's validation numbers are
replaced by the three readings above. Agreement between the earlier Sonnet reading and the API Sonnet reading
is reported once as a run-to-run figure.

## What is fixed here

The readers, their settings, the prompt form, the verdict rule, the no-answer rule and the list of reported
statistics. Nothing in this plan is changed after the run starts; any later change is recorded as an
amendment with its own hash.
