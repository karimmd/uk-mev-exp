# pack_083

Block 12259990. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x967179d8618b8a59a5cffe0efaca0cd118cc31dcf47eb78775d980d573bb30af`
- block 12259990, position 0, result success, from `0xb38a9f021a3bf6bebcb7b7c4f4df3064b9143098`, to `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16`, value 0.000000 ETH, gas used 162279 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 7.659549 WETH (`0xc02aaa39`): `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16` -> `0xceff51756c56ceffca006cd410b03ffc46dd3a58`
  - 0.299478 WBTC (`0x2260fac5`): `0xceff51756c56ceffca006cd410b03ffc46dd3a58` -> `0x1f3d61248ec81542889535595903078109707941`
  - 0.313561 KBTC (`0xe6c35029`): `0x1f3d61248ec81542889535595903078109707941` -> `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xceff51756c56ceffca006cd410b03ffc46dd3a58` UniswapV2 Sync
  - `0xceff51756c56ceffca006cd410b03ffc46dd3a58` UniswapV2 Swap
  - `0xe6c3502997f97f9bde34cb165fbce191065e068f` Transfer
  - `0x1f3d61248ec81542889535595903078109707941` UniswapV2 Sync
  - `0x1f3d61248ec81542889535595903078109707941` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x615a2292d0624c52530b1f56b99fa428834db30df01c82eaee2e7ecc5628bff1`
- block 12259990, position 1, result success, from `0xaf293854c232c3de882d6d15217a83c2ae83d46b`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 96489 at 102.0 gwei, fee 0.009842 ETH
- token transfers (Blockscout, decoded):
  - 2.031973 WBTC (`0x2260fac5`): `0xaf293854c232c3de882d6d15217a83c2ae83d46b` -> `0x1f3d61248ec81542889535595903078109707941`
  - 2.086668 KBTC (`0xe6c35029`): `0x1f3d61248ec81542889535595903078109707941` -> `0xaf293854c232c3de882d6d15217a83c2ae83d46b`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xe6c3502997f97f9bde34cb165fbce191065e068f` Transfer
  - `0x1f3d61248ec81542889535595903078109707941` UniswapV2 Sync
  - `0x1f3d61248ec81542889535595903078109707941` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xc1133fe23d8a17bb677b66af6dcee78364a22158f23bda68341524cd815255d1`
- block 12259990, position 2, result success, from `0xb38a9f021a3bf6bebcb7b7c4f4df3064b9143098`, to `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16`, value 0.000000 ETH, gas used 118716 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.313561 KBTC (`0xe6c35029`): `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16` -> `0x1f3d61248ec81542889535595903078109707941`
  - 0.307908 WBTC (`0x2260fac5`): `0x1f3d61248ec81542889535595903078109707941` -> `0xceff51756c56ceffca006cd410b03ffc46dd3a58`
  - 7.827973 WETH (`0xc02aaa39`): `0xceff51756c56ceffca006cd410b03ffc46dd3a58` -> `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16`
- internal ETH transfers (Etherscan):
  - 0.083513 ETH: `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16` -> `0x99c85bb64564d9ef9a99621301f22c9993cb89e3` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xe6c3502997f97f9bde34cb165fbce191065e068f` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x1f3d61248ec81542889535595903078109707941` UniswapV2 Sync
  - `0x1f3d61248ec81542889535595903078109707941` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xceff51756c56ceffca006cd410b03ffc46dd3a58` UniswapV2 Sync
  - `0xceff51756c56ceffca006cd410b03ffc46dd3a58` UniswapV2 Swap
- receipt status 1, index 2
