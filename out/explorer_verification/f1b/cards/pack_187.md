# pack_187

Block 12554966. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xfb229df1e958e0e6d8aad25c303aba52010fdd370467386289fbb5abe74be339`
- block 12554966, position 0, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 113317 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 3.910000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c`
  - 4657697853.780863 SHIBAL (`0x77f39c61`): `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xae9e9b24365e5d5908c9995d715020b2e389b141` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x147994008aa734d47f98e8ef67d7836d64730fdb` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x77f39c61ddac121ca1b24fdea984fab734fdce8f` Transfer
  - `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` UniswapV2 Sync
  - `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x3206d75f2d1109e4ce38f7b693de70774fef31093dded92e08d66a161569f04c`
- block 12554966, position 1, result success, from `0xe356fe28b7b6b015a3b2bb4419dbdf2777d7420b`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 172909 at 3000.0 gwei, fee 0.518727 ETH
- token transfers (Blockscout, decoded):
  - 30000.000000 USDC (`0xa0b86991`): `0xe356fe28b7b6b015a3b2bb4419dbdf2777d7420b` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 11.080747 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c`
  - 9337721199.786066 SHIBAL (`0x77f39c61`): `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` -> `0xe356fe28b7b6b015a3b2bb4419dbdf2777d7420b`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0x77f39c61ddac121ca1b24fdea984fab734fdce8f` Transfer
  - `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` UniswapV2 Sync
  - `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x54f88aeaa5dd9a713d2fa16bee71b9310e9042ae3a4b5fc704d31c1bd20408ca`
- block 12554966, position 2, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 1.925876 ETH, gas used 122474 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 4565847915.118942 SHIBAL (`0x77f39c61`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c`
  - 5.956627 WETH (`0xc02aaa39`): `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 1.925876 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xea674fdde714fd979de3edf0f56aa9716b898ec8` [call]
  - 0.000000 ETH: `0xa8d6317060974118245a6f2a78fb54af8cb05bcb` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x841e9381d42fcf9864acf2bd3585a1476502d5e8` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x77f39c61ddac121ca1b24fdea984fab734fdce8f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` UniswapV2 Sync
  - `0xd2f1fd188f127cde9d0feef58c3eb457cc0bcb9c` UniswapV2 Swap
- receipt status 1, index 2
