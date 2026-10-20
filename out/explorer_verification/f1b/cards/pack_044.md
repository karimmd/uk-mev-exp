# pack_044

Block 12498646. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x81bb169777b688c080c5ad0bf94afc209f7c243f1d756eb16ea29dcc033ca27e`
- block 12498646, position 162, result success, from `0xa2f21e340890408625c27a37aabbc8ccf51b727f`, to `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533`, value 0.000000 ETH, gas used 156534 at 106.0 gwei, fee 0.016593 ETH
- token transfers (Blockscout, decoded):
  - 0.740000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533`
  - 0.740000 WETH (`0xc02aaa39`): `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533` -> `0x03a6947837d25c4d060fc6b78c0277b67a6adc40`
  - 19252978868.595230 SCOOINU (`0x354ff53d`): `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` -> `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533`
- internal ETH transfers (Etherscan):
  - 0.740000 ETH: `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.740000 ETH for `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x354ff53d243e59483fb939072304562dc34f018d` Transfer
  - `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` UniswapV2 Sync
  - `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` UniswapV2 Swap
- receipt status 1, index 162

### Victim leg: `0x64aa045603e63ef3b88efb0a2a920b91c264e8bba3a6f61663c84a96a59809c5`
- block 12498646, position 165, result success, from `0xc606d66ab3e7a21bf8b325bfcd15c250cf8e1dc4`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 181786 at 106.0 gwei, fee 0.019269 ETH
- token transfers (Blockscout, decoded):
  - 2000.000000 USDT (`0xdac17f95`): `0xc606d66ab3e7a21bf8b325bfcd15c250cf8e1dc4` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 0.773244 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x03a6947837d25c4d060fc6b78c0277b67a6adc40`
  - 15287575757.875160 SCOOINU (`0x354ff53d`): `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` -> `0xc606d66ab3e7a21bf8b325bfcd15c250cf8e1dc4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x354ff53d243e59483fb939072304562dc34f018d` Transfer
  - `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` UniswapV2 Sync
  - `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` UniswapV2 Swap
- receipt status 1, index 165

### Back leg: `0xb704effc0d26f04a65ba805c074eeb5d1668d18f798667d7fa9339810e406995`
- block 12498646, position 168, result success, from `0xa2f21e340890408625c27a37aabbc8ccf51b727f`, to `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533`, value 0.000000 ETH, gas used 124042 at 106.0 gwei, fee 0.013148 ETH
- token transfers (Blockscout, decoded):
  - 18881226528.392124 SCOOINU (`0x354ff53d`): `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533` -> `0x03a6947837d25c4d060fc6b78c0277b67a6adc40`
  - 0.909456 WETH (`0xc02aaa39`): `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` -> `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533`
  - 0.909456 WETH (`0xc02aaa39`): `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.909456 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x354ff53d243e59483fb939072304562dc34f018d` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` UniswapV2 Sync
  - `0x03a6947837d25c4d060fc6b78c0277b67a6adc40` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.909456 ETH for `0xfad95b6089c53a0d1d861eabfaadd8901b0f8533`
- receipt status 1, index 168
