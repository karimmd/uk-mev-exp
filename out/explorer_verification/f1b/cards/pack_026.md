# pack_026

Block 12457726. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xab2f4108ddbd65096ecfa0ca15e879727dcc87ba31dcfc31308bd9b87d0b1e9c`
- block 12457726, position 250, result success, from `0x96ca003cb319b5024125154a94a7911ef898cd7e`, to `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7`, value 0.000000 ETH, gas used 133307 at 59.4 gwei, fee 0.007918 ETH
- token transfers (Blockscout, decoded):
  - 0.450000 WETH (`0xc02aaa39`): `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7` -> `0x0000000000000000000000000000000000000000`
  - 0.450000 WETH (`0xc02aaa39`): `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7` -> `0x1549a45a18b1658783aa27068fee449cc80876ce`
  - 90815923163824.687500 MADINU (`0x62af108d`): `0x1549a45a18b1658783aa27068fee449cc80876ce` -> `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7`
- internal ETH transfers (Etherscan):
  - 0.450000 ETH: `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.450000 ETH for `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x62af108df4d945288f13400bcc26580147f7f0ce` Transfer
  - `0x1549a45a18b1658783aa27068fee449cc80876ce` UniswapV2 Sync
  - `0x1549a45a18b1658783aa27068fee449cc80876ce` UniswapV2 Swap
- receipt status 1, index 250

### Victim leg: `0x10e86e49d5d549ea3164871861bc035d9c68e9de556cf5d5b22977c8b687f4ea`
- block 12457726, position 251, result success, from `0x1dab8a0deebd7d77a5558c0de7f07e25663e6975`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 166113 at 59.4 gwei, fee 0.009867 ETH
- token transfers (Blockscout, decoded):
  - 7269.603135 USDT (`0xdac17f95`): `0x1dab8a0deebd7d77a5558c0de7f07e25663e6975` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 2.090085 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x1549a45a18b1658783aa27068fee449cc80876ce`
  - 388599137310250.375000 MADINU (`0x62af108d`): `0x1549a45a18b1658783aa27068fee449cc80876ce` -> `0x1dab8a0deebd7d77a5558c0de7f07e25663e6975`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x62af108df4d945288f13400bcc26580147f7f0ce` Transfer
  - `0x1549a45a18b1658783aa27068fee449cc80876ce` UniswapV2 Sync
  - `0x1549a45a18b1658783aa27068fee449cc80876ce` UniswapV2 Swap
- receipt status 1, index 251

### Back leg: `0xdb105bff31c99aec0190b9577e3a76201de803b8052ef74b17d6ff9a2ab1e7f8`
- block 12457726, position 252, result success, from `0x96ca003cb319b5024125154a94a7911ef898cd7e`, to `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7`, value 0.000000 ETH, gas used 120155 at 59.4 gwei, fee 0.007137 ETH
- token transfers (Blockscout, decoded):
  - 89008313126009.531250 MADINU (`0x62af108d`): `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7` -> `0x1549a45a18b1658783aa27068fee449cc80876ce`
  - 0.491661 WETH (`0xc02aaa39`): `0x1549a45a18b1658783aa27068fee449cc80876ce` -> `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7`
  - 0.491661 WETH (`0xc02aaa39`): `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.491661 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x62af108df4d945288f13400bcc26580147f7f0ce` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1549a45a18b1658783aa27068fee449cc80876ce` UniswapV2 Sync
  - `0x1549a45a18b1658783aa27068fee449cc80876ce` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.491661 ETH for `0x9282dc5c422fa91ff2f6ff3a0b45b7bf97cf78e7`
- receipt status 1, index 252
