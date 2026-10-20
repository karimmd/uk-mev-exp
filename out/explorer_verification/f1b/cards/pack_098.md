# pack_098

Block 12822134. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x1e6b41b645ba3c800564be9f5b45cb4e5d46a1ad1f1817c2eb46135f62cf9515`
- block 12822134, position 3, result success, from `0xb7ab1de5b259a880c4bb5451bdbe6f80f3798538`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 61444 at 1108.9 gwei, fee 0.068133 ETH
- token transfers (Blockscout, decoded):
  - 69.817709 MM (`0x6b4c7a5e`): `0x9ac681f68a589cc3763bad9ce43be3380696b136` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 7.796880 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x9ac681f68a589cc3763bad9ce43be3380696b136`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x55576a668e465d6154464dce634643b2b5dfad99` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x6a4fac5aa2f54ef38f3e75edba428183e5a5ac48` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xa51e4c1299ec8b233d1bc726c49f3df2e499b2a6` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x6b4c7a5e3f0b99fcd83e9c089bddd6c7fce5c611` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9ac681f68a589cc3763bad9ce43be3380696b136` UniswapV3 Swap
- receipt status 1, index 3

### Victim leg: `0x0bae29f1ed7201bd09e35c157e4919b76177b928716a3139f0ab9d6b01f96159`
- block 12822134, position 4, result success, from `0x7a976faaf9c404c680593b20123039847f083d0e`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 2.891229 ETH, gas used 122504 at 38.0 gwei, fee 0.004655 ETH
- token transfers (Blockscout, decoded):
  - 25.100000 MM (`0x6b4c7a5e`): `0x9ac681f68a589cc3763bad9ce43be3380696b136` -> `0x7a976faaf9c404c680593b20123039847f083d0e`
  - 2.891105 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xe592427a0aece92de3edee1f18e0157c05861564`
  - 2.891105 WETH (`0xc02aaa39`): `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0x9ac681f68a589cc3763bad9ce43be3380696b136`
- internal ETH transfers (Etherscan):
  - 2.891105 ETH: `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000124 ETH: `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0x7a976faaf9c404c680593b20123039847f083d0e` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x6b4c7a5e3f0b99fcd83e9c089bddd6c7fce5c611` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 2.891105 ETH for `0xe592427a0aece92de3edee1f18e0157c05861564`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9ac681f68a589cc3763bad9ce43be3380696b136` UniswapV3 Swap
- receipt status 1, index 4

### Back leg: `0x5a816972c82176a23293f1f25c6661d9162c8870b7bff30696ea3d544ca30e26`
- block 12822134, position 5, result success, from `0xb7ab1de5b259a880c4bb5451bdbe6f80f3798538`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 60435 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 7.878552 WETH (`0xc02aaa39`): `0x9ac681f68a589cc3763bad9ce43be3380696b136` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 69.817709 MM (`0x6b4c7a5e`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x9ac681f68a589cc3763bad9ce43be3380696b136`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x9f9a30d20622640acf3a50e1dff9de969645f481` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x153538913a70fcacab2a885cb47256d5cc5051ca` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xf53bb0b06fa1d4f2121664e132403784dae6268e` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b4c7a5e3f0b99fcd83e9c089bddd6c7fce5c611` Transfer
  - `0x9ac681f68a589cc3763bad9ce43be3380696b136` UniswapV3 Swap
- receipt status 1, index 5
