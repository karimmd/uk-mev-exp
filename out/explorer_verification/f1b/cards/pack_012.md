# pack_012

Block 12497062. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xae4799228c87211afe0ddff44e75dc56c67d7293d4551945886747a9d088a0da`
- block 12497062, position 19, result success, from `0xdd07249e403979bd79848c27aa5454c7e66bdee7`, to `0x000000000000084e91743124a982076c59f10084`, value 0.000000 ETH, gas used 114900 at 294.0 gwei, fee 0.033781 ETH
- token transfers (Blockscout, decoded):
  - 7.109631 WETH (`0xc02aaa39`): `0x000000000000084e91743124a982076c59f10084` -> `0x9314941c11d6dee1d7bf93113eb74d4718949f3b`
  - 12545994060244.000000 $HOKK (`0xc40af1e4`): `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` -> `0x000000000000084e91743124a982076c59f10084`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc40af1e4fecfa05ce6bab79dcd8b373d2e436c4e` Transfer
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Sync
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Swap
- receipt status 1, index 19

### Victim leg: `0xc7b3c0bc51091e251ebc41a397de9429ee8b59f5c62ab2ebe7be019b03969b53`
- block 12497062, position 108, result success, from `0xb8ca22a9b2cd28b697690a62b2d0851f339a13ea`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 175486 at 90.0 gwei, fee 0.015794 ETH
- token transfers (Blockscout, decoded):
  - 35000.688607 USDC (`0xa0b86991`): `0xb8ca22a9b2cd28b697690a62b2d0851f339a13ea` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 14.239149 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0x9314941c11d6dee1d7bf93113eb74d4718949f3b`
  - 23445505836495.289062 $HOKK (`0xc40af1e4`): `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` -> `0xb8ca22a9b2cd28b697690a62b2d0851f339a13ea`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0xc40af1e4fecfa05ce6bab79dcd8b373d2e436c4e` Transfer
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Sync
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Swap
- receipt status 1, index 108

### Back leg: `0x92619f041ee0f6085b291b7e451faebb68e5facf0d8c8f5dd82b2f94f28206e6`
- block 12497062, position 109, result success, from `0xdb9c8428e68a1e6b2244c92127d2dcd708f893f4`, to `0x000000000000084e91743124a982076c59f10084`, value 0.000000 ETH, gas used 113111 at 90.0 gwei, fee 0.010180 ETH
- token transfers (Blockscout, decoded):
  - 12295164489380.625000 $HOKK (`0xc40af1e4`): `0x000000000000084e91743124a982076c59f10084` -> `0x9314941c11d6dee1d7bf93113eb74d4718949f3b`
  - 7.437456 WETH (`0xc02aaa39`): `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` -> `0x000000000000084e91743124a982076c59f10084`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc40af1e4fecfa05ce6bab79dcd8b373d2e436c4e` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Sync
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Swap
- receipt status 1, index 109
