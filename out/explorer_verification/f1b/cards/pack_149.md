# pack_149

Block 12692950. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x4528fb6d48b76624c455a492578e8b23133fbaf305c0e8687bd43bdb1900f0d7`
- block 12692950, position 0, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 113151 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 11.096637 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88`
  - 13349661072931.722656 KISHU (`0xa2b4c0af`): `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x942821b545a56fc62a320624bc8f747f3fea0ea4` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xa01bad3f1dbf71612442d222747d481ebc8f6d59` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x7df8577a5c094d4f43ec3f272b593729bce58d16` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xa12cd517388df2f590ec8f9349c3890842489c10` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x9bdde6c0f20cefe39a0a7c1af40a3c2458f979ef` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa2b4c0af19cc16a6cfacce81f192b024d625817d` Transfer
  - `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` UniswapV2 Sync
  - `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x2fdbf2ec346c3be21c2d49d8c6671dc00db819e5e9c793bb3d3caa53d80a1f14`
- block 12692950, position 1, result success, from `0x219a96badc02aa68df42951277cb981a23aaa877`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 244166 at 11.0 gwei, fee 0.002686 ETH
- token transfers (Blockscout, decoded):
  - 36807.899820 USDC (`0xa0b86991`): `0x219a96badc02aa68df42951277cb981a23aaa877` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 18.947700 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88`
  - 21758044822461.507812 KISHU (`0xa2b4c0af`): `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` -> `0x219a96badc02aa68df42951277cb981a23aaa877`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0xa2b4c0af19cc16a6cfacce81f192b024d625817d` Transfer
  - `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` UniswapV2 Sync
  - `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x12764ca82dd3ae6843f3016b1f54978f6b4e7f5c9e994d4428844130f3369550`
- block 12692950, position 2, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.125885 ETH, gas used 118731 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 13082763216650.994141 KISHU (`0xa2b4c0af`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88`
  - 11.233617 WETH (`0xc02aaa39`): `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x81bd562c35be19a91afb81103a29ad5a8209ceda` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xe133aa8f81815ab681e1cec0abf6a3d6fb8801d8` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x85ae2b176a6b9aa6e0bba9a6a6d1dc328402bd4a` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x5d9976e56db48b460806bf00a4dc71d1e3cb7e4d` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.125885 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x1ad91ee08f21be3de0ba2ba6918e714da6b45836` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xa2b4c0af19cc16a6cfacce81f192b024d625817d` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` UniswapV2 Sync
  - `0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88` UniswapV2 Swap
- receipt status 1, index 2
