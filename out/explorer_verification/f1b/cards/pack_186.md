# pack_186

Block 12117518. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xdf374c25a2dab3f7e69be3ff4afc9b3a8e940d438e53b06451d468c27cdd3d82`
- block 12117518, position 184, result success, from `0x978770f230afa5b25250649ce9cb76e26a08ccec`, to `0x00000000c9fdd743c60055c0e4ea30d266272c1f`, value 0.000000 ETH, gas used 86894 at 134.0 gwei, fee 0.011644 ETH
- token transfers (Blockscout, decoded):
  - 2.239345 WETH (`0xc02aaa39`): `0x00000000c9fdd743c60055c0e4ea30d266272c1f` -> `0xaa736ca527252cf9f65abed23c21f5ac46af27e3`
  - 19848.649072 $GOLD (`0xf1b8762a`): `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` -> `0x00000000c9fdd743c60055c0e4ea30d266272c1f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf1b8762a7fa8c244e36f7234edf40cfae24394e3` Transfer
  - `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` UniswapV2 Sync
  - `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` UniswapV2 Swap
- receipt status 1, index 184

### Victim leg: `0xe817e6a96f812b2045ab460d4367d1f44412f0527602b2532e37f4a78841ffcd`
- block 12117518, position 185, result success, from `0x44424c777a8710cd583188d4d3126b7b03320d0f`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 1.242795 ETH, gas used 114776 at 134.0 gwei, fee 0.015380 ETH
- token transfers (Blockscout, decoded):
  - 1.242795 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 1.242795 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xaa736ca527252cf9f65abed23c21f5ac46af27e3`
  - 8927.505636 $GOLD (`0xf1b8762a`): `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` -> `0x44424c777a8710cd583188d4d3126b7b03320d0f`
- internal ETH transfers (Etherscan):
  - 1.242795 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.242795 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf1b8762a7fa8c244e36f7234edf40cfae24394e3` Transfer
  - `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` UniswapV2 Sync
  - `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` UniswapV2 Swap
- receipt status 1, index 185

### Back leg: `0x616358dff10667b7ec3d1b90781657e8e65d4bfff1c1c1fe269ef0c1d1d923ae`
- block 12117518, position 186, result success, from `0x978770f230afa5b25250649ce9cb76e26a08ccec`, to `0x00000000c9fdd743c60055c0e4ea30d266272c1f`, value 0.000000 ETH, gas used 82841 at 134.0 gwei, fee 0.011101 ETH
- token transfers (Blockscout, decoded):
  - 36674.453999 $GOLD (`0xf1b8762a`): `0x00000000c9fdd743c60055c0e4ea30d266272c1f` -> `0xaa736ca527252cf9f65abed23c21f5ac46af27e3`
  - 4.198289 WETH (`0xc02aaa39`): `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` -> `0x00000000c9fdd743c60055c0e4ea30d266272c1f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xf1b8762a7fa8c244e36f7234edf40cfae24394e3` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` UniswapV2 Sync
  - `0xaa736ca527252cf9f65abed23c21f5ac46af27e3` UniswapV2 Swap
- receipt status 1, index 186
