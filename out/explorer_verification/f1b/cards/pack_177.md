# pack_177

Block 13844430. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x6b9e89189a7b2d3730f9329384be513391d6e3a7e92f2120abb800d1fe816535`
- block 13844430, position 0, result success, from `0xba02a83d3fead87c1bfdc15f1c07db53888305a3`, to `0x00000081c57cbc967248bea482c417207e84cffb`, value 0.000000 ETH, gas used 230468 at 149.8 gwei, fee 0.034517 ETH
- token transfers (Blockscout, decoded):
  - 1096.878903 FLEX (`0xfcf8eda0`): `0x932a7b9941499f93ee7b1f9bfb3251a123636877` -> `0x3f61171b1297f6e512c750c172ba86026ab0e820`
  - 2.095656 WETH (`0xc02aaa39`): `0x00000081c57cbc967248bea482c417207e84cffb` -> `0x932a7b9941499f93ee7b1f9bfb3251a123636877`
  - 6077.899056 USDC (`0xa0b86991`): `0x3f61171b1297f6e512c750c172ba86026ab0e820` -> `0x00000081c57cbc967248bea482c417207e84cffb`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x932a7b9941499f93ee7b1f9bfb3251a123636877` UniswapV3 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Sync
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x61ef4f17860897e0ce470d7f3b8d721a33589ce619c0b0fde7475fe4e0124d53`
- block 13844430, position 1, result success, from `0x4085e9fb679dd2f60c2e64afe9533107fa1c18f2`, to `0xdef1c0ded9bec7f1a1670819833240f027b25eff`, value 0.000000 ETH, gas used 121988 at 141.9 gwei, fee 0.017309 ETH
- token transfers (Blockscout, decoded):
  - 1000.000000 FLEX (`0xfcf8eda0`): `0x4085e9fb679dd2f60c2e64afe9533107fa1c18f2` -> `0x3f61171b1297f6e512c750c172ba86026ab0e820`
  - 5100.657298 USDC (`0xa0b86991`): `0x3f61171b1297f6e512c750c172ba86026ab0e820` -> `0x4085e9fb679dd2f60c2e64afe9533107fa1c18f2`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Transfer
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Approval
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Sync
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xa8ec18ee55c3092e5237ad9a08a82622b3f9c38d1141f0a1b62e66d3b9a947b8`
- block 13844430, position 2, result success, from `0xba02a83d3fead87c1bfdc15f1c07db53888305a3`, to `0x00000081c57cbc967248bea482c417207e84cffb`, value 0.030522 ETH, gas used 220904 at 149.8 gwei, fee 0.033084 ETH
- token transfers (Blockscout, decoded):
  - 6077.899056 USDC (`0xa0b86991`): `0x00000081c57cbc967248bea482c417207e84cffb` -> `0x3f61171b1297f6e512c750c172ba86026ab0e820`
  - 1176.207067 FLEX (`0xfcf8eda0`): `0x3f61171b1297f6e512c750c172ba86026ab0e820` -> `0x00000081c57cbc967248bea482c417207e84cffb`
  - 2.197855 WETH (`0xc02aaa39`): `0x932a7b9941499f93ee7b1f9bfb3251a123636877` -> `0x00000081c57cbc967248bea482c417207e84cffb`
  - 1176.207067 FLEX (`0xfcf8eda0`): `0x00000081c57cbc967248bea482c417207e84cffb` -> `0x932a7b9941499f93ee7b1f9bfb3251a123636877`
- internal ETH transfers (Etherscan):
  - 0.030522 ETH: `0x00000081c57cbc967248bea482c417207e84cffb` -> `0x2daa35962a6d43eb54c48367b33d0b379c930e5e` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Transfer
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Sync
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Transfer
  - `0x932a7b9941499f93ee7b1f9bfb3251a123636877` UniswapV3 Swap
- receipt status 1, index 2
