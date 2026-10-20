# pack_025

Block 13645462. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x257bfffc682cdd95d962daef1d9b898eaa9cf125f35304fb48162706deaf57d1`
- block 13645462, position 0, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 248893 at 159.7 gwei, fee 0.039752 ETH
- token transfers (Blockscout, decoded):
  - 5165767.805948 XMT (`0x3e5d9d8a`): `0xb143bbeb287dcd1034da6e7186ec695316fff78f` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 1386981.861770 USDT (`0xdac17f95`): `0x11b815efb8f581194ae79006d24e0d814b7697f6` -> `0xb143bbeb287dcd1034da6e7186ec695316fff78f`
  - 338.123524 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x11b815efb8f581194ae79006d24e0d814b7697f6`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x3e5d9d8a63cc8a88748f229999cf59487e90721e` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x11b815efb8f581194ae79006d24e0d814b7697f6` UniswapV3 Swap
  - `0xb143bbeb287dcd1034da6e7186ec695316fff78f` UniswapV3 Swap
- receipt status 1, index 0

### Victim leg: `0x85fe7eb718681b6909b64dfbad36e47d7d64b758a293da38d370a2daf42664b9`
- block 13645462, position 1, result success, from `0x25b9dd9115f8ba5920b3894fb7e64a51aadfb768`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 0.000000 ETH, gas used 133502 at 154.2 gwei, fee 0.020582 ETH
- token transfers (Blockscout, decoded):
  - 378375.906848 XMT (`0x3e5d9d8a`): `0xb143bbeb287dcd1034da6e7186ec695316fff78f` -> `0x25b9dd9115f8ba5920b3894fb7e64a51aadfb768`
  - 124645.705816 USDT (`0xdac17f95`): `0x25b9dd9115f8ba5920b3894fb7e64a51aadfb768` -> `0xb143bbeb287dcd1034da6e7186ec695316fff78f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x3e5d9d8a63cc8a88748f229999cf59487e90721e` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xb143bbeb287dcd1034da6e7186ec695316fff78f` UniswapV3 Swap
- receipt status 1, index 1

### Back leg: `0xe2a568709d46d3f3f7cb0f71a119c7034ff2aa07da5653533dc1b881445bdcf0`
- block 13645462, position 2, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 238646 at 10578.3 gwei, fee 2.524465 ETH
- token transfers (Blockscout, decoded):
  - 341.047361 WETH (`0xc02aaa39`): `0x11b815efb8f581194ae79006d24e0d814b7697f6` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 1400525.821476 USDT (`0xdac17f95`): `0xb143bbeb287dcd1034da6e7186ec695316fff78f` -> `0x11b815efb8f581194ae79006d24e0d814b7697f6`
  - 5165767.783035 XMT (`0x3e5d9d8a`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xb143bbeb287dcd1034da6e7186ec695316fff78f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x3e5d9d8a63cc8a88748f229999cf59487e90721e` Transfer
  - `0xb143bbeb287dcd1034da6e7186ec695316fff78f` UniswapV3 Swap
  - `0x11b815efb8f581194ae79006d24e0d814b7697f6` UniswapV3 Swap
- receipt status 1, index 2
