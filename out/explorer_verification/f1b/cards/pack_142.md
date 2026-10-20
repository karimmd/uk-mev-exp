# pack_142

Block 12818614. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x373eff4aefc0796ebaf4f6f87d85741c0a09d183542efca355b9f85770cdda9b`
- block 12818614, position 3, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 73129 at 547.7 gwei, fee 0.040054 ETH
- token transfers (Blockscout, decoded):
  - 0.172002 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d`
  - 34394.678763 DRIP (`0x239119c4`): `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x713c9256f50cc85fc1533aa4e9bf21436ae7c09b` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x873220c1e6e7c36be2c81ca41d31e08a401aee97` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x4c039cc43cab35beaea039bd8363d8415b50057d` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x239119c43e3cac84c8a2d45bcba0e46f528e5f77` Transfer
  - `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` UniswapV2 Sync
  - `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x28c15f319267bf885eb816b1db76b9b1bb4e3b14139149a1b01ecdd1dff9beab`
- block 12818614, position 4, result success, from `0x6b0b5260bd86e1f9ceb91c428496a2bf352ee087`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 195069 at 25.0 gwei, fee 0.004877 ETH
- token transfers (Blockscout, decoded):
  - 1000.000000 USDC (`0xa0b86991`): `0x6b0b5260bd86e1f9ceb91c428496a2bf352ee087` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 0.493992 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d`
  - 82174.929980 DRIP (`0x239119c4`): `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` -> `0x6b0b5260bd86e1f9ceb91c428496a2bf352ee087`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0x239119c43e3cac84c8a2d45bcba0e46f528e5f77` Transfer
  - `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` UniswapV2 Sync
  - `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x1e906cdf81994d4817d622069def95180d91adc5937d74bc2b1cc080e62fa27b`
- block 12818614, position 5, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 77661 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 33706.785188 DRIP (`0x239119c4`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d`
  - 0.217508 WETH (`0xc02aaa39`): `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x11d5860699ad47c02957c840b9a7dc65a5a1b14a` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x62db30e159dd973782d602d90b7c47bed773f7cd` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x521416d28900bbe88bd62fb5a60f0ee37a25834c` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x239119c43e3cac84c8a2d45bcba0e46f528e5f77` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` UniswapV2 Sync
  - `0xd2efbe4b7da66c152ee1d2f09b274e45fbd0120d` UniswapV2 Swap
- receipt status 1, index 5
