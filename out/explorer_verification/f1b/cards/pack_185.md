# pack_185

Block 12524958. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x3691cbce87c503e2cf535951b81f21ffc96762844aa684cc83a9db21d2d57199`
- block 12524958, position 1, result success, from `0xc3630a4ea157b0b2fe07c98217581416c90e2f3b`, to `0x000000000000cb53d776774284822b1298ade47f`, value 0.000000 ETH, gas used 117492 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 1.554598 WETH (`0xc02aaa39`): `0x000000000000cb53d776774284822b1298ade47f` -> `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3`
  - 24057112862586.113281 KEANU (`0x106552c1`): `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` -> `0x000000000000cb53d776774284822b1298ade47f`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xb2361780d34b0775163f966cc6b19e632bac6302` -> `0x000000000000cb53d776774284822b1298ade47f` [self-destruct]
  - 0.000000 ETH: `0xff3426ea91d81e56c390e554fd448d0c6a02beb4` -> `0x000000000000cb53d776774284822b1298ade47f` [self-destruct]
  - 0.000000 ETH: `0xb40d303500527ee626f13a117ce0e09b2a73f475` -> `0x000000000000cb53d776774284822b1298ade47f` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x106552c11272420aad5d7e94f8acab9095a6c952` Transfer
  - `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` UniswapV2 Sync
  - `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` UniswapV2 Swap
- receipt status 1, index 1

### Victim leg: `0x9dd74a9312b320c16fe0f847a6d2617eb709ddadb11ec52a6cc3df9ebbf494e0`
- block 12524958, position 2, result success, from `0xef178179bca364ffedbfc13ea9fbe0fff4b9f7f9`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 147946 at 32.0 gwei, fee 0.004734 ETH
- token transfers (Blockscout, decoded):
  - 10000.000000 DAI (`0x6b175474`): `0xef178179bca364ffedbfc13ea9fbe0fff4b9f7f9` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 3.985301 WETH (`0xc02aaa39`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3`
  - 58391599554676.125000 KEANU (`0x106552c1`): `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` -> `0xef178179bca364ffedbfc13ea9fbe0fff4b9f7f9`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
  - `0x106552c11272420aad5d7e94f8acab9095a6c952` Transfer
  - `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` UniswapV2 Sync
  - `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` UniswapV2 Swap
- receipt status 1, index 2

### Back leg: `0xdaddfb3f6b66a672dd09624bca0be39d77eac161f5b01ba21a64ac2e08b74bcb`
- block 12524958, position 3, result success, from `0xc3630a4ea157b0b2fe07c98217581416c90e2f3b`, to `0x000000000000cb53d776774284822b1298ade47f`, value 0.042298 ETH, gas used 116822 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 23576086360726.500000 KEANU (`0x106552c1`): `0x000000000000cb53d776774284822b1298ade47f` -> `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3`
  - 1.604821 WETH (`0xc02aaa39`): `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` -> `0x000000000000cb53d776774284822b1298ade47f`
- internal ETH transfers (Etherscan):
  - 0.042298 ETH: `0x000000000000cb53d776774284822b1298ade47f` -> `0xea674fdde714fd979de3edf0f56aa9716b898ec8` [call]
  - 0.000000 ETH: `0x23bdeb0b487d1f485e9cf1bb340074ef792b9548` -> `0x000000000000cb53d776774284822b1298ade47f` [self-destruct]
  - 0.000000 ETH: `0xd0183c5adbfb6dd324ddfb932e11cbb8c3d7d833` -> `0x000000000000cb53d776774284822b1298ade47f` [self-destruct]
  - 0.000000 ETH: `0x18c1bbe63d668b2f602e65685ae032057a7052c5` -> `0x000000000000cb53d776774284822b1298ade47f` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x106552c11272420aad5d7e94f8acab9095a6c952` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` UniswapV2 Sync
  - `0xfee4800067bfc9dff564d116cba4d4b16ca7b7b3` UniswapV2 Swap
- receipt status 1, index 3
