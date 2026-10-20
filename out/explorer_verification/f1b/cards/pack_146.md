# pack_146

Block 11943982. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xf9969b6b30599fde031b4827495b7ece0ca4a34b120c838614d6fcba7f9799a4`
- block 11943982, position 144, result success, from `0xf529aeb37f7ddf8f2d32fc12f984936bf0c0aff7`, to `0x00000000000064c443ef440577c26525a3c34a30`, value 0.000000 ETH, gas used 80497 at 87.2 gwei, fee 0.007020 ETH
- token transfers (Blockscout, decoded):
  - 51071915653.522133 AKITA (`0x3301ee63`): `0x00000000000064c443ef440577c26525a3c34a30` -> `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b`
  - 3.035358 WETH (`0xc02aaa39`): `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` -> `0x00000000000064c443ef440577c26525a3c34a30`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x3301ee63fb29f863f2333bd4466acb46cd8323e6` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Sync
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Swap
- receipt status 1, index 144

### Victim leg: `0x4181b8aa9c72b005b7a3fdcbeac5949b6eb4842ef3361c337b0cd67aaf4ee429`
- block 11943982, position 157, result success, from `0xda19f2711140485a143af7bc1753c02256ca7b89`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 116045 at 87.0 gwei, fee 0.010096 ETH
- token transfers (Blockscout, decoded):
  - 65150996855.988838 AKITA (`0x3301ee63`): `0xda19f2711140485a143af7bc1753c02256ca7b89` -> `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b`
  - 3.626479 WETH (`0xc02aaa39`): `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 3.626479 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 3.626479 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 3.626479 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xda19f2711140485a143af7bc1753c02256ca7b89` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x3301ee63fb29f863f2333bd4466acb46cd8323e6` Transfer
  - `0x3301ee63fb29f863f2333bd4466acb46cd8323e6` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Sync
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 3.626479 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 157

### Back leg: `0xfd8402363f1b1165a2b85372fdfd5d34024da995005ba2cdee7f284c742cb046`
- block 11943982, position 158, result success, from `0xf529aeb37f7ddf8f2d32fc12f984936bf0c0aff7`, to `0x00000000000064c443ef440577c26525a3c34a30`, value 0.000000 ETH, gas used 89431 at 87.0 gwei, fee 0.007780 ETH
- token transfers (Blockscout, decoded):
  - 2.837288 WETH (`0xc02aaa39`): `0x00000000000064c443ef440577c26525a3c34a30` -> `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b`
  - 51071915653.522133 AKITA (`0x3301ee63`): `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` -> `0x00000000000064c443ef440577c26525a3c34a30`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x3301ee63fb29f863f2333bd4466acb46cd8323e6` Transfer
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Sync
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Swap
- receipt status 1, index 158
