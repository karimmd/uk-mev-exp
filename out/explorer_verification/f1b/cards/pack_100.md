# pack_100

Block 12979214. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xa6f42b5ebb486aaca4d2c9f3381486b27ad60e9d34477cd3500e7bf8ef0fc4cc`
- block 12979214, position 0, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 166228 at 55.9 gwei, fee 0.009294 ETH
- token transfers (Blockscout, decoded):
  - 15496.180535 USDT (`0xdac17f95`): `0x11b815efb8f581194ae79006d24e0d814b7697f6` -> `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28`
  - 5.019531 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x11b815efb8f581194ae79006d24e0d814b7697f6`
  - 70338.629241 HORD (`0x43a96962`): `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x11b815efb8f581194ae79006d24e0d814b7697f6` UniswapV3 Swap
  - `0x43a96962254855f16b925556f9e97be436a43448` Transfer
  - `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` UniswapV2 Sync
  - `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x4b8f962b7591c94804abf6147e1a162b18b3520de2ae93b6d1917a3a346912b8`
- block 12979214, position 1, result success, from `0x3c6cdbc3b3bcb026d55fd2d4368741aa05a4381a`, to `0x881d40237659c251811cec9c364ef91dc08d300c`, value 0.000000 ETH, gas used 164971 at 63.0 gwei, fee 0.010393 ETH
- token transfers (Blockscout, decoded):
  - 8404.080072 USDT (`0xdac17f95`): `0x3c6cdbc3b3bcb026d55fd2d4368741aa05a4381a` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 8330.544372 USDT (`0xdac17f95`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28`
  - 36937.906440 HORD (`0x43a96962`): `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 73.535700 USDT (`0xdac17f95`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11ededebf63bef0ea2d2d071bdf88f71543ec6fb`
  - 36937.906440 HORD (`0x43a96962`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x3c6cdbc3b3bcb026d55fd2d4368741aa05a4381a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x43a96962254855f16b925556f9e97be436a43448` Transfer
  - `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` UniswapV2 Sync
  - `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` UniswapV2 Swap
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x43a96962254855f16b925556f9e97be436a43448` Transfer
  - `0x881d40237659c251811cec9c364ef91dc08d300c` other
- receipt status 1, index 1

### Back leg: `0xe67a01f6d1a00f87bdd5918c83da65ab93db8458f5756cdda3b88cfe6ac6c37f`
- block 12979214, position 2, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.024128 ETH, gas used 167598 at 55.9 gwei, fee 0.009370 ETH
- token transfers (Blockscout, decoded):
  - 70338.629241 HORD (`0x43a96962`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28`
  - 15655.087951 USDT (`0xdac17f95`): `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 5.065932 WETH (`0xc02aaa39`): `0x11b815efb8f581194ae79006d24e0d814b7697f6` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 15655.087951 USDT (`0xdac17f95`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x11b815efb8f581194ae79006d24e0d814b7697f6`
- internal ETH transfers (Etherscan):
  - 0.024128 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x3ecef08d0e2dad803847e052249bb4f8bff2d5bb` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x43a96962254855f16b925556f9e97be436a43448` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` UniswapV2 Sync
  - `0xde6faedbcae38eec6d33ad61473a04a6dd7f6e28` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x11b815efb8f581194ae79006d24e0d814b7697f6` UniswapV3 Swap
- receipt status 1, index 2
