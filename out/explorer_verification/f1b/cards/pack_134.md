# pack_134

Block 14302294. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xcfbd97f7eaadb1893a3cd1506130d539034a7a73ed250369141812ed0cf94acc`
- block 14302294, position 1, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 81288 at 43.1 gwei, fee 0.003501 ETH
- token transfers (Blockscout, decoded):
  - 1.013765 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0xc9919a9eb691f571e41db417f911135b4ac46fe7`
  - 5723.438406 LSS (`0x3b9be07d`): `0xc9919a9eb691f571e41db417f911135b4ac46fe7` -> `0x62e3c242b5e903071458ad90a160493d84911c77`
  - 2457.341661 USDT (`0xdac17f95`): `0x62e3c242b5e903071458ad90a160493d84911c77` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x3b9be07d622accaed78f479bc0edabfd6397e320` Transfer
  - `0xc9919a9eb691f571e41db417f911135b4ac46fe7` UniswapV2 Sync
  - `0xc9919a9eb691f571e41db417f911135b4ac46fe7` UniswapV2 Swap
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x62e3c242b5e903071458ad90a160493d84911c77` UniswapV2 Sync
  - `0x62e3c242b5e903071458ad90a160493d84911c77` UniswapV2 Swap
- receipt status 1, index 1

### Victim leg: `0x2cd39e9f0edf50c1d5cbccaad9b72c7cc6454c7980e51d077a4789c5fbfc9a2f`
- block 14302294, position 2, result success, from `0xd266d61ac22c2a2ac2dd832e79c14ea152c998d6`, to `0x1111111254fb6c44bac0bed2854e76f90643097d`, value 0.000000 ETH, gas used 99400 at 59.8 gwei, fee 0.005949 ETH
- token transfers (Blockscout, decoded):
  - 50000.000000 LSS (`0x3b9be07d`): `0xd266d61ac22c2a2ac2dd832e79c14ea152c998d6` -> `0x62e3c242b5e903071458ad90a160493d84911c77`
  - 20444.452862 USDT (`0xdac17f95`): `0x62e3c242b5e903071458ad90a160493d84911c77` -> `0xd266d61ac22c2a2ac2dd832e79c14ea152c998d6`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x3b9be07d622accaed78f479bc0edabfd6397e320` Transfer
  - `0x3b9be07d622accaed78f479bc0edabfd6397e320` Approval
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x62e3c242b5e903071458ad90a160493d84911c77` UniswapV2 Sync
  - `0x62e3c242b5e903071458ad90a160493d84911c77` UniswapV2 Swap
- receipt status 1, index 2

### Back leg: `0xb5ab860ffa79486ae3180de693a59655996bb9219113aae5d1c8270f0d37cb7c`
- block 14302294, position 3, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 132083 at 373.3 gwei, fee 0.049313 ETH
- token transfers (Blockscout, decoded):
  - 2457.341661 USDT (`0xdac17f95`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x62e3c242b5e903071458ad90a160493d84911c77`
  - 6208.112451 LSS (`0x3b9be07d`): `0x62e3c242b5e903071458ad90a160493d84911c77` -> `0xc9919a9eb691f571e41db417f911135b4ac46fe7`
  - 1.078212 WETH (`0xc02aaa39`): `0xc9919a9eb691f571e41db417f911135b4ac46fe7` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x3b9be07d622accaed78f479bc0edabfd6397e320` Transfer
  - `0x62e3c242b5e903071458ad90a160493d84911c77` UniswapV2 Sync
  - `0x62e3c242b5e903071458ad90a160493d84911c77` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc9919a9eb691f571e41db417f911135b4ac46fe7` UniswapV2 Sync
  - `0xc9919a9eb691f571e41db417f911135b4ac46fe7` UniswapV2 Swap
- receipt status 1, index 3
