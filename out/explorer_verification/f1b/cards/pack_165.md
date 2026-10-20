# pack_165

Block 13672654. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xdab9b25c70c695fae6979e4bd6cb1ff9ef31235f082056c2925b3aaf7b8e7b5c`
- block 13672654, position 0, result success, from `0x1dd71645847ba3a22df1261ad32d66d9a701552d`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 160730 at 107.2 gwei, fee 0.017226 ETH
- token transfers (Blockscout, decoded):
  - 1997.688058 WTON (`0xc4a11aaf`): `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 4650.145952 TOS (`0x409c4d8c`): `0x2ad99c938471770da0cd60e08eaf29ebff67a92a` -> `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4`
  - 4.060760 WETH (`0xc02aaa39`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x2ad99c938471770da0cd60e08eaf29ebff67a92a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc4a11aaf6ea915ed7ac194161d2fc9384f15bff2` Transfer
  - `0x409c4d8cd5d2924b9bc5509230d16a61289c8153` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2ad99c938471770da0cd60e08eaf29ebff67a92a` UniswapV3 Swap
  - `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4` UniswapV3 Swap
- receipt status 1, index 0

### Victim leg: `0x2d1b338000781e9a20268524f4f8d30bf1396d8a45656ff43559c418f168a4d3`
- block 13672654, position 1, result success, from `0xdabd0cd9c9573c59f5aa0aeef551475ff5a39fa2`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 0.000000 ETH, gas used 261533 at 200.0 gwei, fee 0.052307 ETH
- token transfers (Blockscout, decoded):
  - 74366.874975 WTON (`0xc4a11aaf`): `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4` -> `0xdabd0cd9c9573c59f5aa0aeef551475ff5a39fa2`
  - 180000.000000 TOS (`0x409c4d8c`): `0xdabd0cd9c9573c59f5aa0aeef551475ff5a39fa2` -> `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc4a11aaf6ea915ed7ac194161d2fc9384f15bff2` Transfer
  - `0x409c4d8cd5d2924b9bc5509230d16a61289c8153` Transfer
  - `0x409c4d8cd5d2924b9bc5509230d16a61289c8153` Approval
  - `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4` UniswapV3 Swap
- receipt status 1, index 1

### Back leg: `0x263fe0a6200a799107de2f66dec89a84fabe905ea139c62b4ebddc7a06f38ae7`
- block 13672654, position 2, result success, from `0x1dd71645847ba3a22df1261ad32d66d9a701552d`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 185016 at 4006.9 gwei, fee 0.741337 ETH
- token transfers (Blockscout, decoded):
  - 4.858748 WETH (`0xc02aaa39`): `0x2ad99c938471770da0cd60e08eaf29ebff67a92a` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 5666.560626 TOS (`0x409c4d8c`): `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4` -> `0x2ad99c938471770da0cd60e08eaf29ebff67a92a`
  - 1997.688058 WTON (`0xc4a11aaf`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x409c4d8cd5d2924b9bc5509230d16a61289c8153` Transfer
  - `0xc4a11aaf6ea915ed7ac194161d2fc9384f15bff2` Transfer
  - `0x1c0ce9aaa0c12f53df3b4d8d77b82d6ad343b4e4` UniswapV3 Swap
  - `0x2ad99c938471770da0cd60e08eaf29ebff67a92a` UniswapV3 Swap
- receipt status 1, index 2
