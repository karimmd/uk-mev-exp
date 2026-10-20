# pack_156

Block 12794150. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x9c1f2e3f263817f27c0a74d2f8e3b7b2204fd8f449e09d2ba29323aa5c51b0b5`
- block 12794150, position 0, result success, from `0x26ccc3a2052be5898d60683c7bb621047153bb19`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 78819 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.626025 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x95cfa1f48fad82232772d3b1415ad4393517f3b5`
  - 5617.071840 XRUNE (`0x69fa0fee`): `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xcb5210c3f074db7c6f100cb1c21c0c1c6a2c4c8e` -> `0x000000000035b5e5ad9019092c665357240f594e` [self-destruct]
  - 0.000000 ETH: `0x3c933de0cb8981b41813d884cccb7953ce6baae3` -> `0x000000000035b5e5ad9019092c665357240f594e` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c` other
  - `0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c` Transfer
  - `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` UniswapV2 Sync
  - `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x6fadd6bcb4deddce7910ebb6ef71f48199c4c2776bc75780a7fe9e555ce39851`
- block 12794150, position 1, result success, from `0x9f6c1e8242443c3900a22e6b9895264860ae7199`, to `0x11111112542d85b3ef69ae05771c2dccff4faa26`, value 0.000000 ETH, gas used 347389 at 70.0 gwei, fee 0.024317 ETH
- token transfers (Blockscout, decoded):
  - 15000.000000 USDT (`0xdac17f95`): `0x9f6c1e8242443c3900a22e6b9895264860ae7199` -> `0x5f5207df64b0f7ed56bf0b61733d3be8795f4e5a`
  - 15000.000000 USDT (`0xdac17f95`): `0x5f5207df64b0f7ed56bf0b61733d3be8795f4e5a` -> `0xb3c839dbde6b96d37c56ee4f9dad3390d49310aa`
  - 6.916810 WETH (`0xc02aaa39`): `0xb3c839dbde6b96d37c56ee4f9dad3390d49310aa` -> `0x95cfa1f48fad82232772d3b1415ad4393517f3b5`
  - 60224.673281 XRUNE (`0x69fa0fee`): `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` -> `0xfd3dfb524b2da40c8a6d703c62be36b5d8540626`
  - 60224.673281 XRUNE (`0x69fa0fee`): `0xfd3dfb524b2da40c8a6d703c62be36b5d8540626` -> `0x9f6c1e8242443c3900a22e6b9895264860ae7199`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x5f5207df64b0f7ed56bf0b61733d3be8795f4e5a` other
  - `0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c` other
  - `0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c` Transfer
  - `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` UniswapV2 Sync
  - `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` UniswapV2 Swap
  - `0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c` other
  - `0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c` Transfer
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
- receipt status 1, index 1

### Back leg: `0x8e79a06ea7bf262e4b9921b7e7481b956ae6a54e351a8ad19ef2256faf9e0469`
- block 12794150, position 2, result success, from `0x26ccc3a2052be5898d60683c7bb621047153bb19`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 78217 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 5617.071840 XRUNE (`0x69fa0fee`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x95cfa1f48fad82232772d3b1415ad4393517f3b5`
  - 0.657492 WETH (`0xc02aaa39`): `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xe3aeec9935684af8bcc37e931ddd7ae828163686` -> `0x000000000035b5e5ad9019092c665357240f594e` [self-destruct]
  - 0.000000 ETH: `0xfce1ca8c5e7d3615f0ac4088fba9f355aa49ae2b` -> `0x000000000035b5e5ad9019092c665357240f594e` [self-destruct]
  - 0.029893 ETH: `0x000000000035b5e5ad9019092c665357240f594e` -> `0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c` other
  - `0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` UniswapV2 Sync
  - `0x95cfa1f48fad82232772d3b1415ad4393517f3b5` UniswapV2 Swap
- receipt status 1, index 2
