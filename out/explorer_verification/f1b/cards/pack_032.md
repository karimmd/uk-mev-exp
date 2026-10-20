# pack_032

Block 13702750. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xad33ffdb4ad39200374daf71e033de2b34c512826d640295013d37f5186671d6`
- block 13702750, position 102, result success, from `0x5aa17fc7f2950eca85376c3a8cb1509e8e4b39df`, to `0x01ff6318440f7d5553a82294d78262d5f5084eff`, value 0.000000 ETH, gas used 128567 at 64.9 gwei, fee 0.008342 ETH
- token transfers (Blockscout, decoded):
  - 0.515420 WETH (`0xc02aaa39`): `0x01ff6318440f7d5553a82294d78262d5f5084eff` -> `0x87c6c475f40299e5ce3cba736f613f97e820f101`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfb40e79e56cc7d406707b66c4fd175e07eb2ae3c` Transfer
  - `0x87c6c475f40299e5ce3cba736f613f97e820f101` UniswapV2 Sync
  - `0x87c6c475f40299e5ce3cba736f613f97e820f101` UniswapV2 Swap
- receipt status 1, index 102

### Victim leg: `0xeac17d9dd90752258e2aef932c3a331d3d01752e1ee30beecc5a1540a41e62ea`
- block 13702750, position 103, result success, from `0x84a450d7e780b562d46784650b5cf6074cd8dbcb`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 2.853330 ETH, gas used 134593 at 70.0 gwei, fee 0.009422 ETH
- token transfers (Blockscout, decoded):
  - 2.853330 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 2.853330 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x87c6c475f40299e5ce3cba736f613f97e820f101`
- internal ETH transfers (Etherscan):
  - 2.853330 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 2.853330 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfb40e79e56cc7d406707b66c4fd175e07eb2ae3c` Transfer
  - `0x87c6c475f40299e5ce3cba736f613f97e820f101` UniswapV2 Sync
  - `0x87c6c475f40299e5ce3cba736f613f97e820f101` UniswapV2 Swap
- receipt status 1, index 103

### Back leg: `0x16a31d7edb694e43c75e18350aba3f0f810aac83cdbbb67531487623f3c6a547`
- block 13702750, position 104, result success, from `0x5aa17fc7f2950eca85376c3a8cb1509e8e4b39df`, to `0x01ff6318440f7d5553a82294d78262d5f5084eff`, value 0.000000 ETH, gas used 103782 at 298.3 gwei, fee 0.030956 ETH
- token transfers (Blockscout, decoded):
  - 0.554796 WETH (`0xc02aaa39`): `0x87c6c475f40299e5ce3cba736f613f97e820f101` -> `0x01ff6318440f7d5553a82294d78262d5f5084eff`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xfb40e79e56cc7d406707b66c4fd175e07eb2ae3c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x87c6c475f40299e5ce3cba736f613f97e820f101` UniswapV2 Sync
  - `0x87c6c475f40299e5ce3cba736f613f97e820f101` UniswapV2 Swap
- receipt status 1, index 104
