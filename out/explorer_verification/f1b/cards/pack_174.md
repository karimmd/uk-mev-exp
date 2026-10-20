# pack_174

Block 12528742. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xd0194676810ad4406b34fb50e64b2187ed603e035622acfa78c70bfab7e7bde5`
- block 12528742, position 0, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 120577 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.501452 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1`
  - 25196703991548.847656 BUGG (`0x1aabf9b5`): `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x6ad73e3f8a99e71d3321f763a1b779d9586759f5` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x46d7f164aaf329cf20ad23869ff245e0fadba171` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xb4f835e2ea1a30a42a2dcd6eda85d20a8abf092c` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1aabf9b575e4329b8c8f272428ad5e43ab4aefc8` Transfer
  - `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` UniswapV2 Sync
  - `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xb64a169afb5b840cb31f4f1168b5383c556f35300d5e2422cfa00460eb2b1514`
- block 12528742, position 1, result success, from `0x9f4116024f862ac16f30aa5517f00af642bf7a9b`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 172909 at 50.0 gwei, fee 0.008645 ETH
- token transfers (Blockscout, decoded):
  - 3000.000000 USDC (`0xa0b86991`): `0x9f4116024f862ac16f30aa5517f00af642bf7a9b` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 1.233119 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1`
  - 55124648364273.187500 BUGG (`0x1aabf9b5`): `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` -> `0x9f4116024f862ac16f30aa5517f00af642bf7a9b`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0x1aabf9b575e4329b8c8f272428ad5e43ab4aefc8` Transfer
  - `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` UniswapV2 Sync
  - `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x4213edf354ee0582fc4c967e24dc7a70bf4db66a14eb1b201927e1a29e94f75e`
- block 12528742, position 2, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.051473 ETH, gas used 119794 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 24693174683592.359375 BUGG (`0x1aabf9b5`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1`
  - 0.563097 WETH (`0xc02aaa39`): `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.051473 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x99c85bb64564d9ef9a99621301f22c9993cb89e3` [call]
  - 0.000000 ETH: `0x0244b4b392279768e0b91711c5b848bd7dfe5fc7` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xe15156ddc3cb6bd4704aa128391b017c570a1061` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x54e7acc746f09caee178d42e699a33f8351d48ba` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x1aabf9b575e4329b8c8f272428ad5e43ab4aefc8` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` UniswapV2 Sync
  - `0x360bb0c0c8451095f65568e77d04b4ee970c6ec1` UniswapV2 Swap
- receipt status 1, index 2
