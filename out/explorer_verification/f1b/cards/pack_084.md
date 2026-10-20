# pack_084

Block 10608054. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x52633f9d13efdf6130365a3689c3b68ffd5c5a3145e20040ddf1f5e98db15550`
- block 10608054, position 74, result success, from `0xb3d8ab962cba81b923d9f4dcb56864e1d0e20a4e`, to `0xf0ff36954b81e6bf8dc9e70046a26cf49a03ec9e`, value 0.000000 ETH, gas used 106810 at 54.0 gwei, fee 0.005768 ETH
- token transfers (Blockscout, decoded):
  - 3622.000000 XIO (`0x0f7f9616`): `0xf0ff36954b81e6bf8dc9e70046a26cf49a03ec9e` -> `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf`
  - 6.119153 WETH (`0xc02aaa39`): `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` -> `0xf0ff36954b81e6bf8dc9e70046a26cf49a03ec9e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x0f7f961648ae6db43c75663ac7e5414eb79b5704` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` UniswapV2 Sync
  - `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` UniswapV2 Swap
- receipt status 1, index 74

### Victim leg: `0xb17acf0789d3d4d2a2fec0bbbf836e883d679af4b7408c72af0348e73e655a51`
- block 10608054, position 78, result success, from `0x17e5d2907b839ced19a5077e654c010781addca2`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 117163 at 53.9 gwei, fee 0.006315 ETH
- token transfers (Blockscout, decoded):
  - 25000.089482 XIO (`0x0f7f9616`): `0x17e5d2907b839ced19a5077e654c010781addca2` -> `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf`
  - 41.413347 WETH (`0xc02aaa39`): `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 41.413347 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 41.413347 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 41.413347 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x17e5d2907b839ced19a5077e654c010781addca2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x0f7f961648ae6db43c75663ac7e5414eb79b5704` Transfer
  - `0x0f7f961648ae6db43c75663ac7e5414eb79b5704` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` UniswapV2 Sync
  - `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 41.413347 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 78

### Back leg: `0xcaef8930693e674a0118d087116c46c16ad06ebe4778d277df6c1a8ae8c7a96c`
- block 10608054, position 80, result success, from `0xb3d8ab962cba81b923d9f4dcb56864e1d0e20a4e`, to `0xf0ff36954b81e6bf8dc9e70046a26cf49a03ec9e`, value 0.000000 ETH, gas used 80356 at 53.9 gwei, fee 0.004331 ETH
- token transfers (Blockscout, decoded):
  - 6.119153 WETH (`0xc02aaa39`): `0xf0ff36954b81e6bf8dc9e70046a26cf49a03ec9e` -> `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf`
  - 3726.061985 XIO (`0x0f7f9616`): `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` -> `0xf0ff36954b81e6bf8dc9e70046a26cf49a03ec9e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0f7f961648ae6db43c75663ac7e5414eb79b5704` Transfer
  - `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` UniswapV2 Sync
  - `0xe0cc5afc0ff2c76183416fb8d1a29f6799fb2cdf` UniswapV2 Swap
- receipt status 1, index 80
