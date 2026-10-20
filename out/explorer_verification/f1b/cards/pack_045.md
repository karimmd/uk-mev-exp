# pack_045

Block 12620350. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x147661be222b04716b8560d0135ea9014dabf52da63460b7c4bb7fb0b1c54a10`
- block 12620350, position 12, result success, from `0xb54206d66747abe7d6b3ccc8adeaad953a0764c6`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 1.000000 ETH, gas used 177072 at 62.0 gwei, fee 0.010978 ETH
- token transfers (Blockscout, decoded):
  - 1.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 1.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 547.139906 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 17143.717040 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0xb54206d66747abe7d6b3ccc8adeaad953a0764c6`
- internal ETH transfers (Etherscan):
  - 1.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 12

### Victim leg: `0x1e8c7991d01da6ac30bb551216151779aca53b425a410e0b2ba1a349e13590b2`
- block 12620350, position 19, result success, from `0x6745ac639d018a7cd11ee4925b7455bb58802c74`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 234605 at 61.0 gwei, fee 0.014311 ETH
- token transfers (Blockscout, decoded):
  - 6927.189577 USDC (`0xa0b86991`): `0x6745ac639d018a7cd11ee4925b7455bb58802c74` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 2.839778 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 1547.508558 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 48488.601486 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x6745ac639d018a7cd11ee4925b7455bb58802c74`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 19

### Back leg: `0x972da8018ceb92b6132d69d18738973a89db27eb1760eb55aff945655b350362`
- block 12620350, position 62, result success, from `0x7440e38fffd1b182e71f552bb5e48d64fd3a45c3`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.270000 ETH, gas used 177060 at 60.5 gwei, fee 0.010712 ETH
- token transfers (Blockscout, decoded):
  - 0.270000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.270000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 147.411609 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 4618.897084 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7440e38fffd1b182e71f552bb5e48d64fd3a45c3`
- internal ETH transfers (Etherscan):
  - 0.270000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.270000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 62
