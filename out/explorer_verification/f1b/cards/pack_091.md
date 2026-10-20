# pack_091

Block 12134854. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x598467ebe9b4049e15867869d6b2048d92f6bdfa70c9e41485aadb3223338100`
- block 12134854, position 110, result success, from `0x978770f230afa5b25250649ce9cb76e26a08ccec`, to `0x00000000c9fdd743c60055c0e4ea30d266272c1f`, value 0.000000 ETH, gas used 163611 at 163.9 gwei, fee 0.026816 ETH
- token transfers (Blockscout, decoded):
  - 9.479658 WETH (`0xc02aaa39`): `0x00000000c9fdd743c60055c0e4ea30d266272c1f` -> `0x7fd1de95fc975fbbd8be260525758549ec477960`
  - 125816053.436246 HOGE (`0xfad45e47`): `0x7fd1de95fc975fbbd8be260525758549ec477960` -> `0x00000000c9fdd743c60055c0e4ea30d266272c1f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfad45e47083e4607302aa43c65fb3106f1cd7607` Transfer
  - `0x7fd1de95fc975fbbd8be260525758549ec477960` UniswapV2 Sync
  - `0x7fd1de95fc975fbbd8be260525758549ec477960` UniswapV2 Swap
- receipt status 1, index 110

### Victim leg: `0x85e26216e7f9d5ab98f012d3737497ce6536ab0d1e1670727fe3cab98e9231e3`
- block 12134854, position 137, result success, from `0xde74395831f3ba9edc7cbee1fcb441cf24c0af4d`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 167650 at 163.9 gwei, fee 0.027478 ETH
- token transfers (Blockscout, decoded):
  - 30000.000000 USDC (`0xa0b86991`): `0xde74395831f3ba9edc7cbee1fcb441cf24c0af4d` -> `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc`
  - 16.793313 WETH (`0xc02aaa39`): `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` -> `0x7fd1de95fc975fbbd8be260525758549ec477960`
  - 211132355.589296 HOGE (`0xfad45e47`): `0x7fd1de95fc975fbbd8be260525758549ec477960` -> `0xde74395831f3ba9edc7cbee1fcb441cf24c0af4d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Sync
  - `0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc` UniswapV2 Swap
  - `0xfad45e47083e4607302aa43c65fb3106f1cd7607` Transfer
  - `0x7fd1de95fc975fbbd8be260525758549ec477960` UniswapV2 Sync
  - `0x7fd1de95fc975fbbd8be260525758549ec477960` UniswapV2 Swap
- receipt status 1, index 137

### Back leg: `0x388fb6c17f97c811d197341828ec042086c40285676d13e1c7c74abc6d732812`
- block 12134854, position 139, result success, from `0x978770f230afa5b25250649ce9cb76e26a08ccec`, to `0x00000000c9fdd743c60055c0e4ea30d266272c1f`, value 0.000000 ETH, gas used 140483 at 163.9 gwei, fee 0.023025 ETH
- token transfers (Blockscout, decoded):
  - 123300580.242368 HOGE (`0xfad45e47`): `0x00000000c9fdd743c60055c0e4ea30d266272c1f` -> `0x7fd1de95fc975fbbd8be260525758549ec477960`
  - 9.695817 WETH (`0xc02aaa39`): `0x7fd1de95fc975fbbd8be260525758549ec477960` -> `0x00000000c9fdd743c60055c0e4ea30d266272c1f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xfad45e47083e4607302aa43c65fb3106f1cd7607` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7fd1de95fc975fbbd8be260525758549ec477960` UniswapV2 Sync
  - `0x7fd1de95fc975fbbd8be260525758549ec477960` UniswapV2 Swap
- receipt status 1, index 139
