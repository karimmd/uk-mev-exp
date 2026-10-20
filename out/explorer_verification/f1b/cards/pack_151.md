# pack_151

Block 12621054. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x985882fc10618a07235e7d6df0746905a1fc17238aeccc0455b6dc008db0891b`
- block 12621054, position 3, result success, from `0x2cfcbd233268c302996c767347eb45bec36fb08d`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 189446 at 150.0 gwei, fee 0.028417 ETH
- token transfers (Blockscout, decoded):
  - 96472.466718 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 3022803.957165 MXS (`0x632fd938`): `0x2cfcbd233268c302996c767347eb45bec36fb08d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 0.279685 WETH (`0xc02aaa39`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.279685 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.279685 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.279685 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x2cfcbd233268c302996c767347eb45bec36fb08d` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.279685 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 3

### Victim leg: `0x6f23ce51cef4240dc537dacc3ab7047e60841f4301d4c04549de3fc2946ee59e`
- block 12621054, position 123, result success, from `0x45fc5d7588e280b4b44139d33fe7bc85d991ddd2`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 230449 at 23.0 gwei, fee 0.005300 ETH
- token transfers (Blockscout, decoded):
  - 200.000000 USDT (`0xdac17f95`): `0x45fc5d7588e280b4b44139d33fe7bc85d991ddd2` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 0.082481 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 27514.775382 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 862129.628643 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x45fc5d7588e280b4b44139d33fe7bc85d991ddd2`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 123

### Back leg: `0x5f92a9246335e607b4e7f6fe1c57ebb2a3f1a6b2f791eb6290e8f63a77c7d840`
- block 12621054, position 132, result success, from `0x2435de45239b4a80c7946c6a251738d7adb6ea4a`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 179030 at 22.0 gwei, fee 0.003939 ETH
- token transfers (Blockscout, decoded):
  - 51753.546379 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 1621611.119890 MXS (`0x632fd938`): `0x2435de45239b4a80c7946c6a251738d7adb6ea4a` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 0.148546 WETH (`0xc02aaa39`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.148546 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.148546 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.148546 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x2435de45239b4a80c7946c6a251738d7adb6ea4a` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.148546 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 132
