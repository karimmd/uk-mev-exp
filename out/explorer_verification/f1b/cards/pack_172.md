# pack_172

Block 12393574. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x0a318e5365c18c362dbde28a1be7ef1b88032e42d38d077ece5d5c4072367f16`
- block 12393574, position 0, result success, from `0x30b8235f492265a734347c0bf36e2ffcad887be2`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 90976 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 5.560000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a`
  - 1401697.565164 CHOW (`0x925f2c11`): `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xaa611abd021beea10f416813a2284f048db77703` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x5f37a1079113a7fc7efa0b603a549d54fa62765b` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x925f2c11b99c1a4c46606898ee91ed3d450cfeda` Transfer
  - `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` UniswapV2 Sync
  - `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xd2956bc84b93461600c6a69f4c7ebd72554348a4b6a000304811e131c414ca10`
- block 12393574, position 1, result success, from `0xb943e534ccb68a976bfa9007ad6705c76da81ec6`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 199383 at 77.0 gwei, fee 0.015352 ETH
- token transfers (Blockscout, decoded):
  - 1000000000.000000 SHIB (`0x95ad61b0`): `0xb943e534ccb68a976bfa9007ad6705c76da81ec6` -> `0x811beed0119b4afce20d2583eb608c6f7af1954f`
  - 2.353404 WETH (`0xc02aaa39`): `0x811beed0119b4afce20d2583eb608c6f7af1954f` -> `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a`
  - 520893.325267 CHOW (`0x925f2c11`): `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` -> `0xb943e534ccb68a976bfa9007ad6705c76da81ec6`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Transfer
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x811beed0119b4afce20d2583eb608c6f7af1954f` UniswapV2 Sync
  - `0x811beed0119b4afce20d2583eb608c6f7af1954f` UniswapV2 Swap
  - `0x925f2c11b99c1a4c46606898ee91ed3d450cfeda` Transfer
  - `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` UniswapV2 Sync
  - `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xa79ab50286955d7b2c25764b68b3293bf5f1e86685125a47703f3772154dd129`
- block 12393574, position 2, result success, from `0x30b8235f492265a734347c0bf36e2ffcad887be2`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.068540 ETH, gas used 105441 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 1360455.491444 CHOW (`0x925f2c11`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a`
  - 5.639697 WETH (`0xc02aaa39`): `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.068540 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x1ad91ee08f21be3de0ba2ba6918e714da6b45836` [call]
  - 0.000000 ETH: `0x293382553dbdc72ba36d18e4fd2ee744015bb943` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x09fd435389df56c8d4958c8b2a1b72d7fa405c84` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x925f2c11b99c1a4c46606898ee91ed3d450cfeda` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` UniswapV2 Sync
  - `0xd234e8493d6690d6a7820d3f6e4f1f13579efe3a` UniswapV2 Swap
- receipt status 1, index 2
