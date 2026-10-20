# pack_022

Block 13231598. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x3dffead8e755e4d8001ee7e4bf32d308c4aa19e2ff8dcf0041737f1737b1027a`
- block 13231598, position 1, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 153511 at 103.1 gwei, fee 0.015823 ETH
- token transfers (Blockscout, decoded):
  - 1.905144 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x9553c7f43c0ffe1f20bdf5cb3ad23484850983a9`
  - 911697.646625 TIDAL (`0x29cbd051`): `0x9553c7f43c0ffe1f20bdf5cb3ad23484850983a9` -> `0xb43542e6b7c209f7da4b579792f67a1844546ce8`
  - 4266.374147 USDC (`0xa0b86991`): `0xb43542e6b7c209f7da4b579792f67a1844546ce8` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x29cbd0510eec0327992cd6006e63f9fa8e7f33b7` Transfer
  - `0x9553c7f43c0ffe1f20bdf5cb3ad23484850983a9` UniswapV2 Sync
  - `0x9553c7f43c0ffe1f20bdf5cb3ad23484850983a9` UniswapV2 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xb43542e6b7c209f7da4b579792f67a1844546ce8` UniswapV2 Sync
  - `0xb43542e6b7c209f7da4b579792f67a1844546ce8` UniswapV2 Swap
- receipt status 1, index 1

### Victim leg: `0x55006b661c87652a9598a58acec6f0414bb9ddde02c53600186bc054099b290f`
- block 13231598, position 2, result success, from `0x1e29e2cefd3395d892678add3eb791ed74114f3b`, to `0x11111112542d85b3ef69ae05771c2dccff4faa26`, value 0.000000 ETH, gas used 230205 at 103.4 gwei, fee 0.023803 ETH
- token transfers (Blockscout, decoded):
  - 634000.000000 TIDAL (`0x29cbd051`): `0x1e29e2cefd3395d892678add3eb791ed74114f3b` -> `0xb43542e6b7c209f7da4b579792f67a1844546ce8`
  - 2760.627540 USDC (`0xa0b86991`): `0xb43542e6b7c209f7da4b579792f67a1844546ce8` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 2760.627540 USDC (`0xa0b86991`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xfc7b1dad07111c77c5d619043d75ac9a19680760`
- internal ETH transfers (Etherscan):
  - 0.781873 ETH: `0xfc7b1dad07111c77c5d619043d75ac9a19680760` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` [call]
  - 0.781873 ETH: `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x1e29e2cefd3395d892678add3eb791ed74114f3b` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x29cbd0510eec0327992cd6006e63f9fa8e7f33b7` Transfer
  - `0x29cbd0510eec0327992cd6006e63f9fa8e7f33b7` Approval
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xb43542e6b7c209f7da4b579792f67a1844546ce8` UniswapV2 Sync
  - `0xb43542e6b7c209f7da4b579792f67a1844546ce8` UniswapV2 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Approval
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xfc7b1dad07111c77c5d619043d75ac9a19680760` other
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
- receipt status 1, index 2

### Back leg: `0xaa70773ba61cbb74f20dbaebe19912c4ae22abd5ae4fa7c0fc5f82cb4564f5ea`
- block 13231598, position 3, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 142154 at 103.1 gwei, fee 0.014652 ETH
- token transfers (Blockscout, decoded):
  - 4266.374147 USDC (`0xa0b86991`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0xb43542e6b7c209f7da4b579792f67a1844546ce8`
  - 959255.164638 TIDAL (`0x29cbd051`): `0xb43542e6b7c209f7da4b579792f67a1844546ce8` -> `0x9553c7f43c0ffe1f20bdf5cb3ad23484850983a9`
  - 1.958710 WETH (`0xc02aaa39`): `0x9553c7f43c0ffe1f20bdf5cb3ad23484850983a9` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - 0.018479 ETH: `0x000000000035b5e5ad9019092c665357240f594e` -> `0x8595dd9e0438640b5e1254f9df579ac12a86865f` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x29cbd0510eec0327992cd6006e63f9fa8e7f33b7` Transfer
  - `0xb43542e6b7c209f7da4b579792f67a1844546ce8` UniswapV2 Sync
  - `0xb43542e6b7c209f7da4b579792f67a1844546ce8` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9553c7f43c0ffe1f20bdf5cb3ad23484850983a9` UniswapV2 Sync
  - `0x9553c7f43c0ffe1f20bdf5cb3ad23484850983a9` UniswapV2 Swap
- receipt status 1, index 3
