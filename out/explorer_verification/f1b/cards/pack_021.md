# pack_021

Block 13121246. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xd201e0e6c1e2d654888c9a8ab0757d8aa2146b56f6c6c679c3ac8dcdc8633398`
- block 13121246, position 7, result success, from `0x607bd5bbc7c6a2111273b28d4309e5c04b024f00`, to `0x66f049111958809841bbe4b81c034da2d953aa0c`, value 0.000000 ETH, gas used 88013 at 70.8 gwei, fee 0.006230 ETH
- token transfers (Blockscout, decoded):
  - 57.772711 WETH (`0xc02aaa39`): `0x66f049111958809841bbe4b81c034da2d953aa0c` -> `0x82dbc2673e9640343d263a3c55de49021ad39ae2`
  - 29779.520984 EDEN (`0x1559fa1b`): `0x82dbc2673e9640343d263a3c55de49021ad39ae2` -> `0x66f049111958809841bbe4b81c034da2d953aa0c`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1559fa1b8f28238fd5d76d9f434ad86fd20d1559` Transfer
  - `0x82dbc2673e9640343d263a3c55de49021ad39ae2` UniswapV2 Sync
  - `0x82dbc2673e9640343d263a3c55de49021ad39ae2` UniswapV2 Swap
- receipt status 1, index 7

### Victim leg: `0x124511c60acd039d69e0163101bb1c21003357f5030b1a6fb0c136088419925a`
- block 13121246, position 8, result success, from `0x3a213a156e21a0b89b1e430c1fad6c73ef310b04`, to `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`, value 74.000000 ETH, gas used 92151 at 65.0 gwei, fee 0.005985 ETH
- token transfers (Blockscout, decoded):
  - 74.000000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - 74.000000 WETH (`0xc02aaa39`): `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0x82dbc2673e9640343d263a3c55de49021ad39ae2`
  - 37931.100474 EDEN (`0x1559fa1b`): `0x82dbc2673e9640343d263a3c55de49021ad39ae2` -> `0x3a213a156e21a0b89b1e430c1fad6c73ef310b04`
- internal ETH transfers (Etherscan):
  - 74.000000 ETH: `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 74.000000 ETH for `0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1559fa1b8f28238fd5d76d9f434ad86fd20d1559` Transfer
  - `0x82dbc2673e9640343d263a3c55de49021ad39ae2` UniswapV2 Sync
  - `0x82dbc2673e9640343d263a3c55de49021ad39ae2` UniswapV2 Swap
- receipt status 1, index 8

### Back leg: `0x60c0eca74eb055ad64431f1cd3adda16553b6d74797e212143631b4a047ce0b9`
- block 13121246, position 9, result success, from `0x607bd5bbc7c6a2111273b28d4309e5c04b024f00`, to `0x66f049111958809841bbe4b81c034da2d953aa0c`, value 0.004506 ETH, gas used 86809 at 70.8 gwei, fee 0.006144 ETH
- token transfers (Blockscout, decoded):
  - 29779.520984 EDEN (`0x1559fa1b`): `0x66f049111958809841bbe4b81c034da2d953aa0c` -> `0x82dbc2673e9640343d263a3c55de49021ad39ae2`
  - 57.788830 WETH (`0xc02aaa39`): `0x82dbc2673e9640343d263a3c55de49021ad39ae2` -> `0x66f049111958809841bbe4b81c034da2d953aa0c`
- internal ETH transfers (Etherscan):
  - 0.004506 ETH: `0x66f049111958809841bbe4b81c034da2d953aa0c` -> `0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x1559fa1b8f28238fd5d76d9f434ad86fd20d1559` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x82dbc2673e9640343d263a3c55de49021ad39ae2` UniswapV2 Sync
  - `0x82dbc2673e9640343d263a3c55de49021ad39ae2` UniswapV2 Swap
- receipt status 1, index 9
