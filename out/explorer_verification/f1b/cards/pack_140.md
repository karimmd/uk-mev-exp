# pack_140

Block 13837126. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x1e277b4336c864dca87a25ce56f89abb97fa17d56718b12d97b1500c2bf31d0d`
- block 13837126, position 0, result success, from `0xf5d463e6050f59e47750cb2af4047cc536d36103`, to `0x00000000726422a6fecb4759b44d47e48cf746aa`, value 0.000000 ETH, gas used 81759 at 52.3 gwei, fee 0.004273 ETH
- token transfers (Blockscout, decoded):
  - 47.660716 WETH (`0xc02aaa39`): `0x00000000726422a6fecb4759b44d47e48cf746aa` -> `0x18a797c7c70c1bf22fdee1c09062aba709cacf04`
  - 6976.184938 RGT (`0xd291e7a0`): `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` -> `0x00000000726422a6fecb4759b44d47e48cf746aa`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd291e7a03283640fdc51b121ac401383a46cc623` Transfer
  - `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` UniswapV2 Sync
  - `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xedd2192ced20be8472c14be974bb8f21a93a1bfd3e1eff9b8f8b659348edb5ca`
- block 13837126, position 2, result success, from `0x98041ab523024dacaefa3bb70dd982dbac68e855`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 4.390115 ETH, gas used 112143 at 89.8 gwei, fee 0.010066 ETH
- token transfers (Blockscout, decoded):
  - 4.178880 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x0000000000000000000000000000000000000000`
  - 4.178880 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x18a797c7c70c1bf22fdee1c09062aba709cacf04`
  - 600.000000 RGT (`0xd291e7a0`): `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` -> `0xa494c8bf3a9cf0d8a15048095f78fc1126a98801`
- internal ETH transfers (Etherscan):
  - 4.178880 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.211235 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x98041ab523024dacaefa3bb70dd982dbac68e855` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 4.178880 ETH for `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd291e7a03283640fdc51b121ac401383a46cc623` Transfer
  - `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` UniswapV2 Sync
  - `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` UniswapV2 Swap
- receipt status 1, index 2

### Back leg: `0x3ab4d085452c896022ee8d5150325db4537377e19683fd52f0fe5bcb5769ea5e`
- block 13837126, position 3, result success, from `0xf5d463e6050f59e47750cb2af4047cc536d36103`, to `0x00000000726422a6fecb4759b44d47e48cf746aa`, value 0.000000 ETH, gas used 71224 at 143.9 gwei, fee 0.010251 ETH
- token transfers (Blockscout, decoded):
  - 6976.184938 RGT (`0xd291e7a0`): `0x00000000726422a6fecb4759b44d47e48cf746aa` -> `0x18a797c7c70c1bf22fdee1c09062aba709cacf04`
  - 47.683839 WETH (`0xc02aaa39`): `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` -> `0x00000000726422a6fecb4759b44d47e48cf746aa`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xd291e7a03283640fdc51b121ac401383a46cc623` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` UniswapV2 Sync
  - `0x18a797c7c70c1bf22fdee1c09062aba709cacf04` UniswapV2 Swap
- receipt status 1, index 3
