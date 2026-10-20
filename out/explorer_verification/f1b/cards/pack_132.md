# pack_132

Block 13715950. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x1563ed7b93d2c8cdde81f2505ed6801dd1f48c407822d7ba8c83338760ab4812`
- block 13715950, position 1, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.000000 ETH, gas used 93773 at 750.0 gwei, fee 0.070330 ETH
- token transfers (Blockscout, decoded):
  - 905428.168460 SPICE (`0x9b6db759`): `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 1.060936 WETH (`0xc02aaa39`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x9b6db7597a74602a5a806e33408e7e2dafa58193` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e` UniswapV3 Swap
- receipt status 1, index 1

### Victim leg: `0x89d1853e17e7457b0f269deea3ae1dab6dada165fddff8418a25012275268feb`
- block 13715950, position 2, result success, from `0x5a9a32c1c2e0e6d7151c6ab42336eecc651ec732`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 0.000000 ETH, gas used 193675 at 152.2 gwei, fee 0.029474 ETH
- token transfers (Blockscout, decoded):
  - 2.190883 WETH (`0xc02aaa39`): `0x11b815efb8f581194ae79006d24e0d814b7697f6` -> `0xe592427a0aece92de3edee1f18e0157c05861564`
  - 10000.000000 USDT (`0xdac17f95`): `0x5a9a32c1c2e0e6d7151c6ab42336eecc651ec732` -> `0x11b815efb8f581194ae79006d24e0d814b7697f6`
  - 1627275.267128 SPICE (`0x9b6db759`): `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e` -> `0x5a9a32c1c2e0e6d7151c6ab42336eecc651ec732`
  - 2.190883 WETH (`0xc02aaa39`): `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x11b815efb8f581194ae79006d24e0d814b7697f6` UniswapV3 Swap
  - `0x9b6db7597a74602a5a806e33408e7e2dafa58193` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e` UniswapV3 Swap
- receipt status 1, index 2

### Back leg: `0x9ce26260f74d471b960686cc84c10315ff9baf195e77183711ff65cc0d119cdd`
- block 13715950, position 3, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.151329 ETH, gas used 88227 at 750.0 gwei, fee 0.066170 ETH
- token transfers (Blockscout, decoded):
  - 1.260769 WETH (`0xc02aaa39`): `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 905428.168460 SPICE (`0x9b6db759`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e`
- internal ETH transfers (Etherscan):
  - 0.151329 ETH: `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x829bd824b016326a401d083b33d092293333a830` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9b6db7597a74602a5a806e33408e7e2dafa58193` Transfer
  - `0xa0b6ef2377fa53687f36ad6ba308d2d2bc70a07e` UniswapV3 Swap
- receipt status 1, index 3
