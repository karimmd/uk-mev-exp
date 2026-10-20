# pack_086

Block 13986814. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x2b023b27f1afc906cbceb2394517b22adbae043d70b79cc361dc8acc4523bcdc`
- block 13986814, position 1, result success, from `0xb3b6dceeb3b6501ac72feb06f36b0446facf38b4`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 87451 at 198.4 gwei, fee 0.017349 ETH
- token transfers (Blockscout, decoded):
  - 8255.821796 USDT (`0xdac17f95`): `0x70885952f174fb5396deebb66ce3b4b2adfcef8a` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 2.620977 WETH (`0xc02aaa39`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x80d972d2a62ba71814f4e08bd27f95e5d81d02a9`
  - 3600.292601 STOS (`0x08c32b07`): `0x80d972d2a62ba71814f4e08bd27f95e5d81d02a9` -> `0x70885952f174fb5396deebb66ce3b4b2adfcef8a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x08c32b0726c5684024ea6e141c50ade9690bbdcc` Transfer
  - `0x80d972d2a62ba71814f4e08bd27f95e5d81d02a9` UniswapV2 Sync
  - `0x80d972d2a62ba71814f4e08bd27f95e5d81d02a9` UniswapV2 Swap
  - `0x70885952f174fb5396deebb66ce3b4b2adfcef8a` UniswapV3 Swap
- receipt status 1, index 1

### Victim leg: `0x15d4f52d1a301e04f0f7fbd235c35fe2f2518fac45e8f71a04ce0982f97abd95`
- block 13986814, position 2, result success, from `0x33c6b73432b3aea0c1725e415cc40d04908b85fd`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 0.000000 ETH, gas used 101808 at 333.0 gwei, fee 0.033902 ETH
- token transfers (Blockscout, decoded):
  - 26360.762731 USDT (`0xdac17f95`): `0x70885952f174fb5396deebb66ce3b4b2adfcef8a` -> `0x33c6b73432b3aea0c1725e415cc40d04908b85fd`
  - 11744.542638 STOS (`0x08c32b07`): `0x33c6b73432b3aea0c1725e415cc40d04908b85fd` -> `0x70885952f174fb5396deebb66ce3b4b2adfcef8a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x08c32b0726c5684024ea6e141c50ade9690bbdcc` Transfer
  - `0x08c32b0726c5684024ea6e141c50ade9690bbdcc` Approval
  - `0x70885952f174fb5396deebb66ce3b4b2adfcef8a` UniswapV3 Swap
- receipt status 1, index 2

### Back leg: `0xf25bc9aa3e01b5a0fed26048e38d61a98cecda42abbb462b32747ecaf92c166b`
- block 13986814, position 3, result success, from `0xb3b6dceeb3b6501ac72feb06f36b0446facf38b4`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 131714 at 221.0 gwei, fee 0.029114 ETH
- token transfers (Blockscout, decoded):
  - 3697.427653 STOS (`0x08c32b07`): `0x70885952f174fb5396deebb66ce3b4b2adfcef8a` -> `0x80d972d2a62ba71814f4e08bd27f95e5d81d02a9`
  - 2.674771 WETH (`0xc02aaa39`): `0x80d972d2a62ba71814f4e08bd27f95e5d81d02a9` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 8255.821796 USDT (`0xdac17f95`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x70885952f174fb5396deebb66ce3b4b2adfcef8a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x08c32b0726c5684024ea6e141c50ade9690bbdcc` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x80d972d2a62ba71814f4e08bd27f95e5d81d02a9` UniswapV2 Sync
  - `0x80d972d2a62ba71814f4e08bd27f95e5d81d02a9` UniswapV2 Swap
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x70885952f174fb5396deebb66ce3b4b2adfcef8a` UniswapV3 Swap
- receipt status 1, index 3
