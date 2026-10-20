# pack_135

Block 12281550. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xd5a511842909f2efe6903c9a488e3182831aadaa303a42bff2ff1ba02918d5d0`
- block 12281550, position 0, result success, from `0xf6da21e95d74767009accb145b96897ac3630bad`, to `0xd78a3280085ee846196cb5fab7d510b279486d44`, value 0.000000 ETH, gas used 150627 at 1.0 gwei, fee 0.000151 ETH
- token transfers (Blockscout, decoded):
  - 200.000000 WETH (`0xc02aaa39`): `0xf6da21e95d74767009accb145b96897ac3630bad` -> `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff`
  - 15106258.037614 WSHIBA (`0xb475f178`): `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` -> `0xf6da21e95d74767009accb145b96897ac3630bad`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb475f178be3314d7b61a736451f6842b96903076` Transfer
  - `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` UniswapV2 Sync
  - `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xf1a2a6ba2f23cb6a2c5060567ff995e89b4a2eb5362a4c2cd6b0e370d93531f2`
- block 12281550, position 1, result success, from `0x9e0f0ada57d2de32e56e8a76e73e232d165f101b`, to `0x601ce3bb299e4ee04218fdbcd5660d35f777760b`, value 1.030000 ETH, gas used 189270 at 255.0 gwei, fee 0.048264 ETH
- token transfers (Blockscout, decoded):
  - 0.978500 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.978500 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff`
  - 1265.069431 WSHIBA (`0xb475f178`): `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` -> `0x9e0f0ada57d2de32e56e8a76e73e232d165f101b`
  - 0.051500 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.051500 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff`
  - 66.247346 WSHIBA (`0xb475f178`): `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` -> `0xc496d84215d5018f6f53e7f6f12e45c9b5e8e8a9`
- internal ETH transfers (Etherscan):
  - 0.978500 ETH: `0x601ce3bb299e4ee04218fdbcd5660d35f777760b` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.978500 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.051500 ETH: `0x601ce3bb299e4ee04218fdbcd5660d35f777760b` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.051500 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.978500 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb475f178be3314d7b61a736451f6842b96903076` Transfer
  - `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` UniswapV2 Sync
  - `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.051500 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb475f178be3314d7b61a736451f6842b96903076` Transfer
  - `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` UniswapV2 Sync
  - `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x004c9f1671b5fcdf76587b8c3752b63a5280ad1841eee449af2bfa19443d9a86`
- block 12281550, position 3, result success, from `0xf6da21e95d74767009accb145b96897ac3630bad`, to `0xd78a3280085ee846196cb5fab7d510b279486d44`, value 0.000000 ETH, gas used 79278 at 1.0 gwei, fee 0.000079 ETH
- token transfers (Blockscout, decoded):
  - 15106258.037614 WSHIBA (`0xb475f178`): `0xf6da21e95d74767009accb145b96897ac3630bad` -> `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff`
  - 201.008911 WETH (`0xc02aaa39`): `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` -> `0xf6da21e95d74767009accb145b96897ac3630bad`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xb475f178be3314d7b61a736451f6842b96903076` Transfer
  - `0xb475f178be3314d7b61a736451f6842b96903076` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` UniswapV2 Sync
  - `0x0cd898d165aa2f36c5f32ecac67c4c5b713926ff` UniswapV2 Swap
- receipt status 1, index 3
