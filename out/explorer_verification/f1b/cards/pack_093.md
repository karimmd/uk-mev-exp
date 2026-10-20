# pack_093

Block 11152070. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x35eca598fba4cdfaadd838af7705d8c9a4d8f2ae66a23b0541550e3c956d7960`
- block 11152070, position 165, result success, from `0xe104053d23918cf2787883508834661c138c9f61`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 115765 at 103.0 gwei, fee 0.011924 ETH
- token transfers (Blockscout, decoded):
  - 0.002336 OTEN (`0x061206cf`): `0xe104053d23918cf2787883508834661c138c9f61` -> `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5`
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
- receipt status 1, index 165

### Victim leg: `0x4dbef2b53576c5952c2867f53848a9123a8ef38cbb288f751edd6ffa96a9ddaa`
- block 11152070, position 169, result success, from `0xe104053d23918cf2787883508834661c138c9f61`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 115765 at 103.0 gwei, fee 0.011924 ETH
- token transfers (Blockscout, decoded):
  - 0.002377 OTEN (`0x061206cf`): `0xe104053d23918cf2787883508834661c138c9f61` -> `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5`
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
- receipt status 1, index 169

### Back leg: `0x8b08298f9b320b9225b1412dc32ce04d90a34737f981e30048adec7745f86eb8`
- block 11152070, position 170, result success, from `0xe104053d23918cf2787883508834661c138c9f61`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 115765 at 103.0 gwei, fee 0.011924 ETH
- token transfers (Blockscout, decoded):
  - 0.002391 OTEN (`0x061206cf`): `0xe104053d23918cf2787883508834661c138c9f61` -> `0x93670adb8f8b3b6802b37a7a511e0e45a6ff93e5`
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
- receipt status 1, index 170
