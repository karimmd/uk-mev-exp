# pack_124

Block 13424670. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x9f8c88176556846c4defcfe6989855c79e4e562437bd1079f4fb2dda9717339b`
- block 13424670, position 6, result success, from `0xd6f660aea79dabd5220332a73d4effaeb70b3547`, to `0xa405e822d1c3a8568c6b82eb6e570fca0136f802`, value 0.000000 ETH, gas used 87512 at 107.8 gwei, fee 0.009433 ETH
- token transfers (Blockscout, decoded):
  - 0.885515 WETH (`0xc02aaa39`): `0xa405e822d1c3a8568c6b82eb6e570fca0136f802` -> `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e`
  - 12558.190023 EQX (`0xbd3de9a0`): `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` -> `0xa405e822d1c3a8568c6b82eb6e570fca0136f802`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xbd3de9a069648c84d27d74d701c9fa3253098b15` Transfer
  - `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` UniswapV2 Sync
  - `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` UniswapV2 Swap
- receipt status 1, index 6

### Victim leg: `0xfa7aef1233b8af480510de5655b919c2de72c308ec52c536729436f8777a893e`
- block 13424670, position 7, result success, from `0x6794471ebc084a4ca462c506afeabb93d9657c25`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 5.000000 ETH, gas used 109672 at 109.4 gwei, fee 0.012002 ETH
- token transfers (Blockscout, decoded):
  - 5.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 5.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e`
  - 68605.147831 EQX (`0xbd3de9a0`): `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` -> `0x6794471ebc084a4ca462c506afeabb93d9657c25`
- internal ETH transfers (Etherscan):
  - 5.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 5.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xbd3de9a069648c84d27d74d701c9fa3253098b15` Transfer
  - `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` UniswapV2 Sync
  - `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` UniswapV2 Swap
- receipt status 1, index 7

### Back leg: `0xbd93cf7b3f84b04f2f84797c4184da69914ce8b7b7be0a20eecb1d20570d0855`
- block 13424670, position 8, result success, from `0xd6f660aea79dabd5220332a73d4effaeb70b3547`, to `0xa405e822d1c3a8568c6b82eb6e570fca0136f802`, value 0.000000 ETH, gas used 77304 at 461.3 gwei, fee 0.035663 ETH
- token transfers (Blockscout, decoded):
  - 12558.190023 EQX (`0xbd3de9a0`): `0xa405e822d1c3a8568c6b82eb6e570fca0136f802` -> `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e`
  - 0.930838 WETH (`0xc02aaa39`): `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` -> `0xa405e822d1c3a8568c6b82eb6e570fca0136f802`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xbd3de9a069648c84d27d74d701c9fa3253098b15` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` UniswapV2 Sync
  - `0x09062ce4f20aac71f8074ac6cf8e6968abd4d03e` UniswapV2 Swap
- receipt status 1, index 8
