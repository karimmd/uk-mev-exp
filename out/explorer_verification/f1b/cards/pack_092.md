# pack_092

Block 12132566. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x099f6bca12ec0c0c95c328a51f41f359c35393017ec6c1d6ef68181c7f539560`
- block 12132566, position 0, result success, from `0x7d92ad7e1b6ae22c6a43283af3856028cd3d856a`, to `0x86a53c9e32abd3677e38bd0b390f24dd080e6426`, value 0.000000 ETH, gas used 74451 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 10.570436 WETH (`0xc02aaa39`): `0x86a53c9e32abd3677e38bd0b390f24dd080e6426` -> `0x8867f20c1c63baccec7617626254a060eeb0e61e`
  - 18653.127364 PHA (`0x6c5ba916`): `0x8867f20c1c63baccec7617626254a060eeb0e61e` -> `0x86a53c9e32abd3677e38bd0b390f24dd080e6426`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xa7554105df1751a4f19d8325113be77a2ddccc43` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0xc86761e1b1f4f4898484d8e1a28c6f872354fbf2` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0xe38f2a9dadf9ff0125a5dcdbbe9259ca24c532fd` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6c5ba91642f10282b576d91922ae6448c9d52f4e` Transfer
  - `0x8867f20c1c63baccec7617626254a060eeb0e61e` UniswapV2 Sync
  - `0x8867f20c1c63baccec7617626254a060eeb0e61e` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xeb83b59cf9bd0cde7d8c3e6b708568fb203b70a1f510684984e602c6d6e98884`
- block 12132566, position 1, result success, from `0xa91b82084b37b01a7b5fd60160eef7b04302517f`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 146527 at 92.0 gwei, fee 0.013480 ETH
- token transfers (Blockscout, decoded):
  - 100.000000 CRU (`0x32a7c02e`): `0xa91b82084b37b01a7b5fd60160eef7b04302517f` -> `0x469506e58d4d0d7abb476dd5c0a999d46723351f`
  - 4.322538 WETH (`0xc02aaa39`): `0x469506e58d4d0d7abb476dd5c0a999d46723351f` -> `0x8867f20c1c63baccec7617626254a060eeb0e61e`
  - 7369.903162 PHA (`0x6c5ba916`): `0x8867f20c1c63baccec7617626254a060eeb0e61e` -> `0xa91b82084b37b01a7b5fd60160eef7b04302517f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x32a7c02e79c4ea1008dd6564b35f131428673c41` Transfer
  - `0x32a7c02e79c4ea1008dd6564b35f131428673c41` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x469506e58d4d0d7abb476dd5c0a999d46723351f` UniswapV2 Sync
  - `0x469506e58d4d0d7abb476dd5c0a999d46723351f` UniswapV2 Swap
  - `0x6c5ba91642f10282b576d91922ae6448c9d52f4e` Transfer
  - `0x8867f20c1c63baccec7617626254a060eeb0e61e` UniswapV2 Sync
  - `0x8867f20c1c63baccec7617626254a060eeb0e61e` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x030d66f67565ba3c9788e5a4f35448163b727121db57c79f77349ea5a9f2f0db`
- block 12132566, position 2, result success, from `0x7d92ad7e1b6ae22c6a43283af3856028cd3d856a`, to `0x86a53c9e32abd3677e38bd0b390f24dd080e6426`, value 0.000000 ETH, gas used 70417 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 18653.127364 PHA (`0x6c5ba916`): `0x86a53c9e32abd3677e38bd0b390f24dd080e6426` -> `0x8867f20c1c63baccec7617626254a060eeb0e61e`
  - 10.715240 WETH (`0xc02aaa39`): `0x8867f20c1c63baccec7617626254a060eeb0e61e` -> `0x86a53c9e32abd3677e38bd0b390f24dd080e6426`
  - 0.120141 WETH (`0xc02aaa39`): `0x86a53c9e32abd3677e38bd0b390f24dd080e6426` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x1fc576c5ba1831198713982edc25d6fc54d2c6d1` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x0b0ee31b5cef4074bfd27544b87b1f7b0b7db03c` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.120141 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x86a53c9e32abd3677e38bd0b390f24dd080e6426` [call]
  - 0.120141 ETH: `0x86a53c9e32abd3677e38bd0b390f24dd080e6426` -> `0xd224ca0c819e8e97ba0136b3b95ceff503b79f53` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x6c5ba91642f10282b576d91922ae6448c9d52f4e` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8867f20c1c63baccec7617626254a060eeb0e61e` UniswapV2 Sync
  - `0x8867f20c1c63baccec7617626254a060eeb0e61e` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.120141 ETH for `0x86a53c9e32abd3677e38bd0b390f24dd080e6426`
- receipt status 1, index 2
