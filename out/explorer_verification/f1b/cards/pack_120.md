# pack_120

Block 11152070. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xa5be47f38f76315d2cc2b954b6da62b41afcb9d10a046ce13308b625eff46770`
- block 11152070, position 161, result success, from `0xe104053d23918cf2787883508834661c138c9f61`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 115765 at 103.0 gwei, fee 0.011924 ETH
- token transfers (Blockscout, decoded):
  - 0.002283 OTEN (`0x061206cf`): `0xe104053d23918cf2787883508834661c138c9f61` -> `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5`
  - 0.100000 WETH (`0xc02aaa39`): `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.100000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.100000 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.100000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe104053d23918cf2787883508834661c138c9f61` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x061206cff531afe9b69f1c82cedd036a15a7c4a9` Transfer
  - `0x061206cff531afe9b69f1c82cedd036a15a7c4a9` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` UniswapV2 Sync
  - `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.100000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 161

### Victim leg: `0xd5b14a445c85a2805317bffeb734901442dbe6268c61a172a23086ee1164a707`
- block 11152070, position 162, result success, from `0xe104053d23918cf2787883508834661c138c9f61`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 115765 at 103.0 gwei, fee 0.011924 ETH
- token transfers (Blockscout, decoded):
  - 0.002296 OTEN (`0x061206cf`): `0xe104053d23918cf2787883508834661c138c9f61` -> `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5`
  - 0.100000 WETH (`0xc02aaa39`): `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.100000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.100000 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.100000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe104053d23918cf2787883508834661c138c9f61` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x061206cff531afe9b69f1c82cedd036a15a7c4a9` Transfer
  - `0x061206cff531afe9b69f1c82cedd036a15a7c4a9` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` UniswapV2 Sync
  - `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.100000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 162

### Back leg: `0x3497ab374a5c5257de870453f36f6be00b72832fd19d30e02c11800626cfbc36`
- block 11152070, position 168, result success, from `0xe104053d23918cf2787883508834661c138c9f61`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 115765 at 103.0 gwei, fee 0.011924 ETH
- token transfers (Blockscout, decoded):
  - 0.002363 OTEN (`0x061206cf`): `0xe104053d23918cf2787883508834661c138c9f61` -> `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5`
  - 0.100000 WETH (`0xc02aaa39`): `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.100000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.100000 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.100000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe104053d23918cf2787883508834661c138c9f61` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x061206cff531afe9b69f1c82cedd036a15a7c4a9` Transfer
  - `0x061206cff531afe9b69f1c82cedd036a15a7c4a9` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` UniswapV2 Sync
  - `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.100000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 168
