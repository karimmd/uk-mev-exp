# pack_030

Block 12362774. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x9656586199b5fc85e744d7e0101dee74cdcd26fadb00c4387bdcb2eca81a6cb4`
- block 12362774, position 0, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 86407 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 3.620000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x9b577e849b128ee1a69144b218e809b8bb98c35d`
  - 16632.276565 NAOS (`0x4a615bb7`): `0x9b577e849b128ee1a69144b218e809b8bb98c35d` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xc6e268331995674d9475c87a1f24e41e69f779cd` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0xd60d89addc979e3eccb3fb79a530ccc0a2659a44` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4a615bb7166210cce20e6642a6f8fb5d4d044496` Transfer
  - `0x9b577e849b128ee1a69144b218e809b8bb98c35d` UniswapV2 Sync
  - `0x9b577e849b128ee1a69144b218e809b8bb98c35d` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xe239cbbe08b453ec0189ea8caba49f400b0694429801df505d490af4536fadbd`
- block 12362774, position 1, result success, from `0xfa98bcb727c284897f4fd75beabc9201011d0e93`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 3.000000 ETH, gas used 108232 at 140.0 gwei, fee 0.015152 ETH
- token transfers (Blockscout, decoded):
  - 3.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 3.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x9b577e849b128ee1a69144b218e809b8bb98c35d`
  - 13182.422999 NAOS (`0x4a615bb7`): `0x9b577e849b128ee1a69144b218e809b8bb98c35d` -> `0xfa98bcb727c284897f4fd75beabc9201011d0e93`
- internal ETH transfers (Etherscan):
  - 3.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 3.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4a615bb7166210cce20e6642a6f8fb5d4d044496` Transfer
  - `0x9b577e849b128ee1a69144b218e809b8bb98c35d` UniswapV2 Sync
  - `0x9b577e849b128ee1a69144b218e809b8bb98c35d` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x52b90b0f6f445d5e165044666aec0c29a747bf2302d7e68108e1720e08e20ddd`
- block 12362774, position 2, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 3.586598 ETH, gas used 91947 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 33669.791897 NAOS (`0x4a615bb7`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x9b577e849b128ee1a69144b218e809b8bb98c35d`
  - 7.391397 WETH (`0xc02aaa39`): `0x9b577e849b128ee1a69144b218e809b8bb98c35d` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 3.586598 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xb3b7874f13387d44a3398d298b075b7a3505d8d4` [call]
  - 0.000000 ETH: `0xfcbb878b85cfa21f249385b3cc0ff7379e46211c` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x5596e7f3f534513690739caa1ddf88864aa05ab5` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x4a615bb7166210cce20e6642a6f8fb5d4d044496` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9b577e849b128ee1a69144b218e809b8bb98c35d` UniswapV2 Sync
  - `0x9b577e849b128ee1a69144b218e809b8bb98c35d` UniswapV2 Swap
- receipt status 1, index 2
