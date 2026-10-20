# pack_004

Block 10636918. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x040ef5f7838b80dc77ddc76c3db2756a0df22c610aaff22648aeef481f953d97`
- block 10636918, position 1, result success, from `0x51db325b736aabee2b614957ab93b9bb5261f954`, to `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d`, value 0.000000 ETH, gas used 162890 at 432.6 gwei, fee 0.070459 ETH
- token transfers (Blockscout, decoded):
  - 4.422105 WETH (`0xc02aaa39`): `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d` -> `0x0000000000000000000000000000000000000000`
  - 4.422105 WETH (`0xc02aaa39`): `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d` -> `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138`
  - 5429.894650 PLT (`0x9fbfed65`): `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` -> `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d`
  - 3.000000 CHI (`0x00000000`): `0x000000006cc74a85f3bbea90b2b6c453cbed90b3` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 4.422105 ETH: `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000000 ETH: `0x60a4d418e8ea1aaa66b9319c97ed9c6b0b123d0b` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x09de52070582cd2eddf52ec943d2154fb4182d0a` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xea13115abd015e21346b8c5773bf710b6d3d4b2a` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 4.422105 ETH for `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9fbfed658919a896b5dc7b00456ce22d780f9b65` Transfer
  - `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` UniswapV2 Sync
  - `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` UniswapV2 Swap
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Transfer
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Approval
- receipt status 1, index 1

### Victim leg: `0xdec870b57859f70df9dd38abd5b6848472c987cb0f8c609dbf6284b38835dcd6`
- block 10636918, position 125, result success, from `0x27e14bfcaee57e93125d13b0b4dd003a1c952049`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 10.000000 ETH, gas used 112821 at 114.0 gwei, fee 0.012862 ETH
- token transfers (Blockscout, decoded):
  - 10.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 10.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138`
  - 11399.002861 PLT (`0x9fbfed65`): `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` -> `0x27e14bfcaee57e93125d13b0b4dd003a1c952049`
- internal ETH transfers (Etherscan):
  - 10.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 10.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9fbfed658919a896b5dc7b00456ce22d780f9b65` Transfer
  - `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` UniswapV2 Sync
  - `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` UniswapV2 Swap
- receipt status 1, index 125

### Back leg: `0xf23eb15c58bff869ba275989133d34c7d95e7f1f676c2c69c7d9883094c461b9`
- block 10636918, position 127, result success, from `0x51db325b736aabee2b614957ab93b9bb5261f954`, to `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d`, value 0.000000 ETH, gas used 103170 at 114.0 gwei, fee 0.011761 ETH
- token transfers (Blockscout, decoded):
  - 5429.894650 PLT (`0x9fbfed65`): `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d` -> `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138`
  - 4.862404 WETH (`0xc02aaa39`): `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` -> `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d`
  - 4.862404 WETH (`0xc02aaa39`): `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 4.862404 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x9fbfed658919a896b5dc7b00456ce22d780f9b65` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` UniswapV2 Sync
  - `0x504c65569f5ed6a7a8218a526a38c4c9d6a6b138` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 4.862404 ETH for `0xdf1bac82673d6b9a18d9c476fd90bbecf00fce5d`
- receipt status 1, index 127
