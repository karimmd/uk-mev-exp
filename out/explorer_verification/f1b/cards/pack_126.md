# pack_126

Block 12930550. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xca3022c73285931b7743f2c575eb14b4838af0896e711b62dbb15b7c6546dd73`
- block 12930550, position 0, result success, from `0x5aa17fc7f2950eca85376c3a8cb1509e8e4b39df`, to `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32`, value 0.000000 ETH, gas used 117717 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.316928 WETH (`0xc02aaa39`): `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32` -> `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46`
  - 235028948319.595581 SAITAMA (`0x8b3192f5`): `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` -> `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8b3192f5eebd8579568a2ed41e6feb402f93f73f` Transfer
  - `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` UniswapV2 Sync
  - `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x754edc395c13db6dac9987090894bdfec8e55917bb84bc788c452a954c3a6067`
- block 12930550, position 1, result success, from `0xe7b1354bbbba77ae7166c70f0ad46939a5f9a2e7`, to `0x03f7724180aa6b939894b5ca4314783b0b36b329`, value 0.000000 ETH, gas used 181050 at 28.0 gwei, fee 0.005069 ETH
- token transfers (Blockscout, decoded):
  - 664469057.211161 SHIB (`0x95ad61b0`): `0xe7b1354bbbba77ae7166c70f0ad46939a5f9a2e7` -> `0xcf6daab95c476106eca715d48de4b13287ffdeaa`
  - 1.680894 WETH (`0xc02aaa39`): `0xcf6daab95c476106eca715d48de4b13287ffdeaa` -> `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46`
  - 1178812600000.000000 SAITAMA (`0x8b3192f5`): `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` -> `0xe7b1354bbbba77ae7166c70f0ad46939a5f9a2e7`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Transfer
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcf6daab95c476106eca715d48de4b13287ffdeaa` UniswapV2 Sync
  - `0xcf6daab95c476106eca715d48de4b13287ffdeaa` UniswapV2 Swap
  - `0x8b3192f5eebd8579568a2ed41e6feb402f93f73f` Transfer
  - `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` UniswapV2 Sync
  - `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x3cd5d1a20aa9a5c0f26a4974530009b9220f0fa7c752d568aface26e513120d2`
- block 12930550, position 2, result success, from `0x5aa17fc7f2950eca85376c3a8cb1509e8e4b39df`, to `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32`, value 0.014564 ETH, gas used 120206 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 230328435811.958618 SAITAMA (`0x8b3192f5`): `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32` -> `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46`
  - 0.332259 WETH (`0xc02aaa39`): `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` -> `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32`
- internal ETH transfers (Etherscan):
  - 0.014564 ETH: `0x36c1c59dcca0fd4a8c28551f7b2fe6421d53ce32` -> `0x1ad91ee08f21be3de0ba2ba6918e714da6b45836` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x8b3192f5eebd8579568a2ed41e6feb402f93f73f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` UniswapV2 Sync
  - `0xd0dcb7a4f8cfcdb29364d621ca5d997b7eddbc46` UniswapV2 Swap
- receipt status 1, index 2
