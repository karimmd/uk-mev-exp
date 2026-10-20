# pack_028

Block 11958414. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xaf101459153ce41847e50e77c7265bd48e9cbf99717b94a407d62b08fd30fe6e`
- block 11958414, position 66, result success, from `0xdead1241f2ee2a7950ad967993efb72d62bf6822`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 120.000000 ETH, gas used 113217 at 80.0 gwei, fee 0.009057 ETH
- token transfers (Blockscout, decoded):
  - 120.000000 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x0000000000000000000000000000000000000000`
  - 120.000000 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x795065dcc9f64b5614c407a6efdc400da6221fb0`
  - 10292.562367 SUSHI (`0x6b359506`): `0x795065dcc9f64b5614c407a6efdc400da6221fb0` -> `0xdead1241f2ee2a7950ad967993efb72d62bf6822`
- internal ETH transfers (Etherscan):
  - 120.000000 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 120.000000 ETH for `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b3595068778dd592e39a122f4f5a5cf09c90fe2` Transfer
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Sync
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Swap
- receipt status 1, index 66

### Victim leg: `0x80baba3cc271b12de994845a2ab5c90a5e52788b95ac73eee90cc1deaaef9f30`
- block 11958414, position 70, result success, from `0x0000000036deb131f6dcd641e4323a8df22268dd`, to `0x0000000000005117dd3a72e64a705198753fdd54`, value 0.000000 ETH, gas used 312100 at 80.0 gwei, fee 0.024968 ETH
- token transfers (Blockscout, decoded):
  - 447.888434 SUSHI (`0x6b359506`): `0x795065dcc9f64b5614c407a6efdc400da6221fb0` -> `0x0000000000005117dd3a72e64a705198753fdd54`
  - 447.888434 SUSHI (`0x6b359506`): `0x0000000000005117dd3a72e64a705198753fdd54` -> `0x513d5f1df52eb1b70ffe6b89f3685920fc6c5d89`
  - 1569.262348 RUNE (`0x3155ba85`): `0x513d5f1df52eb1b70ffe6b89f3685920fc6c5d89` -> `0x0000000000005117dd3a72e64a705198753fdd54`
  - 1569.262348 RUNE (`0x3155ba85`): `0x0000000000005117dd3a72e64a705198753fdd54` -> `0x8d2a4cc2e2ca0f7ab011b686449dc82c3af924c7`
  - 5.331081 WETH (`0xc02aaa39`): `0x8d2a4cc2e2ca0f7ab011b686449dc82c3af924c7` -> `0x0000000000005117dd3a72e64a705198753fdd54`
  - 5.228879 WETH (`0xc02aaa39`): `0x0000000000005117dd3a72e64a705198753fdd54` -> `0x795065dcc9f64b5614c407a6efdc400da6221fb0`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x0000000000005117dd3a72e64a705198753fdd54` other
  - `0x0000000000005117dd3a72e64a705198753fdd54` other
  - `0x0000000000005117dd3a72e64a705198753fdd54` other
  - `0x0000000000005117dd3a72e64a705198753fdd54` other
  - `0x6b3595068778dd592e39a122f4f5a5cf09c90fe2` Transfer
  - `0x6b3595068778dd592e39a122f4f5a5cf09c90fe2` Transfer
  - `0x6b3595068778dd592e39a122f4f5a5cf09c90fe2` Approval
  - `0x3155ba85d5f96b2d030a4966af206230e46849cb` Transfer
  - `0x513d5f1df52eb1b70ffe6b89f3685920fc6c5d89` UniswapV2 Sync
  - `0x513d5f1df52eb1b70ffe6b89f3685920fc6c5d89` UniswapV2 Swap
  - `0x3155ba85d5f96b2d030a4966af206230e46849cb` Transfer
  - `0x3155ba85d5f96b2d030a4966af206230e46849cb` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8d2a4cc2e2ca0f7ab011b686449dc82c3af924c7` UniswapV2 Sync
  - `0x8d2a4cc2e2ca0f7ab011b686449dc82c3af924c7` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Sync
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Swap
- receipt status 1, index 70

### Back leg: `0x04dbd083482a31e1b2b92be315d46ab79b9126ff266b0ce78896120afab9ed87`
- block 11958414, position 98, result success, from `0xdead1241f2ee2a7950ad967993efb72d62bf6822`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 60.000000 ETH, gas used 98217 at 80.0 gwei, fee 0.007857 ETH
- token transfers (Blockscout, decoded):
  - 60.000000 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x0000000000000000000000000000000000000000`
  - 60.000000 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x795065dcc9f64b5614c407a6efdc400da6221fb0`
  - 5127.933609 SUSHI (`0x6b359506`): `0x795065dcc9f64b5614c407a6efdc400da6221fb0` -> `0xdead1241f2ee2a7950ad967993efb72d62bf6822`
- internal ETH transfers (Etherscan):
  - 60.000000 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 60.000000 ETH for `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b3595068778dd592e39a122f4f5a5cf09c90fe2` Transfer
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Sync
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Swap
- receipt status 1, index 98
