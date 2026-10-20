# pack_113

Block 13876990. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x5130698c2526df25c476ea3474825ee7c468d7ae2e41777b2ce6751befa54647`
- block 13876990, position 0, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 86865 at 100.9 gwei, fee 0.008766 ETH
- token transfers (Blockscout, decoded):
  - 3.134871 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x9d18248e03122a198eb17b11d3442665d7c5b16f`
  - 470857416.100036 FlokiSanta (`0xee5f2ce5`): `0x9d18248e03122a198eb17b11d3442665d7c5b16f` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xee5f2ce50a6d988007f90986af0de91995c4e794` Transfer
  - `0x9d18248e03122a198eb17b11d3442665d7c5b16f` UniswapV2 Sync
  - `0x9d18248e03122a198eb17b11d3442665d7c5b16f` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x513f5d47dd519d70ab706ffb7271ff973cee59cba7c9bdfc211099b7c41e96e1`
- block 13876990, position 1, result success, from `0x699a905b4d117c758eea4bfdf153170893f58dc6`, to `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`, value 0.050000 ETH, gas used 114182 at 97.6 gwei, fee 0.011140 ETH
- token transfers (Blockscout, decoded):
  - 0.050000 WETH (`0xc02aaa39`): `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0x0000000000000000000000000000000000000000`
  - 0.050000 WETH (`0xc02aaa39`): `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0x9d18248e03122a198eb17b11d3442665d7c5b16f`
  - 1120575.307059 FlokiSanta (`0xee5f2ce5`): `0x9d18248e03122a198eb17b11d3442665d7c5b16f` -> `0x699a905b4d117c758eea4bfdf153170893f58dc6`
- internal ETH transfers (Etherscan):
  - 0.050000 ETH: `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.050000 ETH for `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xee5f2ce50a6d988007f90986af0de91995c4e794` Transfer
  - `0x9d18248e03122a198eb17b11d3442665d7c5b16f` UniswapV2 Sync
  - `0x9d18248e03122a198eb17b11d3442665d7c5b16f` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xdc528d7fd573df4ef578906f9a8c3068292057905268cda7df7cf5c2dde8eab3`
- block 13876990, position 2, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 76860 at 487.4 gwei, fee 0.037464 ETH
- token transfers (Blockscout, decoded):
  - 470857212.960479 FlokiSanta (`0xee5f2ce5`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x9d18248e03122a198eb17b11d3442665d7c5b16f`
  - 3.180855 WETH (`0xc02aaa39`): `0x9d18248e03122a198eb17b11d3442665d7c5b16f` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xee5f2ce50a6d988007f90986af0de91995c4e794` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9d18248e03122a198eb17b11d3442665d7c5b16f` UniswapV2 Sync
  - `0x9d18248e03122a198eb17b11d3442665d7c5b16f` UniswapV2 Swap
- receipt status 1, index 2
