# pack_001

Block 12434846. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x79bb8dbec466af839f2ae6bd06c37caf6bf74079c27aa44b18c269668de349f9`
- block 12434846, position 0, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 84295 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 5.840000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x280ab9403372be0371313a9ddd9222b5590dbfef`
  - 34917813261615.925781 JSHIBA (`0x1426cc6d`): `0x280ab9403372be0371313a9ddd9222b5590dbfef` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xb5cd22a8327bba58e7412074503feaf99ad26e47` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x6cb63b2b1b3f0b2ebec347a70dba6b7435401c99` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1426cc6d52d1b14e2b3b1cb04d57ea42b39c4c7c` Transfer
  - `0x280ab9403372be0371313a9ddd9222b5590dbfef` UniswapV2 Sync
  - `0x280ab9403372be0371313a9ddd9222b5590dbfef` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x3e9536ae35aae7d35aae40d9be492369d3a1f848ad5fb0ea8c196650dedf689f`
- block 12434846, position 1, result success, from `0x5e00692612cfb0b3cdc0bc2ab41bd05f384cd037`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 178622 at 123.2 gwei, fee 0.022006 ETH
- token transfers (Blockscout, decoded):
  - 6.219570 LEASH (`0x27c70cd1`): `0x5e00692612cfb0b3cdc0bc2ab41bd05f384cd037` -> `0x874376be8231dad99aabf9ef0767b3cc054c60ee`
  - 7.114293 WETH (`0xc02aaa39`): `0x874376be8231dad99aabf9ef0767b3cc054c60ee` -> `0x280ab9403372be0371313a9ddd9222b5590dbfef`
  - 38274110652692.609375 JSHIBA (`0x1426cc6d`): `0x280ab9403372be0371313a9ddd9222b5590dbfef` -> `0x5e00692612cfb0b3cdc0bc2ab41bd05f384cd037`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x27c70cd1946795b66be9d954418546998b546634` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x874376be8231dad99aabf9ef0767b3cc054c60ee` UniswapV2 Sync
  - `0x874376be8231dad99aabf9ef0767b3cc054c60ee` UniswapV2 Swap
  - `0x1426cc6d52d1b14e2b3b1cb04d57ea42b39c4c7c` Transfer
  - `0x280ab9403372be0371313a9ddd9222b5590dbfef` UniswapV2 Sync
  - `0x280ab9403372be0371313a9ddd9222b5590dbfef` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x9828376567eadb4584f674eb8087ed5175f93c6642e5e52e7e2565628c74c2a0`
- block 12434846, position 2, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.359620 ETH, gas used 93560 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 34219968142500.207031 JSHIBA (`0x1426cc6d`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x280ab9403372be0371313a9ddd9222b5590dbfef`
  - 6.241362 WETH (`0xc02aaa39`): `0x280ab9403372be0371313a9ddd9222b5590dbfef` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.359620 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x2f731c3e8cd264371ffdb635d07c14a6303df52a` [call]
  - 0.000000 ETH: `0x0bcb85f19df9dd356d37aeaa4cb5c784db8ec4e6` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x7f6b511004f97df08d159b66422ddf6db88b4df1` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x1426cc6d52d1b14e2b3b1cb04d57ea42b39c4c7c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x280ab9403372be0371313a9ddd9222b5590dbfef` UniswapV2 Sync
  - `0x280ab9403372be0371313a9ddd9222b5590dbfef` UniswapV2 Swap
- receipt status 1, index 2
