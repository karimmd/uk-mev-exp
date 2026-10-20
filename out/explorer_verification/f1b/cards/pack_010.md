# pack_010

Block 13347494. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x0787ea19b7281f7c39b92475577956a7d92240bed665a9270681e42794118f2f`
- block 13347494, position 1, result success, from `0xcc8efeb2a5f50c81c5d7403676b198ae094b2f3c`, to `0x00000000500e2fece27a7600435d0c48d64e0c00`, value 0.000000 ETH, gas used 87193 at 79.6 gwei, fee 0.006944 ETH
- token transfers (Blockscout, decoded):
  - 1.859508 WETH (`0xc02aaa39`): `0x00000000500e2fece27a7600435d0c48d64e0c00` -> `0x72af4d1d175672d1f99506e68e6e7cff484be4de`
  - 234.177926 ASH (`0x64d91f12`): `0x72af4d1d175672d1f99506e68e6e7cff484be4de` -> `0x00000000500e2fece27a7600435d0c48d64e0c00`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x64d91f12ece7362f91a6f8e7940cd55f05060b92` Transfer
  - `0x72af4d1d175672d1f99506e68e6e7cff484be4de` UniswapV2 Sync
  - `0x72af4d1d175672d1f99506e68e6e7cff484be4de` UniswapV2 Swap
- receipt status 1, index 1

### Victim leg: `0xe21d6f64c8cf2dc2fb72f68b0e327ebf49b309925e3e614a6c8a94cdffe1932d`
- block 13347494, position 3, result success, from `0x5573dc5545462be19bd6b73cc50dc855e53395ac`, to `0x881d40237659c251811cec9c364ef91dc08d300c`, value 0.200000 ETH, gas used 145670 at 81.6 gwei, fee 0.011892 ETH
- token transfers (Blockscout, decoded):
  - 0.198250 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x11111112542d85b3ef69ae05771c2dccff4faa26`
  - 0.198250 WETH (`0xc02aaa39`): `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0x72af4d1d175672d1f99506e68e6e7cff484be4de`
  - 22.191521 ASH (`0x64d91f12`): `0x72af4d1d175672d1f99506e68e6e7cff484be4de` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 22.191521 ASH (`0x64d91f12`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x5573dc5545462be19bd6b73cc50dc855e53395ac`
- internal ETH transfers (Etherscan):
  - 0.200000 ETH: `0x881d40237659c251811cec9c364ef91dc08d300c` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631` [call]
  - 0.198250 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11111112542d85b3ef69ae05771c2dccff4faa26` [call]
  - 0.198250 ETH: `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.001750 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11ededebf63bef0ea2d2d071bdf88f71543ec6fb` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.198250 ETH for `0x11111112542d85b3ef69ae05771c2dccff4faa26`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x64d91f12ece7362f91a6f8e7940cd55f05060b92` Transfer
  - `0x72af4d1d175672d1f99506e68e6e7cff484be4de` UniswapV2 Sync
  - `0x72af4d1d175672d1f99506e68e6e7cff484be4de` UniswapV2 Swap
  - `0x64d91f12ece7362f91a6f8e7940cd55f05060b92` Transfer
  - `0x881d40237659c251811cec9c364ef91dc08d300c` other
- receipt status 1, index 3

### Back leg: `0xfdd68490e07e6d33fe9b9b851cfa19a6450ced696a7c2397c763e4beff8c0ea0`
- block 13347494, position 4, result success, from `0xcc8efeb2a5f50c81c5d7403676b198ae094b2f3c`, to `0x00000000500e2fece27a7600435d0c48d64e0c00`, value 0.000000 ETH, gas used 77124 at 201.8 gwei, fee 0.015563 ETH
- token transfers (Blockscout, decoded):
  - 234.177926 ASH (`0x64d91f12`): `0x00000000500e2fece27a7600435d0c48d64e0c00` -> `0x72af4d1d175672d1f99506e68e6e7cff484be4de`
  - 1.887642 WETH (`0xc02aaa39`): `0x72af4d1d175672d1f99506e68e6e7cff484be4de` -> `0x00000000500e2fece27a7600435d0c48d64e0c00`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x64d91f12ece7362f91a6f8e7940cd55f05060b92` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x72af4d1d175672d1f99506e68e6e7cff484be4de` UniswapV2 Sync
  - `0x72af4d1d175672d1f99506e68e6e7cff484be4de` UniswapV2 Swap
- receipt status 1, index 4
