# pack_017

Block 12446902. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x42805c921cad5d69623b309717fac57c43b6506afeacf88a2aaec1b175dcbc51`
- block 12446902, position 0, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 84295 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.570000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131`
  - 266728859863781.093750 MOONPUG (`0x856710ea`): `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x9528ee1cd52c998ddcc56c192d319280472c2885` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x062eb990da9aba3686d8424d15238f9ee693d03b` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x856710ea0007af7bdc387fe54f64db51dddaf0a2` Transfer
  - `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` UniswapV2 Sync
  - `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xd5b3fd8a0443aab352bc3d43a53ba0235bda4d9e4e29673fd3adfd3fc5e0b28a`
- block 12446902, position 1, result success, from `0x148c02c1bcb98960e82e86aa29f949c2308c5e66`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 184121 at 115.5 gwei, fee 0.021266 ETH
- token transfers (Blockscout, decoded):
  - 8073.803624 USDT (`0xdac17f95`): `0x148c02c1bcb98960e82e86aa29f949c2308c5e66` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 2.255429 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131`
  - 924127762297001.875000 MOONPUG (`0x856710ea`): `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` -> `0x148c02c1bcb98960e82e86aa29f949c2308c5e66`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x856710ea0007af7bdc387fe54f64db51dddaf0a2` Transfer
  - `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` UniswapV2 Sync
  - `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x051fba6330016a5645ea6266ebb40734d131c421a493aa81f844c7fe5b56b74d`
- block 12446902, position 2, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.087418 ETH, gas used 125558 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 261457822590376.781250 MOONPUG (`0x856710ea`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131`
  - 0.670962 WETH (`0xc02aaa39`): `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.087418 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xb3b7874f13387d44a3398d298b075b7a3505d8d4` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x856710ea0007af7bdc387fe54f64db51dddaf0a2` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` UniswapV2 Sync
  - `0x4cb57a0b9298cb43b21cea7eed1cdb8f05e60131` UniswapV2 Swap
- receipt status 1, index 2
