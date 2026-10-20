# pack_089

Block 13065894. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x3b5034fa8d6c5c2afded35079c1b0b59552bbd6a219efdcbcc1fbf86aa775c53`
- block 13065894, position 0, result success, from `0xe5dac13de28cb067b5262a9c08648b7a439d546e`, to `0x1315c6c26123383a2eb369a53fb72c4b9f227eec`, value 0.000000 ETH, gas used 179020 at 26.8 gwei, fee 0.004790 ETH
- token transfers (Blockscout, decoded):
  - 2.919025 WETH (`0xc02aaa39`): `0x1315c6c26123383a2eb369a53fb72c4b9f227eec` -> `0x06da0fd433c1a5d7a4faa01111c044910a184553`
  - 9472.382674 USDT (`0xdac17f95`): `0x06da0fd433c1a5d7a4faa01111c044910a184553` -> `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f`
  - 7707.977757 EPK (`0xdaf88906`): `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` -> `0x1315c6c26123383a2eb369a53fb72c4b9f227eec`
- internal ETH transfers (Etherscan):
  - 0.100192 ETH: `0x1315c6c26123383a2eb369a53fb72c4b9f227eec` -> `0xe5dac13de28cb067b5262a9c08648b7a439d546e` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Sync
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Swap
  - `0xdaf88906ac1de12ba2b1d2f7bfc94e9638ac40c4` Transfer
  - `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` UniswapV2 Sync
  - `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x2bdb615320465d58e1d2325899e0df54530fd722f8116bbc71d3ff75a401ccae`
- block 13065894, position 1, result success, from `0xafa084d8e70bccaa53eb60b6ed0ae50d2720e298`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 112037 at 27.9 gwei, fee 0.003122 ETH
- token transfers (Blockscout, decoded):
  - 1422.857706 USDT (`0xdac17f95`): `0xafa084d8e70bccaa53eb60b6ed0ae50d2720e298` -> `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f`
  - 1089.676668 EPK (`0xdaf88906`): `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` -> `0xafa084d8e70bccaa53eb60b6ed0ae50d2720e298`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xdaf88906ac1de12ba2b1d2f7bfc94e9638ac40c4` Transfer
  - `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` UniswapV2 Sync
  - `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x9cc976e2ae803f995ac2de1d28fdbe87f86e357b94bfb34c2d6c510eb376e447`
- block 13065894, position 2, result success, from `0xe5dac13de28cb067b5262a9c08648b7a439d546e`, to `0x1315c6c26123383a2eb369a53fb72c4b9f227eec`, value 0.000000 ETH, gas used 138542 at 26.8 gwei, fee 0.003707 ETH
- token transfers (Blockscout, decoded):
  - 7707.977757 EPK (`0xdaf88906`): `0x1315c6c26123383a2eb369a53fb72c4b9f227eec` -> `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f`
  - 9561.069144 USDT (`0xdac17f95`): `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` -> `0x06da0fd433c1a5d7a4faa01111c044910a184553`
  - 2.928702 WETH (`0xc02aaa39`): `0x06da0fd433c1a5d7a4faa01111c044910a184553` -> `0x1315c6c26123383a2eb369a53fb72c4b9f227eec`
- internal ETH transfers (Etherscan):
  - 0.000973 ETH: `0x1315c6c26123383a2eb369a53fb72c4b9f227eec` -> `0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xdaf88906ac1de12ba2b1d2f7bfc94e9638ac40c4` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` UniswapV2 Sync
  - `0x66e32d1b776a43935ed20e8dc39a27a140d31c8f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Sync
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Swap
- receipt status 1, index 2
