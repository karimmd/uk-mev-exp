# pack_150

Block 12543350. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x2d6992d057b4f345a037f0a6056c4a44891a0e64fac76fba300886fa4e7c4713`
- block 12543350, position 0, result success, from `0x3376ebc8dce3453a045a145ab7b1e728b2ed581e`, to `0x0000000099cb7fc48a935bceb9f05bbae54e8987`, value 0.000000 ETH, gas used 86000 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 3.268073 WETH (`0xc02aaa39`): `0x0000000099cb7fc48a935bceb9f05bbae54e8987` -> `0x60f6e2200bfef8b4d120028faff4d9a4486526f4`
  - 5923.743951 IONX (`0x02d3a27a`): `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` -> `0x0000000099cb7fc48a935bceb9f05bbae54e8987`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x02d3a27ac3f55d5d91fb0f52759842696a864217` Transfer
  - `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` UniswapV2 Sync
  - `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x6fad8ef2a166b2b889b8b4ddc963f701529060e8c49aecb199703f8b3538a764`
- block 12543350, position 1, result success, from `0x352179f2020d73b77fce1b3c9292fe4d11884b08`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.320000 ETH, gas used 108305 at 46.0 gwei, fee 0.004982 ETH
- token transfers (Blockscout, decoded):
  - 0.320000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.320000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x60f6e2200bfef8b4d120028faff4d9a4486526f4`
  - 522.608922 IONX (`0x02d3a27a`): `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` -> `0x352179f2020d73b77fce1b3c9292fe4d11884b08`
- internal ETH transfers (Etherscan):
  - 0.320000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.320000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x02d3a27ac3f55d5d91fb0f52759842696a864217` Transfer
  - `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` UniswapV2 Sync
  - `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x9a1689ae04eb2bcb845d5947bc1d49b848df7f10329c4def5cf806c75e705bfd`
- block 12543350, position 2, result success, from `0x3376ebc8dce3453a045a145ab7b1e728b2ed581e`, to `0x0000000099cb7fc48a935bceb9f05bbae54e8987`, value 0.000000 ETH, gas used 67923 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 5923.743951 IONX (`0x02d3a27a`): `0x0000000099cb7fc48a935bceb9f05bbae54e8987` -> `0x60f6e2200bfef8b4d120028faff4d9a4486526f4`
  - 3.305701 WETH (`0xc02aaa39`): `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` -> `0x0000000099cb7fc48a935bceb9f05bbae54e8987`
- internal ETH transfers (Etherscan):
  - 0.037253 ETH: `0x0000000099cb7fc48a935bceb9f05bbae54e8987` -> `0x1ad91ee08f21be3de0ba2ba6918e714da6b45836` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x02d3a27ac3f55d5d91fb0f52759842696a864217` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` UniswapV2 Sync
  - `0x60f6e2200bfef8b4d120028faff4d9a4486526f4` UniswapV2 Swap
- receipt status 1, index 2
