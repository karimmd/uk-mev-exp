# pack_189

Block 11163246. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x4e71420bf8f806644ebe2fc7ef794c9b40bd828d46b7db4769fd09528819a226`
- block 11163246, position 11, result success, from `0x9b568d160ebc9a73d32e88d1d2a9ee0570ad5c9e`, to `0xf27b6320e9fa107c9ae72f1c82fa57000fbc0792`, value 0.000000 ETH, gas used 113768 at 55.0 gwei, fee 0.006257 ETH
- token transfers (Blockscout, decoded):
  - 0.507410 WETH (`0xc02aaa39`): `0xf27b6320e9fa107c9ae72f1c82fa57000fbc0792` -> `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca`
  - 0.213904 SAIYAN (`0x2b83fc17`): `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` -> `0x0000000000000000000000000000000000000000`
  - 5.133686 SAIYAN (`0x2b83fc17`): `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` -> `0xf27b6320e9fa107c9ae72f1c82fa57000fbc0792`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2b83fc177e887e4109f69c7a6f9a056797b0028e` Transfer
  - `0x2b83fc177e887e4109f69c7a6f9a056797b0028e` Transfer
  - `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` UniswapV2 Sync
  - `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` UniswapV2 Swap
- receipt status 1, index 11

### Victim leg: `0x7b83609a1c8b0d4c35670af5c5ed4f2361c6ed5a254de579a8e76d832432b1a1`
- block 11163246, position 12, result success, from `0xea1b49ac4a80ce9f2d15e3881a18ffb4bc7556b1`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 1.500000 ETH, gas used 129978 at 55.0 gwei, fee 0.007149 ETH
- token transfers (Blockscout, decoded):
  - 1.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 1.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca`
  - 0.574698 SAIYAN (`0x2b83fc17`): `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` -> `0x0000000000000000000000000000000000000000`
  - 13.792762 SAIYAN (`0x2b83fc17`): `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` -> `0xea1b49ac4a80ce9f2d15e3881a18ffb4bc7556b1`
- internal ETH transfers (Etherscan):
  - 1.500000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.500000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2b83fc177e887e4109f69c7a6f9a056797b0028e` Transfer
  - `0x2b83fc177e887e4109f69c7a6f9a056797b0028e` Transfer
  - `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` UniswapV2 Sync
  - `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` UniswapV2 Swap
- receipt status 1, index 12

### Back leg: `0x37e6910d5e76afee10df5548b8cad384c028a887b2402ca2945f8382f1e94669`
- block 11163246, position 13, result success, from `0x9b568d160ebc9a73d32e88d1d2a9ee0570ad5c9e`, to `0xf27b6320e9fa107c9ae72f1c82fa57000fbc0792`, value 0.000000 ETH, gas used 96220 at 55.0 gwei, fee 0.005292 ETH
- token transfers (Blockscout, decoded):
  - 0.205347 SAIYAN (`0x2b83fc17`): `0xf27b6320e9fa107c9ae72f1c82fa57000fbc0792` -> `0x0000000000000000000000000000000000000000`
  - 4.928338 SAIYAN (`0x2b83fc17`): `0xf27b6320e9fa107c9ae72f1c82fa57000fbc0792` -> `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca`
  - 0.535538 WETH (`0xc02aaa39`): `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` -> `0xf27b6320e9fa107c9ae72f1c82fa57000fbc0792`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x2b83fc177e887e4109f69c7a6f9a056797b0028e` Transfer
  - `0x2b83fc177e887e4109f69c7a6f9a056797b0028e` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` UniswapV2 Sync
  - `0x7a21a32b536d72613cda8f4d2739821e8dc0f8ca` UniswapV2 Swap
- receipt status 1, index 13
