# pack_088

Block 13028934. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x8e2e919a3568d3f11751dc48897c571504ca57d027e302b845f6707095a0f9ff`
- block 13028934, position 3, result success, from `0x5b5001c4f80f33ec93b891062ed2e1d0acc05bb6`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 159604 at 26.1 gwei, fee 0.004163 ETH
- token transfers (Blockscout, decoded):
  - 105427.643800 DAI (`0x6b175474`): `0x60594a405d53811d3bc4766596efd80fd545a270` -> `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c`
  - 33.461349 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x60594a405d53811d3bc4766596efd80fd545a270`
  - 373.776975 OHM (`0x38351818`): `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x60594a405d53811d3bc4766596efd80fd545a270` UniswapV3 Swap
  - `0x383518188c0c6d7730d91b2c03a03c837814a899` Transfer
  - `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` UniswapV2 Sync
  - `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0xd33682e27e9506f81f66ad0f6ebb85461b64b01353fb01d4e5990ab5aafaa49d`
- block 13028934, position 4, result success, from `0xf13f7bf69a5e57ea3367222c65dd3380096d3fbf`, to `0x11111112542d85b3ef69ae05771c2dccff4faa26`, value 0.000000 ETH, gas used 268036 at 31.0 gwei, fee 0.008309 ETH
- token transfers (Blockscout, decoded):
  - 120000.000000 USDT (`0xdac17f95`): `0xf13f7bf69a5e57ea3367222c65dd3380096d3fbf` -> `0xc176761d388caf2f56cf03329d82e1e7c48ae09c`
  - 119924.685206 DAI (`0x6b175474`): `0xa5d07e978398eb1715056d3ca5cb31035c02fdad` -> `0xc176761d388caf2f56cf03329d82e1e7c48ae09c`
  - 120000.000000 USDT (`0xdac17f95`): `0xc176761d388caf2f56cf03329d82e1e7c48ae09c` -> `0xa5d07e978398eb1715056d3ca5cb31035c02fdad`
  - 119924.685206 DAI (`0x6b175474`): `0xc176761d388caf2f56cf03329d82e1e7c48ae09c` -> `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c`
  - 420.645329 OHM (`0x38351818`): `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` -> `0xc176761d388caf2f56cf03329d82e1e7c48ae09c`
  - 420.645329 OHM (`0x38351818`): `0xc176761d388caf2f56cf03329d82e1e7c48ae09c` -> `0xf13f7bf69a5e57ea3367222c65dd3380096d3fbf`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Approval
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x3ef51736315f52d568d6d2cf289419b9cfffe782` other
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0x383518188c0c6d7730d91b2c03a03c837814a899` Transfer
  - `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` UniswapV2 Sync
  - `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` UniswapV2 Swap
  - `0x383518188c0c6d7730d91b2c03a03c837814a899` Transfer
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
- receipt status 1, index 4

### Back leg: `0x151c212f7f98b96d030aa15e2738b992ee712c1e557039205bd41350e48e1605`
- block 13028934, position 5, result success, from `0x5b5001c4f80f33ec93b891062ed2e1d0acc05bb6`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.075956 ETH, gas used 157616 at 26.1 gwei, fee 0.004111 ETH
- token transfers (Blockscout, decoded):
  - 373.776975 OHM (`0x38351818`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c`
  - 105994.495373 DAI (`0x6b175474`): `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 33.607418 WETH (`0xc02aaa39`): `0x60594a405d53811d3bc4766596efd80fd545a270` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 105994.495373 DAI (`0x6b175474`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x60594a405d53811d3bc4766596efd80fd545a270`
- internal ETH transfers (Etherscan):
  - 0.075956 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xb7e390864a90b7b923c9f9310c6f98aafe43f707` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x383518188c0c6d7730d91b2c03a03c837814a899` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` UniswapV2 Sync
  - `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0x60594a405d53811d3bc4766596efd80fd545a270` UniswapV3 Swap
- receipt status 1, index 5
