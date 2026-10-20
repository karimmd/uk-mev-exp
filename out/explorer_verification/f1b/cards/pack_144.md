# pack_144

Block 10933654. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x58e877efb733ae0da0ed5abf8d34bc1e7904c851319032d0a0a291263a1ddda4`
- block 10933654, position 125, result success, from `0xe73c1e4d7992a4a4f19f31531ae7b5dc352b74b0`, to `0x000000000000740a22fa209cf6806d38f7605385`, value 0.000000 ETH, gas used 72923 at 77.0 gwei, fee 0.005615 ETH
- token transfers (Blockscout, decoded):
  - 0.151825 WETH (`0xc02aaa39`): `0x000000000000740a22fa209cf6806d38f7605385` -> `0x287856d10418e01ef1e93df9962b04d9a3a521c9`
  - 0.127231 SSL (`0x0d9227f9`): `0x287856d10418e01ef1e93df9962b04d9a3a521c9` -> `0x000000000000740a22fa209cf6806d38f7605385`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d9227f9c4ab3972f994fccc6eeba3213c0305c4` Transfer
  - `0x287856d10418e01ef1e93df9962b04d9a3a521c9` UniswapV2 Sync
  - `0x287856d10418e01ef1e93df9962b04d9a3a521c9` UniswapV2 Swap
- receipt status 1, index 125

### Victim leg: `0xc1fa69dd508c11f28c2258d2c52cfdd67b066c24027c9e6332aa3681b92d5879`
- block 10933654, position 128, result success, from `0x3da41b4398faf97f1b477a755ffb67e61840d429`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 39.067970 ETH, gas used 113995 at 77.0 gwei, fee 0.008778 ETH
- token transfers (Blockscout, decoded):
  - 39.067970 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 39.067970 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x287856d10418e01ef1e93df9962b04d9a3a521c9`
  - 15.936928 SSL (`0x0d9227f9`): `0x287856d10418e01ef1e93df9962b04d9a3a521c9` -> `0x3da41b4398faf97f1b477a755ffb67e61840d429`
- internal ETH transfers (Etherscan):
  - 39.067970 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 39.067970 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d9227f9c4ab3972f994fccc6eeba3213c0305c4` Transfer
  - `0x287856d10418e01ef1e93df9962b04d9a3a521c9` UniswapV2 Sync
  - `0x287856d10418e01ef1e93df9962b04d9a3a521c9` UniswapV2 Swap
- receipt status 1, index 128

### Back leg: `0xf56d0d3d6972884829ba1d1d7775cc8a1c672a52af8e33ce01035ee550e442fc`
- block 10933654, position 129, result success, from `0x725277600a1b1416eab510aabedbf6911e0bbd84`, to `0x000000000000740a22fa209cf6806d38f7605385`, value 0.000000 ETH, gas used 76824 at 77.0 gwei, fee 0.005915 ETH
- token transfers (Blockscout, decoded):
  - 0.127231 SSL (`0x0d9227f9`): `0x000000000000740a22fa209cf6806d38f7605385` -> `0x287856d10418e01ef1e93df9962b04d9a3a521c9`
  - 0.630026 WETH (`0xc02aaa39`): `0x287856d10418e01ef1e93df9962b04d9a3a521c9` -> `0x000000000000740a22fa209cf6806d38f7605385`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x0d9227f9c4ab3972f994fccc6eeba3213c0305c4` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x287856d10418e01ef1e93df9962b04d9a3a521c9` UniswapV2 Sync
  - `0x287856d10418e01ef1e93df9962b04d9a3a521c9` UniswapV2 Swap
- receipt status 1, index 129
