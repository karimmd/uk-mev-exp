# pack_034

Block 13492518. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x1a60bdb7a02f58f51660a46eb7952ec9b32e6f6ce514d9911ecf72a0975852f9`
- block 13492518, position 6, result success, from `0x38563699560e4512c7574c8cc5cf89fd43923bca`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 69012 at 69.0 gwei, fee 0.004763 ETH
- token transfers (Blockscout, decoded):
  - 5.966286 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x23a9292830fc80db7f563edb28d2fe6fb47f8624`
  - 38.437980 SFI (`0xb753428a`): `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb753428af26e81097e7fd17f40c88aaa3e04902c` Transfer
  - `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` UniswapV2 Sync
  - `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` UniswapV2 Swap
- receipt status 1, index 6

### Victim leg: `0x911161c049fcb53a775c4cdd7965959beee1f9b2045be1e2e8bb09647769a61c`
- block 13492518, position 7, result success, from `0x302b5a9d4610aa31ec5879e7885e436b58dc1354`, to `0x11111112542d85b3ef69ae05771c2dccff4faa26`, value 7.455010 ETH, gas used 215834 at 80.0 gwei, fee 0.017272 ETH
- token transfers (Blockscout, decoded):
  - 7.455010 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x0000000000000000000000000000000000000000`
  - 3.131104 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x23a9292830fc80db7f563edb28d2fe6fb47f8624`
  - 19.450837 SFI (`0xb753428a`): `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 4.323906 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xc76225124f3caab07f609b1d147a31de43926cd6`
  - 28.163233 SFI (`0xb753428a`): `0xc76225124f3caab07f609b1d147a31de43926cd6` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 47.614070 SFI (`0xb753428a`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x302b5a9d4610aa31ec5879e7885e436b58dc1354`
- internal ETH transfers (Etherscan):
  - 7.455010 ETH: `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` [call]
  - 7.455010 ETH: `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 7.455010 ETH for `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb753428af26e81097e7fd17f40c88aaa3e04902c` Transfer
  - `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` UniswapV2 Sync
  - `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb753428af26e81097e7fd17f40c88aaa3e04902c` Transfer
  - `0xc76225124f3caab07f609b1d147a31de43926cd6` UniswapV2 Sync
  - `0xc76225124f3caab07f609b1d147a31de43926cd6` UniswapV2 Swap
  - `0xb753428af26e81097e7fd17f40c88aaa3e04902c` Transfer
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
- receipt status 1, index 7

### Back leg: `0x868b20dbc14f85d70784e905109d70f5be6b35d959f08fc08f6822713eda5a62`
- block 13492518, position 8, result success, from `0x38563699560e4512c7574c8cc5cf89fd43923bca`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 58509 at 1347.6 gwei, fee 0.078847 ETH
- token transfers (Blockscout, decoded):
  - 38.437980 SFI (`0xb753428a`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x23a9292830fc80db7f563edb28d2fe6fb47f8624`
  - 6.078279 WETH (`0xc02aaa39`): `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xb753428af26e81097e7fd17f40c88aaa3e04902c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` UniswapV2 Sync
  - `0x23a9292830fc80db7f563edb28d2fe6fb47f8624` UniswapV2 Swap
- receipt status 1, index 8
