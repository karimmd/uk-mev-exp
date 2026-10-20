# pack_162

Block 13931198. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x67ae3171a3ec1bba93d84f1f8a405e2dd7e56d1ca4cb1f053c86355a578361d1`
- block 13931198, position 0, result success, from `0x74b892425a206eb23905a5f5c322e4386460312d`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 41148 at 88.5 gwei, fee 0.003640 ETH
- token transfers (Blockscout, decoded):
  - 1.573666 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c`
  - 8864.669729 GLCH (`0x038a68ff`): `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x038a68ff68c393373ec894015816e33ad41bd564` Transfer
  - `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` UniswapV2 Sync
  - `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x68ece219c52ea228b7b143a2f29e91775440073c81ea306bc190592e5c8df042`
- block 13931198, position 1, result success, from `0xf3f4fa24bb91e0390e0aa37e467942467ad76460`, to `0x11111112542d85b3ef69ae05771c2dccff4faa26`, value 5.400000 ETH, gas used 268606 at 114.2 gwei, fee 0.030671 ETH
- token transfers (Blockscout, decoded):
  - 5.400000 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x0000000000000000000000000000000000000000`
  - 4289.123920 GLCH (`0x038a68ff`): `0xf784ce42e5d95a9f047bb6dec0d20729a30ceb77` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 0.756000 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xf784ce42e5d95a9f047bb6dec0d20729a30ceb77`
  - 4.644000 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c`
  - 25561.640486 GLCH (`0x038a68ff`): `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 29850.764406 GLCH (`0x038a68ff`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xf3f4fa24bb91e0390e0aa37e467942467ad76460`
- internal ETH transfers (Etherscan):
  - 5.400000 ETH: `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` [call]
  - 5.400000 ETH: `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 5.400000 ETH for `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - `0x038a68ff68c393373ec894015816e33ad41bd564` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf784ce42e5d95a9f047bb6dec0d20729a30ceb77` UniswapV3 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x038a68ff68c393373ec894015816e33ad41bd564` Transfer
  - `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` UniswapV2 Sync
  - `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` UniswapV2 Swap
  - `0x038a68ff68c393373ec894015816e33ad41bd564` Transfer
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
- receipt status 1, index 1

### Back leg: `0xdffe09ff6dfbbf9b4b1fe1e7f891fd73e9299225e2a6867ab35aabde3566e46c`
- block 13931198, position 2, result success, from `0x74b892425a206eb23905a5f5c322e4386460312d`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 34694 at 490.7 gwei, fee 0.017025 ETH
- token transfers (Blockscout, decoded):
  - 8864.669729 GLCH (`0x038a68ff`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c`
  - 1.619044 WETH (`0xc02aaa39`): `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x038a68ff68c393373ec894015816e33ad41bd564` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` UniswapV2 Sync
  - `0x1037fa1f40b69c9266c4aeb2abcedc7553614b4c` UniswapV2 Swap
- receipt status 1, index 2
