# pack_105

Block 13242862. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x92340901a5b5940089e05e41e4a464edd2c55e8411d2287f3aff34f5364d122f`
- block 13242862, position 0, result success, from `0xae75d1db460a63d593d9cbbd83fa457f3619cdaf`, to `0x0000007c68390193776e8b44df3b698d311070b9`, value 0.000000 ETH, gas used 104591 at 55.7 gwei, fee 0.005831 ETH
- token transfers (Blockscout, decoded):
  - 328460.712404 POP (`0x5d858bcd`): `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690` -> `0x0000007c68390193776e8b44df3b698d311070b9`
  - 1.529115 WETH (`0xc02aaa39`): `0x0000007c68390193776e8b44df3b698d311070b9` -> `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x5d858bcd53e085920620549214a8b27ce2f04670` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690` UniswapV3 Swap
- receipt status 1, index 0

### Victim leg: `0x2612df8b7b97ca98f5d5c2c2162e9db89b6d179d270790de092fe22deb2ca346`
- block 13242862, position 1, result success, from `0x06ca515711650b4a835bea6260b7a6fbdad0ac44`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 0.750000 ETH, gas used 123594 at 57.2 gwei, fee 0.007076 ETH
- token transfers (Blockscout, decoded):
  - 150056.627850 POP (`0x5d858bcd`): `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690` -> `0x06ca515711650b4a835bea6260b7a6fbdad0ac44`
  - 0.750000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xe592427a0aece92de3edee1f18e0157c05861564`
  - 0.750000 WETH (`0xc02aaa39`): `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690`
- internal ETH transfers (Etherscan):
  - 0.750000 ETH: `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x5d858bcd53e085920620549214a8b27ce2f04670` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.750000 ETH for `0xe592427a0aece92de3edee1f18e0157c05861564`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690` UniswapV3 Swap
- receipt status 1, index 1

### Back leg: `0xb933b4214934c5d3ec54bc5c2ea204affe88acdfba74b116a8defbf7dcb0448b`
- block 13242862, position 2, result success, from `0xae75d1db460a63d593d9cbbd83fa457f3619cdaf`, to `0x0000007c68390193776e8b44df3b698d311070b9`, value 0.000000 ETH, gas used 94825 at 492.2 gwei, fee 0.046672 ETH
- token transfers (Blockscout, decoded):
  - 1.589444 WETH (`0xc02aaa39`): `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690` -> `0x0000007c68390193776e8b44df3b698d311070b9`
  - 328460.712404 POP (`0x5d858bcd`): `0x0000007c68390193776e8b44df3b698d311070b9` -> `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x5d858bcd53e085920620549214a8b27ce2f04670` Transfer
  - `0xc4002da5ceb8c65b3dd985f6c4a9bc961d932690` UniswapV3 Swap
- receipt status 1, index 2
