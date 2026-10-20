# pack_041

Block 11283102. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x97454c19999ed0275191212e064e8eca668c514411ad3242807569e46bd8ce54`
- block 11283102, position 132, result success, from `0xa21caebd27a296678176ac886735bfd18f875b8f`, to `0x0000000071e801062eb0544403f66176bba42dc0`, value 0.000000 ETH, gas used 60114 at 501.3 gwei, fee 0.030135 ETH
- token transfers (Blockscout, decoded):
  - 38.055664 WETH (`0xc02aaa39`): `0x0000000071e801062eb0544403f66176bba42dc0` -> `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35`
  - 214.508315 YUI (`0x4c10bd19`): `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` -> `0x0000000071e801062eb0544403f66176bba42dc0`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x541acfd6393438361d0801a8a926f07ac78cf03f` -> `0x0000000071e801062eb0544403f66176bba42dc0` [self-destruct]
  - 0.000000 ETH: `0x658e88c9653006c189b669740d0ffd6fa2e27bd9` -> `0x0000000071e801062eb0544403f66176bba42dc0` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4c10bd19688b906665fbd53415f279f34b44ece7` Transfer
  - `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` UniswapV2 Sync
  - `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` UniswapV2 Swap
- receipt status 1, index 132

### Victim leg: `0x7e55c8e27dca583e8233ac8e1cf08726ad799a170dc08ad6d73dcb984d529aae`
- block 11283102, position 211, result success, from `0x1bb7a8053a0a68f056f109db5c0fbb91b58030f3`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 5.588663 ETH, gas used 107977 at 55.5 gwei, fee 0.005998 ETH
- token transfers (Blockscout, decoded):
  - 5.585562 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 5.585562 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35`
  - 25.000000 YUI (`0x4c10bd19`): `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` -> `0x1bb7a8053a0a68f056f109db5c0fbb91b58030f3`
- internal ETH transfers (Etherscan):
  - 5.585562 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.003101 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x1bb7a8053a0a68f056f109db5c0fbb91b58030f3` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 5.585562 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4c10bd19688b906665fbd53415f279f34b44ece7` Transfer
  - `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` UniswapV2 Sync
  - `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` UniswapV2 Swap
- receipt status 1, index 211

### Back leg: `0x7b016ab8d39653b771f381d282b4e9e56da4d3d41a1994786abfeedc6e8fa8e0`
- block 11283102, position 214, result success, from `0x464587ee0cc5185686b29af7856b1d13647e93be`, to `0x0000000071e801062eb0544403f66176bba42dc0`, value 0.000000 ETH, gas used 89730 at 55.5 gwei, fee 0.004985 ETH
- token transfers (Blockscout, decoded):
  - 214.508315 YUI (`0x4c10bd19`): `0x0000000071e801062eb0544403f66176bba42dc0` -> `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35`
  - 39.595972 WETH (`0xc02aaa39`): `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` -> `0x0000000071e801062eb0544403f66176bba42dc0`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x4c10bd19688b906665fbd53415f279f34b44ece7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` UniswapV2 Sync
  - `0x4a39d635581dd0fb39fe0e211c4b03590e44aa35` UniswapV2 Swap
- receipt status 1, index 214
