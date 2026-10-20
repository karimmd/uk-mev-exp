# pack_114

Block 12123150. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x29f155b6d220840ca02bdecbdf3b27440cfaeca2f2bc92e04300b76e0c5d2786`
- block 12123150, position 5, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 59844 at 1336.7 gwei, fee 0.079991 ETH
- token transfers (Blockscout, decoded):
  - 16.800000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223`
  - 1039067.564282 FERA (`0x539f3615`): `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x97d048dbaf22544cbf19a2dc722008daa1aefe2e` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x1cdcc5ed944e11542c2e04f29d7dbd1290c18595` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x539f3615c1dbafa0d008d87504667458acbd16fa` Transfer
  - `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` UniswapV2 Sync
  - `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` UniswapV2 Swap
- receipt status 1, index 5

### Victim leg: `0xfb8f341cac1201a98932d3e7ed8b40748b1cba0201bf68ec44bd9ffc8761243a`
- block 12123150, position 11, result success, from `0xbaea104e6a3691bb1279d50faae8f4ce8d544fac`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 160477 at 250.0 gwei, fee 0.040119 ETH
- token transfers (Blockscout, decoded):
  - 166.231463 SVX (`0xc434b277`): `0xbaea104e6a3691bb1279d50faae8f4ce8d544fac` -> `0x0e550efde3e9875e05be2d24b52dad6ce2155364`
  - 4.042447 WETH (`0xc02aaa39`): `0x0e550efde3e9875e05be2d24b52dad6ce2155364` -> `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223`
  - 237092.283805 FERA (`0x539f3615`): `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` -> `0xbaea104e6a3691bb1279d50faae8f4ce8d544fac`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc434b27736a6882d33094d34792999702860a13c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0e550efde3e9875e05be2d24b52dad6ce2155364` UniswapV2 Sync
  - `0x0e550efde3e9875e05be2d24b52dad6ce2155364` UniswapV2 Swap
  - `0x539f3615c1dbafa0d008d87504667458acbd16fa` Transfer
  - `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` UniswapV2 Sync
  - `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` UniswapV2 Swap
- receipt status 1, index 11

### Back leg: `0xf87a4db7f331a92da39f2e4d9d301b9fc5d732e964472b8ea6d74fe4447cafbd`
- block 12123150, position 12, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 96572 at 250.0 gwei, fee 0.024143 ETH
- token transfers (Blockscout, decoded):
  - 1039067.564282 FERA (`0x539f3615`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223`
  - 17.036228 WETH (`0xc02aaa39`): `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x539f3615c1dbafa0d008d87504667458acbd16fa` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` UniswapV2 Sync
  - `0x9c6c852a56de59a59f7a4527724a2a0a87f7d223` UniswapV2 Swap
- receipt status 1, index 12
