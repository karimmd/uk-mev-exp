# pack_087

Block 12351774. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x010733afe13a5ba20b17cc506cdf78eb2030cef5de3d6a6a62afb16f785100a0`
- block 12351774, position 37, result success, from `0xb9ce805e792ac6ab5055054d1a43954b8d1647c9`, to `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`, value 0.000000 ETH, gas used 81989 at 144.1 gwei, fee 0.011814 ETH
- token transfers (Blockscout, decoded):
  - 61603.191854 TRU (`0xf65b5c51`): `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de` -> `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5`
  - 13.726000 WETH (`0xc02aaa39`): `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` -> `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xf65b5c5104c4fafd4b709d9d60a185eae063276c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` UniswapV2 Sync
  - `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` UniswapV2 Swap
- receipt status 1, index 37

### Victim leg: `0x163f23a538a51f443b1ab2b23253efaf50a8f6bba0005fab16803cdce0619047`
- block 12351774, position 64, result success, from `0x793acdce9db7bc3269513652923d543b4818e817`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 117754 at 50.0 gwei, fee 0.005888 ETH
- token transfers (Blockscout, decoded):
  - 47177.952906 TRU (`0xf65b5c51`): `0x793acdce9db7bc3269513652923d543b4818e817` -> `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5`
  - 10.494259 WETH (`0xc02aaa39`): `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 10.494259 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 10.494259 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 10.494259 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x793acdce9db7bc3269513652923d543b4818e817` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xf65b5c5104c4fafd4b709d9d60a185eae063276c` Transfer
  - `0xf65b5c5104c4fafd4b709d9d60a185eae063276c` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` UniswapV2 Sync
  - `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 10.494259 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 64

### Back leg: `0xb899fabb887a812ec99a10821c333da0aa38beeed880d956c37406e5cd53d920`
- block 12351774, position 66, result success, from `0xb9ce805e792ac6ab5055054d1a43954b8d1647c9`, to `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`, value 0.000000 ETH, gas used 75968 at 50.0 gwei, fee 0.003798 ETH
- token transfers (Blockscout, decoded):
  - 13.726000 WETH (`0xc02aaa39`): `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de` -> `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5`
  - 61083.750332 TRU (`0xf65b5c51`): `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` -> `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf65b5c5104c4fafd4b709d9d60a185eae063276c` Transfer
  - `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` UniswapV2 Sync
  - `0x80b4d4e9d88d9f78198c56c5a27f3bacb9a685c5` UniswapV2 Swap
- receipt status 1, index 66
