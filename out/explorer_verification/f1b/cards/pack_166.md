# pack_166

Block 12443998. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x6458a6a9d7ed9fdcb05ba561be9484000d165cc389d6f43bbe4326866e6c3128`
- block 12443998, position 0, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 113118 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 2.110000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44`
  - 2889577707006.020020 HATT (`0x829999b5`): `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xed39b71db4976f0b347a657da68795b4f6522e94` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0xaecd847e0755ea42c8711443bc962b17fd4c02dc` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x829999b513491cb93c96b08daa5b262f451d5d77` Transfer
  - `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` UniswapV2 Sync
  - `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x8f158f36a9c73aee2bf2c25a062aca4eab1f690d369fbf7f5152f142c21bc72d`
- block 12443998, position 1, result success, from `0x02500fc3935a62eaa818fcaae1c741a1e7867b86`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 152523 at 53.0 gwei, fee 0.008084 ETH
- token transfers (Blockscout, decoded):
  - 6484.033888 DAI (`0x6b175474`): `0x02500fc3935a62eaa818fcaae1c741a1e7867b86` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 1.669292 WETH (`0xc02aaa39`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44`
  - 2004419824776.526367 HATT (`0x829999b5`): `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` -> `0x02500fc3935a62eaa818fcaae1c741a1e7867b86`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
  - `0x829999b513491cb93c96b08daa5b262f451d5d77` Transfer
  - `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` UniswapV2 Sync
  - `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xb7b1d7f59be119d67250f38e0a88b20501e2457d51bd297b234fc3198835ab05`
- block 12443998, position 2, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.123765 ETH, gas used 122055 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 2832069006008.090820 HATT (`0x829999b5`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44`
  - 2.252916 WETH (`0xc02aaa39`): `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.123765 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c` [call]
  - 0.000000 ETH: `0x70ac60e0be4f654e7bdd33609fd8e5acea686bc7` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x11b7230d33a2457f613f8871d3ecf5bf3127e96d` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x829999b513491cb93c96b08daa5b262f451d5d77` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` UniswapV2 Sync
  - `0xd2e19525ca8dd5e2787e8553aa50f7d5039a0b44` UniswapV2 Swap
- receipt status 1, index 2
