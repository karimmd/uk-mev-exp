# pack_192

Block 12212382. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x934cd26506b6ed344fa7bee0821b5cb577e49ddc3020219e686e43d21a0de5f7`
- block 12212382, position 0, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 97195 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 2.810000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1`
  - 3.177798 UDT (`0x90de7426`): `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xd55d5bebd843f11939096c11ec93e733d2e3fa1d` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x3951c49954eae5b23bd7bd78088854460443618c` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x90de74265a416e1393a450752175aed98fe11517` Transfer
  - `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` UniswapV2 Sync
  - `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xd7312efdac16c185838be70d0c778dacc6a63fbcd2df0a06b113c2cc1294d162`
- block 12212382, position 1, result success, from `0x26dabf0d8fb77a08f306be212c398044f166157d`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 159780 at 100.1 gwei, fee 0.015994 ETH
- token transfers (Blockscout, decoded):
  - 50000.000000 CHAIN (`0xc4c2614e`): `0x26dabf0d8fb77a08f306be212c398044f166157d` -> `0x33906431e44553411b8668543ffc20aaa24f75f9`
  - 12.138539 WETH (`0xc02aaa39`): `0x33906431e44553411b8668543ffc20aaa24f75f9` -> `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1`
  - 13.369646 UDT (`0x90de7426`): `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` -> `0x26dabf0d8fb77a08f306be212c398044f166157d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc4c2614e694cf534d407ee49f8e44d125e4681c4` Transfer
  - `0xc4c2614e694cf534d407ee49f8e44d125e4681c4` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x33906431e44553411b8668543ffc20aaa24f75f9` UniswapV2 Sync
  - `0x33906431e44553411b8668543ffc20aaa24f75f9` UniswapV2 Swap
  - `0x90de74265a416e1393a450752175aed98fe11517` Transfer
  - `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` UniswapV2 Sync
  - `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xd4945b8e1b96ac3b2170c11d9019f2959bb065de4abf99d157f91582e3d9f051`
- block 12212382, position 2, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.094707 ETH, gas used 85561 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 3.177798 UDT (`0x90de7426`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1`
  - 2.915113 WETH (`0xc02aaa39`): `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.094707 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x829bd824b016326a401d083b33d092293333a830` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x90de74265a416e1393a450752175aed98fe11517` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` UniswapV2 Sync
  - `0x9ca8aef2372c705d6848fdda3c1267a7f51267c1` UniswapV2 Swap
- receipt status 1, index 2
