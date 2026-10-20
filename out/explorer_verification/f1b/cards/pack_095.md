# pack_095

Block 13455734. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x476f497448ea44793f60616b4cd8baf3e858c7b6a4f70e116ad1d0bc6d8cb41b`
- block 13455734, position 0, result success, from `0x1dd71645847ba3a22df1261ad32d66d9a701552d`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 120032 at 177.3 gwei, fee 0.021284 ETH
- token transfers (Blockscout, decoded):
  - 2.759247 WETH (`0xc02aaa39`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 11205.140265 USDC (`0xa0b86991`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 111713.462276 ASM (`0x2565ae03`): `0xc47047e59bbc58cf223eaf2de10bc722cd46f325` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 11205.140265 USDC (`0xa0b86991`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0xc47047e59bbc58cf223eaf2de10bc722cd46f325`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0x2565ae0385659badcada1031db704442e1b69982` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc47047e59bbc58cf223eaf2de10bc722cd46f325` UniswapV3 Swap
- receipt status 1, index 0

### Victim leg: `0x5234956f0d3f34d4eb5cba137c8982a39b3604271c95ef7985907c4805deeafd`
- block 13455734, position 1, result success, from `0xa2a96f8d112d4eb47bb1630946cbfaecfe2a6efb`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 0.000000 ETH, gas used 199165 at 224.0 gwei, fee 0.044613 ETH
- token transfers (Blockscout, decoded):
  - 19985.972498 USDC (`0xa0b86991`): `0x7858e59e0c01ea06df3af3d20ac7b0003275d4bf` -> `0xe592427a0aece92de3edee1f18e0157c05861564`
  - 20000.000000 USDT (`0xdac17f95`): `0xa2a96f8d112d4eb47bb1630946cbfaecfe2a6efb` -> `0x7858e59e0c01ea06df3af3d20ac7b0003275d4bf`
  - 161708.965348 ASM (`0x2565ae03`): `0xc47047e59bbc58cf223eaf2de10bc722cd46f325` -> `0xa2a96f8d112d4eb47bb1630946cbfaecfe2a6efb`
  - 19985.972498 USDC (`0xa0b86991`): `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0xc47047e59bbc58cf223eaf2de10bc722cd46f325`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x7858e59e0c01ea06df3af3d20ac7b0003275d4bf` UniswapV3 Swap
  - `0x2565ae0385659badcada1031db704442e1b69982` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc47047e59bbc58cf223eaf2de10bc722cd46f325` UniswapV3 Swap
- receipt status 1, index 1

### Back leg: `0xbe377f9ed4b7e4fd60d7cac516ff0133c0d8f77949d54ba37a8ac31c3424dece`
- block 13455734, position 2, result success, from `0x1dd71645847ba3a22df1261ad32d66d9a701552d`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.578343 ETH, gas used 109977 at 177.3 gwei, fee 0.019501 ETH
- token transfers (Blockscout, decoded):
  - 14069.101940 USDC (`0xa0b86991`): `0xc47047e59bbc58cf223eaf2de10bc722cd46f325` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 111713.462276 ASM (`0x2565ae03`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0xc47047e59bbc58cf223eaf2de10bc722cd46f325`
  - 3.443655 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
- internal ETH transfers (Etherscan):
  - 0.578343 ETH: `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x829bd824b016326a401d083b33d092293333a830` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x2565ae0385659badcada1031db704442e1b69982` Transfer
  - `0xc47047e59bbc58cf223eaf2de10bc722cd46f325` UniswapV3 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
- receipt status 1, index 2
