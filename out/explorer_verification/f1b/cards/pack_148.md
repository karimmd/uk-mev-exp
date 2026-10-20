# pack_148

Block 11225902. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x92b762c8d4594f8547e548fc135d4e9dbec0c60c9a6bfe32c9cac42c248e5cbd`
- block 11225902, position 55, result success, from `0xb5c2d8d414ef99b34303496cfa667fc15e71b71a`, to `0xeb46faa47a6a52519839a2e52c7b28a2db17651e`, value 0.000000 ETH, gas used 101225 at 24.0 gwei, fee 0.002429 ETH
- token transfers (Blockscout, decoded):
  - 1.632892 WETH (`0xc02aaa39`): `0xeb46faa47a6a52519839a2e52c7b28a2db17651e` -> `0xc930fedc53a8426203c9203079ca76d49f65b964`
  - 27.925853 RL3R (`0xf771733a`): `0xc930fedc53a8426203c9203079ca76d49f65b964` -> `0xeb46faa47a6a52519839a2e52c7b28a2db17651e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf771733a465441437ecf64ff410e261516c7c5f3` Transfer
  - `0xc930fedc53a8426203c9203079ca76d49f65b964` UniswapV2 Sync
  - `0xc930fedc53a8426203c9203079ca76d49f65b964` UniswapV2 Swap
- receipt status 1, index 55

### Victim leg: `0x93946427be70110eff6844f0d53bcc032e20ddac7862974c26d53cd922e0c4de`
- block 11225902, position 70, result success, from `0x85d130ee8346967b6b738c7356485f9ae90e15b8`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 5.000000 ETH, gas used 112415 at 24.0 gwei, fee 0.002698 ETH
- token transfers (Blockscout, decoded):
  - 5.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 5.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc930fedc53a8426203c9203079ca76d49f65b964`
  - 82.849507 RL3R (`0xf771733a`): `0xc930fedc53a8426203c9203079ca76d49f65b964` -> `0x85d130ee8346967b6b738c7356485f9ae90e15b8`
- internal ETH transfers (Etherscan):
  - 5.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 5.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf771733a465441437ecf64ff410e261516c7c5f3` Transfer
  - `0xc930fedc53a8426203c9203079ca76d49f65b964` UniswapV2 Sync
  - `0xc930fedc53a8426203c9203079ca76d49f65b964` UniswapV2 Swap
- receipt status 1, index 70

### Back leg: `0x4f3a04785fb23bd08d1274b15a34dbdc83dfae6652be2f1ac40a527ac96f5d8f`
- block 11225902, position 72, result success, from `0xb5c2d8d414ef99b34303496cfa667fc15e71b71a`, to `0xeb46faa47a6a52519839a2e52c7b28a2db17651e`, value 0.000000 ETH, gas used 82252 at 24.0 gwei, fee 0.001974 ETH
- token transfers (Blockscout, decoded):
  - 27.925853 RL3R (`0xf771733a`): `0xeb46faa47a6a52519839a2e52c7b28a2db17651e` -> `0xc930fedc53a8426203c9203079ca76d49f65b964`
  - 1.701843 WETH (`0xc02aaa39`): `0xc930fedc53a8426203c9203079ca76d49f65b964` -> `0xeb46faa47a6a52519839a2e52c7b28a2db17651e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xf771733a465441437ecf64ff410e261516c7c5f3` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc930fedc53a8426203c9203079ca76d49f65b964` UniswapV2 Sync
  - `0xc930fedc53a8426203c9203079ca76d49f65b964` UniswapV2 Swap
- receipt status 1, index 72
