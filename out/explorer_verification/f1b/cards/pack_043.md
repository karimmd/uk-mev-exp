# pack_043

Block 13263190. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x21894c9d1c8bdea2f1643131115ec052de456975a0539d6fb20a653b9ebebb8f`
- block 13263190, position 2, result success, from `0x38563699560e4512c7574c8cc5cf89fd43923bca`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 88109 at 137.8 gwei, fee 0.012139 ETH
- token transfers (Blockscout, decoded):
  - 22.526624 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x05767d9ef41dc40689678ffca0608878fb3de906`
  - 8217.906837 CVX (`0x4e3fbd56`): `0x05767d9ef41dc40689678ffca0608878fb3de906` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b` Transfer
  - `0x05767d9ef41dc40689678ffca0608878fb3de906` UniswapV2 Sync
  - `0x05767d9ef41dc40689678ffca0608878fb3de906` UniswapV2 Swap
- receipt status 1, index 2

### Victim leg: `0xdce8eb3c5a84ec7d724bfbaa397840777eca34d8db893a4180ff07a55f9c4ea8`
- block 13263190, position 3, result success, from `0x11c9a7bc7dc20859f04408166c0af218d5cadc00`, to `0xdef171fe48cf0115b1d80b88dc8eab59176fee57`, value 56.000000 ETH, gas used 111738 at 220.0 gwei, fee 0.024582 ETH
- token transfers (Blockscout, decoded):
  - 56.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xdef171fe48cf0115b1d80b88dc8eab59176fee57`
  - 56.000000 WETH (`0xc02aaa39`): `0xdef171fe48cf0115b1d80b88dc8eab59176fee57` -> `0x05767d9ef41dc40689678ffca0608878fb3de906`
  - 20251.691923 CVX (`0x4e3fbd56`): `0x05767d9ef41dc40689678ffca0608878fb3de906` -> `0x11c9a7bc7dc20859f04408166c0af218d5cadc00`
- internal ETH transfers (Etherscan):
  - 56.000000 ETH: `0xdef171fe48cf0115b1d80b88dc8eab59176fee57` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 56.000000 ETH for `0xdef171fe48cf0115b1d80b88dc8eab59176fee57`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b` Transfer
  - `0x05767d9ef41dc40689678ffca0608878fb3de906` UniswapV2 Sync
  - `0x05767d9ef41dc40689678ffca0608878fb3de906` UniswapV2 Swap
- receipt status 1, index 3

### Back leg: `0x6752f5ad83a2b587f67af609e12be9824a0f2079c78cd1742c83987514c01a62`
- block 13263190, position 4, result success, from `0x38563699560e4512c7574c8cc5cf89fd43923bca`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 77974 at 1544.5 gwei, fee 0.120430 ETH
- token transfers (Blockscout, decoded):
  - 8217.906837 CVX (`0x4e3fbd56`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x05767d9ef41dc40689678ffca0608878fb3de906`
  - 22.672061 WETH (`0xc02aaa39`): `0x05767d9ef41dc40689678ffca0608878fb3de906` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x05767d9ef41dc40689678ffca0608878fb3de906` UniswapV2 Sync
  - `0x05767d9ef41dc40689678ffca0608878fb3de906` UniswapV2 Swap
- receipt status 1, index 4
