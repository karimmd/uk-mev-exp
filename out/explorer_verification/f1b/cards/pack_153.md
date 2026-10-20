# pack_153

Block 12709318. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x8f36f793e3205eee088b2025dbfa8ad717e1b8bb479fdd8c2b827706faab43ac`
- block 12709318, position 0, result success, from `0x01af3c277703da8510c202698e939c7a83aca361`, to `0xf2972a2b8eda253678877995147869ed99b50e39`, value 0.000000 ETH, gas used 162892 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 3.554376 WETH (`0xc02aaa39`): `0xf2972a2b8eda253678877995147869ed99b50e39` -> `0xc491405d542a393d8d202a72f0fb076447e61891`
  - 213636.452861 WHACKD (`0xcf833572`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0xf2972a2b8eda253678877995147869ed99b50e39`
  - 23737.383651 WHACKD (`0xcf833572`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Sync
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x1bfb93c23f7a49f5b8753e5387e63fb5448b682257e7f7df9b70c26545fb6efc`
- block 12709318, position 1, result success, from `0x5a659e1e34f6d52428589a0e8078f9713feaeb83`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 231485 at 10.0 gwei, fee 0.002315 ETH
- token transfers (Blockscout, decoded):
  - 9913.230000 TCR (`0xe38b72d6`): `0x5a659e1e34f6d52428589a0e8078f9713feaeb83` -> `0x420725a69e79eeffb000f98ccd78a52369b6c5d4`
  - 17858.507438 USDT (`0xdac17f95`): `0x420725a69e79eeffb000f98ccd78a52369b6c5d4` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 9.996799 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0xc491405d542a393d8d202a72f0fb076447e61891`
  - 456669.797009 WHACKD (`0xcf833572`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0x5a659e1e34f6d52428589a0e8078f9713feaeb83`
  - 50741.088557 WHACKD (`0xcf833572`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xe38b72d6595fd3885d1d2f770aa23e94757f91a1` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x420725a69e79eeffb000f98ccd78a52369b6c5d4` UniswapV2 Sync
  - `0x420725a69e79eeffb000f98ccd78a52369b6c5d4` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Sync
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xefe29fb729916607c5139679f7b0506129fdeb9db44323473112f6d2385d7ec9`
- block 12709318, position 2, result success, from `0x01af3c277703da8510c202698e939c7a83aca361`, to `0xf2972a2b8eda253678877995147869ed99b50e39`, value 0.000000 ETH, gas used 121833 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 192272.807575 WHACKD (`0xcf833572`): `0xf2972a2b8eda253678877995147869ed99b50e39` -> `0xc491405d542a393d8d202a72f0fb076447e61891`
  - 21363.645286 WHACKD (`0xcf833572`): `0xf2972a2b8eda253678877995147869ed99b50e39` -> `0x0000000000000000000000000000000000000000`
  - 4.233317 WETH (`0xc02aaa39`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0xf2972a2b8eda253678877995147869ed99b50e39`
  - 0.474728 WETH (`0xc02aaa39`): `0xf2972a2b8eda253678877995147869ed99b50e39` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.474728 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0xf2972a2b8eda253678877995147869ed99b50e39` [call]
  - 0.474728 ETH: `0xf2972a2b8eda253678877995147869ed99b50e39` -> `0xbcc817f057950b0df41206c5d7125e6225cae18e` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Sync
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.474728 ETH for `0xf2972a2b8eda253678877995147869ed99b50e39`
- receipt status 1, index 2
