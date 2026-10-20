# pack_052

Block 13855870. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x7d477724752289892a59ba65f81acfab2c742d80851b6655376d428826995ac0`
- block 13855870, position 3, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 75021 at 85.4 gwei, fee 0.006409 ETH
- token transfers (Blockscout, decoded):
  - 9.577905 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x69b81152c5a8d35a67b32a4d3772795d96cae4da`
  - 84.640407 OHM (`0x64aa3364`): `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` -> `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4`
  - 24.393202 BTRFLY (`0xc0d4ceb2`): `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5` Transfer
  - `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` UniswapV2 Sync
  - `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` UniswapV2 Swap
  - `0xc0d4ceb216b3ba9c3701b291766fdcba977cec3a` Transfer
  - `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` UniswapV2 Sync
  - `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x6b35efa04ef3694780ba108746d13e8d4d3ae31ea131fdfa8cf505cca2e403a9`
- block 13855870, position 4, result success, from `0xd71db81be94cba42a39ad7171b36db67b9b464c6`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 0.000000 ETH, gas used 214732 at 82.6 gwei, fee 0.017735 ETH
- token transfers (Blockscout, decoded):
  - 25000.000000 USDC (`0xa0b86991`): `0xd71db81be94cba42a39ad7171b36db67b9b464c6` -> `0x397ff1542f962076d0bfe58ea045ffa2d347aca0`
  - 6.241531 WETH (`0xc02aaa39`): `0x397ff1542f962076d0bfe58ea045ffa2d347aca0` -> `0x69b81152c5a8d35a67b32a4d3772795d96cae4da`
  - 55.098817 OHM (`0x64aa3364`): `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` -> `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4`
  - 15.512766 BTRFLY (`0xc0d4ceb2`): `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` -> `0xd71db81be94cba42a39ad7171b36db67b9b464c6`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x397ff1542f962076d0bfe58ea045ffa2d347aca0` UniswapV2 Sync
  - `0x397ff1542f962076d0bfe58ea045ffa2d347aca0` UniswapV2 Swap
  - `0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5` Transfer
  - `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` UniswapV2 Sync
  - `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` UniswapV2 Swap
  - `0xc0d4ceb216b3ba9c3701b291766fdcba977cec3a` Transfer
  - `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` UniswapV2 Sync
  - `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x62c499583794887542a27cb36fcc5f9ad9fdb15ac16a6d098184b4f4cec54c23`
- block 13855870, position 5, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 61937 at 466.3 gwei, fee 0.028883 ETH
- token transfers (Blockscout, decoded):
  - 24.393202 BTRFLY (`0xc0d4ceb2`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4`
  - 85.681948 OHM (`0x64aa3364`): `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` -> `0x69b81152c5a8d35a67b32a4d3772795d96cae4da`
  - 9.645623 WETH (`0xc02aaa39`): `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc0d4ceb216b3ba9c3701b291766fdcba977cec3a` Transfer
  - `0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5` Transfer
  - `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` UniswapV2 Sync
  - `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` UniswapV2 Sync
  - `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` UniswapV2 Swap
- receipt status 1, index 5
