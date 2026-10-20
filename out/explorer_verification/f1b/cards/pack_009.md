# pack_009

Block 13505102. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe41fbb99084c0c2fe709d5e3cf8aec1d363127a7b363b07bd8b0053dc53f42c9`
- block 13505102, position 3, result success, from `0x5b5001c4f80f33ec93b891062ed2e1d0acc05bb6`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 115835 at 125.1 gwei, fee 0.014486 ETH
- token transfers (Blockscout, decoded):
  - 2.510557 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x4d96369002fc5b9687ee924d458a7e5baa5df34e`
  - 113.434682 MPH (`0x8888801a`): `0x4d96369002fc5b9687ee924d458a7e5baa5df34e` -> `0xb2c29e311916a346304f83aa44527092d5bd4f0f`
  - 2.341998 WETH (`0xc02aaa39`): `0xb2c29e311916a346304f83aa44527092d5bd4f0f` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8888801af4d980682e47f1a9036e589479e835c5` Transfer
  - `0x4d96369002fc5b9687ee924d458a7e5baa5df34e` UniswapV2 Sync
  - `0x4d96369002fc5b9687ee924d458a7e5baa5df34e` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb2c29e311916a346304f83aa44527092d5bd4f0f` UniswapV2 Sync
  - `0xb2c29e311916a346304f83aa44527092d5bd4f0f` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0xda498d0efe02284d9b73350626a82ea728a3a2bfa5999049c3f5de2ffc2f7409`
- block 13505102, position 4, result success, from `0x1ca0e2851d79b866ce7ab34683ab20f4d7758fab`, to `0x11111112542d85b3ef69ae05771c2dccff4faa26`, value 0.000000 ETH, gas used 140930 at 216.4 gwei, fee 0.030493 ETH
- token transfers (Blockscout, decoded):
  - 348.539751 MPH (`0x8888801a`): `0x1ca0e2851d79b866ce7ab34683ab20f4d7758fab` -> `0xb2c29e311916a346304f83aa44527092d5bd4f0f`
  - 7.049926 WETH (`0xc02aaa39`): `0xb2c29e311916a346304f83aa44527092d5bd4f0f` -> `0x611cde65dea90918c0078ac0400a72b0d25b9bb1`
  - 27884.567757 REN (`0x408e4187`): `0x611cde65dea90918c0078ac0400a72b0d25b9bb1` -> `0x1ca0e2851d79b866ce7ab34683ab20f4d7758fab`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x8888801af4d980682e47f1a9036e589479e835c5` Transfer
  - `0x8888801af4d980682e47f1a9036e589479e835c5` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb2c29e311916a346304f83aa44527092d5bd4f0f` UniswapV2 Sync
  - `0xb2c29e311916a346304f83aa44527092d5bd4f0f` UniswapV2 Swap
  - `0x408e41876cccdc0f92210600ef50372656052a38` Transfer
  - `0x611cde65dea90918c0078ac0400a72b0d25b9bb1` UniswapV2 Sync
  - `0x611cde65dea90918c0078ac0400a72b0d25b9bb1` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x7ab430e98eb5009e8c6fd70fb68f86f5ff635c83f17f055fdfd5ab7449f1ee6e`
- block 13505102, position 5, result success, from `0x5b5001c4f80f33ec93b891062ed2e1d0acc05bb6`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.012270 ETH, gas used 104281 at 125.1 gwei, fee 0.013041 ETH
- token transfers (Blockscout, decoded):
  - 2.341998 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xb2c29e311916a346304f83aa44527092d5bd4f0f`
  - 116.287650 MPH (`0x8888801a`): `0xb2c29e311916a346304f83aa44527092d5bd4f0f` -> `0x4d96369002fc5b9687ee924d458a7e5baa5df34e`
  - 2.556263 WETH (`0xc02aaa39`): `0x4d96369002fc5b9687ee924d458a7e5baa5df34e` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.012270 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x7f101fe45e6649a6fb8f3f8b43ed03d353f2b90c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8888801af4d980682e47f1a9036e589479e835c5` Transfer
  - `0xb2c29e311916a346304f83aa44527092d5bd4f0f` UniswapV2 Sync
  - `0xb2c29e311916a346304f83aa44527092d5bd4f0f` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4d96369002fc5b9687ee924d458a7e5baa5df34e` UniswapV2 Sync
  - `0x4d96369002fc5b9687ee924d458a7e5baa5df34e` UniswapV2 Swap
- receipt status 1, index 5
