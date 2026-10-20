# pack_064

Block 14156390. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xaa1610f4b2b16ca1f746927ee125b46c4c95e09287af5e9e6fe3f00897fafff7`
- block 14156390, position 5, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.000000 ETH, gas used 108303 at 1200.0 gwei, fee 0.129964 ETH
- token transfers (Blockscout, decoded):
  - 423402468.646795 HARAMBE (`0xade6fdab`): `0x2a4a220beb6a0fd217a129125d0034e2db0dee46` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 20.336594 WETH (`0xc02aaa39`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x2a4a220beb6a0fd217a129125d0034e2db0dee46`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xade6fdaba1643e4d1eef68da7170f234470938c6` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2a4a220beb6a0fd217a129125d0034e2db0dee46` UniswapV3 Swap
- receipt status 1, index 5

### Victim leg: `0x25ec58cec03c8f1837cf6c4163c8f04ca51a5588758af2eb36ed69dcdd70289f`
- block 14156390, position 7, result success, from `0x56bf24f635b39ac01da6761c69aee7ba4f1cfe3f`, to `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`, value 0.000000 ETH, gas used 209575 at 122.9 gwei, fee 0.025765 ETH
- token transfers (Blockscout, decoded):
  - 14.037565 WETH (`0xc02aaa39`): `0x4585fe77225b41b697c938b018e2ac67ac5a20c0` -> `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`
  - 1.007618 WBTC (`0x2260fac5`): `0x56bf24f635b39ac01da6761c69aee7ba4f1cfe3f` -> `0x4585fe77225b41b697c938b018e2ac67ac5a20c0`
  - 284310967.043909 HARAMBE (`0xade6fdab`): `0x2a4a220beb6a0fd217a129125d0034e2db0dee46` -> `0x56bf24f635b39ac01da6761c69aee7ba4f1cfe3f`
  - 14.037565 WETH (`0xc02aaa39`): `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45` -> `0x2a4a220beb6a0fd217a129125d0034e2db0dee46`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x4585fe77225b41b697c938b018e2ac67ac5a20c0` UniswapV3 Swap
  - `0xade6fdaba1643e4d1eef68da7170f234470938c6` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2a4a220beb6a0fd217a129125d0034e2db0dee46` UniswapV3 Swap
- receipt status 1, index 7

### Back leg: `0x1e6a50a1e5a4136813322912a055ccb8fa6b19ca4ac50a35c8f12fc60c29d00a`
- block 14156390, position 9, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.081792 ETH, gas used 121302 at 1200.0 gwei, fee 0.145562 ETH
- token transfers (Blockscout, decoded):
  - 20.452645 WETH (`0xc02aaa39`): `0x2a4a220beb6a0fd217a129125d0034e2db0dee46` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 423402468.646795 HARAMBE (`0xade6fdab`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x2a4a220beb6a0fd217a129125d0034e2db0dee46`
- internal ETH transfers (Etherscan):
  - 0.081792 ETH: `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x829bd824b016326a401d083b33d092293333a830` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xade6fdaba1643e4d1eef68da7170f234470938c6` Transfer
  - `0x2a4a220beb6a0fd217a129125d0034e2db0dee46` UniswapV3 Swap
- receipt status 1, index 9
