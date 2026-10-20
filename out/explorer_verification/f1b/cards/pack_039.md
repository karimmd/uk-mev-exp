# pack_039

Block 10618174. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x3f5669dddbaa8df1299125c6b8601e9db41953b0b2bb6fa5185b57e1c3656046`
- block 10618174, position 60, result success, from `0x726cdc837384a7deb8bbea64beba2e7b4d7346c0`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.020100 ETH, gas used 110838 at 69.0 gwei, fee 0.007648 ETH
- token transfers (Blockscout, decoded):
  - 0.020100 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.020100 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 7.457245 DAI (`0x6b175474`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0x726cdc837384a7deb8bbea64beba2e7b4d7346c0`
- internal ETH transfers (Etherscan):
  - 0.020100 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.020100 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
- receipt status 1, index 60

### Victim leg: `0x0e3a80c963cee8d8e9458d7e71b841e0bfc2e365f9b6d79f21f66df06475dd9d`
- block 10618174, position 63, result success, from `0x726cdc837384a7deb8bbea64beba2e7b4d7346c0`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.023100 ETH, gas used 98822 at 72.0 gwei, fee 0.007115 ETH
- token transfers (Blockscout, decoded):
  - 0.023100 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.023100 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 8.570195 DAI (`0x6b175474`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0x726cdc837384a7deb8bbea64beba2e7b4d7346c0`
- internal ETH transfers (Etherscan):
  - 0.023100 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.023100 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
- receipt status 1, index 63

### Back leg: `0x67e1f09398af9c38e3de016118357c40d152b110a70ffc0c44e59f9441fd14d2`
- block 10618174, position 67, result success, from `0x726cdc837384a7deb8bbea64beba2e7b4d7346c0`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.027100 ETH, gas used 98822 at 76.0 gwei, fee 0.007510 ETH
- token transfers (Blockscout, decoded):
  - 0.027100 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.027100 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 10.054080 DAI (`0x6b175474`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0x726cdc837384a7deb8bbea64beba2e7b4d7346c0`
- internal ETH transfers (Etherscan):
  - 0.027100 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.027100 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
- receipt status 1, index 67
