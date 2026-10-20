# pack_106

Block 11140806. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x12e96fd1b019b49bd303f4d4e418534e83f4addc6ceef0ff393d1dca88127f2d`
- block 11140806, position 179, result success, from `0x7117791fea7f8da5b10c41a8b3d1c433401c74b7`, to `0xa6c484c80919be6bec5dfe596b54a90c0f6be843`, value 0.000000 ETH, gas used 122292 at 23.1 gwei, fee 0.002825 ETH
- token transfers (Blockscout, decoded):
  - 0.061713 WETH (`0xc02aaa39`): `0xa6c484c80919be6bec5dfe596b54a90c0f6be843` -> `0xe211637a32d526b2bdbb3d61f0c98869ad73c666`
  - 31.537692 X10 (`0xca18228a`): `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` -> `0x0000000000000000000000000000000000000000`
  - 1450.733835 X10 (`0xca18228a`): `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` -> `0xa6c484c80919be6bec5dfe596b54a90c0f6be843`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xca18228a825145cfd342e1bc83ed1559052b4ec6` Transfer
  - `0xca18228a825145cfd342e1bc83ed1559052b4ec6` Transfer
  - `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` UniswapV2 Sync
  - `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` UniswapV2 Swap
- receipt status 1, index 179

### Victim leg: `0xfa418feb915a8fe24eae7a94ff0c7610e2534e873cbeb1c8d980c72a5e56b263`
- block 11140806, position 180, result success, from `0xbbe167e5c3379de355430dc168d098d7fdcbd2d3`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.139901 ETH, gas used 133027 at 23.1 gwei, fee 0.003073 ETH
- token transfers (Blockscout, decoded):
  - 0.139750 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.139750 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe211637a32d526b2bdbb3d61f0c98869ad73c666`
  - 185.848822 X10 (`0xca18228a`): `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` -> `0x0000000000000000000000000000000000000000`
  - 2416.034680 X10 (`0xca18228a`): `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` -> `0xbbe167e5c3379de355430dc168d098d7fdcbd2d3`
- internal ETH transfers (Etherscan):
  - 0.139750 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000151 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xbbe167e5c3379de355430dc168d098d7fdcbd2d3` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.139750 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xca18228a825145cfd342e1bc83ed1559052b4ec6` Transfer
  - `0xca18228a825145cfd342e1bc83ed1559052b4ec6` Transfer
  - `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` UniswapV2 Sync
  - `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` UniswapV2 Swap
- receipt status 1, index 180

### Back leg: `0x5973a7f615958a67bb5fcccb133debeb8a065e78e7846bb86a5b33ed9d4a6403`
- block 11140806, position 183, result success, from `0x7117791fea7f8da5b10c41a8b3d1c433401c74b7`, to `0xa6c484c80919be6bec5dfe596b54a90c0f6be843`, value 0.000000 ETH, gas used 99265 at 23.1 gwei, fee 0.002293 ETH
- token transfers (Blockscout, decoded):
  - 18.599152 X10 (`0xca18228a`): `0xa6c484c80919be6bec5dfe596b54a90c0f6be843` -> `0x0000000000000000000000000000000000000000`
  - 1432.134683 X10 (`0xca18228a`): `0xa6c484c80919be6bec5dfe596b54a90c0f6be843` -> `0xe211637a32d526b2bdbb3d61f0c98869ad73c666`
  - 0.082282 WETH (`0xc02aaa39`): `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` -> `0xa6c484c80919be6bec5dfe596b54a90c0f6be843`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xca18228a825145cfd342e1bc83ed1559052b4ec6` Transfer
  - `0xca18228a825145cfd342e1bc83ed1559052b4ec6` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` UniswapV2 Sync
  - `0xe211637a32d526b2bdbb3d61f0c98869ad73c666` UniswapV2 Swap
- receipt status 1, index 183
