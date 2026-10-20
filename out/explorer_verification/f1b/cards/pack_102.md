# pack_102

Block 12254534. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x4b7d306955df9a6e89b3ea6855f2bcf8af3a1ebc6de8da4ce01577fc545a74cd`
- block 12254534, position 3, result success, from `0xf6da21e95d74767009accb145b96897ac3630bad`, to `0xd78a3280085ee846196cb5fab7d510b279486d44`, value 0.000000 ETH, gas used 122141 at 1.0 gwei, fee 0.000122 ETH
- token transfers (Blockscout, decoded):
  - 2.000800 WETH (`0xc02aaa39`): `0xf6da21e95d74767009accb145b96897ac3630bad` -> `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee`
  - 30967.458211 UCT (`0x6d1dc392`): `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` -> `0xf6da21e95d74767009accb145b96897ac3630bad`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6d1dc3928604b00180bb570bdae94b9698d33b79` Transfer
  - `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` UniswapV2 Sync
  - `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x1177e296c4e193be1f48225bc974a2ef628be12565df9ebc428880ee3fd07395`
- block 12254534, position 4, result success, from `0x71812d389deac281c18fc1a138714659f87b87bc`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 144023 at 101.0 gwei, fee 0.014546 ETH
- token transfers (Blockscout, decoded):
  - 6891.153111 RAZE (`0x5eaa69b2`): `0x71812d389deac281c18fc1a138714659f87b87bc` -> `0x4fc47579ecf6aa76677ee142b6b75faf9eeafba8`
  - 3.137322 WETH (`0xc02aaa39`): `0x4fc47579ecf6aa76677ee142b6b75faf9eeafba8` -> `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee`
  - 46443.430058 UCT (`0x6d1dc392`): `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` -> `0x71812d389deac281c18fc1a138714659f87b87bc`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x5eaa69b29f99c84fe5de8200340b4e9b4ab38eac` Transfer
  - `0x5eaa69b29f99c84fe5de8200340b4e9b4ab38eac` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4fc47579ecf6aa76677ee142b6b75faf9eeafba8` UniswapV2 Sync
  - `0x4fc47579ecf6aa76677ee142b6b75faf9eeafba8` UniswapV2 Swap
  - `0x6d1dc3928604b00180bb570bdae94b9698d33b79` Transfer
  - `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` UniswapV2 Sync
  - `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x5ed0a7970ec1ee8566e8da6c81b282243fd894476e362b9744c58ea90077cbfc`
- block 12254534, position 6, result success, from `0xf6da21e95d74767009accb145b96897ac3630bad`, to `0xd78a3280085ee846196cb5fab7d510b279486d44`, value 0.000000 ETH, gas used 85413 at 1.0 gwei, fee 0.000085 ETH
- token transfers (Blockscout, decoded):
  - 30967.458211 UCT (`0x6d1dc392`): `0xf6da21e95d74767009accb145b96897ac3630bad` -> `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee`
  - 2.098212 WETH (`0xc02aaa39`): `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` -> `0xf6da21e95d74767009accb145b96897ac3630bad`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x6d1dc3928604b00180bb570bdae94b9698d33b79` Transfer
  - `0x6d1dc3928604b00180bb570bdae94b9698d33b79` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` UniswapV2 Sync
  - `0x7e02eb1c6cc7b817891d5fbbdd567f6435dd31ee` UniswapV2 Swap
- receipt status 1, index 6
