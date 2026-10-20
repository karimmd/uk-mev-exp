# pack_112

Block 11830110. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x031a26fdd2b7a9d1803aea2d4fa72fe86191a3ec6ab2311b95df04303a1643d7`
- block 11830110, position 55, result success, from `0x8ad7695bcb758c6c090ded08e4cb5240d1875e6b`, to `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af`, value 0.000000 ETH, gas used 137968 at 178.2 gwei, fee 0.024586 ETH
- token transfers (Blockscout, decoded):
  - 0.540000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af`
  - 0.540000 WETH (`0xc02aaa39`): `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af` -> `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a`
  - 620476359389.324341 HUSKY (`0xd5281bb2`): `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` -> `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af`
- internal ETH transfers (Etherscan):
  - 0.540000 ETH: `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.540000 ETH for `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd5281bb2d1ee94866b03a0fccdd4e900c8cb5091` Transfer
  - `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` UniswapV2 Sync
  - `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` UniswapV2 Swap
- receipt status 1, index 55

### Victim leg: `0x4e4e4dd7c1f707995a137370e08db7ddba323557d1b7b1bb51571a58e5d596b4`
- block 11830110, position 82, result success, from `0x2a20ffad28a0d451ae0ce7d886355d4fe54563a2`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 192710 at 178.2 gwei, fee 0.034341 ETH
- token transfers (Blockscout, decoded):
  - 1155.542116 PAID (`0x8c8687fc`): `0x2a20ffad28a0d451ae0ce7d886355d4fe54563a2` -> `0x75e5852385fa856791d703e3f04da24f5bc13975`
  - 2.166354 WETH (`0xc02aaa39`): `0x75e5852385fa856791d703e3f04da24f5bc13975` -> `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a`
  - 2205645295064.273926 HUSKY (`0xd5281bb2`): `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` -> `0x2a20ffad28a0d451ae0ce7d886355d4fe54563a2`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x8c8687fc965593dfb2f0b4eaefd55e9d8df348df` Transfer
  - `0x8c8687fc965593dfb2f0b4eaefd55e9d8df348df` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x75e5852385fa856791d703e3f04da24f5bc13975` UniswapV2 Sync
  - `0x75e5852385fa856791d703e3f04da24f5bc13975` UniswapV2 Swap
  - `0xd5281bb2d1ee94866b03a0fccdd4e900c8cb5091` Transfer
  - `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` UniswapV2 Sync
  - `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` UniswapV2 Swap
- receipt status 1, index 82

### Back leg: `0xda49c79b98edd886144aa14f719c9e947406a6f8cd2bc2ff2e36f4ad8151f989`
- block 11830110, position 85, result success, from `0x8ad7695bcb758c6c090ded08e4cb5240d1875e6b`, to `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af`, value 0.000000 ETH, gas used 139946 at 178.2 gwei, fee 0.024938 ETH
- token transfers (Blockscout, decoded):
  - 601914678668.387573 HUSKY (`0xd5281bb2`): `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af` -> `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a`
  - 0.611570 WETH (`0xc02aaa39`): `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` -> `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af`
  - 0.611570 WETH (`0xc02aaa39`): `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.611570 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xd5281bb2d1ee94866b03a0fccdd4e900c8cb5091` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` UniswapV2 Sync
  - `0x1be574041828303f0bfb5d06a2414f3bd6da1b2a` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.611570 ETH for `0xda6b746b76fdc8424764d6981e9ef5c3b13a56af`
- receipt status 1, index 85
