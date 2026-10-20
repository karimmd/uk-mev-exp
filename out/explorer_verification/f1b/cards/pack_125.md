# pack_125

Block 13928206. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x139514130984528812a873f33cd96df210fd84f8569bd9d44927750cea9606d2`
- block 13928206, position 2, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.000000 ETH, gas used 116601 at 122.4 gwei, fee 0.014274 ETH
- token transfers (Blockscout, decoded):
  - 508890.137675 TWO (`0xb711bac0`): `0x377931b4f6adceccfc1a080f7a88b4af9d060336` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 2.093795 WETH (`0xc02aaa39`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x377931b4f6adceccfc1a080f7a88b4af9d060336`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xb711bac062f74c5c6d4a2cb55639a270881a12ee` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x377931b4f6adceccfc1a080f7a88b4af9d060336` UniswapV3 Swap
- receipt status 1, index 2

### Victim leg: `0xf465eb5431ca912f79fdd2ed6a7ce921a90b739bbf5cc14d5f3a0701bcdf7dce`
- block 13928206, position 5, result success, from `0x6b2b037371bf6d6c9010e2f07a2aa9aae024c805`, to `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`, value 1.000000 ETH, gas used 110816 at 142.4 gwei, fee 0.015782 ETH
- token transfers (Blockscout, decoded):
  - 109879.950465 TWO (`0xb711bac0`): `0x377931b4f6adceccfc1a080f7a88b4af9d060336` -> `0x6b2b037371bf6d6c9010e2f07a2aa9aae024c805`
  - 1.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`
  - 1.000000 WETH (`0xc02aaa39`): `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0x377931b4f6adceccfc1a080f7a88b4af9d060336`
- internal ETH transfers (Etherscan):
  - 1.000000 ETH: `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xb711bac062f74c5c6d4a2cb55639a270881a12ee` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.000000 ETH for `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x377931b4f6adceccfc1a080f7a88b4af9d060336` UniswapV3 Swap
- receipt status 1, index 5

### Back leg: `0xaf8e9b60c522048875fa17cefbf7a7fb5c572c923ba2be6afe34cd00d49091ed`
- block 13928206, position 6, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.660043 ETH, gas used 112220 at 122.4 gwei, fee 0.013737 ETH
- token transfers (Blockscout, decoded):
  - 2.992646 WETH (`0xc02aaa39`): `0x377931b4f6adceccfc1a080f7a88b4af9d060336` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 508890.137675 TWO (`0xb711bac0`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x377931b4f6adceccfc1a080f7a88b4af9d060336`
- internal ETH transfers (Etherscan):
  - 0.660043 ETH: `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x829bd824b016326a401d083b33d092293333a830` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb711bac062f74c5c6d4a2cb55639a270881a12ee` Transfer
  - `0x377931b4f6adceccfc1a080f7a88b4af9d060336` UniswapV3 Swap
- receipt status 1, index 6
