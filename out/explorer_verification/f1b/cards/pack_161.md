# pack_161

Block 11453470. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x95297c8c5b697d4787b8d25970b8a4c628b194015d0783cf94589fe9325023e9`
- block 11453470, position 57, result success, from `0xf1971b9c48538b6240fe6d5b647aafda7ef86863`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 91352 at 66.1 gwei, fee 0.006035 ETH
- token transfers (Blockscout, decoded):
  - 41.561861 YLD (`0xdcb01cc4`): `0xf1971b9c48538b6240fe6d5b647aafda7ef86863` -> `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3`
  - 1.677888 WETH (`0xc02aaa39`): `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` -> `0xf1971b9c48538b6240fe6d5b647aafda7ef86863`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdcb01cc464238396e213a6fdd933e36796eaff9f` Transfer
  - `0xdcb01cc464238396e213a6fdd933e36796eaff9f` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` UniswapV2 Sync
  - `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` UniswapV2 Swap
- receipt status 1, index 57

### Victim leg: `0x6ebf1a052c8d3593dd43780735fd6b49e0c54a41b36fb965a8c8c35b6684de14`
- block 11453470, position 68, result success, from `0xbd22896a3c597a57c0eafdf47d3bf1e283110820`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 115835 at 60.0 gwei, fee 0.006950 ETH
- token transfers (Blockscout, decoded):
  - 504.865846 YLD (`0xdcb01cc4`): `0xbd22896a3c597a57c0eafdf47d3bf1e283110820` -> `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3`
  - 19.726986 WETH (`0xc02aaa39`): `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 19.726986 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 19.726986 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 19.726986 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xbd22896a3c597a57c0eafdf47d3bf1e283110820` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xdcb01cc464238396e213a6fdd933e36796eaff9f` Transfer
  - `0xdcb01cc464238396e213a6fdd933e36796eaff9f` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` UniswapV2 Sync
  - `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 19.726986 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 68

### Back leg: `0xef433aba9b528e951bd5a82594aa733edc95b99f2dc2e0cfbdd80bdf68adaaea`
- block 11453470, position 69, result success, from `0xf1971b9c48538b6240fe6d5b647aafda7ef86863`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 71868 at 60.0 gwei, fee 0.004312 ETH
- token transfers (Blockscout, decoded):
  - 1.589026 WETH (`0xc02aaa39`): `0xf1971b9c48538b6240fe6d5b647aafda7ef86863` -> `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3`
  - 41.561861 YLD (`0xdcb01cc4`): `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` -> `0xf1971b9c48538b6240fe6d5b647aafda7ef86863`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdcb01cc464238396e213a6fdd933e36796eaff9f` Transfer
  - `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` UniswapV2 Sync
  - `0x242d289b3eeb6842ce0fcc0d87932402299ae5b3` UniswapV2 Swap
- receipt status 1, index 69
