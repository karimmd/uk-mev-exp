# pack_097

Block 13888078. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x07c6a91be61eab4659cd860bc682f987d5dd573164bb48739904b7d3e239500d`
- block 13888078, position 1, result success, from `0xb3b6dceeb3b6501ac72feb06f36b0446facf38b4`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 128502 at 92.6 gwei, fee 0.011895 ETH
- token transfers (Blockscout, decoded):
  - 33.774883 WETH (`0xc02aaa39`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0xec8c342bc3e07f05b9a782bc34e7f04fb9b44502`
  - 128134.301455 FRAX (`0x853d955a`): `0xec8c342bc3e07f05b9a782bc34e7f04fb9b44502` -> `0xe1573b9d29e2183b1af0e743dc2754979a40d237`
  - 5782.131347 FRAX (`0x3432b6a6`): `0xe1573b9d29e2183b1af0e743dc2754979a40d237` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x853d955acef822db058eb8505911ed77f175b99e` Transfer
  - `0xec8c342bc3e07f05b9a782bc34e7f04fb9b44502` UniswapV2 Sync
  - `0xec8c342bc3e07f05b9a782bc34e7f04fb9b44502` UniswapV2 Swap
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` Transfer
  - `0xe1573b9d29e2183b1af0e743dc2754979a40d237` UniswapV2 Sync
  - `0xe1573b9d29e2183b1af0e743dc2754979a40d237` UniswapV2 Swap
- receipt status 1, index 1

### Victim leg: `0x147d6bc9d79859d9d467fb85f4eb704c51f3e76140c1b4645728f590360e4f06`
- block 13888078, position 2, result success, from `0x77f6821146cce5993282d940eef472c4b09d7537`, to `0xdef1c0ded9bec7f1a1670819833240f027b25eff`, value 0.000000 ETH, gas used 708974 at 101.0 gwei, fee 0.071606 ETH
- token transfers (Blockscout, decoded):
  - 1002738.267927 USDC (`0xa0b86991`): `0x77f6821146cce5993282d940eef472c4b09d7537` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 1002738.267927 USDC (`0xa0b86991`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xd632f22692fac7611d2aa1c0d552930d43caed3b`
  - 1002738.267927 USDC (`0xa0b86991`): `0xd632f22692fac7611d2aa1c0d552930d43caed3b` -> `0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7`
  - 982951.431696 3CRV (`0x6c3f90f0`): `0x0000000000000000000000000000000000000000` -> `0xd632f22692fac7611d2aa1c0d552930d43caed3b`
  - 1002063.841436 FRAX (`0x853d955a`): `0xd632f22692fac7611d2aa1c0d552930d43caed3b` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 1002063.841436 FRAX (`0x853d955a`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xe1573b9d29e2183b1af0e743dc2754979a40d237`
  - 44228.365306 FRAX (`0x3432b6a6`): `0xe1573b9d29e2183b1af0e743dc2754979a40d237` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 44228.365306 FRAX (`0x3432b6a6`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0x77f6821146cce5993282d940eef472c4b09d7537`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x6c3f90f043a72fa612cbac8115ee7e52bde6e490` Transfer
  - `0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7` other
  - `0x853d955acef822db058eb8505911ed77f175b99e` Transfer
  - `0xd632f22692fac7611d2aa1c0d552930d43caed3b` other
  - `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` other
  - `0x853d955acef822db058eb8505911ed77f175b99e` Transfer
  - `0x853d955acef822db058eb8505911ed77f175b99e` Approval
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` Transfer
  - `0xe1573b9d29e2183b1af0e743dc2754979a40d237` UniswapV2 Sync
  - `0xe1573b9d29e2183b1af0e743dc2754979a40d237` UniswapV2 Swap
  - `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` Transfer
  - `0xdef1c0ded9bec7f1a1670819833240f027b25eff` other
- receipt status 1, index 2

### Back leg: `0x34b8151f482d3860539189e38dc70cc0119c16e7692fd5e9fe375843091df1aa`
- block 13888078, position 3, result success, from `0xb3b6dceeb3b6501ac72feb06f36b0446facf38b4`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.806658 ETH, gas used 84267 at 92.6 gwei, fee 0.007800 ETH
- token transfers (Blockscout, decoded):
  - 5782.131347 FRAX (`0x3432b6a6`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0xe1573b9d29e2183b1af0e743dc2754979a40d237`
  - 132462.232606 FRAX (`0x853d955a`): `0xe1573b9d29e2183b1af0e743dc2754979a40d237` -> `0xec8c342bc3e07f05b9a782bc34e7f04fb9b44502`
  - 34.641501 WETH (`0xc02aaa39`): `0xec8c342bc3e07f05b9a782bc34e7f04fb9b44502` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
- internal ETH transfers (Etherscan):
  - 0.806658 ETH: `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x829bd824b016326a401d083b33d092293333a830` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` other
  - `0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0` Transfer
  - `0x853d955acef822db058eb8505911ed77f175b99e` Transfer
  - `0xe1573b9d29e2183b1af0e743dc2754979a40d237` UniswapV2 Sync
  - `0xe1573b9d29e2183b1af0e743dc2754979a40d237` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xec8c342bc3e07f05b9a782bc34e7f04fb9b44502` UniswapV2 Sync
  - `0xec8c342bc3e07f05b9a782bc34e7f04fb9b44502` UniswapV2 Swap
- receipt status 1, index 3
