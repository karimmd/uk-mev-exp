# pack_061

Block 13839326. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe005be9bf2616088f7600aaed21b0086ae58a9c160fa999ada4266cb783cdbee`
- block 13839326, position 0, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 75021 at 45.8 gwei, fee 0.003434 ETH
- token transfers (Blockscout, decoded):
  - 4.918250 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x69b81152c5a8d35a67b32a4d3772795d96cae4da`
  - 47.912126 OHM (`0x64aa3364`): `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` -> `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4`
  - 13.260718 BTRFLY (`0xc0d4ceb2`): `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
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
- receipt status 1, index 0

### Victim leg: `0xbdf256e87855fe3908657147a7b14e19b5197c0872a82f3e4639f8e43e41de3e`
- block 13839326, position 1, result success, from `0x00937e2643c5746431e40b96d361c60b00b1f348`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 0.000000 ETH, gas used 75890 at 60.3 gwei, fee 0.004573 ETH
- token transfers (Blockscout, decoded):
  - 50.000000 OHM (`0x64aa3364`): `0x00937e2643c5746431e40b96d361c60b00b1f348` -> `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4`
  - 13.560061 BTRFLY (`0xc0d4ceb2`): `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` -> `0x00937e2643c5746431e40b96d361c60b00b1f348`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5` Transfer
  - `0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5` Approval
  - `0xc0d4ceb216b3ba9c3701b291766fdcba977cec3a` Transfer
  - `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` UniswapV2 Sync
  - `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xea99fddba2bb383471f77bf474c37d6eb8ecb75299e08c8e8073bf7edc2481be`
- block 13839326, position 2, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 61937 at 298.2 gwei, fee 0.018468 ETH
- token transfers (Blockscout, decoded):
  - 13.260718 BTRFLY (`0xc0d4ceb2`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4`
  - 48.617273 OHM (`0x64aa3364`): `0xe9ab8038ee6dd4fcc7612997fe28d4e22019c4b4` -> `0x69b81152c5a8d35a67b32a4d3772795d96cae4da`
  - 4.960720 WETH (`0xc02aaa39`): `0x69b81152c5a8d35a67b32a4d3772795d96cae4da` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
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
- receipt status 1, index 2
