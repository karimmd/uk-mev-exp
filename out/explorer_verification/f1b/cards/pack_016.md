# pack_016

Block 12984142. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x3b5f0b047d4e6b65fc8250d81c5d95fcca6ab235a5a97fe10e3641ff914876f6`
- block 12984142, position 0, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 198523 at 24.2 gwei, fee 0.004800 ETH
- token transfers (Blockscout, decoded):
  - 310896.438133 USDC (`0xa0b86991`): `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` -> `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244`
  - 99.994507 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640`
  - 11445.287856 BOND (`0x0391d202`): `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` UniswapV3 Swap
  - `0x0391d2021f89dc339f60fff84546ea23e337750f` Transfer
  - `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` UniswapV2 Sync
  - `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x43854e69e14836951190d4584aae913042867a78ca8a156405402cb36b0df524`
- block 12984142, position 1, result success, from `0xb2edde593ddfcb46b8081ae557c43f5cbce73295`, to `0xa57bd00134b2850b2a1c55860c9e9ea100fdd6cf`, value 0.000000 ETH, gas used 117139 at 56.8 gwei, fee 0.006658 ETH
- token transfers (Blockscout, decoded):
  - 80774.518721 USDC (`0xa0b86991`): `0x56178a0d5f301baf6cf3e1cd53d9863437345bf9` -> `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244`
  - 2889.609089 BOND (`0x0391d202`): `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` -> `0x56178a0d5f301baf6cf3e1cd53d9863437345bf9`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x0391d2021f89dc339f60fff84546ea23e337750f` Transfer
  - `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` UniswapV2 Sync
  - `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x362ef1c07aa31cb815a44b454c1215e06a8209300afd6edd3626f5ac8d86519d`
- block 12984142, position 2, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.243284 ETH, gas used 201820 at 24.2 gwei, fee 0.004880 ETH
- token transfers (Blockscout, decoded):
  - 11445.287856 BOND (`0x0391d202`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244`
  - 312664.680000 USDC (`0xa0b86991`): `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 100.462361 WETH (`0xc02aaa39`): `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 312664.680000 USDC (`0xa0b86991`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640`
- internal ETH transfers (Etherscan):
  - 0.243284 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x0391d2021f89dc339f60fff84546ea23e337750f` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` UniswapV2 Sync
  - `0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` UniswapV3 Swap
- receipt status 1, index 2
