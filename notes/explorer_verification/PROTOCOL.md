# Explorer verification protocol, version 1

You are an independent reader verifying one candidate sandwich episode from public block-explorer data.
You see three Ethereum transactions from one block in block order, labelled front, victim and back. For
each you see what Blockscout and Etherscan return: sender, target, position, result, gas, value, decoded
ERC-20 token transfers, internal ETH transfers, and the events in the receipt by emitting contract,
including WETH deposits and withdrawals. Nothing from any MEV dataset and nothing from any other
analysis is included. Explorer name tags have been removed. Treat ETH and WETH as one asset.

Work step by step, as a careful human validator would on the explorer pages:

1. Identify the pool or pools each leg trades on (the contracts that emit Swap or Sync events and that
   send or receive the token transfers).
2. Identify the economic actor of the front and back legs: the address that ends up holding the token
   position after the front leg and gives it up in the back leg. It is often a contract called by the
   sender, not the sender itself. Pools and token contracts are never the actor.
3. Decide the questions below.

Q1. Is this a sandwich bracket? Answer "yes" if, in this block, one economic actor opens a position in a
non-WETH token in the front leg and closes it in the back leg on a pool the victim also trades, with the
victim between them. Answer "no" if any of these fails (different actors, no shared pool, no position
opened and closed, victim not on that pool). Answer "cannot tell" if the evidence shown does not settle
it.

Q2. Is the actor's position positive after observable cost? Net the actor's ETH and WETH across the
front and back legs (token transfers of WETH, WETH deposits and withdrawals, internal ETH transfers,
transaction value), subtract the gas fees of the front and back legs, and note any residual non-WETH
holding. Answer "yes" if positive, "no" if not, "cannot tell" if a residual holding or a missing figure
prevents a sign.

Confidence: 1 (guess) to 5 (certain).

Reply with one JSON object and nothing else:
{"actor": "<0x address or null>", "pool": "<0x address of the shared pool or null>", "Q1": "yes|no|cannot tell", "Q2": "yes|no|cannot tell", "net_eth": <number or null>, "gas_eth": <number or null>, "residual": "<token holding left, or none>", "confidence": <1 to 5>, "note": "<what influenced you, one to three sentences>"}
