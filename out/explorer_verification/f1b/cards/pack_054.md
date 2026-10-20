# pack_054

Block 13814334. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe30ede4392299c6cbfdb46be9f01ca5313f922c64a9511b662fbb7af52f361a5`
- block 13814334, position 0, result success, from `0xe51c5f47f08fd806575e5682b090d2f2d1038192`, to `0x00000000726422a6fecb4759b44d47e48cf746aa`, value 0.000000 ETH, gas used 140437 at 73.9 gwei, fee 0.010383 ETH
- token transfers (Blockscout, decoded):
  - 3211873.523710 FREE (`0x4cd0c43b`): `0x78ab16803d92f6db77ef6d4e92fe139affab78cf` -> `0x00000000726422a6fecb4759b44d47e48cf746aa`
  - 8.263597 WETH (`0xc02aaa39`): `0x00000000726422a6fecb4759b44d47e48cf746aa` -> `0x78ab16803d92f6db77ef6d4e92fe139affab78cf`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x4cd0c43b0d53bc318cc5342b77eb6f124e47f526` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x78ab16803d92f6db77ef6d4e92fe139affab78cf` UniswapV3 Swap
- receipt status 1, index 0

### Victim leg: `0xccb7408cc5f904e0d4af4f1a30046a41c6807560f753e36d03320678d3688877`
- block 13814334, position 3, result success, from `0x4f6e6bacc1449d79476608ce93bddadaea7d2d75`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 4.850000 ETH, gas used 112213 at 98.0 gwei, fee 0.011002 ETH
- token transfers (Blockscout, decoded):
  - 1786806.263114 FREE (`0x4cd0c43b`): `0x78ab16803d92f6db77ef6d4e92fe139affab78cf` -> `0x4f6e6bacc1449d79476608ce93bddadaea7d2d75`
  - 4.850000 WETH (`0xc02aaa39`): `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0x0000000000000000000000000000000000000000`
  - 4.850000 WETH (`0xc02aaa39`): `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0x78ab16803d92f6db77ef6d4e92fe139affab78cf`
- internal ETH transfers (Etherscan):
  - 4.850000 ETH: `0xe592427a0aece92de3edee1f18e0157c05861564` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x4cd0c43b0d53bc318cc5342b77eb6f124e47f526` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 4.850000 ETH for `0xe592427a0aece92de3edee1f18e0157c05861564`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x78ab16803d92f6db77ef6d4e92fe139affab78cf` UniswapV3 Swap
- receipt status 1, index 3

### Back leg: `0xf692d8f9c4893191d9301620f6318ad0ccb61477e233c9a7a5eda40afc24eca3`
- block 13814334, position 4, result success, from `0xe51c5f47f08fd806575e5682b090d2f2d1038192`, to `0x00000000726422a6fecb4759b44d47e48cf746aa`, value 0.000000 ETH, gas used 84050 at 1103.2 gwei, fee 0.092724 ETH
- token transfers (Blockscout, decoded):
  - 8.457417 WETH (`0xc02aaa39`): `0x78ab16803d92f6db77ef6d4e92fe139affab78cf` -> `0x00000000726422a6fecb4759b44d47e48cf746aa`
  - 3211873.523710 FREE (`0x4cd0c43b`): `0x00000000726422a6fecb4759b44d47e48cf746aa` -> `0x78ab16803d92f6db77ef6d4e92fe139affab78cf`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4cd0c43b0d53bc318cc5342b77eb6f124e47f526` Transfer
  - `0x78ab16803d92f6db77ef6d4e92fe139affab78cf` UniswapV3 Swap
- receipt status 1, index 4
