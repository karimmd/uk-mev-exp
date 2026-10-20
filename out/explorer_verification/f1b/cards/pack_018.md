# pack_018

Block 13743142. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x424cffa2e65753aaecacd5104af8794d5289707f4f5d68e56635533d5dfcc30b`
- block 13743142, position 0, result success, from `0x38563699560e4512c7574c8cc5cf89fd43923bca`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 41444 at 121.2 gwei, fee 0.005021 ETH
- token transfers (Blockscout, decoded):
  - 4.474893 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x87898263b6c5babe34b4ec53f22d98430b91e371`
  - 18562.711660 BEAN (`0xdc59ac4f`): `0x87898263b6c5babe34b4ec53f22d98430b91e371` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdc59ac4fefa32293a95889dc396682858d52e5db` Transfer
  - `0x87898263b6c5babe34b4ec53f22d98430b91e371` UniswapV2 Sync
  - `0x87898263b6c5babe34b4ec53f22d98430b91e371` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xd74478e45be5cb8d43678d633641923f3715058c47f1d20f96de09096f5cb917`
- block 13743142, position 1, result success, from `0x532744d22891c4fccd5c4250d62894b3153667a7`, to `0xc1e088fc1323b20bcbee9bd1b9fc9546db5624c5`, value 25.000000 ETH, gas used 176492 at 142.9 gwei, fee 0.025219 ETH
- token transfers (Blockscout, decoded):
  - 25.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 25.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x87898263b6c5babe34b4ec53f22d98430b91e371`
  - 101926.466070 BEAN (`0xdc59ac4f`): `0x87898263b6c5babe34b4ec53f22d98430b91e371` -> `0xc1e088fc1323b20bcbee9bd1b9fc9546db5624c5`
  - 101926.466070 BEAN (`0xdc59ac4f`): `0xc1e088fc1323b20bcbee9bd1b9fc9546db5624c5` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 25.000000 ETH: `0xc1e088fc1323b20bcbee9bd1b9fc9546db5624c5` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 25.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 25.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdc59ac4fefa32293a95889dc396682858d52e5db` Transfer
  - `0x87898263b6c5babe34b4ec53f22d98430b91e371` UniswapV2 Sync
  - `0x87898263b6c5babe34b4ec53f22d98430b91e371` UniswapV2 Swap
  - `0xdc59ac4fefa32293a95889dc396682858d52e5db` Transfer
  - `0xc1e088fc1323b20bcbee9bd1b9fc9546db5624c5` other
- receipt status 1, index 1

### Back leg: `0x31cde1790eaadebb0a2dc69d998ca4e162b88b6d408c26237a97bf02ec4fd5f2`
- block 13743142, position 2, result success, from `0x38563699560e4512c7574c8cc5cf89fd43923bca`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 58585 at 1182.3 gwei, fee 0.069266 ETH
- token transfers (Blockscout, decoded):
  - 18562.711659 BEAN (`0xdc59ac4f`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x87898263b6c5babe34b4ec53f22d98430b91e371`
  - 4.580386 WETH (`0xc02aaa39`): `0x87898263b6c5babe34b4ec53f22d98430b91e371` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdc59ac4fefa32293a95889dc396682858d52e5db` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x87898263b6c5babe34b4ec53f22d98430b91e371` UniswapV2 Sync
  - `0x87898263b6c5babe34b4ec53f22d98430b91e371` UniswapV2 Swap
- receipt status 1, index 2
