# arb106 explorer verification, unsealed 2026-10-13T22:39:00+08:00

Reader claude-sonnet-5-5 headless, PROTOCOL_ARBITRAGE.md sha256 b20e6fd0…6156, 106 cards, mapping sha256 eaeeb4be…

## 1. Random sample of 100 record-absent, canonical-flow, profitable arbitrage transactions

- reader Q1 arbitrage yes: 100/100 = 100.0% [96.3, 100.0]
- reader Q2 positive after cost yes: 96/100 = 96.0% [90.2, 98.4]
- reader supported (both yes): 96/100 = 96.0% [90.2, 98.4]
- Q1 reasons: {'arbitrage': 100}
- reader actor equals the rule's economic actor: 100 of 100
- first-on-all-pools (rule flag) among reader-confirmed arbitrages: 84 of 100

## 2. The six largest record-absent transactions by apparent profit

| case | hash | profit (ETH, rule) | reader Q1 | reason | Q2 | conf | note |
|---|---|---:|---|---|---|---|---|
| arb106_052 | 0x46c8f3e94d… | 88.88 | no | other | no | 3 | The actor takes 88.86 WETH from two pools (the FLI/WETH pool and the USDC/WETH pool), unwraps it, mints cETH, and uses that to issue ETH2X-FLI. It also borrows USDC via the FLI contract and cUSDC. The CETH and USDC it handles come from the cETH, cUSDC and FLI contracts rather than from pools, and th |
| arb106_006 | 0x184e207732… | 56.61 | yes | arbitrage | yes | 3 | The actor paid 56.118353 ETH to the ibETH contract and was minted 53.906 IBETH. It sold the IBETH into the IBETH/LINK pool, and the LINK went to the LINK/WETH pool, which returned 57.159460 WETH. It unwrapped that to ETH, so the ETH cycle closes with +1.041107 ETH before gas. The IBETH came from a m |
| arb106_014 | 0xa28aa478c6… | 46.58 | no | flash loan only | no | 3 | The actor borrowed 7,075,827 USDC from 0x56178a, which emits no events. It swapped 112,849 USDC through USDT to 46.64 WETH on two V3 pools, then repaid 6,962,978 USDC and 46.64 WETH to the lender. Every token nets to exactly zero for the actor, so no positive token position remains, and the gas fee  |
| arb106_087 | 0x47b0d92d4d… | 30.00 | cannot tell | unclear | no | 3 | The actor takes 3,567,488.91 USDC from the USDC/WETH pool and returns exactly that amount. It uses 68,686.97 USDC to buy FEI on the FEI/USDC V3 pool, then sells the FEI on the FEI/WETH V2 pool. The 30.07 WETH from that sale goes straight to the first pool, so the actor never holds it. Every token ne |
| arb106_073 | 0x04ff20fe6d… | 29.70 | yes | arbitrage | yes | 3 | The actor paid 29.568745 ETH into the ibETH contract, which minted IBETH to it. It sold the IBETH for LINK on one pool and the LINK for WETH on another, then unwrapped 29.842610 ETH. That is a gross gain of 0.273865 ETH and about 0.013535 ETH after the 0.260330 ETH gas fee. The IBETH mint was paid f |
| arb106_065 | 0x48ba14c72c… | 29.01 | no | flash loan only | no | 2 | The actor takes 9.73M USDC from pool 0x5617 as a flash swap. It sells 100.4k USDC for FEI on the V3 pool and FEI for 29.03 WETH on the V2 pair. It then repays the lender with 9.63M USDC plus that WETH, which goes straight from the V2 pair to the lender. The actor nets zero in USDC, FEI and WETH, so  |

Reader says arbitrage for 2 of the six (the magnitudes note says none is).

## 3. Non-arbitrage cases in the random sample, itemised

| case | hash | reader Q1 | reason | note |
|---|---|---|---|---|
