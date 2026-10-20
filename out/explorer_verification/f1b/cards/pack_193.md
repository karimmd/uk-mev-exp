# pack_193

Block 11708494. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x6201257943c92549c1aee8d450425905e0d76b4b57f17dc9e822fd108c6f8c3e`
- block 11708494, position 24, result success, from `0x979636bfeecd6a3ba720cf6eb8b7135f247e0b4a`, to `0x7a08ed5862ba4c2887ef169a17637eadb27beecf`, value 0.000000 ETH, gas used 134331 at 133.0 gwei, fee 0.017866 ETH
- token transfers (Blockscout, decoded):
  - 7.440000 WETH (`0xc02aaa39`): `0x7a08ed5862ba4c2887ef169a17637eadb27beecf` -> `0x0000000000000000000000000000000000000000`
  - 7.440000 WETH (`0xc02aaa39`): `0x7a08ed5862ba4c2887ef169a17637eadb27beecf` -> `0xaadb00551312a3c2a8b46597a39ef1105afb2c08`
  - 39651792.148310 AXN (`0x71f85b2e`): `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` -> `0x7a08ed5862ba4c2887ef169a17637eadb27beecf`
- internal ETH transfers (Etherscan):
  - 7.440000 ETH: `0x7a08ed5862ba4c2887ef169a17637eadb27beecf` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 7.440000 ETH for `0x7a08ed5862ba4c2887ef169a17637eadb27beecf`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x71f85b2e46976bd21302b64329868fd15eb0d127` Transfer
  - `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` UniswapV2 Sync
  - `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` UniswapV2 Swap
- receipt status 1, index 24

### Victim leg: `0xbd3cdc0cc6a29e19acbf08b8fdcd0ad4deeaaf87ecf0f38e36e213354e0db55a`
- block 11708494, position 25, result success, from `0x273bd834e6852ea44e0988b9e5b8d56090fe5edf`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 149060 at 133.0 gwei, fee 0.019825 ETH
- token transfers (Blockscout, decoded):
  - 8048.766176 USDT (`0xdac17f95`): `0x273bd834e6852ea44e0988b9e5b8d56090fe5edf` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 6.656208 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0xaadb00551312a3c2a8b46597a39ef1105afb2c08`
  - 35000000.000000 AXN (`0x71f85b2e`): `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` -> `0x273bd834e6852ea44e0988b9e5b8d56090fe5edf`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x71f85b2e46976bd21302b64329868fd15eb0d127` Transfer
  - `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` UniswapV2 Sync
  - `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` UniswapV2 Swap
- receipt status 1, index 25

### Back leg: `0x238ea7bfa6c49b884cd6fdb0027266340fa4228f7657d11ad488e117a5c6f235`
- block 11708494, position 26, result success, from `0x979636bfeecd6a3ba720cf6eb8b7135f247e0b4a`, to `0x7a08ed5862ba4c2887ef169a17637eadb27beecf`, value 0.000000 ETH, gas used 118403 at 133.0 gwei, fee 0.015748 ETH
- token transfers (Blockscout, decoded):
  - 39651792.148310 AXN (`0x71f85b2e`): `0x7a08ed5862ba4c2887ef169a17637eadb27beecf` -> `0xaadb00551312a3c2a8b46597a39ef1105afb2c08`
  - 7.489721 WETH (`0xc02aaa39`): `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` -> `0x7a08ed5862ba4c2887ef169a17637eadb27beecf`
  - 7.489721 WETH (`0xc02aaa39`): `0x7a08ed5862ba4c2887ef169a17637eadb27beecf` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 7.489721 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a08ed5862ba4c2887ef169a17637eadb27beecf` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x71f85b2e46976bd21302b64329868fd15eb0d127` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` UniswapV2 Sync
  - `0xaadb00551312a3c2a8b46597a39ef1105afb2c08` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 7.489721 ETH for `0x7a08ed5862ba4c2887ef169a17637eadb27beecf`
- receipt status 1, index 26
