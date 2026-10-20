# pack_014

Block 12039638. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xc2a2d49826cb5a963b2dd13c33c8056a3facc8a72aad826a079e3b01d997d608`
- block 12039638, position 0, result success, from `0x86254cb5a96c161e503d3255d67fdddec056fefe`, to `0xc6e6dd6a0c61651d1bc055dc1c22418a729d41bb`, value 0.000000 ETH, gas used 61459 at 4730.4 gwei, fee 0.290728 ETH
- token transfers (Blockscout, decoded):
  - 16.530000 WETH (`0xc02aaa39`): `0xc6e6dd6a0c61651d1bc055dc1c22418a729d41bb` -> `0x51c1d5cdf10dda49219054920c22c8d4a23eed89`
  - 2478058.296219 LX (`0xcf3c8be2`): `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` -> `0xc6e6dd6a0c61651d1bc055dc1c22418a729d41bb`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xaf692ba8792945d9f3dfeb5ccb8add7a33655bb6` -> `0xc6e6dd6a0c61651d1bc055dc1c22418a729d41bb` [self-destruct]
  - 0.000000 ETH: `0x53eea33a28fdb05c221c18bb7ecbebb383e5fe7a` -> `0xc6e6dd6a0c61651d1bc055dc1c22418a729d41bb` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcf3c8be2e2c42331da80ef210e9b1b307c03d36a` Transfer
  - `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` UniswapV2 Sync
  - `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x87efbf9b884a35c45d9850228ada87b76a27ca80441704ddfed381c558134afd`
- block 12039638, position 130, result success, from `0x298c5fcaa68d18caf1c28ac42047eca8d59c1416`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 8.515764 ETH, gas used 114253 at 143.0 gwei, fee 0.016338 ETH
- token transfers (Blockscout, decoded):
  - 8.515764 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 8.515764 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x51c1d5cdf10dda49219054920c22c8d4a23eed89`
  - 1151689.584070 LX (`0xcf3c8be2`): `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` -> `0x298c5fcaa68d18caf1c28ac42047eca8d59c1416`
- internal ETH transfers (Etherscan):
  - 8.515764 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 8.515764 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcf3c8be2e2c42331da80ef210e9b1b307c03d36a` Transfer
  - `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` UniswapV2 Sync
  - `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` UniswapV2 Swap
- receipt status 1, index 130

### Back leg: `0x475caaca5cb2853c668fe65b0948c422fd6224dbdc82b459f76147458352a557`
- block 12039638, position 131, result success, from `0xb27179fb6d0412f0ec9873baf26dae3457c5494a`, to `0xc6e6dd6a0c61651d1bc055dc1c22418a729d41bb`, value 0.000000 ETH, gas used 98339 at 143.0 gwei, fee 0.014062 ETH
- token transfers (Blockscout, decoded):
  - 2478058.296219 LX (`0xcf3c8be2`): `0xc6e6dd6a0c61651d1bc055dc1c22418a729d41bb` -> `0x51c1d5cdf10dda49219054920c22c8d4a23eed89`
  - 17.547831 WETH (`0xc02aaa39`): `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` -> `0xc6e6dd6a0c61651d1bc055dc1c22418a729d41bb`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xcf3c8be2e2c42331da80ef210e9b1b307c03d36a` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` UniswapV2 Sync
  - `0x51c1d5cdf10dda49219054920c22c8d4a23eed89` UniswapV2 Swap
- receipt status 1, index 131
