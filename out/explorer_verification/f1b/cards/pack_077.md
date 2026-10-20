# pack_077

Block 13443766. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xfce780d8b5b9996ac34fd2ab0ad4b3b7cbfc7f0179cafb2ca95493bed755ba7b`
- block 13443766, position 6, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.000000 ETH, gas used 84034 at 750.0 gwei, fee 0.063025 ETH
- token transfers (Blockscout, decoded):
  - 13.817921 aKLIMA (`0x6b4d5e9e`): `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 4.890465 WETH (`0xc02aaa39`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x2fa7361d7e3b812375604681eb155a97b4d65e9e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x6b4d5e9ec2acea23d4110f4803da99e25443c5df` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` UniswapV3 Swap
- receipt status 1, index 6

### Victim leg: `0xbf745067211e05bb293208a2642077ad037e61ff2e80807d91422c588d2f168f`
- block 13443766, position 7, result success, from `0x295f09b5f51c0de42e841942258876de531980ca`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 0.000000 ETH, gas used 192322 at 130.0 gwei, fee 0.025002 ETH
- token transfers (Blockscout, decoded):
  - 3.000000 aKLIMA (`0x6b4d5e9e`): `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` -> `0x295f09b5f51c0de42e841942258876de531980ca`
  - 1.099528 WETH (`0xc02aaa39`): `0x11b815efb8f581194ae79006d24e0d814b7697f6` -> `0x2fa7361d7e3b812375604681eb155a97b4d65e9e`
  - 4112.617072 USDT (`0xdac17f95`): `0x295f09b5f51c0de42e841942258876de531980ca` -> `0x11b815efb8f581194ae79006d24e0d814b7697f6`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x6b4d5e9ec2acea23d4110f4803da99e25443c5df` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x11b815efb8f581194ae79006d24e0d814b7697f6` UniswapV3 Swap
  - `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` UniswapV3 Swap
- receipt status 1, index 7

### Back leg: `0xa9926df2afd2d9c1a00ac8578f7fce5464fcd7b282186b26afb632cbac93fe8b`
- block 13443766, position 9, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.190440 ETH, gas used 151230 at 750.0 gwei, fee 0.113422 ETH
- token transfers (Blockscout, decoded):
  - 5.202896 WETH (`0xc02aaa39`): `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 13.817921 aKLIMA (`0x6b4d5e9e`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x2fa7361d7e3b812375604681eb155a97b4d65e9e`
- internal ETH transfers (Etherscan):
  - 0.190440 ETH: `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x3ecef08d0e2dad803847e052249bb4f8bff2d5bb` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b4d5e9ec2acea23d4110f4803da99e25443c5df` Transfer
  - `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` UniswapV3 Swap
- receipt status 1, index 9
