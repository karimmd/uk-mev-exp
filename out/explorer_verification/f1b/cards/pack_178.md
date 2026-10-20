# pack_178

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

### Victim leg: `0xa71367581fcab9d961ee10903225515af5a3db6a6183c0669b1769aae864cacf`
- block 13928206, position 4, result success, from `0xc14480bd7bb6d36377c75286b80452654f5b7a79`, to `0xdef1c0ded9bec7f1a1670819833240f027b25eff`, value 0.100000 ETH, gas used 256191 at 150.0 gwei, fee 0.038429 ETH
- token transfers (Blockscout, decoded):
  - 0.100000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 13058.605322 TWO (`0xb711bac0`): `0x377931b4f6adceccfc1a080f7a88b4af9d060336` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 0.100000 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0x377931b4f6adceccfc1a080f7a88b4af9d060336`
  - 37.347827 TWO (`0xb711bac0`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0x96c195f6643a3d797cb90cb6ba0ae2776d51b5f3`
  - 13021.257495 TWO (`0xb711bac0`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xc14480bd7bb6d36377c75286b80452654f5b7a79`
- internal ETH transfers (Etherscan):
  - 0.100000 ETH: `0xdef1c0ded9bec7f1a1670819833240f027b25eff` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` [call]
  - 0.100000 ETH: `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.100000 ETH for `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - `0xb711bac062f74c5c6d4a2cb55639a270881a12ee` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x377931b4f6adceccfc1a080f7a88b4af9d060336` UniswapV3 Swap
  - `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` other
  - `0xb711bac062f74c5c6d4a2cb55639a270881a12ee` Transfer
  - `0xb711bac062f74c5c6d4a2cb55639a270881a12ee` Transfer
  - `0xdef1c0ded9bec7f1a1670819833240f027b25eff` other
- receipt status 1, index 4

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
