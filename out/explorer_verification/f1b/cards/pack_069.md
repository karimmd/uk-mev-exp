# pack_069

Block 12817470. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x0481538b62aefa8bd18afd3f3019158456c48a0b35b2c508f05ffb348cefbaa9`
- block 12817470, position 0, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 92078 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 2.211908 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b`
  - 25104904877090.121094 BEZOGE (`0xdc349913`): `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x966c5d34b5a3305ed3f400516c72b12b5eab8fe5` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x9afe03b01a0747628e5530aef38ebb80ea60f2c4` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x47fb75a1589029795c6eb2eb81aeaf1125c7c63d` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x86095ac5fc7beab9b80342d96ae86419d5abcd12` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdc349913d53b446485e98b76800b6254f43df695` Transfer
  - `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` UniswapV2 Sync
  - `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xd743b1d194b586babcdcb6bfdac98b41e61c9370e55f1e02acce25808e4027c2`
- block 12817470, position 1, result success, from `0x023ced7a33b19fdfb9fd7d77771d3814a6e1c46d`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 216176 at 33.0 gwei, fee 0.007134 ETH
- token transfers (Blockscout, decoded):
  - 11000.000000 USDT (`0xdac17f95`): `0x023ced7a33b19fdfb9fd7d77771d3814a6e1c46d` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 5.419051 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b`
  - 58450697933409.515625 BEZOGE (`0xdc349913`): `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` -> `0x023ced7a33b19fdfb9fd7d77771d3814a6e1c46d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0xdc349913d53b446485e98b76800b6254f43df695` Transfer
  - `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` UniswapV2 Sync
  - `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xf2af0b3658fa9292e02a832072644ef51f82b418b859aefea9399a509d759d0a`
- block 12817470, position 2, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.051798 ETH, gas used 100652 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 24603226316290.773438 BEZOGE (`0xdc349913`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b`
  - 2.270042 WETH (`0xc02aaa39`): `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xd488244497ae6d46a3ad801802a31263e370bb9a` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x08721d75bace5e7dcd05000ecb6b5611c2fd7163` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xfa813d6bdef6778b41c97a612608a9b9cdecd7d1` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.051798 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x00192fb10df37c9fb26829eb2cc623cd1bf599e8` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xdc349913d53b446485e98b76800b6254f43df695` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` UniswapV2 Sync
  - `0x1f964ff83c54ce447adae5cb93f9ec17018bf55b` UniswapV2 Swap
- receipt status 1, index 2
