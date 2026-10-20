# pack_171

Block 11422582. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x6fe0f96027986d1d99d0e2b41c19bcbe4c658924dd0b662fd128d85b7c889eb0`
- block 11422582, position 121, result success, from `0xe64881ba7c41a8615c5f31474dea23d63812087f`, to `0x00c409001c1900ddcda20000008e112417db003b`, value 0.000000 ETH, gas used 267139 at 30.8 gwei, fee 0.008230 ETH
- token transfers (Blockscout, decoded):
  - 0.717853 WETH (`0xc02aaa39`): `0x00c409001c1900ddcda20000008e112417db003b` -> `0x0000000000000000000000000000000000000000`
  - 0.717853 WETH (`0xc02aaa39`): `0x00c409001c1900ddcda20000008e112417db003b` -> `0xc0917d9f473618029bea42dd61b05fcf0251be42`
  - 371.515345 YETI (`0xb4bebd34`): `0xc0917d9f473618029bea42dd61b05fcf0251be42` -> `0x00c409001c1900ddcda20000008e112417db003b`
  - 371.515345 YETI (`0xb4bebd34`): `0x00c409001c1900ddcda20000008e112417db003b` -> `0x4cfa6c06b29a5d3e802b99ea747bc52d79f30942`
  - 0.733925 WETH (`0xc02aaa39`): `0x4cfa6c06b29a5d3e802b99ea747bc52d79f30942` -> `0x00c409001c1900ddcda20000008e112417db003b`
  - 0.733925 WETH (`0xc02aaa39`): `0x00c409001c1900ddcda20000008e112417db003b` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.717853 ETH: `0x00c409001c1900ddcda20000008e112417db003b` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.733925 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x00c409001c1900ddcda20000008e112417db003b` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.717853 ETH for `0x00c409001c1900ddcda20000008e112417db003b`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4bebd34f6daafd808f73de0d10235a92fbb6c3d` Transfer
  - `0xc0917d9f473618029bea42dd61b05fcf0251be42` UniswapV2 Sync
  - `0xc0917d9f473618029bea42dd61b05fcf0251be42` UniswapV2 Swap
  - `0xb4bebd34f6daafd808f73de0d10235a92fbb6c3d` Approval
  - `0x4cfa6c06b29a5d3e802b99ea747bc52d79f30942` other
  - `0x4cfa6c06b29a5d3e802b99ea747bc52d79f30942` other
  - `0xb4bebd34f6daafd808f73de0d10235a92fbb6c3d` Transfer
  - `0xb4bebd34f6daafd808f73de0d10235a92fbb6c3d` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.733925 ETH for `0x00c409001c1900ddcda20000008e112417db003b`
- receipt status 1, index 121

### Victim leg: `0x16d94b40a34f71de73b4b82c3ae1052b3ce519b42157fc0ded6077a62e228e26`
- block 11422582, position 123, result success, from `0xe291cc6ea10fa07135e07ae218dd52709dde2fe1`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 1.000000 ETH, gas used 115463 at 30.8 gwei, fee 0.003557 ETH
- token transfers (Blockscout, decoded):
  - 1.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 1.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc0917d9f473618029bea42dd61b05fcf0251be42`
  - 493.088872 YETI (`0xb4bebd34`): `0xc0917d9f473618029bea42dd61b05fcf0251be42` -> `0xe291cc6ea10fa07135e07ae218dd52709dde2fe1`
- internal ETH transfers (Etherscan):
  - 1.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4bebd34f6daafd808f73de0d10235a92fbb6c3d` Transfer
  - `0xc0917d9f473618029bea42dd61b05fcf0251be42` UniswapV2 Sync
  - `0xc0917d9f473618029bea42dd61b05fcf0251be42` UniswapV2 Swap
- receipt status 1, index 123

### Back leg: `0xfad75bb7a5681f57dd075b157a3b33a051bd16f8dc3dbef6799f7c4f894689fb`
- block 11422582, position 126, result success, from `0x4a2b2b8dcec9a749cad6e1e216c6d7045c288718`, to `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`, value 0.000000 ETH, gas used 271759 at 30.8 gwei, fee 0.008372 ETH
- token transfers (Blockscout, decoded):
  - 1.534156 WETH (`0xc02aaa39`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0x0000000000000000000000000000000000000000`
  - 1.534156 WETH (`0xc02aaa39`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0x4cfa6c06b29a5d3e802b99ea747bc52d79f30942`
  - 772.875486 YETI (`0xb4bebd34`): `0x4cfa6c06b29a5d3e802b99ea747bc52d79f30942` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - 772.875486 YETI (`0xb4bebd34`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0xc0917d9f473618029bea42dd61b05fcf0251be42`
  - 1.534441 WETH (`0xc02aaa39`): `0xc0917d9f473618029bea42dd61b05fcf0251be42` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - 1.534441 WETH (`0xc02aaa39`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 1.534156 ETH: `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 1.534441 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.534156 ETH for `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Approval
  - `0x4cfa6c06b29a5d3e802b99ea747bc52d79f30942` other
  - `0x4cfa6c06b29a5d3e802b99ea747bc52d79f30942` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4bebd34f6daafd808f73de0d10235a92fbb6c3d` Transfer
  - `0xb4bebd34f6daafd808f73de0d10235a92fbb6c3d` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc0917d9f473618029bea42dd61b05fcf0251be42` UniswapV2 Sync
  - `0xc0917d9f473618029bea42dd61b05fcf0251be42` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 1.534441 ETH for `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
- receipt status 1, index 126
