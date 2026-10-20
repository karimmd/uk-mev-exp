# pack_128

Block 11208302. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xd3b111160f6c2975b16278e15daf2eb038f2062fec5ec3631f5a1d15d30bd756`
- block 11208302, position 31, result success, from `0x470f932c3dd58b1a22197428838687e5809b5e41`, to `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`, value 0.000000 ETH, gas used 122552 at 53.4 gwei, fee 0.006545 ETH
- token transfers (Blockscout, decoded):
  - 11.000000 WETH (`0xc02aaa39`): `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0x0000000000000000000000000000000000000000`
  - 11.000000 WETH (`0xc02aaa39`): `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6`
  - 2765.985300 CEL (`0xaaaebe6f`): `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` -> `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`
- internal ETH transfers (Etherscan):
  - 11.000000 ETH: `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 11.000000 ETH for `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d` Transfer
  - `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` UniswapV2 Sync
  - `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` UniswapV2 Swap
- receipt status 1, index 31

### Victim leg: `0x6192a9a3430495d6e02c9b13fa6e141b03e5a27dde63c3f4b7926685c850c9f6`
- block 11208302, position 33, result success, from `0xc9d86956cff0cab4c9fae35534c7273fd8353646`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 32.771600 ETH, gas used 99458 at 50.9 gwei, fee 0.005060 ETH
- token transfers (Blockscout, decoded):
  - 32.771600 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 32.771600 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6`
  - 8181.232600 CEL (`0xaaaebe6f`): `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` -> `0xc9d86956cff0cab4c9fae35534c7273fd8353646`
- internal ETH transfers (Etherscan):
  - 32.771600 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 32.771600 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d` Transfer
  - `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` UniswapV2 Sync
  - `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` UniswapV2 Swap
- receipt status 1, index 33

### Back leg: `0x8f9610b3f09ba90224f15c1d969f139e903f3aac08b49f33f9bd8aa56d078da5`
- block 11208302, position 34, result success, from `0x470f932c3dd58b1a22197428838687e5809b5e41`, to `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`, value 0.000000 ETH, gas used 103260 at 50.9 gwei, fee 0.005253 ETH
- token transfers (Blockscout, decoded):
  - 2765.985300 CEL (`0xaaaebe6f`): `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6`
  - 11.052961 WETH (`0xc02aaa39`): `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` -> `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`
  - 11.052961 WETH (`0xc02aaa39`): `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 11.052961 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x42d0ba0223700dea8bca7983cc4bf0e000dee772` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` UniswapV2 Sync
  - `0xa5e79baee540f000ef6f23d067cd3ac22c7d9fe6` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 11.052961 ETH for `0x42d0ba0223700dea8bca7983cc4bf0e000dee772`
- receipt status 1, index 34
