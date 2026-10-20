# pack_033

Block 12193550. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x9c894b94367094c077bcbb885b4ac745ee147451b97ecc4063fb7ee949d0b9a5`
- block 12193550, position 0, result success, from `0x40a15a4f062a6c562333ad9b4d530c099f255a7b`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 125728 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 68.900000 WETH (`0xc02aaa39`): `0x40a15a4f062a6c562333ad9b4d530c099f255a7b` -> `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304`
  - 64768.806987 LKR (`0x80ce3027`): `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` -> `0x40a15a4f062a6c562333ad9b4d530c099f255a7b`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x80ce3027a70e0a928d9268994e9b85d03bd4cdcf` Transfer
  - `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` UniswapV2 Sync
  - `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x842c35ea3b846922219e45c1f1a148e8706895a616b1f10370520a0f256e4156`
- block 12193550, position 1, result success, from `0x846b2ec87caa0112d0bcf9dd44da599791521c7c`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 1.800000 ETH, gas used 132546 at 170.0 gwei, fee 0.022533 ETH
- token transfers (Blockscout, decoded):
  - 1.800000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 1.800000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304`
  - 1383.666427 LKR (`0x80ce3027`): `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` -> `0x846b2ec87caa0112d0bcf9dd44da599791521c7c`
- internal ETH transfers (Etherscan):
  - 1.800000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.800000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x80ce3027a70e0a928d9268994e9b85d03bd4cdcf` Transfer
  - `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` UniswapV2 Sync
  - `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xe19386e7289730f7ba0702e6dfd6739bb9b7d75a970c4dcc9b9dd1dd7d2eda65`
- block 12193550, position 3, result success, from `0x40a15a4f062a6c562333ad9b4d530c099f255a7b`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 99051 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 64768.806987 LKR (`0x80ce3027`): `0x40a15a4f062a6c562333ad9b4d530c099f255a7b` -> `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304`
  - 69.143281 WETH (`0xc02aaa39`): `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` -> `0x40a15a4f062a6c562333ad9b4d530c099f255a7b`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x80ce3027a70e0a928d9268994e9b85d03bd4cdcf` Transfer
  - `0x80ce3027a70e0a928d9268994e9b85d03bd4cdcf` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` UniswapV2 Sync
  - `0x670c0f67a4dc05b6d482c3ddaf0bcb8a20cdc304` UniswapV2 Swap
- receipt status 1, index 3
