# pack_029

Block 12827766. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x191a62e6245e6f7f684af4751dd0831380b51a00c5b125990cd0437ae16ee1be`
- block 12827766, position 0, result success, from `0x160d981f3a6cf177052f803f2c59636312564e1d`, to `0x50004cb09702ced04e59dcdaff9df58b6cc97983`, value 0.000000 ETH, gas used 135060 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 20.366370 WETH (`0xc02aaa39`): `0x50004cb09702ced04e59dcdaff9df58b6cc97983` -> `0xbb2b8038a1640196fbe3e38816f3e67cba72d940`
  - 1.232134 WBTC (`0x2260fac5`): `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` -> `0x18d98d452072ac2eb7b74ce3db723374360539f1`
  - 1.224440 ibBTC (`0xc4e15973`): `0x18d98d452072ac2eb7b74ce3db723374360539f1` -> `0x50004cb09702ced04e59dcdaff9df58b6cc97983`
  - 4.000000 CHI (`0x00000000`): `0x50004cb09702ced04e59dcdaff9df58b6cc97983` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x8d61b39726b09e4ca15698b72b83f88997606c81` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xb8a7a70920e628ba80b6d3bc9669d1c9fd7bc018` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x5c83ffc93aac76919b4192acf5677c22a19a4a88` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xdd321bacb6247428f526b1003d9a242f001e8d5f` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` UniswapV2 Sync
  - `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` UniswapV2 Swap
  - `0xc4e15973e6ff2a35cc804c2cf9d2a1b817a8b40f` Transfer
  - `0x18d98d452072ac2eb7b74ce3db723374360539f1` UniswapV2 Sync
  - `0x18d98d452072ac2eb7b74ce3db723374360539f1` UniswapV2 Swap
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Transfer
- receipt status 1, index 0

### Victim leg: `0x3a697d18ab74b173b7bc03cca4b2eede3b2c8421e28acdd2eaa88bf84f6bb0aa`
- block 12827766, position 1, result success, from `0x4e5ed30e3b4eb39abce3c150f31e180a3ae5806e`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 0.000000 ETH, gas used 97596 at 191.1 gwei, fee 0.018651 ETH
- token transfers (Blockscout, decoded):
  - 9.900000 WBTC (`0x2260fac5`): `0x4e5ed30e3b4eb39abce3c150f31e180a3ae5806e` -> `0x18d98d452072ac2eb7b74ce3db723374360539f1`
  - 9.619263 ibBTC (`0xc4e15973`): `0x18d98d452072ac2eb7b74ce3db723374360539f1` -> `0x4e5ed30e3b4eb39abce3c150f31e180a3ae5806e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xc4e15973e6ff2a35cc804c2cf9d2a1b817a8b40f` Transfer
  - `0x18d98d452072ac2eb7b74ce3db723374360539f1` UniswapV2 Sync
  - `0x18d98d452072ac2eb7b74ce3db723374360539f1` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x527d4545e8efcc9a1ee6eb4f0860c539ebc780400acb88c466b7cf4577358a90`
- block 12827766, position 2, result success, from `0x160d981f3a6cf177052f803f2c59636312564e1d`, to `0x50004cb09702ced04e59dcdaff9df58b6cc97983`, value 0.000000 ETH, gas used 104125 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 1.224440 ibBTC (`0xc4e15973`): `0x50004cb09702ced04e59dcdaff9df58b6cc97983` -> `0x18d98d452072ac2eb7b74ce3db723374360539f1`
  - 1.274716 WBTC (`0x2260fac5`): `0x18d98d452072ac2eb7b74ce3db723374360539f1` -> `0xbb2b8038a1640196fbe3e38816f3e67cba72d940`
  - 20.943623 WETH (`0xc02aaa39`): `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` -> `0x50004cb09702ced04e59dcdaff9df58b6cc97983`
  - 4.000000 CHI (`0x00000000`): `0x50004cb09702ced04e59dcdaff9df58b6cc97983` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.346351 ETH: `0x50004cb09702ced04e59dcdaff9df58b6cc97983` -> `0xb3b7874f13387d44a3398d298b075b7a3505d8d4` [call]
  - 0.000000 ETH: `0x0e618746499d0664ccb8e8a4b472491e5be666da` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x1186883da7406c358be890082236290ca9b5df63` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xcb2f49d74fedc5117835e776566847ab705b1f18` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xe1c4741359c246b6cf0bc5fffd88553bf7621758` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc4e15973e6ff2a35cc804c2cf9d2a1b817a8b40f` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x18d98d452072ac2eb7b74ce3db723374360539f1` UniswapV2 Sync
  - `0x18d98d452072ac2eb7b74ce3db723374360539f1` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` UniswapV2 Sync
  - `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` UniswapV2 Swap
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Transfer
- receipt status 1, index 2
