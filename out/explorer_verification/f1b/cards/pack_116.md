# pack_116

Block 12335230. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xf567670c0b062f4f50e9804ac73d9685502f63964549d2ad45df820e78a3005c`
- block 12335230, position 2, result success, from `0xf6da21e95d74767009accb145b96897ac3630bad`, to `0xd78a3280085ee846196cb5fab7d510b279486d44`, value 0.000000 ETH, gas used 101110 at 1.0 gwei, fee 0.000101 ETH
- token transfers (Blockscout, decoded):
  - 9.000100 WETH (`0xc02aaa39`): `0xf6da21e95d74767009accb145b96897ac3630bad` -> `0xa00d47b4b304792eb07b09233467b690db847c91`
  - 68530.198289 IMX (`0x7b35ce52`): `0xa00d47b4b304792eb07b09233467b690db847c91` -> `0xf6da21e95d74767009accb145b96897ac3630bad`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7b35ce522cb72e4077baeb96cb923a5529764a00` Transfer
  - `0xa00d47b4b304792eb07b09233467b690db847c91` UniswapV2 Sync
  - `0xa00d47b4b304792eb07b09233467b690db847c91` UniswapV2 Swap
- receipt status 1, index 2

### Victim leg: `0x2ac7a1086a637fde14e78243bb1bcc2bd0ac83d0ce8d52c219bcb3df92d841d2`
- block 12335230, position 3, result success, from `0xcd3f877250b0cf8288426dc05cacc5e6e24be245`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.500000 ETH, gas used 113483 at 61.6 gwei, fee 0.006991 ETH
- token transfers (Blockscout, decoded):
  - 0.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xa00d47b4b304792eb07b09233467b690db847c91`
  - 3318.964922 IMX (`0x7b35ce52`): `0xa00d47b4b304792eb07b09233467b690db847c91` -> `0xcd3f877250b0cf8288426dc05cacc5e6e24be245`
- internal ETH transfers (Etherscan):
  - 0.500000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.500000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7b35ce522cb72e4077baeb96cb923a5529764a00` Transfer
  - `0xa00d47b4b304792eb07b09233467b690db847c91` UniswapV2 Sync
  - `0xa00d47b4b304792eb07b09233467b690db847c91` UniswapV2 Swap
- receipt status 1, index 3

### Back leg: `0xd51de22236e47d41324f13fee1ad33771ff3933cee2737649b3a4923753979f1`
- block 12335230, position 5, result success, from `0xf6da21e95d74767009accb145b96897ac3630bad`, to `0xd78a3280085ee846196cb5fab7d510b279486d44`, value 0.000000 ETH, gas used 73767 at 1.0 gwei, fee 0.000074 ETH
- token transfers (Blockscout, decoded):
  - 68530.198289 IMX (`0x7b35ce52`): `0xf6da21e95d74767009accb145b96897ac3630bad` -> `0xa00d47b4b304792eb07b09233467b690db847c91`
  - 9.067183 WETH (`0xc02aaa39`): `0xa00d47b4b304792eb07b09233467b690db847c91` -> `0xf6da21e95d74767009accb145b96897ac3630bad`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x7b35ce522cb72e4077baeb96cb923a5529764a00` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa00d47b4b304792eb07b09233467b690db847c91` UniswapV2 Sync
  - `0xa00d47b4b304792eb07b09233467b690db847c91` UniswapV2 Swap
- receipt status 1, index 5
