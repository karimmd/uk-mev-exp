# pack_200

Block 10658390. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xdd2e96acd21f94c1d2ab6cf4fa0e4a7d9b8c74053b641efd15ad7aa9f17cd645`
- block 10658390, position 71, result success, from `0x0f8f3fbaa732bbf83c23616fed9aef29fa0bb29b`, to `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`, value 0.000000 ETH, gas used 126224 at 280.6 gwei, fee 0.035413 ETH
- token transfers (Blockscout, decoded):
  - 11.000000 WETH (`0xc02aaa39`): `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0x0000000000000000000000000000000000000000`
  - 11.000000 WETH (`0xc02aaa39`): `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e`
  - 632.746926 KEN (`0x6a7ef499`): `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` -> `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`
- internal ETH transfers (Etherscan):
  - 11.000000 ETH: `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 11.000000 ETH for `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6a7ef4998eb9d0f706238756949f311a59e05745` Transfer
  - `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` UniswapV2 Sync
  - `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` UniswapV2 Swap
- receipt status 1, index 71

### Victim leg: `0xf0eacb204de6b490b347ea4dcc558e9de44245fdb7c85edd4e53d9c8af5d345b`
- block 10658390, position 77, result success, from `0xf20782bcf4f093f255822884c3967752153e286c`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 13.078290 ETH, gas used 126133 at 278.0 gwei, fee 0.035065 ETH
- token transfers (Blockscout, decoded):
  - 12.726994 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 12.726994 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e`
  - 700.000000 KEN (`0x6a7ef499`): `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` -> `0xf20782bcf4f093f255822884c3967752153e286c`
- internal ETH transfers (Etherscan):
  - 12.726994 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.351296 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xf20782bcf4f093f255822884c3967752153e286c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 12.726994 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6a7ef4998eb9d0f706238756949f311a59e05745` Transfer
  - `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` UniswapV2 Sync
  - `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` UniswapV2 Swap
- receipt status 1, index 77

### Back leg: `0x53adc64364ace9ed66f0192f773192bffe8b48384541206f35fb0ef835c18b95`
- block 10658390, position 78, result success, from `0x0f8f3fbaa732bbf83c23616fed9aef29fa0bb29b`, to `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`, value 0.000000 ETH, gas used 107038 at 278.0 gwei, fee 0.029757 ETH
- token transfers (Blockscout, decoded):
  - 632.746926 KEN (`0x6a7ef499`): `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e`
  - 11.462709 WETH (`0xc02aaa39`): `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` -> `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`
  - 11.462709 WETH (`0xc02aaa39`): `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 11.462709 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x6a7ef4998eb9d0f706238756949f311a59e05745` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` UniswapV2 Sync
  - `0x6225f6d7ad5ea259a2227d3f39cf808f3098af6e` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 11.462709 ETH for `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`
- receipt status 1, index 78
