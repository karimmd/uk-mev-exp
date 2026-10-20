# pack_164

Block 13687526. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x39abc400db40b99901c02fed44ce0cd2610b4cb006c427cea608a47f81bbc22e`
- block 13687526, position 3, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 129426 at 100.3 gwei, fee 0.012986 ETH
- token transfers (Blockscout, decoded):
  - 7.884759 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0xc926990039045611eb1de520c1e249fd0d20a8ea`
  - 88085.201693 REVV (`0x557b933a`): `0xc926990039045611eb1de520c1e249fd0d20a8ea` -> `0x724d5c9c618a2152e99a45649a3b8cf198321f46`
  - 7.277507 WETH (`0xc02aaa39`): `0x724d5c9c618a2152e99a45649a3b8cf198321f46` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x557b933a7c2c45672b610f8954a3deb39a51a8ca` Transfer
  - `0xc926990039045611eb1de520c1e249fd0d20a8ea` UniswapV2 Sync
  - `0xc926990039045611eb1de520c1e249fd0d20a8ea` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x724d5c9c618a2152e99a45649a3b8cf198321f46` UniswapV2 Sync
  - `0x724d5c9c618a2152e99a45649a3b8cf198321f46` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x188bc5fbcf35926448050a93f2f490000d0361764f20cf4cb0fb3771eefece24`
- block 13687526, position 4, result success, from `0x9877313817a7f38c32fe92164e25bfcac9f24812`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 199869 at 147.7 gwei, fee 0.029511 ETH
- token transfers (Blockscout, decoded):
  - 34883.370429 REVV (`0x557b933a`): `0x9877313817a7f38c32fe92164e25bfcac9f24812` -> `0x724d5c9c618a2152e99a45649a3b8cf198321f46`
  - 2.789159 WETH (`0xc02aaa39`): `0x724d5c9c618a2152e99a45649a3b8cf198321f46` -> `0x21a7afa9f7e2d48bfa8e8f384d77f3b5c19a5add`
  - 481067188.926866 DINGER (`0x9e5bd9d9`): `0x21a7afa9f7e2d48bfa8e8f384d77f3b5c19a5add` -> `0x9877313817a7f38c32fe92164e25bfcac9f24812`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x557b933a7c2c45672b610f8954a3deb39a51a8ca` Approval
  - `0x557b933a7c2c45672b610f8954a3deb39a51a8ca` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x724d5c9c618a2152e99a45649a3b8cf198321f46` UniswapV2 Sync
  - `0x724d5c9c618a2152e99a45649a3b8cf198321f46` UniswapV2 Swap
  - `0x9e5bd9d9fad182ff0a93ba8085b664bcab00fa68` Transfer
  - `0x21a7afa9f7e2d48bfa8e8f384d77f3b5c19a5add` UniswapV2 Sync
  - `0x21a7afa9f7e2d48bfa8e8f384d77f3b5c19a5add` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x8a789dbb9349e573ae1f7e6976b7ecd2670a2c10e3bc6a1ebb4d5a0b058cadba`
- block 13687526, position 5, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 110550 at 292.7 gwei, fee 0.032362 ETH
- token transfers (Blockscout, decoded):
  - 7.277507 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x724d5c9c618a2152e99a45649a3b8cf198321f46`
  - 89172.771071 REVV (`0x557b933a`): `0x724d5c9c618a2152e99a45649a3b8cf198321f46` -> `0xc926990039045611eb1de520c1e249fd0d20a8ea`
  - 7.931585 WETH (`0xc02aaa39`): `0xc926990039045611eb1de520c1e249fd0d20a8ea` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x557b933a7c2c45672b610f8954a3deb39a51a8ca` Transfer
  - `0x724d5c9c618a2152e99a45649a3b8cf198321f46` UniswapV2 Sync
  - `0x724d5c9c618a2152e99a45649a3b8cf198321f46` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc926990039045611eb1de520c1e249fd0d20a8ea` UniswapV2 Sync
  - `0xc926990039045611eb1de520c1e249fd0d20a8ea` UniswapV2 Swap
- receipt status 1, index 5
