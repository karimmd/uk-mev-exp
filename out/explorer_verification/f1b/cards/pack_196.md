# pack_196

Block 12620878. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x995f4797dca826ec24f41c437656414a3d271ee4c71e48a192a9310e466d0d68`
- block 12620878, position 5, result success, from `0x09c950e4b7b3345c626e9c1188c720de68958a05`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.050000 ETH, gas used 159960 at 33.0 gwei, fee 0.005279 ETH
- token transfers (Blockscout, decoded):
  - 0.050000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.050000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 2738.343990 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 85801.445022 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x09c950e4b7b3345c626e9c1188c720de68958a05`
- internal ETH transfers (Etherscan):
  - 0.050000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.050000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 5

### Victim leg: `0x4b46debaa4cf3e7cc0e3d162d65363901666bf57a1797b55e42ee6b5191141ac`
- block 12620878, position 25, result success, from `0x0448b39b7805fba1eb0092863829794250f585c0`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 179006 at 25.3 gwei, fee 0.004529 ETH
- token transfers (Blockscout, decoded):
  - 10739.192567 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 336494.700421 MXS (`0x632fd938`): `0x0448b39b7805fba1eb0092863829794250f585c0` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 0.184296 WETH (`0xc02aaa39`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.184296 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.184296 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.184296 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0448b39b7805fba1eb0092863829794250f585c0` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.184296 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 25

### Back leg: `0x2cbd2fb8e92b876cef9e01772dae12f04363271f7a8eae8c8da73c4db75a065b`
- block 12620878, position 110, result success, from `0x5e4872715dcd6488d7b9417e8a77e592e5a0814b`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.052500 ETH, gas used 177072 at 17.6 gwei, fee 0.003116 ETH
- token transfers (Blockscout, decoded):
  - 0.052500 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.052500 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f`
  - 2812.907290 MXS (`0x632fd938`): `0x632fd938b98d740faee69112ed41257be3f83c7c` -> `0x0000000000000000000000000000000000000000`
  - 88137.761741 MXS (`0x632fd938`): `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` -> `0x5e4872715dcd6488d7b9417e8a77e592e5a0814b`
- internal ETH transfers (Etherscan):
  - 0.052500 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.052500 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x632fd938b98d740faee69112ed41257be3f83c7c` Transfer
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Sync
  - `0x13bb5add7fd43c52d987e2c320f95d4b5e9cfa5f` UniswapV2 Swap
- receipt status 1, index 110
