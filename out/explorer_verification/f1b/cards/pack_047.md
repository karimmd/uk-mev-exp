# pack_047

Block 12103790. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x861d72fa096660d3542cde87377357f6cdf8fb89fdcf58adafc32d4f4877115d`
- block 12103790, position 74, result success, from `0xc005f9dd90fe94ee5f45ba1d879f88e2d4c2c2f6`, to `0x51acf0af77adcb20de482e1cd678f620baf07e0c`, value 0.000000 ETH, gas used 173092 at 286.0 gwei, fee 0.049504 ETH
- token transfers (Blockscout, decoded):
  - 6.750000 WETH (`0xc02aaa39`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x0000000000000000000000000000000000000000`
  - 6.750000 WETH (`0xc02aaa39`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x9c4cc862f51b1ba90485de3502aa058ca4331f32`
  - 2072.583500 CELL (`0x26c8afbb`): `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - 4.000000 CHI (`0x00000000`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 6.750000 ETH: `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000000 ETH: `0x89c6bf8569d724a6fc377ec5afb3e5411f665a8b` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xea1e57a119a5ff49697c84be9299c3cdfa9fcc6b` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x7c8f5c6595b2911f96cd7551a50b32b1d3b05763` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xffe590485864744acc2c43498aa9f8e3ba28c0ea` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 6.750000 ETH for `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x26c8afbbfe1ebaca03c2bb082e69d0476bffe099` Transfer
  - `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` UniswapV2 Sync
  - `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` UniswapV2 Swap
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Transfer
- receipt status 1, index 74

### Victim leg: `0x6d90f87f1d500369ddf2b0041b0ed1b33dbf83b46dfe45c56f6f4f07a789001a`
- block 12103790, position 76, result success, from `0x042428b3e98d8d90f416105dd28fc09d0dd2f4ca`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 143720 at 286.0 gwei, fee 0.041104 ETH
- token transfers (Blockscout, decoded):
  - 250000.000000 JUP (`0x4b1e80ca`): `0x042428b3e98d8d90f416105dd28fc09d0dd2f4ca` -> `0x2dfee82f4250dd3f3c6811c5d2926ede8b37a7d5`
  - 13.130906 WETH (`0xc02aaa39`): `0x2dfee82f4250dd3f3c6811c5d2926ede8b37a7d5` -> `0x9c4cc862f51b1ba90485de3502aa058ca4331f32`
  - 3980.111667 CELL (`0x26c8afbb`): `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` -> `0x042428b3e98d8d90f416105dd28fc09d0dd2f4ca`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x4b1e80cac91e2216eeb63e29b957eb91ae9c2be8` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2dfee82f4250dd3f3c6811c5d2926ede8b37a7d5` UniswapV2 Sync
  - `0x2dfee82f4250dd3f3c6811c5d2926ede8b37a7d5` UniswapV2 Swap
  - `0x26c8afbbfe1ebaca03c2bb082e69d0476bffe099` Transfer
  - `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` UniswapV2 Sync
  - `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` UniswapV2 Swap
- receipt status 1, index 76

### Back leg: `0x273220fa4869b4ed3c6b93ade77c79ba232e606e97b7d4495a88b5e8f76c7b94`
- block 12103790, position 77, result success, from `0xc005f9dd90fe94ee5f45ba1d879f88e2d4c2c2f6`, to `0x51acf0af77adcb20de482e1cd678f620baf07e0c`, value 0.000000 ETH, gas used 106744 at 286.0 gwei, fee 0.030529 ETH
- token transfers (Blockscout, decoded):
  - 2072.583500 CELL (`0x26c8afbb`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x9c4cc862f51b1ba90485de3502aa058ca4331f32`
  - 6.824708 WETH (`0xc02aaa39`): `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - 6.824708 WETH (`0xc02aaa39`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 6.824708 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x26c8afbbfe1ebaca03c2bb082e69d0476bffe099` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` UniswapV2 Sync
  - `0x9c4cc862f51b1ba90485de3502aa058ca4331f32` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 6.824708 ETH for `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
- receipt status 1, index 77
