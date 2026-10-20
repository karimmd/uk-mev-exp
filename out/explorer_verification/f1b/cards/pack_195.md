# pack_195

Block 12620702. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x68460f6d1aa83edbef5372effeaa57af4ceb73a154d70b934417ab1c9565c78b`
- block 12620702, position 5, result success, from `0x5136a9a5d077ae4247c7706b577f77153c32a01c`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 189434 at 333.0 gwei, fee 0.063082 ETH
- token transfers (Blockscout, decoded):
  - 67220.510307 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 2106242.656301 MXS (`0x632fd938`): `0x5136a9a5d077ae4247c7706b577f77153c32a01c` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 16.111079 WETH (`0xc02aaa39`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 16.111079 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 16.111079 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 16.111079 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x5136a9a5d077ae4247c7706b577f77153c32a01c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 16.111079 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 5

### Victim leg: `0xcf77f17baabff24b10374927d45e72ad3a163986547293f99b61813e89bf10c5`
- block 12620702, position 18, result success, from `0x37cb2a6fbdd1981bba4b2aef17993a3f3df7baca`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 2.000000 ETH, gas used 177072 at 73.0 gwei, fee 0.012926 ETH
- token transfers (Blockscout, decoded):
  - 2.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 2.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 8465.535448 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 265253.444026 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x37cb2a6fbdd1981bba4b2aef17993a3f3df7baca`
- internal ETH transfers (Etherscan):
  - 2.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 2.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 18

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
