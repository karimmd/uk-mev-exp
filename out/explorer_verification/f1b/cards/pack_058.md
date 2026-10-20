# pack_058

Block 12279350. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x801b7ef687308f22a764f3ee2bd900cd5f8694d95bb07d7435cf79ead869a6c5`
- block 12279350, position 3, result success, from `0xf6da21e95d74767009accb145b96897ac3630bad`, to `0xd78a3280085ee846196cb5fab7d510b279486d44`, value 0.000000 ETH, gas used 116530 at 1.0 gwei, fee 0.000117 ETH
- token transfers (Blockscout, decoded):
  - 1.910809 WETH (`0xc02aaa39`): `0xf6da21e95d74767009accb145b96897ac3630bad` -> `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1`
  - 56743425.820471 ARCN (`0x3781731a`): `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` -> `0xf6da21e95d74767009accb145b96897ac3630bad`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x3781731acd887b14d7f7f261f3aada7f6405868a` Transfer
  - `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` UniswapV2 Sync
  - `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0xc1b220673c04b0f0c9849c39d167a1d6031b5a0cdeb194de5d8f55d9631fc74c`
- block 12279350, position 4, result success, from `0xac7ee1786bdbcabc2120ae4162d5d53c56bfdbf0`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 1.000000 ETH, gas used 108567 at 300.0 gwei, fee 0.032570 ETH
- token transfers (Blockscout, decoded):
  - 1.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 1.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1`
  - 22931052.637875 ARCN (`0x3781731a`): `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` -> `0xac7ee1786bdbcabc2120ae4162d5d53c56bfdbf0`
- internal ETH transfers (Etherscan):
  - 1.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x3781731acd887b14d7f7f261f3aada7f6405868a` Transfer
  - `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` UniswapV2 Sync
  - `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x41935a7766d289176cae8ddd13b2ddc1c4c86828b5de7acde1cb65f0e807ff72`
- block 12279350, position 6, result success, from `0xf6da21e95d74767009accb145b96897ac3630bad`, to `0xd78a3280085ee846196cb5fab7d510b279486d44`, value 0.000000 ETH, gas used 77277 at 1.0 gwei, fee 0.000077 ETH
- token transfers (Blockscout, decoded):
  - 56743425.820471 ARCN (`0x3781731a`): `0xf6da21e95d74767009accb145b96897ac3630bad` -> `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1`
  - 2.207333 WETH (`0xc02aaa39`): `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` -> `0xf6da21e95d74767009accb145b96897ac3630bad`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x3781731acd887b14d7f7f261f3aada7f6405868a` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` UniswapV2 Sync
  - `0xaf56ade10a2fec340e09e19a11f32beaf1a3a6a1` UniswapV2 Swap
- receipt status 1, index 6
