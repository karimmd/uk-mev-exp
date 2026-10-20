# pack_103

Block 12926326. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xce2737e3b010ecd4de52e8d92f6940e9f1b0e134b812745f96a2b66e6d61fdb8`
- block 12926326, position 25, result success, from `0xc85ed10b68e4d22b2ec8f2ab94081a8a6f3cd0f9`, to `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`, value 0.000000 ETH, gas used 93722 at 23.1 gwei, fee 0.002165 ETH
- token transfers (Blockscout, decoded):
  - 114948.586662 CUDOS (`0x817bbdbc`): `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de` -> `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e`
  - 1.356000 WETH (`0xc02aaa39`): `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` -> `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x817bbdbc3e8a1204f3691d14bb44992841e3db35` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` UniswapV2 Sync
  - `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` UniswapV2 Swap
- receipt status 1, index 25

### Victim leg: `0x379ddc7677ceedc1b88b7a4c363fb6da0f0a625babfb590f6acf028638e8388d`
- block 12926326, position 26, result success, from `0x7ceafd11836738eca8da42a8153830a8d36e0473`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 109685 at 23.1 gwei, fee 0.002534 ETH
- token transfers (Blockscout, decoded):
  - 170000.000000 CUDOS (`0x817bbdbc`): `0x7ceafd11836738eca8da42a8153830a8d36e0473` -> `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e`
  - 1.959627 WETH (`0xc02aaa39`): `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 1.959627 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 1.959627 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 1.959627 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x7ceafd11836738eca8da42a8153830a8d36e0473` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x817bbdbc3e8a1204f3691d14bb44992841e3db35` Transfer
  - `0x817bbdbc3e8a1204f3691d14bb44992841e3db35` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` UniswapV2 Sync
  - `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 1.959627 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 26

### Back leg: `0x02186b08c0c329a4f5803c381fdb9e6ddc34f3d2f814f366b1d9d2089a4ada20`
- block 12926326, position 27, result success, from `0xc85ed10b68e4d22b2ec8f2ab94081a8a6f3cd0f9`, to `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`, value 0.000000 ETH, gas used 83785 at 23.1 gwei, fee 0.001935 ETH
- token transfers (Blockscout, decoded):
  - 1.327078 WETH (`0xc02aaa39`): `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de` -> `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e`
  - 114948.586662 CUDOS (`0x817bbdbc`): `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` -> `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x817bbdbc3e8a1204f3691d14bb44992841e3db35` Transfer
  - `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` UniswapV2 Sync
  - `0xcb49221ad08e84b1692f80b62cd5f90c1aadbe6e` UniswapV2 Swap
- receipt status 1, index 27
