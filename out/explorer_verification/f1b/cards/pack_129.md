# pack_129

Block 11343382. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x23115bb50bb5505946f43fd6bd69ff95a2bc3b5346d7fd30cd86bcd8bb07bb73`
- block 11343382, position 6, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x00bf034cec51975faece51b285724301436b21c4`, value 0.000000 ETH, gas used 95478 at 42.2 gwei, fee 0.004031 ETH
- token transfers (Blockscout, decoded):
  - 3.240000 WETH (`0xc02aaa39`): `0x00bf034cec51975faece51b285724301436b21c4` -> `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75`
  - 739.094753 RARI (`0xfca59cd8`): `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` -> `0x00bf034cec51975faece51b285724301436b21c4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfca59cd816ab1ead66534d82bc21e7515ce441cf` Transfer
  - `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` UniswapV2 Sync
  - `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` UniswapV2 Swap
- receipt status 1, index 6

### Victim leg: `0xccc3cee411d3af0669f93ad22431a62e60029e9baa50943851dfa011923f5401`
- block 11343382, position 60, result success, from `0x0eb9a7ff5cbf719251989caf1599c1270eafb531`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 4.487021 ETH, gas used 106149 at 20.1 gwei, fee 0.002134 ETH
- token transfers (Blockscout, decoded):
  - 4.486867 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 4.486867 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75`
  - 1000.000000 RARI (`0xfca59cd8`): `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` -> `0x0eb9a7ff5cbf719251989caf1599c1270eafb531`
- internal ETH transfers (Etherscan):
  - 4.486867 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000154 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0eb9a7ff5cbf719251989caf1599c1270eafb531` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 4.486867 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfca59cd816ab1ead66534d82bc21e7515ce441cf` Transfer
  - `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` UniswapV2 Sync
  - `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` UniswapV2 Swap
- receipt status 1, index 60

### Back leg: `0x24906be804b8ebe549c7ec3cefabf7dd606a9c265a3d4b2a966f4d75e4cf58d3`
- block 11343382, position 61, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x00bf034cec51975faece51b285724301436b21c4`, value 0.000000 ETH, gas used 90105 at 20.1 gwei, fee 0.001811 ETH
- token transfers (Blockscout, decoded):
  - 739.094753 RARI (`0xfca59cd8`): `0x00bf034cec51975faece51b285724301436b21c4` -> `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75`
  - 3.308087 WETH (`0xc02aaa39`): `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` -> `0x00bf034cec51975faece51b285724301436b21c4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xfca59cd816ab1ead66534d82bc21e7515ce441cf` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` UniswapV2 Sync
  - `0x86fef14c27c78deaeb4349fd959caa11fc5b5d75` UniswapV2 Swap
- receipt status 1, index 61
