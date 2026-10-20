# pack_160

Block 12566934. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x0db60dd8a909abebf646830619081593ef18b7ff5edf17aca8dc298e0e698ed1`
- block 12566934, position 3, result success, from `0x5aa17fc7f2950eca85376c3a8cb1509e8e4b39df`, to `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32`, value 0.000000 ETH, gas used 86712 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 1.453431 WETH (`0xc02aaa39`): `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32` -> `0xd329d43715aa7b13f6d8aab5746fd824e7b643de`
  - 185.787870 COLLAR (`0x4cde0dd7`): `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` -> `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4cde0dd772eafe365728e6434e55e2c975df5f0f` Transfer
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Sync
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x669160b0af912fcf05f93cd2559b053b6876669035b403c251bd148d2d2c6e75`
- block 12566934, position 5, result success, from `0xa270a94142dbb61cb687f1551293d59af1501efb`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.200000 ETH, gas used 108325 at 20.9 gwei, fee 0.002264 ETH
- token transfers (Blockscout, decoded):
  - 0.200000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.200000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xd329d43715aa7b13f6d8aab5746fd824e7b643de`
  - 24.221259 COLLAR (`0x4cde0dd7`): `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` -> `0xa270a94142dbb61cb687f1551293d59af1501efb`
- internal ETH transfers (Etherscan):
  - 0.200000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.200000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4cde0dd772eafe365728e6434e55e2c975df5f0f` Transfer
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Sync
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Swap
- receipt status 1, index 5

### Back leg: `0xaf004158cba4b2cb12b37e614797530758c64dedca7c8d5ddaee1ac3c642ece2`
- block 12566934, position 6, result success, from `0x5aa17fc7f2950eca85376c3a8cb1509e8e4b39df`, to `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32`, value 0.011270 ETH, gas used 70552 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 185.787870 COLLAR (`0x4cde0dd7`): `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32` -> `0xd329d43715aa7b13f6d8aab5746fd824e7b643de`
  - 1.463231 WETH (`0xc02aaa39`): `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` -> `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32`
- internal ETH transfers (Etherscan):
  - 0.011270 ETH: `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32` -> `0x829bd824b016326a401d083b33d092293333a830` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x4cde0dd772eafe365728e6434e55e2c975df5f0f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Sync
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Swap
- receipt status 1, index 6
