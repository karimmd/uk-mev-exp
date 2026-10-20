# pack_011

Block 13761182. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xf2ecfb7b499b459cdaf747f32c69cdd19493c04b2dae895184010669720da45b`
- block 13761182, position 1, result success, from `0xe51c5f47f08fd806575e5682b090d2f2d1038192`, to `0x00000000726422a6fecb4759b44d47e48cf746aa`, value 0.000000 ETH, gas used 182697 at 91.6 gwei, fee 0.016728 ETH
- token transfers (Blockscout, decoded):
  - 1299.388879 FLEX (`0xfcf8eda0`): `0x932a7b9941499f93ee7b1f9bfb3251a123636877` -> `0x3f61171b1297f6e512c750c172ba86026ab0e820`
  - 7388.229585 USDC (`0xa0b86991`): `0x3f61171b1297f6e512c750c172ba86026ab0e820` -> `0x00000000726422a6fecb4759b44d47e48cf746aa`
  - 2.285589 WETH (`0xc02aaa39`): `0x00000000726422a6fecb4759b44d47e48cf746aa` -> `0x932a7b9941499f93ee7b1f9bfb3251a123636877`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Sync
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x932a7b9941499f93ee7b1f9bfb3251a123636877` UniswapV3 Swap
- receipt status 1, index 1

### Victim leg: `0x397b3982decb5245bf9c2143291eb38af0f503f96a9818339bb0819448ede59f`
- block 13761182, position 2, result success, from `0x4085e9fb679dd2f60c2e64afe9533107fa1c18f2`, to `0xdef1c0ded9bec7f1a1670819833240f027b25eff`, value 0.000000 ETH, gas used 121988 at 99.7 gwei, fee 0.012165 ETH
- token transfers (Blockscout, decoded):
  - 1000.000000 FLEX (`0xfcf8eda0`): `0x4085e9fb679dd2f60c2e64afe9533107fa1c18f2` -> `0x3f61171b1297f6e512c750c172ba86026ab0e820`
  - 5179.742349 USDC (`0xa0b86991`): `0x3f61171b1297f6e512c750c172ba86026ab0e820` -> `0x4085e9fb679dd2f60c2e64afe9533107fa1c18f2`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Transfer
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Approval
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Sync
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Swap
- receipt status 1, index 2

### Back leg: `0x292c67752cab9ed4e4f4265998e30438a6790b896e09a85e091927a04c77f86f`
- block 13761182, position 3, result success, from `0xe51c5f47f08fd806575e5682b090d2f2d1038192`, to `0x00000000726422a6fecb4759b44d47e48cf746aa`, value 0.000000 ETH, gas used 168592 at 483.8 gwei, fee 0.081560 ETH
- token transfers (Blockscout, decoded):
  - 2.394902 WETH (`0xc02aaa39`): `0x932a7b9941499f93ee7b1f9bfb3251a123636877` -> `0x00000000726422a6fecb4759b44d47e48cf746aa`
  - 7388.229584 USDC (`0xa0b86991`): `0x00000000726422a6fecb4759b44d47e48cf746aa` -> `0x3f61171b1297f6e512c750c172ba86026ab0e820`
  - 1395.227724 FLEX (`0xfcf8eda0`): `0x3f61171b1297f6e512c750c172ba86026ab0e820` -> `0x932a7b9941499f93ee7b1f9bfb3251a123636877`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xfcf8eda095e37a41e002e266daad7efc1579bc0a` Transfer
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Sync
  - `0x3f61171b1297f6e512c750c172ba86026ab0e820` UniswapV2 Swap
  - `0x932a7b9941499f93ee7b1f9bfb3251a123636877` UniswapV3 Swap
- receipt status 1, index 3
