# pack_143

Block 11501782. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xcc6ea8bc3e22bab87b2529c85d4fa5d748d9fe008b7123f8857d69ffd3100276`
- block 11501782, position 46, result success, from `0x60530f5ca4cb9907e0fbe67ca3afcbfe56d19a5c`, to `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`, value 0.000000 ETH, gas used 231090 at 65.0 gwei, fee 0.015021 ETH
- token transfers (Blockscout, decoded):
  - 13.415322 WETH (`0xc02aaa39`): `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0x0000000000000000000000000000000000000000`
  - 13.415322 WETH (`0xc02aaa39`): `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0x7b1800b20e87e607b2791282dff9e069bb18493c`
  - 2981.182750 API3 (`0x0b38210e`): `0x7b1800b20e87e607b2791282dff9e069bb18493c` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`
  - 2981.182750 API3 (`0x0b38210e`): `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0x4dd26482738be6c06c31467a19dcda9ad781e8c4`
  - 13.485641 WETH (`0xc02aaa39`): `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`
  - 13.485641 WETH (`0xc02aaa39`): `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 13.415322 ETH: `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.004550 ETH: `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0x61935cbdd02287b511119ddb11aeb42f1593b7ef` [call]
  - 0.004550 ETH: `0x61935cbdd02287b511119ddb11aeb42f1593b7ef` -> `0xa26e80e7dea86279c6d778d702cc413e6cffa777` [call]
  - 13.485641 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 13.415322 ETH for `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`
  - `0x61935cbdd02287b511119ddb11aeb42f1593b7ef` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0b38210ea11411557c13457d4da7dc6ea731b88a` Transfer
  - `0x0b38210ea11411557c13457d4da7dc6ea731b88a` Approval
  - `0x0b38210ea11411557c13457d4da7dc6ea731b88a` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` UniswapV2 Sync
  - `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 13.485641 ETH for `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`
- receipt status 1, index 46

### Victim leg: `0xfb9bed36abb4058f6dca21abc3d222a76641a8d87c01021bdb7568bd534d0f6b`
- block 11501782, position 73, result success, from `0x19313b159827f45f6ea03d7849fae1ddac7c92e8`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 168045 at 56.1 gwei, fee 0.009427 ETH
- token transfers (Blockscout, decoded):
  - 2735.856255 USDC (`0xa0b86991`): `0x19313b159827f45f6ea03d7849fae1ddac7c92e8` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 4.535008 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0x4dd26482738be6c06c31467a19dcda9ad781e8c4`
  - 1000.000000 API3 (`0x0b38210e`): `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` -> `0x19313b159827f45f6ea03d7849fae1ddac7c92e8`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0x0b38210ea11411557c13457d4da7dc6ea731b88a` Transfer
  - `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` UniswapV2 Sync
  - `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` UniswapV2 Swap
- receipt status 1, index 73

### Back leg: `0x37e82b6c84dec8d4cda63207e5cfe2a710015584e3e099b4f2eba4c2134bd100`
- block 11501782, position 126, result success, from `0x0000002cbdf38c64dfc30b9db6537358481a9de0`, to `0x000000000000006f6502b7f2bbac8c30a3f67e9a`, value 0.000000 ETH, gas used 224818 at 53.0 gwei, fee 0.011915 ETH
- token transfers (Blockscout, decoded):
  - 33.999925 WETH (`0xc02aaa39`): `0x000000000000006f6502b7f2bbac8c30a3f67e9a` -> `0x0000000000000000000000000000000000000000`
  - 33.999925 WETH (`0xc02aaa39`): `0x000000000000006f6502b7f2bbac8c30a3f67e9a` -> `0x7b1800b20e87e607b2791282dff9e069bb18493c`
  - 7555.538975 API3 (`0x0b38210e`): `0x7b1800b20e87e607b2791282dff9e069bb18493c` -> `0x000000000000006f6502b7f2bbac8c30a3f67e9a`
  - 7555.538975 API3 (`0x0b38210e`): `0x000000000000006f6502b7f2bbac8c30a3f67e9a` -> `0x4dd26482738be6c06c31467a19dcda9ad781e8c4`
  - 34.949465 WETH (`0xc02aaa39`): `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` -> `0x000000000000006f6502b7f2bbac8c30a3f67e9a`
  - 34.949465 WETH (`0xc02aaa39`): `0x000000000000006f6502b7f2bbac8c30a3f67e9a` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 33.999925 ETH: `0x000000000000006f6502b7f2bbac8c30a3f67e9a` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.003710 ETH: `0x000000000000006f6502b7f2bbac8c30a3f67e9a` -> `0x61935cbdd02287b511119ddb11aeb42f1593b7ef` [call]
  - 0.003710 ETH: `0x61935cbdd02287b511119ddb11aeb42f1593b7ef` -> `0xa26e80e7dea86279c6d778d702cc413e6cffa777` [call]
  - 34.949465 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x000000000000006f6502b7f2bbac8c30a3f67e9a` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 33.999925 ETH for `0x000000000000006f6502b7f2bbac8c30a3f67e9a`
  - `0x61935cbdd02287b511119ddb11aeb42f1593b7ef` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0b38210ea11411557c13457d4da7dc6ea731b88a` Transfer
  - `0x0b38210ea11411557c13457d4da7dc6ea731b88a` Approval
  - `0x0b38210ea11411557c13457d4da7dc6ea731b88a` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` UniswapV2 Sync
  - `0x4dd26482738be6c06c31467a19dcda9ad781e8c4` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 34.949465 ETH for `0x000000000000006f6502b7f2bbac8c30a3f67e9a`
- receipt status 1, index 126
