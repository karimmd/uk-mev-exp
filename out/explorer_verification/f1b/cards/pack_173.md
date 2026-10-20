# pack_173

Block 12461158. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xada818f8fc677bd7d21da16ba29191be6d1d7056bda0eb9b9e61500317841e27`
- block 12461158, position 0, result success, from `0x1a5cce39c514857460ac51fe9e2dcd9ab3ec9b36`, to `0x575c3a99429352eda66661fc3857b9f83f58a73f`, value 0.000000 ETH, gas used 147977 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 2.432921 WETH (`0xc02aaa39`): `0x575c3a99429352eda66661fc3857b9f83f58a73f` -> `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcdebf323521489ed806d7c443cd4f179532079e6` Transfer
  - `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9` UniswapV2 Sync
  - `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xd4fe5c8c7209cb39878112575b2681a7cff049408cf2205e31203d2cca1507bb`
- block 12461158, position 1, result success, from `0xb4cf38ab9fbdbed00b79c851c9e4639b9cce757f`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 160723 at 108.0 gwei, fee 0.017358 ETH
- token transfers (Blockscout, decoded):
  - 2.000000 LEASH (`0x27c70cd1`): `0xb4cf38ab9fbdbed00b79c851c9e4639b9cce757f` -> `0x874376be8231dad99aabf9ef0767b3cc054c60ee`
  - 2.374003 WETH (`0xc02aaa39`): `0x874376be8231dad99aabf9ef0767b3cc054c60ee` -> `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x27c70cd1946795b66be9d954418546998b546634` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x874376be8231dad99aabf9ef0767b3cc054c60ee` UniswapV2 Sync
  - `0x874376be8231dad99aabf9ef0767b3cc054c60ee` UniswapV2 Swap
  - `0xcdebf323521489ed806d7c443cd4f179532079e6` Transfer
  - `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9` UniswapV2 Sync
  - `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xdfce2d7f05c8fba1ca5bb6d5def7dbf5e5ff46a005e2b903f11157ca8f882d89`
- block 12461158, position 2, result success, from `0x1a5cce39c514857460ac51fe9e2dcd9ab3ec9b36`, to `0x575c3a99429352eda66661fc3857b9f83f58a73f`, value 0.000000 ETH, gas used 120340 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 2.681661 WETH (`0xc02aaa39`): `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9` -> `0x575c3a99429352eda66661fc3857b9f83f58a73f`
  - 0.173923 WETH (`0xc02aaa39`): `0x575c3a99429352eda66661fc3857b9f83f58a73f` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.173923 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x575c3a99429352eda66661fc3857b9f83f58a73f` [call]
  - 0.173923 ETH: `0x575c3a99429352eda66661fc3857b9f83f58a73f` -> `0x99c85bb64564d9ef9a99621301f22c9993cb89e3` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xcdebf323521489ed806d7c443cd4f179532079e6` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9` UniswapV2 Sync
  - `0xc532495dfe1b9d43a8e602f0d8da96fd40b92ce9` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.173923 ETH for `0x575c3a99429352eda66661fc3857b9f83f58a73f`
- receipt status 1, index 2
