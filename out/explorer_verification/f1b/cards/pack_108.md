# pack_108

Block 14160966. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x14efeecb25e9c3791fc487f5ae8a6c6a362b5258acf3273d66ca992d1ea66eb3`
- block 14160966, position 4, result success, from `0x75b0bbd46d7752cb2f5ffe645467e0ce6e389795`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 2.380000 ETH, gas used 280976 at 1888.0 gwei, fee 0.530483 ETH
- token transfers (Blockscout, decoded):
  - 2.375039 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 2.375039 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 7480.045437 DAI (`0x6b175474`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b`
  - 12.500000 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc`
  - 2.500000 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0x000000000000000000000000000000000000dead`
  - 235.000000 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0x75b0bbd46d7752cb2f5ffe645467e0ce6e389795`
- internal ETH transfers (Etherscan):
  - 2.375039 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.004961 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x75b0bbd46d7752cb2f5ffe645467e0ce6e389795` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 2.375039 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` UniswapV2 Sync
  - `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` UniswapV2 Swap
- receipt status 1, index 4

### Victim leg: `0xf18963b678ae612a51e65421f0bc460c57315d36700e565245d9aaee2ef893e1`
- block 14160966, position 46, result success, from `0xc66f390f1bac78ff1fdee835e549192de8969c35`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 1.500000 ETH, gas used 264055 at 600.0 gwei, fee 0.158433 ETH
- token transfers (Blockscout, decoded):
  - 1.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 1.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 4702.784086 DAI (`0x6b175474`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b`
  - 5.984046 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc`
  - 1.196809 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0x000000000000000000000000000000000000dead`
  - 112.500065 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0xc66f390f1bac78ff1fdee835e549192de8969c35`
- internal ETH transfers (Etherscan):
  - 1.500000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.500000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` UniswapV2 Sync
  - `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` UniswapV2 Swap
- receipt status 1, index 46

### Back leg: `0x2ae0fd8961a1cd2a0fd764b9152f84d8909fba323818b3b3d2358ba589dc7cff`
- block 14160966, position 48, result success, from `0x2ad4dc274b0965b24c6136b19dec569aa628d8ab`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 1.500000 ETH, gas used 264055 at 600.0 gwei, fee 0.158433 ETH
- token transfers (Blockscout, decoded):
  - 1.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 1.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 4697.170521 DAI (`0x6b175474`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b`
  - 5.595922 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc`
  - 1.119184 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0x000000000000000000000000000000000000dead`
  - 105.203334 SIN (`0x804a4f27`): `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` -> `0x2ad4dc274b0965b24c6136b19dec569aa628d8ab`
- internal ETH transfers (Etherscan):
  - 1.500000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.500000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x804a4f2705f7bd08b1d84ae8698014a18c708dbc` Transfer
  - `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` UniswapV2 Sync
  - `0x39b71cb975280df8f1390c95c4dc861d2c2e7a2b` UniswapV2 Swap
- receipt status 1, index 48
