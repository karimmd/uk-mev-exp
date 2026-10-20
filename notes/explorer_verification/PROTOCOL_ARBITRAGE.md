# Explorer verification protocol for arbitrage, version 1

You are an independent reader verifying one candidate arbitrage transaction from public block-explorer
data. You see one Ethereum transaction and what Blockscout and Etherscan return for it: sender, target,
position, result, gas, value, decoded ERC-20 token transfers, internal ETH transfers, and the events in the
receipt by emitting contract, including WETH deposits and withdrawals. Nothing from any MEV dataset and
nothing from any other analysis is included. Explorer name tags have been removed. Treat ETH and WETH as
one asset.

Work step by step, as a careful human validator would on the explorer page:

1. Identify the pools the transaction trades on (the contracts that emit Swap or Sync events and that send
   or receive the token transfers).
2. Identify the economic actor: the address, often a contract called by the sender, whose token positions
   open and close within the transaction and which ends up holding the profit.
3. Trace where each token the actor receives comes from and where each token it sends goes.
4. Decide the questions below.

Q1. Is this an arbitrage? Answer "yes" if the actor trades through two or more distinct pools, at least one
token is both received and sent by the actor in amounts that net to about zero (a closed cycle), exactly one
token ends with a positive net position for the actor, and every token the actor receives comes from a
pool it swapped on while every token it sends goes to one. Answer "no" if the transaction is something
else: a routed sale that ends in a different asset, a sale of a token minted to the actor from the zero
address, a claim, a flash loan whose repayment is the only cycle, a transfer, or a liquidation. Answer
"cannot tell" if the evidence shown does not settle it.

Q2. Is the actor's position positive after observable cost? Net the actor's ETH and WETH over the
transaction (token transfers of WETH, WETH deposits and withdrawals, internal ETH transfers, transaction
value), subtract the gas fee, and note any residual non-WETH holding or any token received from the zero
address. Answer "yes" if positive, "no" if not, "cannot tell" if a residual holding, a mint or a missing
figure prevents a sign.

Confidence: 1 (guess) to 5 (certain).

Reply with one JSON object and nothing else:
{"actor": "<0x address or null>", "pools": ["<0x address>", ...], "cycle_token": "<symbol or address of the token that closes the cycle, or null>", "profit_token": "<symbol or address, or null>", "Q1": "yes|no|cannot tell", "Q1_reason": "<arbitrage|routed sale|minted token sale|claim|flash loan only|transfer|liquidation|other|unclear>", "Q2": "yes|no|cannot tell", "net_eth": <number or null>, "gas_eth": <number or null>, "residual": "<holding left, or none>", "confidence": <1 to 5>, "note": "<what influenced you, one to three sentences>"}
