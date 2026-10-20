# pack_048

Block 13681894. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x1c125b2386cc15b9439089d70551b5f6e51e59b18a738f7d31b088cb7e4fe902`
- block 13681894, position 2, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.000000 ETH, gas used 98781 at 750.0 gwei, fee 0.074086 ETH
- token transfers (Blockscout, decoded):
  - 3020068.012421 PEOPLE (`0x7a58c0be`): `0x83abecf7204d5afc1bea5df734f085f2535a9976` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 19.216836 WETH (`0xc02aaa39`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x83abecf7204d5afc1bea5df734f085f2535a9976`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x7a58c0be72be218b41c608b7fe7c5bb630736c71` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x83abecf7204d5afc1bea5df734f085f2535a9976` UniswapV3 Swap
- receipt status 1, index 2

### Victim leg: `0xf3a5638ca4b5ed64938f498eec507caa7926e9e85bd13d1ff33f117ab049ac92`
- block 13681894, position 3, result success, from `0x23c3ac023542154b0aabad8d4058c5d2c52dd41b`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 10.000000 ETH, gas used 153403 at 152.1 gwei, fee 0.023339 ETH
- token transfers (Blockscout, decoded):
  - 1540458.172767 PEOPLE (`0x7a58c0be`): `0x83abecf7204d5afc1bea5df734f085f2535a9976` -> `0x23c3ac023542154b0aabad8d4058c5d2c52dd41b`
  - 10.000000 WETH (`0xc02aaa39`): `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0x0000000000000000000000000000000000000000`
  - 10.000000 WETH (`0xc02aaa39`): `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0x83abecf7204d5afc1bea5df734f085f2535a9976`
- internal ETH transfers (Etherscan):
  - 10.000000 ETH: `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x7a58c0be72be218b41c608b7fe7c5bb630736c71` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 10.000000 ETH for `0xe592427a0aece92de3edee1f18e0157c05861564`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x83abecf7204d5afc1bea5df734f085f2535a9976` UniswapV3 Swap
- receipt status 1, index 3

### Back leg: `0x551b6498d906777edf5f37a7044e550341c3907b144dcf6cdbcc63a2755f9c5e`
- block 13681894, position 6, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.121771 ETH, gas used 110874 at 750.0 gwei, fee 0.083155 ETH
- token transfers (Blockscout, decoded):
  - 19.403861 WETH (`0xc02aaa39`): `0x83abecf7204d5afc1bea5df734f085f2535a9976` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 3020068.012421 PEOPLE (`0x7a58c0be`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x83abecf7204d5afc1bea5df734f085f2535a9976`
- internal ETH transfers (Etherscan):
  - 0.121771 ETH: `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0xb7e390864a90b7b923c9f9310c6f98aafe43f707` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x7a58c0be72be218b41c608b7fe7c5bb630736c71` Transfer
  - `0x83abecf7204d5afc1bea5df734f085f2535a9976` UniswapV3 Swap
- receipt status 1, index 6
