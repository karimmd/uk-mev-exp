# pack_199

Block 11250982. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xd3b9c7bafb46214184e4ebee298ff1cb0b6c115ac338197b257f81af19802625`
- block 11250982, position 0, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x00bf034cec51975faece51b285724301436b21c4`, value 0.000000 ETH, gas used 90145 at 476.4 gwei, fee 0.042948 ETH
- token transfers (Blockscout, decoded):
  - 20.000000 WETH (`0xc02aaa39`): `0x00bf034cec51975faece51b285724301436b21c4` -> `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc`
  - 14944.146367 ORO (`0xc3eb2622`): `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` -> `0x00bf034cec51975faece51b285724301436b21c4`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x60479c30cc4027a1e913ae4085da9f1322fa9b6d` -> `0x00bf034cec51975faece51b285724301436b21c4` [self-destruct]
  - 0.000000 ETH: `0x3e9f87b3cd71052a1e967f2671e56ee61d3c2752` -> `0x00bf034cec51975faece51b285724301436b21c4` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc3eb2622190c57429aac3901808994443b64b466` Transfer
  - `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` UniswapV2 Sync
  - `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xf01f278aafda6c85f92e0092699e7e5b7b9d32b47863e5e8a0048c575708267f`
- block 11250982, position 14, result success, from `0x41f4e75a77ca1260a1dc71ca24f76b68da2a0276`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 8.000000 ETH, gas used 113007 at 100.0 gwei, fee 0.011301 ETH
- token transfers (Blockscout, decoded):
  - 8.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 8.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc`
  - 5794.169056 ORO (`0xc3eb2622`): `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` -> `0x41f4e75a77ca1260a1dc71ca24f76b68da2a0276`
- internal ETH transfers (Etherscan):
  - 8.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 8.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc3eb2622190c57429aac3901808994443b64b466` Transfer
  - `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` UniswapV2 Sync
  - `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` UniswapV2 Swap
- receipt status 1, index 14

### Back leg: `0x4cf6d8376f168eedf55aa6933b2d56ec1290819c1d164fb10b23f0b908208122`
- block 11250982, position 15, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x00bf034cec51975faece51b285724301436b21c4`, value 0.000000 ETH, gas used 78907 at 100.0 gwei, fee 0.007891 ETH
- token transfers (Blockscout, decoded):
  - 14944.146367 ORO (`0xc3eb2622`): `0x00bf034cec51975faece51b285724301436b21c4` -> `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc`
  - 20.232048 WETH (`0xc02aaa39`): `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` -> `0x00bf034cec51975faece51b285724301436b21c4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc3eb2622190c57429aac3901808994443b64b466` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` UniswapV2 Sync
  - `0xa89abe11bd3ef4cf68a5004ba99b9fda52d5e8fc` UniswapV2 Swap
- receipt status 1, index 15
