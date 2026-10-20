# pack_056

Block 13203174. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x0bc043b47a84d46843373a611b8c147a330146b74225c6998b615c4e454d3877`
- block 13203174, position 0, result success, from `0x5b5001c4f80f33ec93b891062ed2e1d0acc05bb6`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 160507 at 52.8 gwei, fee 0.008480 ETH
- token transfers (Blockscout, decoded):
  - 9909.538068 USDC (`0xa0b86991`): `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` -> `0x3155acd9f75915fcc21d34035f440da7040bd3ba`
  - 3.064233 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640`
  - 3514.902670 PROS (`0x8642a849`): `0x3155acd9f75915fcc21d34035f440da7040bd3ba` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` UniswapV3 Swap
  - `0x8642a849d0dcb7a15a974794668adcfbe4794b56` Transfer
  - `0x3155acd9f75915fcc21d34035f440da7040bd3ba` UniswapV2 Sync
  - `0x3155acd9f75915fcc21d34035f440da7040bd3ba` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x671ee90a734dfac32ba7bb806d0f0df73720d9ba8be9cf7ebd9c7f3ffd2b1a44`
- block 13203174, position 1, result success, from `0x6eacac9ab65402e8d069db326d7515a467b24ced`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 108802 at 251.8 gwei, fee 0.027402 ETH
- token transfers (Blockscout, decoded):
  - 7000.000000 USDC (`0xa0b86991`): `0x6eacac9ab65402e8d069db326d7515a467b24ced` -> `0x3155acd9f75915fcc21d34035f440da7040bd3ba`
  - 2420.017728 PROS (`0x8642a849`): `0x3155acd9f75915fcc21d34035f440da7040bd3ba` -> `0x9a318b20f45c2fed4e41a972de4157627c8301c4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x8642a849d0dcb7a15a974794668adcfbe4794b56` Transfer
  - `0x3155acd9f75915fcc21d34035f440da7040bd3ba` UniswapV2 Sync
  - `0x3155acd9f75915fcc21d34035f440da7040bd3ba` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xf0957b405139d23dc06c7d998b8d31a1377c7bc1f7ecd50f546865707882c975`
- block 13203174, position 2, result success, from `0x5b5001c4f80f33ec93b891062ed2e1d0acc05bb6`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.019206 ETH, gas used 169039 at 52.8 gwei, fee 0.008931 ETH
- token transfers (Blockscout, decoded):
  - 3514.902670 PROS (`0x8642a849`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x3155acd9f75915fcc21d34035f440da7040bd3ba`
  - 10059.240709 USDC (`0xa0b86991`): `0x3155acd9f75915fcc21d34035f440da7040bd3ba` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 3.107414 WETH (`0xc02aaa39`): `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 10059.240709 USDC (`0xa0b86991`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640`
- internal ETH transfers (Etherscan):
  - 0.019206 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x7f101fe45e6649a6fb8f3f8b43ed03d353f2b90c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x8642a849d0dcb7a15a974794668adcfbe4794b56` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x3155acd9f75915fcc21d34035f440da7040bd3ba` UniswapV2 Sync
  - `0x3155acd9f75915fcc21d34035f440da7040bd3ba` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` UniswapV3 Swap
- receipt status 1, index 2
