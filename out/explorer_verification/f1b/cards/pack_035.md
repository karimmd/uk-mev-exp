# pack_035

Block 12349926. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x32d93c42180ae62855d2fc181ec883c54c2ec901b63d3bbca350b671e2cf4ca8`
- block 12349926, position 232, result success, from `0xb9ce805e792ac6ab5055054d1a43954b8d1647c9`, to `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`, value 0.000000 ETH, gas used 93691 at 56.0 gwei, fee 0.005247 ETH
- token transfers (Blockscout, decoded):
  - 261577.898309 RVP (`0x17ef75aa`): `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de` -> `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c`
  - 9.707000 WETH (`0xc02aaa39`): `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` -> `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x17ef75aa22dd5f6c2763b8304ab24f40ee54d48a` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` UniswapV2 Sync
  - `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` UniswapV2 Swap
- receipt status 1, index 232

### Victim leg: `0x0618bf2569b900e23948636b9bb8dcd1751c4096805c9df165b2bf87d6c7104c`
- block 12349926, position 233, result success, from `0xc30689bf84f9d95dd4bcffc76d0ee8b238d197a7`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 152212 at 56.0 gwei, fee 0.008524 ETH
- token transfers (Blockscout, decoded):
  - 150000.000000 RVP (`0x17ef75aa`): `0xc30689bf84f9d95dd4bcffc76d0ee8b238d197a7` -> `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c`
  - 5.360920 WETH (`0xc02aaa39`): `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 15640.541405 USDT (`0xdac17f95`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0xc30689bf84f9d95dd4bcffc76d0ee8b238d197a7`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x17ef75aa22dd5f6c2763b8304ab24f40ee54d48a` Transfer
  - `0x17ef75aa22dd5f6c2763b8304ab24f40ee54d48a` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` UniswapV2 Sync
  - `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` UniswapV2 Swap
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
- receipt status 1, index 233

### Back leg: `0x179461f381a74a336f57312fa1ab8a55914c59877dc9910b13baec09ad0e85d7`
- block 12349926, position 234, result success, from `0xb9ce805e792ac6ab5055054d1a43954b8d1647c9`, to `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`, value 0.000000 ETH, gas used 83742 at 56.0 gwei, fee 0.004690 ETH
- token transfers (Blockscout, decoded):
  - 9.501490 WETH (`0xc02aaa39`): `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de` -> `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c`
  - 261577.898309 RVP (`0x17ef75aa`): `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` -> `0x3dad8cf200799f82fd8eb68f608220d8f3ebf8de`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x17ef75aa22dd5f6c2763b8304ab24f40ee54d48a` Transfer
  - `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` UniswapV2 Sync
  - `0xee9b50b74a132912cf55e7699ef3aa7ae2b00e0c` UniswapV2 Swap
- receipt status 1, index 234
