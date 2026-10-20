# pack_020

Block 12620702. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xb6c134364ea4b66add5ec07f91212d2db680861beb5b00b7df0be0df03416698`
- block 12620702, position 13, result success, from `0x071cac3a76241945f8e751c836d5c86a10a9acea`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 179030 at 100.0 gwei, fee 0.017903 ETH
- token transfers (Blockscout, decoded):
  - 40247.130473 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 1261076.754820 MXS (`0x632fd938`): `0x071cac3a76241945f8e751c836d5c86a10a9acea` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 9.044372 WETH (`0xc02aaa39`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 9.044372 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 9.044372 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 9.044372 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x071cac3a76241945f8e751c836d5c86a10a9acea` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 9.044372 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 13

### Victim leg: `0xe7afb7589ca710f863c224341e667c1f9b6eb5fb2904496a012a5d6ad2158943`
- block 12620702, position 33, result success, from `0xdefba66ec8642fa0d19c4275e712a76480060634`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 232481 at 50.0 gwei, fee 0.011624 ETH
- token transfers (Blockscout, decoded):
  - 2000.000000 USDC (`0xa0b86991`): `0xdefba66ec8642fa0d19c4275e712a76480060634` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 0.832457 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 3494.034112 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 109479.735508 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0xdefba66ec8642fa0d19c4275e712a76480060634`
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
- receipt status 1, index 33

### Back leg: `0x70f098521d0bf557f215532748e802663d94454ac6b83916dc4acffd0630b9f0`
- block 12620702, position 81, result success, from `0x09aeafc2853c6a81524c8fe57c9fadfb5af4c843`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.030000 ETH, gas used 159960 at 36.3 gwei, fee 0.005807 ETH
- token transfers (Blockscout, decoded):
  - 0.030000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.030000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 125.371745 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 3928.314691 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x09aeafc2853c6a81524c8fe57c9fadfb5af4c843`
- internal ETH transfers (Etherscan):
  - 0.030000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.030000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 81
