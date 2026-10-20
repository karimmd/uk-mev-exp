# pack_169

Block 12858214. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x339c7647c81ea461a164b2c514fc906b1b4accfc8e4b42c55f85ac5df37a1717`
- block 12858214, position 2, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x000000000027d2efc283613d0c3e24a8b430c4d8`, value 0.000000 ETH, gas used 68355 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 12.118578 WETH (`0xc02aaa39`): `0x000000000027d2efc283613d0c3e24a8b430c4d8` -> `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e`
  - 32742191893.925209 STARL (`0x8e6cd950`): `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x5ef43dd3a1182e89f55b7a7d29cbdf24334de5f1` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
  - 0.000000 ETH: `0x641dfc834bc01c7598a3a824efea2c1029e10903` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8e6cd950ad6ba651f6dd608dc70e5886b1aa6b24` Transfer
  - `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` UniswapV2 Sync
  - `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` UniswapV2 Swap
- receipt status 1, index 2

### Victim leg: `0xf6a072bc1e848c1f46e3b9be3e8e1b6aefa96df2d85242c461fb48fd6cceeacd`
- block 12858214, position 4, result success, from `0x2f31931f23c7cbfd95f564c01a871fc3dae7e7c6`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.150000 ETH, gas used 94178 at 43.0 gwei, fee 0.004050 ETH
- token transfers (Blockscout, decoded):
  - 0.150000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.150000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e`
  - 383355029.476286 STARL (`0x8e6cd950`): `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` -> `0x2f31931f23c7cbfd95f564c01a871fc3dae7e7c6`
- internal ETH transfers (Etherscan):
  - 0.150000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.150000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8e6cd950ad6ba651f6dd608dc70e5886b1aa6b24` Transfer
  - `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` UniswapV2 Sync
  - `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x33d12ac859ed1297781a66e6aa972d91861e78d5adba91fb9b16c08690b04c71`
- block 12858214, position 5, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x000000000027d2efc283613d0c3e24a8b430c4d8`, value 0.077441 ETH, gas used 67794 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 32742191893.925209 STARL (`0x8e6cd950`): `0x000000000027d2efc283613d0c3e24a8b430c4d8` -> `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e`
  - 12.273782 WETH (`0xc02aaa39`): `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8`
- internal ETH transfers (Etherscan):
  - 0.077441 ETH: `0x000000000027d2efc283613d0c3e24a8b430c4d8` -> `0xb3b7874f13387d44a3398d298b075b7a3505d8d4` [call]
  - 0.000000 ETH: `0x868bb33f6f7dbeadde9cce7076966971269c6ae5` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
  - 0.000000 ETH: `0x45a0554257bd8391211c5af2a773e81c0b717de2` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
  - 0.000000 ETH: `0x627320172008db97a4e5120c2847fc4dce242121` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x8e6cd950ad6ba651f6dd608dc70e5886b1aa6b24` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` UniswapV2 Sync
  - `0xa5e9c917b4b821e4e0a5bbefce078ab6540d6b5e` UniswapV2 Swap
- receipt status 1, index 5
