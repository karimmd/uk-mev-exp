# pack_170

Block 11306334. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x194314e997cf876b370fb1be36a9ab95f1cf0f510249158fa33d11e86270a5ae`
- block 11306334, position 14, result success, from `0x6b8b20166e61b46e9e73e217568b6a88974c6c7a`, to `0x3f2a2b2729f624bd23f252f46bae42628d822a6e`, value 0.000000 ETH, gas used 65103 at 59.0 gwei, fee 0.003841 ETH
- token transfers (Blockscout, decoded):
  - 28.893796 WETH (`0xc02aaa39`): `0x3f2a2b2729f624bd23f252f46bae42628d822a6e` -> `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22`
  - 189.368585 CP3R (`0x7ef1081e`): `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` -> `0x3f2a2b2729f624bd23f252f46bae42628d822a6e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7ef1081ecc8b5b5b130656a41d4ce4f89dbbcc8c` Transfer
  - `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` UniswapV2 Sync
  - `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` UniswapV2 Swap
- receipt status 1, index 14

### Victim leg: `0x4ecb6b630069e00031914eba57be52e053cd14e577731565ca2ce77bfce83835`
- block 11306334, position 47, result success, from `0x32403efc9e1eb347523e484396415c3e46003588`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 8.255370 ETH, gas used 112809 at 52.0 gwei, fee 0.005866 ETH
- token transfers (Blockscout, decoded):
  - 8.255370 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 8.255370 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22`
  - 47.216379 CP3R (`0x7ef1081e`): `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` -> `0x32403efc9e1eb347523e484396415c3e46003588`
- internal ETH transfers (Etherscan):
  - 8.255370 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 8.255370 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7ef1081ecc8b5b5b130656a41d4ce4f89dbbcc8c` Transfer
  - `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` UniswapV2 Sync
  - `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` UniswapV2 Swap
- receipt status 1, index 47

### Back leg: `0xa9d8b33f71b189a104bca4e064f7f4f9e2e42081be6f7273cad15266cd4123a3`
- block 11306334, position 48, result success, from `0xd11b92824332f966fd7ce0ed79cb70136c5858f7`, to `0x3f2a2b2729f624bd23f252f46bae42628d822a6e`, value 0.000000 ETH, gas used 71479 at 52.0 gwei, fee 0.003717 ETH
- token transfers (Blockscout, decoded):
  - 189.368585 CP3R (`0x7ef1081e`): `0x3f2a2b2729f624bd23f252f46bae42628d822a6e` -> `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22`
  - 31.595595 WETH (`0xc02aaa39`): `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` -> `0x3f2a2b2729f624bd23f252f46bae42628d822a6e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x7ef1081ecc8b5b5b130656a41d4ce4f89dbbcc8c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` UniswapV2 Sync
  - `0xbc6b3dc17e86c8cacf0f384f2e19468c36154a22` UniswapV2 Swap
- receipt status 1, index 48
