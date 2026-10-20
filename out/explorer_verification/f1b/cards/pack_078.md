# pack_078

Block 12620966. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x04aca6f266629516c224f6544f522ea68232f124a299dacc523c50c48da76129`
- block 12620966, position 51, result success, from `0x882efb9e67eda9bf74766e8686259cb3a1fc8b8a`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 189386 at 21.0 gwei, fee 0.003977 ETH
- token transfers (Blockscout, decoded):
  - 30000.000000 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 940000.000000 MXS (`0x632fd938`): `0x882efb9e67eda9bf74766e8686259cb3a1fc8b8a` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 0.058469 WETH (`0xc02aaa39`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.058469 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.058469 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.058469 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x882efb9e67eda9bf74766e8686259cb3a1fc8b8a` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.058469 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 51

### Victim leg: `0x9a04afb29aa190fa61c5e9eb5925b420aa0986a35b26f3253a8f3353bbdaacb3`
- block 12620966, position 93, result success, from `0x563b3d92a0ee49c281ee50324bcd659b2bdba414`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 178994 at 19.0 gwei, fee 0.003401 ETH
- token transfers (Blockscout, decoded):
  - 120000.000000 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 3760000.000000 MXS (`0x632fd938`): `0x563b3d92a0ee49c281ee50324bcd659b2bdba414` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 0.233017 WETH (`0xc02aaa39`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.233017 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.233017 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.233017 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x563b3d92a0ee49c281ee50324bcd659b2bdba414` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.233017 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 93

### Back leg: `0xdf4c8107372a3cb736f69bf83fac1c6212e875265b3b163773cc8b83b31102a7`
- block 12620966, position 100, result success, from `0x1feb8b8b87983ebe826bd12321775b5a51af699d`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.100000 ETH, gas used 159972 at 18.7 gwei, fee 0.002991 ETH
- token transfers (Blockscout, decoded):
  - 0.100000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.100000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 49730.068505 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 1558208.813165 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x1feb8b8b87983ebe826bd12321775b5a51af699d`
- internal ETH transfers (Etherscan):
  - 0.100000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.100000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 100
