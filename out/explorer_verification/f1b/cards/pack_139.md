# pack_139

Block 11530118. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xb45756b60223b2f1055db84b5061e54477c0c3e08ccded7d6cfe5c2557052b22`
- block 11530118, position 165, result success, from `0xa56fb88749ce87d35ef742c3a58ae40da2acdf8c`, to `0xfb5761fde5227d8bb093daf9db87013b3ab9cd24`, value 0.000000 ETH, gas used 128559 at 74.8 gwei, fee 0.009619 ETH
- token transfers (Blockscout, decoded):
  - 8407.290300 ROCKS (`0x92ece485`): `0xfb5761fde5227d8bb093daf9db87013b3ab9cd24` -> `0x5f57c5f9564d6a4e25d908605341632e33e7874d`
  - 0.507316 WETH (`0xc02aaa39`): `0x5f57c5f9564d6a4e25d908605341632e33e7874d` -> `0xfb5761fde5227d8bb093daf9db87013b3ab9cd24`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x92ece48522e1acbcda4aaa8c2fbf2aa9fb15d624` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x5f57c5f9564d6a4e25d908605341632e33e7874d` UniswapV2 Sync
  - `0x5f57c5f9564d6a4e25d908605341632e33e7874d` UniswapV2 Swap
- receipt status 1, index 165

### Victim leg: `0xe632a2482f1fb28c27fa267cd8d5c1f7635e608dd34368192b90b4e354ad57d2`
- block 11530118, position 191, result success, from `0xf89cfa2e6ee4f6e7a6887291751e9a88af591f8a`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 100528 at 73.0 gwei, fee 0.007339 ETH
- token transfers (Blockscout, decoded):
  - 70000.000000 ROCKS (`0x92ece485`): `0xf89cfa2e6ee4f6e7a6887291751e9a88af591f8a` -> `0x5f57c5f9564d6a4e25d908605341632e33e7874d`
  - 4.033361 WETH (`0xc02aaa39`): `0x5f57c5f9564d6a4e25d908605341632e33e7874d` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 4.033361 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 4.033361 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 4.033361 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xf89cfa2e6ee4f6e7a6887291751e9a88af591f8a` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x92ece48522e1acbcda4aaa8c2fbf2aa9fb15d624` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x5f57c5f9564d6a4e25d908605341632e33e7874d` UniswapV2 Sync
  - `0x5f57c5f9564d6a4e25d908605341632e33e7874d` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 4.033361 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 191

### Back leg: `0x20ca00af9c942d5bcf913e0e9553c8654a9ee26d2407dfdfc8fa8b26a8184c4a`
- block 11530118, position 192, result success, from `0xa56fb88749ce87d35ef742c3a58ae40da2acdf8c`, to `0xfb5761fde5227d8bb093daf9db87013b3ab9cd24`, value 0.000000 ETH, gas used 90704 at 73.0 gwei, fee 0.006621 ETH
- token transfers (Blockscout, decoded):
  - 0.037378 WETH (`0xc02aaa39`): `0xfb5761fde5227d8bb093daf9db87013b3ab9cd24` -> `0xefacb3fb194d5e80e569b3ac50669cf22e48f63b`
  - 0.469939 WETH (`0xc02aaa39`): `0xfb5761fde5227d8bb093daf9db87013b3ab9cd24` -> `0x5f57c5f9564d6a4e25d908605341632e33e7874d`
  - 8407.290300 ROCKS (`0x92ece485`): `0x5f57c5f9564d6a4e25d908605341632e33e7874d` -> `0xfb5761fde5227d8bb093daf9db87013b3ab9cd24`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x92ece48522e1acbcda4aaa8c2fbf2aa9fb15d624` Transfer
  - `0x5f57c5f9564d6a4e25d908605341632e33e7874d` UniswapV2 Sync
  - `0x5f57c5f9564d6a4e25d908605341632e33e7874d` UniswapV2 Swap
- receipt status 1, index 192
