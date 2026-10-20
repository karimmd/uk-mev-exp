# pack_006

Block 13199566. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xb3afb54c7eb73a2515bfee2abebf34ba7dae4752d3b5b7243ba490f493cf8d82`
- block 13199566, position 0, result success, from `0x83b4f74296738d8c2e15bd7c1f4a19df122354f5`, to `0x0000000000d41c96294ccdac8612bdfe29c641af`, value 0.000000 ETH, gas used 100567 at 66.9 gwei, fee 0.006723 ETH
- token transfers (Blockscout, decoded):
  - 8.279961 WETH (`0xc02aaa39`): `0x0000000000d41c96294ccdac8612bdfe29c641af` -> `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70`
  - 13434.359994 NTVRK (`0xfc0d6cf3`): `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` -> `0x0000000000d41c96294ccdac8612bdfe29c641af`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfc0d6cf33e38bce7ca7d89c0e292274031b7157a` Transfer
  - `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` UniswapV2 Sync
  - `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x50cbac1f0251ab7daa8009cbf9f81ab9e01340fd530cc603505dc8e33e922e00`
- block 13199566, position 1, result success, from `0x30bb881a96213b4dca453564e9eeca366f4db4d4`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 4.500000 ETH, gas used 104451 at 207.8 gwei, fee 0.021700 ETH
- token transfers (Blockscout, decoded):
  - 4.500000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 4.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70`
  - 6961.878842 NTVRK (`0xfc0d6cf3`): `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` -> `0x30bb881a96213b4dca453564e9eeca366f4db4d4`
- internal ETH transfers (Etherscan):
  - 4.500000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 4.500000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfc0d6cf33e38bce7ca7d89c0e292274031b7157a` Transfer
  - `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` UniswapV2 Sync
  - `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x073ac9312ac78f6b564a7bc64aa2b6fb431047109454e4da03eaa20a271def38`
- block 13199566, position 2, result success, from `0x83b4f74296738d8c2e15bd7c1f4a19df122354f5`, to `0x0000000000d41c96294ccdac8612bdfe29c641af`, value 0.000000 ETH, gas used 90233 at 2368.2 gwei, fee 0.213687 ETH
- token transfers (Blockscout, decoded):
  - 13434.359994 NTVRK (`0xfc0d6cf3`): `0x0000000000d41c96294ccdac8612bdfe29c641af` -> `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70`
  - 8.503703 WETH (`0xc02aaa39`): `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` -> `0x0000000000d41c96294ccdac8612bdfe29c641af`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xfc0d6cf33e38bce7ca7d89c0e292274031b7157a` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` UniswapV2 Sync
  - `0xddf8390ced9fad414b1ca1dd4fe14f881c2cfa70` UniswapV2 Swap
- receipt status 1, index 2
