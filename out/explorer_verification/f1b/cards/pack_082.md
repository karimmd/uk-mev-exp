# pack_082

Block 13620734. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe6b67e074bf8b38e4f2a37bc319a8264eac6746315205e1da38d6c6cad246d37`
- block 13620734, position 5, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 138457 at 246.2 gwei, fee 0.034091 ETH
- token transfers (Blockscout, decoded):
  - 5.170679 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x8b00ee8606cc70c2dce68dea0cefe632cca0fb7b`
  - 23765.493754 USTC (`0xa47c8bf3`): `0x8b00ee8606cc70c2dce68dea0cefe632cca0fb7b` -> `0x860425be6ad1345dc7a3e287facbf32b18bc4fae`
  - 998.436986 mSLV (`0x9d1555d8`): `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa47c8bf37f92abed4a126bda807a7b7498661acd` Transfer
  - `0x8b00ee8606cc70c2dce68dea0cefe632cca0fb7b` UniswapV2 Sync
  - `0x8b00ee8606cc70c2dce68dea0cefe632cca0fb7b` UniswapV2 Swap
  - `0x9d1555d8cb3c846bb4f7d5b1b1080872c3166676` Transfer
  - `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` UniswapV2 Sync
  - `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` UniswapV2 Swap
- receipt status 1, index 5

### Victim leg: `0xe7e27816fd0f45426edb44aff3d65e5a9824ad66662d048bf9410e485e50f3c9`
- block 13620734, position 6, result success, from `0xa70c50a58473b12e8da58f1471d48c1ad8b3415a`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 111076 at 269.7 gwei, fee 0.029952 ETH
- token transfers (Blockscout, decoded):
  - 126000.000000 USTC (`0xa47c8bf3`): `0xa70c50a58473b12e8da58f1471d48c1ad8b3415a` -> `0x860425be6ad1345dc7a3e287facbf32b18bc4fae`
  - 5211.117449 mSLV (`0x9d1555d8`): `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` -> `0xa70c50a58473b12e8da58f1471d48c1ad8b3415a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa47c8bf37f92abed4a126bda807a7b7498661acd` Transfer
  - `0xa47c8bf37f92abed4a126bda807a7b7498661acd` Approval
  - `0x9d1555d8cb3c846bb4f7d5b1b1080872c3166676` Transfer
  - `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` UniswapV2 Sync
  - `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` UniswapV2 Swap
- receipt status 1, index 6

### Back leg: `0x44f14595426f0eaae11a8c8a83f70dd626664f2847dbf4bce72fe598caf62956`
- block 13620734, position 7, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 118227 at 372.6 gwei, fee 0.044057 ETH
- token transfers (Blockscout, decoded):
  - 998.436696 mSLV (`0x9d1555d8`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x860425be6ad1345dc7a3e287facbf32b18bc4fae`
  - 24254.430652 USTC (`0xa47c8bf3`): `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` -> `0x8b00ee8606cc70c2dce68dea0cefe632cca0fb7b`
  - 5.243776 WETH (`0xc02aaa39`): `0x8b00ee8606cc70c2dce68dea0cefe632cca0fb7b` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x9d1555d8cb3c846bb4f7d5b1b1080872c3166676` Transfer
  - `0xa47c8bf37f92abed4a126bda807a7b7498661acd` Transfer
  - `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` UniswapV2 Sync
  - `0x860425be6ad1345dc7a3e287facbf32b18bc4fae` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8b00ee8606cc70c2dce68dea0cefe632cca0fb7b` UniswapV2 Sync
  - `0x8b00ee8606cc70c2dce68dea0cefe632cca0fb7b` UniswapV2 Swap
- receipt status 1, index 7
