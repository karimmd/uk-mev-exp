# pack_145

Block 12890950. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x4d4630b393a59e8ea073a6103f531748c5ab55927d9955ec3c67385a0abdabed`
- block 12890950, position 45, result success, from `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000309 ETH, gas used 183856 at 21.0 gwei, fee 0.003861 ETH
- token transfers (Blockscout, decoded):
  - 0.000307 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.000307 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe9bd6ddc2b13f46715382f74534950e004399d10`
  - 9.015643 DOGIRA (`0x4b86e029`): `0xe9bd6ddc2b13f46715382f74534950e004399d10` -> `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4`
- internal ETH transfers (Etherscan):
  - 0.000307 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000002 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.000307 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4b86e0295e7d32433ffa6411b82b4f4e56a581e1` other
  - `0x4b86e0295e7d32433ffa6411b82b4f4e56a581e1` Transfer
  - `0xe9bd6ddc2b13f46715382f74534950e004399d10` UniswapV2 Sync
  - `0xe9bd6ddc2b13f46715382f74534950e004399d10` UniswapV2 Swap
- receipt status 1, index 45

### Victim leg: `0x20edc46b01c2d3f0cc3b83c5b5e88841e259f319d53af831536cf5a58e6e5ecd`
- block 12890950, position 48, result success, from `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000309 ETH, gas used 173440 at 21.0 gwei, fee 0.003642 ETH
- token transfers (Blockscout, decoded):
  - 0.000307 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.000307 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe9bd6ddc2b13f46715382f74534950e004399d10`
  - 9.015643 DOGIRA (`0x4b86e029`): `0xe9bd6ddc2b13f46715382f74534950e004399d10` -> `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4`
- internal ETH transfers (Etherscan):
  - 0.000307 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000002 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.000307 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4b86e0295e7d32433ffa6411b82b4f4e56a581e1` other
  - `0x4b86e0295e7d32433ffa6411b82b4f4e56a581e1` Transfer
  - `0xe9bd6ddc2b13f46715382f74534950e004399d10` UniswapV2 Sync
  - `0xe9bd6ddc2b13f46715382f74534950e004399d10` UniswapV2 Swap
- receipt status 1, index 48

### Back leg: `0x5487f3d1e9237ee1ca43d8cf6ce39a20b62b5525612c48239efa5f33ac6820a6`
- block 12890950, position 51, result success, from `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000309 ETH, gas used 145288 at 21.0 gwei, fee 0.003051 ETH
- token transfers (Blockscout, decoded):
  - 0.000307 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.000307 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe9bd6ddc2b13f46715382f74534950e004399d10`
  - 9.015643 DOGIRA (`0x4b86e029`): `0xe9bd6ddc2b13f46715382f74534950e004399d10` -> `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4`
- internal ETH transfers (Etherscan):
  - 0.000307 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000002 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x68e8924bbfc74c479bccd4107d0f80209c6c2cc4` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.000307 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4b86e0295e7d32433ffa6411b82b4f4e56a581e1` other
  - `0x4b86e0295e7d32433ffa6411b82b4f4e56a581e1` other
  - `0x4b86e0295e7d32433ffa6411b82b4f4e56a581e1` Transfer
  - `0xe9bd6ddc2b13f46715382f74534950e004399d10` UniswapV2 Sync
  - `0xe9bd6ddc2b13f46715382f74534950e004399d10` UniswapV2 Swap
- receipt status 1, index 51
