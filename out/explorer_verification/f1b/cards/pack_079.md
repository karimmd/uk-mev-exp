# pack_079

Block 12256910. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x9d62542badbe491afeddbdb94c039508ea242c49c641422c70c6e554fd385a59`
- block 12256910, position 25, result success, from `0x520db7c2161aa43fb7eb1bd87c40a084de2c5008`, to `0x9edd647d7d6eceae6bb61d7785ef66c5055a9bee`, value 0.000000 ETH, gas used 82608 at 198.0 gwei, fee 0.016356 ETH
- token transfers (Blockscout, decoded):
  - 8515787148.948834 AKITA (`0x3301ee63`): `0x9edd647d7d6eceae6bb61d7785ef66c5055a9bee` -> `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b`
  - 3.104425 WETH (`0xc02aaa39`): `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` -> `0x9edd647d7d6eceae6bb61d7785ef66c5055a9bee`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x3301ee63fb29f863f2333bd4466acb46cd8323e6` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Sync
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Swap
- receipt status 1, index 25

### Victim leg: `0xf9c29c5290ce6a6bfe4755853d3b3d0efd5a0723caf07f5ac1fa64cafc4cb3ae`
- block 12256910, position 63, result success, from `0xab7f526f09bf96a70fe2a5a8291dc15c6d276363`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 92665 at 179.3 gwei, fee 0.016615 ETH
- token transfers (Blockscout, decoded):
  - 40094831739.142128 AKITA (`0x3301ee63`): `0xab7f526f09bf96a70fe2a5a8291dc15c6d276363` -> `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b`
  - 13.827463 WETH (`0xc02aaa39`): `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 13.827463 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 13.827463 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 13.827463 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xab7f526f09bf96a70fe2a5a8291dc15c6d276363` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x3301ee63fb29f863f2333bd4466acb46cd8323e6` Transfer
  - `0x3301ee63fb29f863f2333bd4466acb46cd8323e6` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Sync
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 13.827463 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 63

### Back leg: `0xff74445cc0b7e0d11cc4635be4c0313a460947f3af4a3d52c51988ae06e32fe0`
- block 12256910, position 64, result success, from `0x520db7c2161aa43fb7eb1bd87c40a084de2c5008`, to `0x9edd647d7d6eceae6bb61d7785ef66c5055a9bee`, value 0.000000 ETH, gas used 84877 at 179.3 gwei, fee 0.015218 ETH
- token transfers (Blockscout, decoded):
  - 2.849676 WETH (`0xc02aaa39`): `0x9edd647d7d6eceae6bb61d7785ef66c5055a9bee` -> `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b`
  - 8515787148.948834 AKITA (`0x3301ee63`): `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` -> `0x9edd647d7d6eceae6bb61d7785ef66c5055a9bee`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x3301ee63fb29f863f2333bd4466acb46cd8323e6` Transfer
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Sync
  - `0xda3a20aad0c34fa742bd9813d45bbf67c787ae0b` UniswapV2 Swap
- receipt status 1, index 64
