# pack_008

Block 11063982. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x8b58e13dd082199729af0903e6a2a8b6a898e449e595b14edce02d210d4de2f2`
- block 11063982, position 0, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x8be4db5926232bc5b02b841dbede8161924495c4`, value 0.000000 ETH, gas used 67654 at 2312.4 gwei, fee 0.156445 ETH
- token transfers (Blockscout, decoded):
  - 25.820000 WETH (`0xc02aaa39`): `0x8be4db5926232bc5b02b841dbede8161924495c4` -> `0x414fbf662fc98415dbee27c72013a6f3a937ed66`
  - 12644.731114 OWL (`0x2a7f709e`): `0x414fbf662fc98415dbee27c72013a6f3a937ed66` -> `0x8be4db5926232bc5b02b841dbede8161924495c4`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x168c5eb53dcd76a3d151f57d7128cf93b2872156` -> `0x8be4db5926232bc5b02b841dbede8161924495c4` [self-destruct]
  - 0.000000 ETH: `0x078c81e9de966bc8bc9cc0f63c9a5fa29b383b91` -> `0x8be4db5926232bc5b02b841dbede8161924495c4` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2a7f709ee001069771ceb6d42e85035f7d18e736` Transfer
  - `0x414fbf662fc98415dbee27c72013a6f3a937ed66` UniswapV2 Sync
  - `0x414fbf662fc98415dbee27c72013a6f3a937ed66` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x93a24a0efa8be0c66591fb2c69cbe92a16b05376ba104b36f59d7a82450c316f`
- block 11063982, position 22, result success, from `0xe600b236312b9d7ce12567322ee79cddb31dc0e2`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 17.000000 ETH, gas used 98447 at 93.1 gwei, fee 0.009165 ETH
- token transfers (Blockscout, decoded):
  - 17.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 17.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x414fbf662fc98415dbee27c72013a6f3a937ed66`
  - 8123.708721 OWL (`0x2a7f709e`): `0x414fbf662fc98415dbee27c72013a6f3a937ed66` -> `0xe600b236312b9d7ce12567322ee79cddb31dc0e2`
- internal ETH transfers (Etherscan):
  - 17.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 17.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2a7f709ee001069771ceb6d42e85035f7d18e736` Transfer
  - `0x414fbf662fc98415dbee27c72013a6f3a937ed66` UniswapV2 Sync
  - `0x414fbf662fc98415dbee27c72013a6f3a937ed66` UniswapV2 Swap
- receipt status 1, index 22

### Back leg: `0xfc9715f8d0b395ce5dc1109b8a6fcc0f8d0075d8fd6de3530ee88462b65b2001`
- block 11063982, position 23, result success, from `0x74b892425a206eb23905a5f5c322e4386460312d`, to `0x8be4db5926232bc5b02b841dbede8161924495c4`, value 0.000000 ETH, gas used 88543 at 93.1 gwei, fee 0.008243 ETH
- token transfers (Blockscout, decoded):
  - 12644.731114 OWL (`0x2a7f709e`): `0x8be4db5926232bc5b02b841dbede8161924495c4` -> `0x414fbf662fc98415dbee27c72013a6f3a937ed66`
  - 26.164520 WETH (`0xc02aaa39`): `0x414fbf662fc98415dbee27c72013a6f3a937ed66` -> `0x8be4db5926232bc5b02b841dbede8161924495c4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x2a7f709ee001069771ceb6d42e85035f7d18e736` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x414fbf662fc98415dbee27c72013a6f3a937ed66` UniswapV2 Sync
  - `0x414fbf662fc98415dbee27c72013a6f3a937ed66` UniswapV2 Swap
- receipt status 1, index 23
