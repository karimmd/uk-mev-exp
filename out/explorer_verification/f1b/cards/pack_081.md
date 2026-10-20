# pack_081

Block 13372486. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x66dc1a0eae01f81782aff7d097f7a832f7729927ee22451e1784367e89d2a6c8`
- block 13372486, position 2, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.000000 ETH, gas used 102058 at 112.5 gwei, fee 0.011483 ETH
- token transfers (Blockscout, decoded):
  - 17.627637 WETH (`0xc02aaa39`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed`
  - 33816.952032 KST (`0xbc17729f`): `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xbc17729fdf562723f0267f79ff25ade441056d87` Transfer
  - `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` UniswapV2 Sync
  - `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` UniswapV2 Swap
- receipt status 1, index 2

### Victim leg: `0x48820d70a6ed2659c02ab095c8c5b204fb79efef173068eb42b61eee4080ad3c`
- block 13372486, position 4, result success, from `0x605c3d51116aff5b9f06886f4947c2eb9ff241c1`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 167451 at 114.0 gwei, fee 0.019092 ETH
- token transfers (Blockscout, decoded):
  - 8096.882984 USDT (`0xdac17f95`): `0x605c3d51116aff5b9f06886f4947c2eb9ff241c1` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 2.265668 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed`
  - 3628.477196 KST (`0xbc17729f`): `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` -> `0x605c3d51116aff5b9f06886f4947c2eb9ff241c1`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0xbc17729fdf562723f0267f79ff25ade441056d87` Transfer
  - `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` UniswapV2 Sync
  - `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x4bcf73452fc5917e100c63308a2313f9d749f2b5438eb328d4a5fbdf2bda46a0`
- block 13372486, position 7, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.873569 ETH, gas used 96127 at 112.5 gwei, fee 0.010816 ETH
- token transfers (Blockscout, decoded):
  - 33816.952032 KST (`0xbc17729f`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed`
  - 19.593682 WETH (`0xc02aaa39`): `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
- internal ETH transfers (Etherscan):
  - 0.873569 ETH: `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x1ad91ee08f21be3de0ba2ba6918e714da6b45836` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xbc17729fdf562723f0267f79ff25ade441056d87` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` UniswapV2 Sync
  - `0xc66ce0de9fd74e6ce40b6b8a9e86103ec56e45ed` UniswapV2 Swap
- receipt status 1, index 7
