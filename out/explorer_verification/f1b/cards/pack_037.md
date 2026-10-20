# pack_037

Block 14053782. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xf22dca09a97a4f832b4a9e139c8c82d494fb48d09dcdf0235dcf59297670721a`
- block 14053782, position 1, result success, from `0x26ccc3a2052be5898d60683c7bb621047153bb19`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 168575 at 144.4 gwei, fee 0.024345 ETH
- token transfers (Blockscout, decoded):
  - 1.419239 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x2084c8115d97a12114a70a27198c3591b6df7d3e`
  - 501773.855512 MFT (`0xdf2c7238`): `0x2084c8115d97a12114a70a27198c3591b6df7d3e` -> `0x000000000035b5e5ad9019092c665357240f594e`
  - 2583.408209 USDC (`0xa0b86991`): `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5` -> `0x000000000035b5e5ad9019092c665357240f594e`
  - 501773.855512 MFT (`0xdf2c7238`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdf2c7238198ad8b389666574f2d8bc411a4b7428` Transfer
  - `0x2084c8115d97a12114a70a27198c3591b6df7d3e` UniswapV2 Sync
  - `0x2084c8115d97a12114a70a27198c3591b6df7d3e` UniswapV2 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xdf2c7238198ad8b389666574f2d8bc411a4b7428` Transfer
  - `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5` UniswapV3 Swap
- receipt status 1, index 1

### Victim leg: `0x49c7935bf4fbf94131ec986de374e45741b1652b95c02b282219ec230ad274cb`
- block 14053782, position 2, result success, from `0x5cfa454b330a9166b377aa51b8d030b3ea5910b7`, to `0x881d40237659c251811cec9c364ef91dc08d300c`, value 0.000000 ETH, gas used 477433 at 171.0 gwei, fee 0.081656 ETH
- token transfers (Blockscout, decoded):
  - 2450599.114439 MFT (`0xdf2c7238`): `0x5cfa454b330a9166b377aa51b8d030b3ea5910b7` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 2450599.114439 MFT (`0xdf2c7238`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4`
  - 966.832960 USDC (`0xa0b86991`): `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4`
  - 245059.911444 MFT (`0xdf2c7238`): `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5`
  - 12472.912819 USDC (`0xa0b86991`): `0xbbb210ea3c86892960b8c2915d2347da48a0ff97` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4`
  - 2205539.202995 MFT (`0xdf2c7238`): `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0xbbb210ea3c86892960b8c2915d2347da48a0ff97`
  - 13439.745779 USDC (`0xa0b86991`): `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0xe82906b6b1b04f631d126c974af57a3a7b6a99d9`
- internal ETH transfers (Etherscan):
  - 5.371281 ETH: `0xe82906b6b1b04f631d126c974af57a3a7b6a99d9` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` [call]
  - 5.371281 ETH: `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0x1111111254fb6c44bac0bed2854e76f90643097d` [call]
  - 5.371281 ETH: `0x1111111254fb6c44bac0bed2854e76f90643097d` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631` [call]
  - 0.048448 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0xf326e4de8f66a0bdc0970b79e0924e33c79f1915` [call]
  - 5.322834 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x5cfa454b330a9166b377aa51b8d030b3ea5910b7` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xdf2c7238198ad8b389666574f2d8bc411a4b7428` Transfer
  - `0xdf2c7238198ad8b389666574f2d8bc411a4b7428` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xdf2c7238198ad8b389666574f2d8bc411a4b7428` Transfer
  - `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5` UniswapV3 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xdf2c7238198ad8b389666574f2d8bc411a4b7428` Transfer
  - `0xbbb210ea3c86892960b8c2915d2347da48a0ff97` UniswapV3 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x2e9c6dcdca22a5952a88c4b18edb5b54c5155bc9` other
  - `0x881d40237659c251811cec9c364ef91dc08d300c` other
- receipt status 1, index 2

### Back leg: `0xab856e0951caaa90938640572cdb73998294e2be274bd420cb35a8c280c82196`
- block 14053782, position 3, result success, from `0x26ccc3a2052be5898d60683c7bb621047153bb19`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 151535 at 897.6 gwei, fee 0.136011 ETH
- token transfers (Blockscout, decoded):
  - 577225.924066 MFT (`0xdf2c7238`): `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5` -> `0x2084c8115d97a12114a70a27198c3591b6df7d3e`
  - 2583.408209 USDC (`0xa0b86991`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5`
  - 1.583857 WETH (`0xc02aaa39`): `0x2084c8115d97a12114a70a27198c3591b6df7d3e` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdf2c7238198ad8b389666574f2d8bc411a4b7428` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x290850efa2d7e130e55bbc1db2b48bc5c03097f5` UniswapV3 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2084c8115d97a12114a70a27198c3591b6df7d3e` UniswapV2 Sync
  - `0x2084c8115d97a12114a70a27198c3591b6df7d3e` UniswapV2 Swap
- receipt status 1, index 3
