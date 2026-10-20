# pack_066

Block 13943254. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xec1d1fc0cf5d677622d3fcd56a96cedf19570e4e5a68c20d15ffd62037ec7ac4`
- block 13943254, position 7, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.000000 ETH, gas used 97596 at 1200.0 gwei, fee 0.117115 ETH
- token transfers (Blockscout, decoded):
  - 5438.946266 POW (`0x43ab765e`): `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 3.580897 WETH (`0xc02aaa39`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x43ab765ee05075d78ad8aa79dcb1978ca3079258` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e` UniswapV3 Swap
- receipt status 1, index 7

### Victim leg: `0x4be4f73c51f45b36acb1409d9c98d996ff0904689f93c59cbb99d238b5052cae`
- block 13943254, position 9, result success, from `0x9de0b0402258a6a562331da7b3c13b29578789c4`, to `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`, value 0.100000 ETH, gas used 126845 at 144.0 gwei, fee 0.018266 ETH
- token transfers (Blockscout, decoded):
  - 126.338545 POW (`0x43ab765e`): `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e` -> `0x9de0b0402258a6a562331da7b3c13b29578789c4`
  - 0.100000 WETH (`0xc02aaa39`): `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0x0000000000000000000000000000000000000000`
  - 0.100000 WETH (`0xc02aaa39`): `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e`
- internal ETH transfers (Etherscan):
  - 0.100000 ETH: `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x43ab765ee05075d78ad8aa79dcb1978ca3079258` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.100000 ETH for `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e` UniswapV3 Swap
- receipt status 1, index 9

### Back leg: `0x46f9c8dede49707cdb7018880259813b0c27cf857cfd9a7ee667168f2a8e11eb`
- block 13943254, position 10, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.111009 ETH, gas used 110191 at 1200.0 gwei, fee 0.132229 ETH
- token transfers (Blockscout, decoded):
  - 3.746107 WETH (`0xc02aaa39`): `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 5438.946266 POW (`0x43ab765e`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e`
- internal ETH transfers (Etherscan):
  - 0.111009 ETH: `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x45a36a8e118c37e4c47ef4ab827a7c9e579e11e2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x43ab765ee05075d78ad8aa79dcb1978ca3079258` Transfer
  - `0xc0793782d11dd9bf7b3a7a5a74614f1debe1da2e` UniswapV3 Swap
- receipt status 1, index 10
