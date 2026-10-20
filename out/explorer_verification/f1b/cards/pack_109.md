# pack_109

Block 13061142. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x874b90aeae703ca4cde4fc118a0d39ea0658863628e606e067200885348b1fb7`
- block 13061142, position 3, result success, from `0x92b075d33de5b3c6d0b9523057f6d60574bd195d`, to `0x1315c6c26123383a2eb369a53fb72c4b9f227eec`, value 0.000000 ETH, gas used 236151 at 31.2 gwei, fee 0.007379 ETH
- token transfers (Blockscout, decoded):
  - 98.999966 WETH (`0xc02aaa39`): `0x1315c6c26123383a2eb369a53fb72c4b9f227eec` -> `0x454f11d58e27858926d7a4ece8bfea2c33e97b13`
  - 10040.236503 LDO (`0x5a98fcbe`): `0x454f11d58e27858926d7a4ece8bfea2c33e97b13` -> `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a`
  - 22.566343 WETH (`0xc02aaa39`): `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` -> `0x1315c6c26123383a2eb369a53fb72c4b9f227eec`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x5a98fcbea516cf06857215779fd812ca3bef1b32` Transfer
  - `0x454f11d58e27858926d7a4ece8bfea2c33e97b13` UniswapV2 Sync
  - `0x454f11d58e27858926d7a4ece8bfea2c33e97b13` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` UniswapV2 Sync
  - `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x34e034c34c9042e10361963ab8be500bd057a8350ab11288c0c11440659ea4d1`
- block 13061142, position 4, result success, from `0x6c88f2d2432becde5738d44a6786e9a2f3e32532`, to `0x881d40237659c251811cec9c364ef91dc08d300c`, value 0.000000 ETH, gas used 284990 at 34.0 gwei, fee 0.009690 ETH
- token transfers (Blockscout, decoded):
  - 10000.000000 LDO (`0x5a98fcbe`): `0x6c88f2d2432becde5738d44a6786e9a2f3e32532` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 10000.000000 LDO (`0x5a98fcbe`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a`
  - 22.090665 WETH (`0xc02aaa39`): `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` -> `0x11111112542d85b3ef69ae05771c2dccff4faa26`
  - 22.090665 WETH (`0xc02aaa39`): `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 22.090665 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x11111112542d85b3ef69ae05771c2dccff4faa26` [call]
  - 22.090665 ETH: `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631` [call]
  - 0.196671 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11ededebf63bef0ea2d2d071bdf88f71543ec6fb` [call]
  - 21.893994 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x6c88f2d2432becde5738d44a6786e9a2f3e32532` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x5a98fcbea516cf06857215779fd812ca3bef1b32` Transfer
  - `0x5a98fcbea516cf06857215779fd812ca3bef1b32` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` UniswapV2 Sync
  - `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 22.090665 ETH for `0x11111112542d85b3ef69ae05771c2dccff4faa26`
  - `0x881d40237659c251811cec9c364ef91dc08d300c` other
- receipt status 1, index 4

### Back leg: `0xf60208ab73ba2bf8909e471c39102efdb929f6b8e349f03a6324d1b5b5d3a719`
- block 13061142, position 5, result success, from `0x92b075d33de5b3c6d0b9523057f6d60574bd195d`, to `0x1315c6c26123383a2eb369a53fb72c4b9f227eec`, value 0.000000 ETH, gas used 187311 at 31.2 gwei, fee 0.005853 ETH
- token transfers (Blockscout, decoded):
  - 22.566343 WETH (`0xc02aaa39`): `0x1315c6c26123383a2eb369a53fb72c4b9f227eec` -> `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a`
  - 10152.789573 LDO (`0x5a98fcbe`): `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` -> `0x454f11d58e27858926d7a4ece8bfea2c33e97b13`
  - 99.114185 WETH (`0xc02aaa39`): `0x454f11d58e27858926d7a4ece8bfea2c33e97b13` -> `0x1315c6c26123383a2eb369a53fb72c4b9f227eec`
- internal ETH transfers (Etherscan):
  - 0.098101 ETH: `0x1315c6c26123383a2eb369a53fb72c4b9f227eec` -> `0xeea5b82b61424df8020f5fedd81767f2d0d25bfb` [call]
  - 0.104963 ETH: `0x1315c6c26123383a2eb369a53fb72c4b9f227eec` -> `0x92b075d33de5b3c6d0b9523057f6d60574bd195d` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x5a98fcbea516cf06857215779fd812ca3bef1b32` Transfer
  - `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` UniswapV2 Sync
  - `0xc558f600b34a5f69dd2f0d06cb8a88d829b7420a` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x454f11d58e27858926d7a4ece8bfea2c33e97b13` UniswapV2 Sync
  - `0x454f11d58e27858926d7a4ece8bfea2c33e97b13` UniswapV2 Swap
- receipt status 1, index 5
