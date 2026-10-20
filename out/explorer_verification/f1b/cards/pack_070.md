# pack_070

Block 12338574. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe8017410418c667ecf1dd192e6d1ff93f7f70a2e690bc077894a0c1f30e8b50b`
- block 12338574, position 63, result success, from `0x85160faa4e645f035bc7c4ac1d82e40d5a59cb6d`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.100000 ETH, gas used 189621 at 39.6 gwei, fee 0.007509 ETH
- token transfers (Blockscout, decoded):
  - 0.100000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.100000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xec745519247642fbf14689ac7254068dffba08e3`
  - 28519172927116.906250 ELONGD (`0x348b7f31`): `0xec745519247642fbf14689ac7254068dffba08e3` -> `0x0000000000000000000000000000000000000000`
  - 3757504363484344.500000 ELONGD (`0x348b7f31`): `0xec745519247642fbf14689ac7254068dffba08e3` -> `0x85160faa4e645f035bc7c4ac1d82e40d5a59cb6d`
- internal ETH transfers (Etherscan):
  - 0.100000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.100000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x348b7f3106b5da47405332534d06069ff9ce4d1b` Transfer
  - `0x348b7f3106b5da47405332534d06069ff9ce4d1b` Transfer
  - `0xec745519247642fbf14689ac7254068dffba08e3` UniswapV2 Sync
  - `0xec745519247642fbf14689ac7254068dffba08e3` UniswapV2 Swap
- receipt status 1, index 63

### Victim leg: `0x740c677d620e7ebbbf5cf8aed11b019357d1b8d2f06b2a0255c018766ff6665c`
- block 12338574, position 79, result success, from `0x9f1a7c3c5ac03c36b8d58a78854a3109c163f6a9`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 306765 at 38.0 gwei, fee 0.011657 ETH
- token transfers (Blockscout, decoded):
  - 7192670123714.145508 Dogefather (`0x73c61dd9`): `0x9f1a7c3c5ac03c36b8d58a78854a3109c163f6a9` -> `0x0c497cab883aeccd08572d1f95d7147f8d2bc411`
  - 0.053913 WETH (`0xc02aaa39`): `0x0c497cab883aeccd08572d1f95d7147f8d2bc411` -> `0xec745519247642fbf14689ac7254068dffba08e3`
  - 15333133903602.259766 ELONGD (`0x348b7f31`): `0xec745519247642fbf14689ac7254068dffba08e3` -> `0x0000000000000000000000000000000000000000`
  - 2020195946632581.750000 ELONGD (`0x348b7f31`): `0xec745519247642fbf14689ac7254068dffba08e3` -> `0x9f1a7c3c5ac03c36b8d58a78854a3109c163f6a9`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x73c61dd9e121de834a4f3ed607263ee33b308c06` Transfer
  - `0x73c61dd9e121de834a4f3ed607263ee33b308c06` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0c497cab883aeccd08572d1f95d7147f8d2bc411` UniswapV2 Sync
  - `0x0c497cab883aeccd08572d1f95d7147f8d2bc411` UniswapV2 Swap
  - `0x348b7f3106b5da47405332534d06069ff9ce4d1b` Transfer
  - `0x348b7f3106b5da47405332534d06069ff9ce4d1b` Transfer
  - `0xec745519247642fbf14689ac7254068dffba08e3` UniswapV2 Sync
  - `0xec745519247642fbf14689ac7254068dffba08e3` UniswapV2 Swap
- receipt status 1, index 79

### Back leg: `0xafb6faa5cd71d4387e01529b5425e790a67528d06382562939072f6d562285b2`
- block 12338574, position 86, result success, from `0x823f536e91757d0364f1103d09110f2be0e0dc33`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.200000 ETH, gas used 189621 at 37.4 gwei, fee 0.007092 ETH
- token transfers (Blockscout, decoded):
  - 0.200000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.200000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xec745519247642fbf14689ac7254068dffba08e3`
  - 56784884091399.585938 ELONGD (`0x348b7f31`): `0xec745519247642fbf14689ac7254068dffba08e3` -> `0x0000000000000000000000000000000000000000`
  - 7481614221375560.000000 ELONGD (`0x348b7f31`): `0xec745519247642fbf14689ac7254068dffba08e3` -> `0x823f536e91757d0364f1103d09110f2be0e0dc33`
- internal ETH transfers (Etherscan):
  - 0.200000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.200000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x348b7f3106b5da47405332534d06069ff9ce4d1b` Transfer
  - `0x348b7f3106b5da47405332534d06069ff9ce4d1b` Transfer
  - `0xec745519247642fbf14689ac7254068dffba08e3` UniswapV2 Sync
  - `0xec745519247642fbf14689ac7254068dffba08e3` UniswapV2 Swap
- receipt status 1, index 86
