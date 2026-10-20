# pack_067

Block 12144270. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xdf46a656f625d5586ab1650532536af34ea24780d799d924161788954e5b86bb`
- block 12144270, position 28, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 94895 at 151.1 gwei, fee 0.014339 ETH
- token transfers (Blockscout, decoded):
  - 4.030000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x21359dfb99489204a3549692dd80f2cff4d4e8f9`
  - 5074.997847 STR (`0x84bb947f`): `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x84bb947fcedba6b9c7dcead42df07e113bb03007` Transfer
  - `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` UniswapV2 Sync
  - `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` UniswapV2 Swap
- receipt status 1, index 28

### Victim leg: `0x2a52395a102e6438e76b6d7a3893c0d649ce6909c4f20b3a5e6cddbc674a9450`
- block 12144270, position 31, result success, from `0xc4cdfb0c94c2fb39630134da5d49a3023bd6b163`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 6.000000 ETH, gas used 112555 at 151.0 gwei, fee 0.016996 ETH
- token transfers (Blockscout, decoded):
  - 6.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 6.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x21359dfb99489204a3549692dd80f2cff4d4e8f9`
  - 7372.159377 STR (`0x84bb947f`): `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` -> `0xc4cdfb0c94c2fb39630134da5d49a3023bd6b163`
- internal ETH transfers (Etherscan):
  - 6.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 6.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x84bb947fcedba6b9c7dcead42df07e113bb03007` Transfer
  - `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` UniswapV2 Sync
  - `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` UniswapV2 Swap
- receipt status 1, index 31

### Back leg: `0xbcc04619a180376404d4c1145e27db900220448a63d1baed092177d04184234d`
- block 12144270, position 34, result success, from `0x74b892425a206eb23905a5f5c322e4386460312d`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 93165 at 151.0 gwei, fee 0.014068 ETH
- token transfers (Blockscout, decoded):
  - 5074.997847 STR (`0x84bb947f`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x21359dfb99489204a3549692dd80f2cff4d4e8f9`
  - 4.124627 WETH (`0xc02aaa39`): `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x84bb947fcedba6b9c7dcead42df07e113bb03007` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` UniswapV2 Sync
  - `0x21359dfb99489204a3549692dd80f2cff4d4e8f9` UniswapV2 Swap
- receipt status 1, index 34
