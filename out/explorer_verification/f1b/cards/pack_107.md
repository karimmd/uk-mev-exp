# pack_107

Block 12451126. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xd5455e69876b71c30f62036011bdcc7ce5fa69fca285a8f0de60e62ccc241e06`
- block 12451126, position 0, result success, from `0x3376ebc8dce3453a045a145ab7b1e728b2ed581e`, to `0x59903993ae67bf48f10832e9be28935fee04d6f6`, value 0.000000 ETH, gas used 77202 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 2.303848 WETH (`0xc02aaa39`): `0x59903993ae67bf48f10832e9be28935fee04d6f6` -> `0xd65e975c7d0d5871eff8b079120e43c9f377ada1`
  - 4441.946284 YOP (`0xae1eaae3`): `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` -> `0x59903993ae67bf48f10832e9be28935fee04d6f6`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xdef1d93b23a9bdfdb032e8463995160d335d8189` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x5453e2fea1d23f41fc5e0dd62317f7a04d51f7a6` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x49e53682a78f797f916ef4de180cf59f4701ea50` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xae1eaae3f627aaca434127644371b67b18444051` Transfer
  - `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` UniswapV2 Sync
  - `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xadd418d87662b324e4aaf406cf93c1d4e9b281a6206e4e22bab4e036daf16b57`
- block 12451126, position 1, result success, from `0x865fda64c867d6c23d6b8a61ca99000c9f2c23c0`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 150851 at 64.9 gwei, fee 0.009790 ETH
- token transfers (Blockscout, decoded):
  - 1048646901.880000 SHIB (`0x95ad61b0`): `0x865fda64c867d6c23d6b8a61ca99000c9f2c23c0` -> `0x811beed0119b4afce20d2583eb608c6f7af1954f`
  - 4.848114 WETH (`0xc02aaa39`): `0x811beed0119b4afce20d2583eb608c6f7af1954f` -> `0xd65e975c7d0d5871eff8b079120e43c9f377ada1`
  - 9207.603949 YOP (`0xae1eaae3`): `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` -> `0x865fda64c867d6c23d6b8a61ca99000c9f2c23c0`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Transfer
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x811beed0119b4afce20d2583eb608c6f7af1954f` UniswapV2 Sync
  - `0x811beed0119b4afce20d2583eb608c6f7af1954f` UniswapV2 Swap
  - `0xae1eaae3f627aaca434127644371b67b18444051` Transfer
  - `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` UniswapV2 Sync
  - `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x133463a94e9c4411e06d89e523d8a8467906e1c2da5fb7941f2afeb9e34588e6`
- block 12451126, position 2, result success, from `0x3376ebc8dce3453a045a145ab7b1e728b2ed581e`, to `0x59903993ae67bf48f10832e9be28935fee04d6f6`, value 0.000000 ETH, gas used 70602 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 4441.946284 YOP (`0xae1eaae3`): `0x59903993ae67bf48f10832e9be28935fee04d6f6` -> `0xd65e975c7d0d5871eff8b079120e43c9f377ada1`
  - 2.337182 WETH (`0xc02aaa39`): `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` -> `0x59903993ae67bf48f10832e9be28935fee04d6f6`
  - 0.029834 WETH (`0xc02aaa39`): `0x59903993ae67bf48f10832e9be28935fee04d6f6` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x069ce80c965a0e78a46664ab637cfaf8c9fcd6be` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x47748414843631fbeb184f387f64a787b4b9320c` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.029834 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x59903993ae67bf48f10832e9be28935fee04d6f6` [call]
  - 0.029834 ETH: `0x59903993ae67bf48f10832e9be28935fee04d6f6` -> `0x1ad91ee08f21be3de0ba2ba6918e714da6b45836` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xae1eaae3f627aaca434127644371b67b18444051` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` UniswapV2 Sync
  - `0xd65e975c7d0d5871eff8b079120e43c9f377ada1` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.029834 ETH for `0x59903993ae67bf48f10832e9be28935fee04d6f6`
- receipt status 1, index 2
