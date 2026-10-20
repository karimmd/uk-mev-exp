# pack_038

Block 12062430. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xd5b88a0a389c05de9a039036bf06ceed4c5f770636399092ef53a22d62c23f06`
- block 12062430, position 3, result success, from `0x8ed86bef2bbd1f685b655c4c95e0e8c282fe9f20`, to `0x000000005be1b41f8ed12d32409c8475e83f2ee3`, value 0.000000 ETH, gas used 102829 at 190.1 gwei, fee 0.019550 ETH
- token transfers (Blockscout, decoded):
  - 13.474489 WETH (`0xc02aaa39`): `0x000000005be1b41f8ed12d32409c8475e83f2ee3` -> `0xfe903a12359496b932e24c5e9b78f1b9060a6342`
  - 11617.865403 PKF (`0x8b39b70e`): `0xfe903a12359496b932e24c5e9b78f1b9060a6342` -> `0x000000005be1b41f8ed12d32409c8475e83f2ee3`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8b39b70e39aa811b69365398e0aace9bee238aeb` Transfer
  - `0xfe903a12359496b932e24c5e9b78f1b9060a6342` UniswapV2 Sync
  - `0xfe903a12359496b932e24c5e9b78f1b9060a6342` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x3cb1c34074b713d64724257aeb59fa502e729e3eb4d8d2fafc21caae8ad93c78`
- block 12062430, position 13, result success, from `0xe58b7265d56c4a1465ca44357d33c240d0cef6ca`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 8.000000 ETH, gas used 112320 at 169.0 gwei, fee 0.018982 ETH
- token transfers (Blockscout, decoded):
  - 8.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 8.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xfe903a12359496b932e24c5e9b78f1b9060a6342`
  - 6655.202058 PKF (`0x8b39b70e`): `0xfe903a12359496b932e24c5e9b78f1b9060a6342` -> `0xe58b7265d56c4a1465ca44357d33c240d0cef6ca`
- internal ETH transfers (Etherscan):
  - 8.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 8.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8b39b70e39aa811b69365398e0aace9bee238aeb` Transfer
  - `0xfe903a12359496b932e24c5e9b78f1b9060a6342` UniswapV2 Sync
  - `0xfe903a12359496b932e24c5e9b78f1b9060a6342` UniswapV2 Swap
- receipt status 1, index 13

### Back leg: `0xdc896452c35452d03ec62fa0fb126a20ce534aa4011c3dcbe495e2ae5e674f74`
- block 12062430, position 15, result success, from `0x8ed86bef2bbd1f685b655c4c95e0e8c282fe9f20`, to `0x000000005be1b41f8ed12d32409c8475e83f2ee3`, value 0.000000 ETH, gas used 98169 at 169.0 gwei, fee 0.016591 ETH
- token transfers (Blockscout, decoded):
  - 11617.865403 PKF (`0x8b39b70e`): `0x000000005be1b41f8ed12d32409c8475e83f2ee3` -> `0xfe903a12359496b932e24c5e9b78f1b9060a6342`
  - 13.749253 WETH (`0xc02aaa39`): `0xfe903a12359496b932e24c5e9b78f1b9060a6342` -> `0x000000005be1b41f8ed12d32409c8475e83f2ee3`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x8b39b70e39aa811b69365398e0aace9bee238aeb` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfe903a12359496b932e24c5e9b78f1b9060a6342` UniswapV2 Sync
  - `0xfe903a12359496b932e24c5e9b78f1b9060a6342` UniswapV2 Swap
- receipt status 1, index 15
