# pack_051

Block 12865430. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xce2a940fce940c47a68604c2bff544b4994e092c49f3f92135bd6fd3e7b96ad7`
- block 12865430, position 0, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 70999 at 555.5 gwei, fee 0.039437 ETH
- token transfers (Blockscout, decoded):
  - 0.801815 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xa7ad4ce6c21d9e875f1067cd377256326b483002`
  - 8425171397408.854492 SANSHU (`0xc73c167e`): `0xa7ad4ce6c21d9e875f1067cd377256326b483002` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xeb3b159cc543bbe0cb9f2608b2e6a1b64a28f734` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x77e478b0af1fe98e08343d8daa7c118e286c54af` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x4fa0510a06c6d5e71d842a7ea3ac9481dde4dcf0` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc73c167e7a4ba109e4052f70d5466d0c312a344d` Transfer
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Sync
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x8e163f771dd3cf973bf4ab8df916c0a76260a8b86f47deb6576a2fe32f108fd5`
- block 12865430, position 1, result success, from `0x57043ee3d107de959e55e6932892874623fc961d`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 182026 at 35.0 gwei, fee 0.006371 ETH
- token transfers (Blockscout, decoded):
  - 10091.390441 USDT (`0xdac17f95`): `0x57043ee3d107de959e55e6932892874623fc961d` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 5.612111 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0xa7ad4ce6c21d9e875f1067cd377256326b483002`
  - 55667760260000.000000 SANSHU (`0xc73c167e`): `0xa7ad4ce6c21d9e875f1067cd377256326b483002` -> `0x57043ee3d107de959e55e6932892874623fc961d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0xc73c167e7a4ba109e4052f70d5466d0c312a344d` Transfer
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Sync
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xc379b933e857c9b832722b37323de53a97a32fabcb6b665bf09467e757a79e04`
- block 12865430, position 2, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 65995 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 8256775969498.965820 SANSHU (`0xc73c167e`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xa7ad4ce6c21d9e875f1067cd377256326b483002`
  - 0.846618 WETH (`0xc02aaa39`): `0xa7ad4ce6c21d9e875f1067cd377256326b483002` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x9c4a185ac9b4cb876c1569b6f5e8f13217962bbf` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x61cac67e31de1ffeabb19a6b5d54387330d51670` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xd8c5af5fa2ca816507ba871bdbf56f5759120a47` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc73c167e7a4ba109e4052f70d5466d0c312a344d` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Sync
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Swap
- receipt status 1, index 2
