# pack_154

Block 13256766. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x9e64171949246586aab665534e35a1bd111badaabb0fa545be9267d1c013407e`
- block 13256766, position 1, result success, from `0xcc8efeb2a5f50c81c5d7403676b198ae094b2f3c`, to `0x00000000500e2fece27a7600435d0c48d64e0c00`, value 0.000000 ETH, gas used 93940 at 38.0 gwei, fee 0.003570 ETH
- token transfers (Blockscout, decoded):
  - 1.568451 WETH (`0xc02aaa39`): `0x00000000500e2fece27a7600435d0c48d64e0c00` -> `0x76efea638426a85a868eac23d5efb34ba52156c1`
  - 26782.993464 UNV (`0xf009f553`): `0x76efea638426a85a868eac23d5efb34ba52156c1` -> `0x00000000500e2fece27a7600435d0c48d64e0c00`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf009f5531de69067435e32c4b9d36077f4c4a673` Transfer
  - `0x76efea638426a85a868eac23d5efb34ba52156c1` UniswapV2 Sync
  - `0x76efea638426a85a868eac23d5efb34ba52156c1` UniswapV2 Swap
- receipt status 1, index 1

### Victim leg: `0x3e277d276c5abcdb7976966a8373988738eb6a52ad4177521dbdcf27c3473e76`
- block 13256766, position 3, result success, from `0xdd86866c9cc3fe81abec83692a3cb72a79e69fa5`, to `0x881d40237659c251811cec9c364ef91dc08d300c`, value 1.500000 ETH, gas used 157195 at 40.0 gwei, fee 0.006288 ETH
- token transfers (Blockscout, decoded):
  - 1.486875 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x11111112542d85b3ef69ae05771c2dccff4faa26`
  - 1.486875 WETH (`0xc02aaa39`): `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0x76efea638426a85a868eac23d5efb34ba52156c1`
  - 24896.271600 UNV (`0xf009f553`): `0x76efea638426a85a868eac23d5efb34ba52156c1` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 24896.271600 UNV (`0xf009f553`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0xdd86866c9cc3fe81abec83692a3cb72a79e69fa5`
- internal ETH transfers (Etherscan):
  - 1.500000 ETH: `0x881d40237659c251811cec9c364ef91dc08d300c` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631` [call]
  - 1.486875 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11111112542d85b3ef69ae05771c2dccff4faa26` [call]
  - 1.486875 ETH: `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.013125 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11ededebf63bef0ea2d2d071bdf88f71543ec6fb` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.486875 ETH for `0x11111112542d85b3ef69ae05771c2dccff4faa26`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xf009f5531de69067435e32c4b9d36077f4c4a673` Transfer
  - `0x76efea638426a85a868eac23d5efb34ba52156c1` UniswapV2 Sync
  - `0x76efea638426a85a868eac23d5efb34ba52156c1` UniswapV2 Swap
  - `0xf009f5531de69067435e32c4b9d36077f4c4a673` Transfer
  - `0x881d40237659c251811cec9c364ef91dc08d300c` other
- receipt status 1, index 3

### Back leg: `0x6169199a90bae8c497ebc7113cc48c62aaad4f1feb36204ef75b827ee8abb208`
- block 13256766, position 4, result success, from `0xcc8efeb2a5f50c81c5d7403676b198ae094b2f3c`, to `0x00000000500e2fece27a7600435d0c48d64e0c00`, value 0.000000 ETH, gas used 86033 at 77.6 gwei, fee 0.006672 ETH
- token transfers (Blockscout, decoded):
  - 26782.993464 UNV (`0xf009f553`): `0x00000000500e2fece27a7600435d0c48d64e0c00` -> `0x76efea638426a85a868eac23d5efb34ba52156c1`
  - 1.588922 WETH (`0xc02aaa39`): `0x76efea638426a85a868eac23d5efb34ba52156c1` -> `0x00000000500e2fece27a7600435d0c48d64e0c00`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xf009f5531de69067435e32c4b9d36077f4c4a673` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x76efea638426a85a868eac23d5efb34ba52156c1` UniswapV2 Sync
  - `0x76efea638426a85a868eac23d5efb34ba52156c1` UniswapV2 Swap
- receipt status 1, index 4
