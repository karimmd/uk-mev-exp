# pack_194

Block 12620790. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe2b229d5aa6d1fb1bd69532db5abee2232a12cf9345e4e060399e0a926d17892`
- block 12620790, position 70, result success, from `0xbcdec0b56453796979fef56747e7de10281e9c25`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.027708 ETH, gas used 184451 at 29.0 gwei, fee 0.005349 ETH
- token transfers (Blockscout, decoded):
  - 0.017438 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.017438 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 673.263000 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 21095.574000 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0xbcdec0b56453796979fef56747e7de10281e9c25`
- internal ETH transfers (Etherscan):
  - 0.017438 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.010270 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xbcdec0b56453796979fef56747e7de10281e9c25` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.017438 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 70

### Victim leg: `0x7fe5dd6d01c2808af71ec078ba9f4c0fd3396292448cb0797f872d526085a9d2`
- block 12620790, position 82, result success, from `0x93ce319485af9a23433050e279c3481c203eb283`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 207008 at 27.5 gwei, fee 0.005693 ETH
- token transfers (Blockscout, decoded):
  - 200000000.000000 SHIB (`0x95ad61b0`): `0x93ce319485af9a23433050e279c3481c203eb283` -> `0x811beed0119b4afce20d2583eb608c6f7af1954f`
  - 0.507968 WETH (`0xc02aaa39`): `0x811beed0119b4afce20d2583eb608c6f7af1954f` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 19532.059640 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 612004.535392 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x93ce319485af9a23433050e279c3481c203eb283`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Transfer
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x811beed0119b4afce20d2583eb608c6f7af1954f` UniswapV2 Sync
  - `0x811beed0119b4afce20d2583eb608c6f7af1954f` UniswapV2 Swap
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 82

### Back leg: `0x3859fc8ac77f83932b9de5fff93ca39f517c238d0437b88d847e5e165aed4a64`
- block 12620790, position 135, result success, from `0x7612f25f5d6a24745a122aa1174e88d8202cff6a`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.005544 ETH, gas used 159960 at 22.0 gwei, fee 0.003519 ETH
- token transfers (Blockscout, decoded):
  - 0.005544 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.005544 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 225.454775 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 7064.249616 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7612f25f5d6a24745a122aa1174e88d8202cff6a`
- internal ETH transfers (Etherscan):
  - 0.005544 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.005544 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 135
