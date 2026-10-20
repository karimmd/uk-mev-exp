# pack_119

Block 11775462. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe5daa8ad0df7409c5d3dc292e99a7897ea34a5ce7b7695fb5d4f729d4448cf6d`
- block 11775462, position 3, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 94963 at 383.9 gwei, fee 0.036454 ETH
- token transfers (Blockscout, decoded):
  - 4.250000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370`
  - 47685.928389 OM (`0x3593d125`): `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x3593d125a4f7849a1b059e64f4517a86dd60c95d` Transfer
  - `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` UniswapV2 Sync
  - `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x07da157c5bfbaf666f5f7ee1724ed93ae7cc0d582465360f96899ed276ce70f2`
- block 11775462, position 7, result success, from `0x50899582199c06d5264eddcd12879e5210783ba8`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 14.000000 ETH, gas used 97599 at 300.0 gwei, fee 0.029280 ETH
- token transfers (Blockscout, decoded):
  - 14.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 14.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370`
  - 153771.683484 OM (`0x3593d125`): `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` -> `0x50899582199c06d5264eddcd12879e5210783ba8`
- internal ETH transfers (Etherscan):
  - 14.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 14.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x3593d125a4f7849a1b059e64f4517a86dd60c95d` Transfer
  - `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` UniswapV2 Sync
  - `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` UniswapV2 Swap
- receipt status 1, index 7

### Back leg: `0x7576aa1a733003793f081591621bb5b607a50fd50f803d05d2520cd2c84b84df`
- block 11775462, position 9, result success, from `0x8517a89b9c47a5631098b37587560262494f5c43`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 89448 at 300.0 gwei, fee 0.026834 ETH
- token transfers (Blockscout, decoded):
  - 47685.928389 OM (`0x3593d125`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370`
  - 4.364444 WETH (`0xc02aaa39`): `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x3593d125a4f7849a1b059e64f4517a86dd60c95d` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` UniswapV2 Sync
  - `0xe46935ae80e05cdebd4a4008b6ccaa36d2845370` UniswapV2 Swap
- receipt status 1, index 9
