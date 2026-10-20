# pack_023

Block 13946950. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x4235ee9893e07743bc980962e01f81116e37d73be05e237367a50243aa6a8074`
- block 13946950, position 0, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 149883 at 363.7 gwei, fee 0.054509 ETH
- token transfers (Blockscout, decoded):
  - 47.541343 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x55d5c232d921b9eaa6b37b5845e439acd04b4dba`
  - 727787.222522 HEX (`0x2b591e99`): `0x55d5c232d921b9eaa6b37b5845e439acd04b4dba` -> `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824`
  - 167518.771209 USDC (`0xa0b86991`): `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2b591e99afe9f32eaa6214f7b7629768c40eeb39` Transfer
  - `0x55d5c232d921b9eaa6b37b5845e439acd04b4dba` UniswapV2 Sync
  - `0x55d5c232d921b9eaa6b37b5845e439acd04b4dba` UniswapV2 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` UniswapV2 Sync
  - `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x843f6b6ac82f31fa03ec1d6d0f6ca55be15689e52a5ac6e3a1ba801198de83d3`
- block 13946950, position 1, result success, from `0x0c3b93a275d4f7c7724d2e2ca4e226a8abf3cb56`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 125166 at 532.1 gwei, fee 0.066604 ETH
- token transfers (Blockscout, decoded):
  - 500000.000000 HEX (`0x2b591e99`): `0x0c3b93a275d4f7c7724d2e2ca4e226a8abf3cb56` -> `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824`
  - 112253.073812 USDC (`0xa0b86991`): `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` -> `0x0c3b93a275d4f7c7724d2e2ca4e226a8abf3cb56`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x2b591e99afe9f32eaa6214f7b7629768c40eeb39` Transfer
  - `0x2b591e99afe9f32eaa6214f7b7629768c40eeb39` Approval
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` UniswapV2 Sync
  - `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x15a95f4cf2bab33d68cc1638a5a5ee786019a4049d6cf91b5a6584fcba3af3cc`
- block 13946950, position 2, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 131951 at 2291.7 gwei, fee 0.302393 ETH
- token transfers (Blockscout, decoded):
  - 167518.771209 USDC (`0xa0b86991`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824`
  - 738112.259288 HEX (`0x2b591e99`): `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` -> `0x55d5c232d921b9eaa6b37b5845e439acd04b4dba`
  - 47.906928 WETH (`0xc02aaa39`): `0x55d5c232d921b9eaa6b37b5845e439acd04b4dba` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x2b591e99afe9f32eaa6214f7b7629768c40eeb39` Transfer
  - `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` UniswapV2 Sync
  - `0xf6dcdce0ac3001b2f67f750bc64ea5beb37b5824` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x55d5c232d921b9eaa6b37b5845e439acd04b4dba` UniswapV2 Sync
  - `0x55d5c232d921b9eaa6b37b5845e439acd04b4dba` UniswapV2 Swap
- receipt status 1, index 2
