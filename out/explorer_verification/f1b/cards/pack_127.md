# pack_127

Block 12264830. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x28978eca2d3ea7292d758effdf1bc16886153e9372a2d24f4d161656fc29318e`
- block 12264830, position 46, result success, from `0x4ef377462b03b650d52140c482394a6703d0d338`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 63.869461 ETH, gas used 99620 at 601.0 gwei, fee 0.059872 ETH
- token transfers (Blockscout, decoded):
  - 63.137389 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - 63.137389 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x795065dcc9f64b5614c407a6efdc400da6221fb0`
  - 10004.000000 SUSHI (`0x6b359506`): `0x795065dcc9f64b5614c407a6efdc400da6221fb0` -> `0x4ef377462b03b650d52140c482394a6703d0d338`
- internal ETH transfers (Etherscan):
  - 63.137389 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.732072 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x4ef377462b03b650d52140c482394a6703d0d338` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 63.137389 ETH for `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b3595068778dd592e39a122f4f5a5cf09c90fe2` Transfer
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Sync
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Swap
- receipt status 1, index 46

### Victim leg: `0x6d3610f545a55f19567d5cc91fc8ca5a193acac96de2923b0ec227b9447d3894`
- block 12264830, position 82, result success, from `0x6e90ae41af1dea6f0006aa7752d9db2cf5e6a49f`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 38.481504 ETH, gas used 116708 at 600.0 gwei, fee 0.070025 ETH
- token transfers (Blockscout, decoded):
  - 37.956675 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - 37.956675 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x795065dcc9f64b5614c407a6efdc400da6221fb0`
  - 6000.000000 SUSHI (`0x6b359506`): `0x795065dcc9f64b5614c407a6efdc400da6221fb0` -> `0x6e90ae41af1dea6f0006aa7752d9db2cf5e6a49f`
- internal ETH transfers (Etherscan):
  - 37.956675 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.524829 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x6e90ae41af1dea6f0006aa7752d9db2cf5e6a49f` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 37.956675 ETH for `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b3595068778dd592e39a122f4f5a5cf09c90fe2` Transfer
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Sync
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Swap
- receipt status 1, index 82

### Back leg: `0x90b114ebec6a38b0672ffe5d449baf35ceb4bce3ee86647414ce2dba493627c8`
- block 12264830, position 86, result success, from `0x4ef377462b03b650d52140c482394a6703d0d338`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 38.481504 ETH, gas used 99620 at 601.0 gwei, fee 0.059872 ETH
- token transfers (Blockscout, decoded):
  - 37.996757 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - 37.996757 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x795065dcc9f64b5614c407a6efdc400da6221fb0`
  - 6000.000000 SUSHI (`0x6b359506`): `0x795065dcc9f64b5614c407a6efdc400da6221fb0` -> `0x4ef377462b03b650d52140c482394a6703d0d338`
- internal ETH transfers (Etherscan):
  - 37.996757 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.484747 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x4ef377462b03b650d52140c482394a6703d0d338` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 37.996757 ETH for `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b3595068778dd592e39a122f4f5a5cf09c90fe2` Transfer
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Sync
  - `0x795065dcc9f64b5614c407a6efdc400da6221fb0` UniswapV2 Swap
- receipt status 1, index 86
