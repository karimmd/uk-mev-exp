# pack_063

Block 13042222. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x40adc6eacf5127d82283235a17c117cc2797b3cd9a9d9e6a7bca56be74dfeed0`
- block 13042222, position 0, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 88447 at 34.7 gwei, fee 0.003068 ETH
- token transfers (Blockscout, decoded):
  - 1.858765 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x0efea698136d636e2babad10821e9064fe08f418`
  - 4360.590635 ICE (`0xf16e81dc`): `0x0efea698136d636e2babad10821e9064fe08f418` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf16e81dce15b08f326220742020379b855b87df9` Transfer
  - `0x0efea698136d636e2babad10821e9064fe08f418` UniswapV2 Sync
  - `0x0efea698136d636e2babad10821e9064fe08f418` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x9751deef9e638b7ee186c4eee8020ab200e8feeeaa9da5a44a0d0523da6045f5`
- block 13042222, position 1, result success, from `0x5d8a9b0b8a8aace7ddb6a631d2f2f4e00c49925a`, to `0x11111112542d85b3ef69ae05771c2dccff4faa26`, value 4.000000 ETH, gas used 233243 at 77.0 gwei, fee 0.017960 ETH
- token transfers (Blockscout, decoded):
  - 4.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 2.000000 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x94b86ca6f7a495930fe7f552eb9e4cbb5ef2b736`
  - 4685.191969 ICE (`0xf16e81dc`): `0x94b86ca6f7a495930fe7f552eb9e4cbb5ef2b736` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 2.000000 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x0efea698136d636e2babad10821e9064fe08f418`
  - 4594.684014 ICE (`0xf16e81dc`): `0x0efea698136d636e2babad10821e9064fe08f418` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 9279.875983 ICE (`0xf16e81dc`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x5d8a9b0b8a8aace7ddb6a631d2f2f4e00c49925a`
- internal ETH transfers (Etherscan):
  - 4.000000 ETH: `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` [call]
  - 4.000000 ETH: `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 4.000000 ETH for `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf16e81dce15b08f326220742020379b855b87df9` Transfer
  - `0x94b86ca6f7a495930fe7f552eb9e4cbb5ef2b736` UniswapV2 Sync
  - `0x94b86ca6f7a495930fe7f552eb9e4cbb5ef2b736` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf16e81dce15b08f326220742020379b855b87df9` Transfer
  - `0x0efea698136d636e2babad10821e9064fe08f418` UniswapV2 Sync
  - `0x0efea698136d636e2babad10821e9064fe08f418` UniswapV2 Swap
  - `0xf16e81dce15b08f326220742020379b855b87df9` Transfer
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
- receipt status 1, index 1

### Back leg: `0xf56c7faf8c4cbe98630f322d9c8f599477ceadd740eae18a1c019e93f6439623`
- block 13042222, position 2, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 78503 at 225.2 gwei, fee 0.017677 ETH
- token transfers (Blockscout, decoded):
  - 4360.590635 ICE (`0xf16e81dc`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x0efea698136d636e2babad10821e9064fe08f418`
  - 1.887881 WETH (`0xc02aaa39`): `0x0efea698136d636e2babad10821e9064fe08f418` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xf16e81dce15b08f326220742020379b855b87df9` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0efea698136d636e2babad10821e9064fe08f418` UniswapV2 Sync
  - `0x0efea698136d636e2babad10821e9064fe08f418` UniswapV2 Swap
- receipt status 1, index 2
