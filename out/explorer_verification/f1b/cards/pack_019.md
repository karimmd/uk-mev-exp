# pack_019

Block 11974606. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x39a772bef56df611bdd6f686f01e2c2962c671fbf99501089b47442693238857`
- block 11974606, position 177, result success, from `0xc005f9dd90fe94ee5f45ba1d879f88e2d4c2c2f6`, to `0x51acf0af77adcb20de482e1cd678f620baf07e0c`, value 0.000000 ETH, gas used 120091 at 88.0 gwei, fee 0.010568 ETH
- token transfers (Blockscout, decoded):
  - 17.430000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - 17.430000 WETH (`0xc02aaa39`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x7ba9b94127d434182287de708643932ec036d365`
  - 132246.658900 eRSDL (`0x5218e472`): `0x7ba9b94127d434182287de708643932ec036d365` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
- internal ETH transfers (Etherscan):
  - 17.430000 ETH: `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 17.430000 ETH for `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x5218e472cfcfe0b64a064f055b43b4cdc9efd3a6` Transfer
  - `0x7ba9b94127d434182287de708643932ec036d365` UniswapV2 Sync
  - `0x7ba9b94127d434182287de708643932ec036d365` UniswapV2 Swap
- receipt status 1, index 177

### Victim leg: `0xab55f6453126a5380b4e5671a2e1a142f86813041e9840d3a5af60d7f74e4e6e`
- block 11974606, position 189, result success, from `0x174d02de89a11aba1b9c3e79ee6ee44aed756ddd`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 72.200000 ETH, gas used 112633 at 88.0 gwei, fee 0.009912 ETH
- token transfers (Blockscout, decoded):
  - 72.200000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 72.200000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x7ba9b94127d434182287de708643932ec036d365`
  - 532148.308652 eRSDL (`0x5218e472`): `0x7ba9b94127d434182287de708643932ec036d365` -> `0x174d02de89a11aba1b9c3e79ee6ee44aed756ddd`
- internal ETH transfers (Etherscan):
  - 72.200000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 72.200000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x5218e472cfcfe0b64a064f055b43b4cdc9efd3a6` Transfer
  - `0x7ba9b94127d434182287de708643932ec036d365` UniswapV2 Sync
  - `0x7ba9b94127d434182287de708643932ec036d365` UniswapV2 Swap
- receipt status 1, index 189

### Back leg: `0x1f7f03a5acf3d106d4188c22289e89872a29cc5db113eaceb1df335dce7990d3`
- block 11974606, position 194, result success, from `0xc005f9dd90fe94ee5f45ba1d879f88e2d4c2c2f6`, to `0x51acf0af77adcb20de482e1cd678f620baf07e0c`, value 0.000000 ETH, gas used 91005 at 88.0 gwei, fee 0.008008 ETH
- token transfers (Blockscout, decoded):
  - 132246.658900 eRSDL (`0x5218e472`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x7ba9b94127d434182287de708643932ec036d365`
  - 18.066694 WETH (`0xc02aaa39`): `0x7ba9b94127d434182287de708643932ec036d365` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - 18.066694 WETH (`0xc02aaa39`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 18.066694 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x5218e472cfcfe0b64a064f055b43b4cdc9efd3a6` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7ba9b94127d434182287de708643932ec036d365` UniswapV2 Sync
  - `0x7ba9b94127d434182287de708643932ec036d365` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 18.066694 ETH for `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
- receipt status 1, index 194
