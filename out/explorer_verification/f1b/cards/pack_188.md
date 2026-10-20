# pack_188

Block 10248838. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xfcadf57caf963eb93357a32c221950a08d535cde6b6947340f005d25c0c462e2`
- block 10248838, position 1, result success, from `0xc3518561f4370c8b826bc6864616991b83327074`, to `0x4df3f167387f93fdc927a6e6d709f166b2ee279b`, value 0.000000 ETH, gas used 105798 at 65.0 gwei, fee 0.006877 ETH
- token transfers (Blockscout, decoded):
  - 2.419244 WETH (`0xc02aaa39`): `0x4df3f167387f93fdc927a6e6d709f166b2ee279b` -> `0x0000000000000000000000000000000000000000`
  - 2.419244 WETH (`0xc02aaa39`): `0x4df3f167387f93fdc927a6e6d709f166b2ee279b` -> `0xbd39b1f24b8960d3d7cd2c5471d0493496888185`
  - 260792.412133 UNIUSD (`0x256845e7`): `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` -> `0x4df3f167387f93fdc927a6e6d709f166b2ee279b`
  - 5322.294125 UNIUSD (`0x256845e7`): `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` -> `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea`
- internal ETH transfers (Etherscan):
  - 2.419244 ETH: `0x4df3f167387f93fdc927a6e6d709f166b2ee279b` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000000 ETH: `0x0b4099273571fc7d769c8474693fc2535545527d` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x8b8d1a23194e1f350cfe84b7ad9110c53577cef9` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0xd5fba2bb7785b552bb4b87950539efc84ecbb6cd` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x912aeba5e91f5359bb192501871106b027d2a290` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 2.419244 ETH for `0x4df3f167387f93fdc927a6e6d709f166b2ee279b`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` Transfer
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` Transfer
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` other
  - `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` UniswapV2 Sync
  - `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` UniswapV2 Swap
- receipt status 1, index 1

### Victim leg: `0x4ba17c9e32b84771fca4b7760da11fa09eaf7d2e1adaac15d38fd8456a4aae72`
- block 10248838, position 33, result success, from `0xb4705fd75ac926ff84a2467eb39a0be12892641f`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 2.800000 ETH, gas used 125168 at 35.0 gwei, fee 0.004381 ETH
- token transfers (Blockscout, decoded):
  - 2.800000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 2.800000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xbd39b1f24b8960d3d7cd2c5471d0493496888185`
  - 287107.143899 UNIUSD (`0x256845e7`): `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` -> `0xb4705fd75ac926ff84a2467eb39a0be12892641f`
  - 5859.329467 UNIUSD (`0x256845e7`): `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` -> `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea`
- internal ETH transfers (Etherscan):
  - 2.800000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 2.800000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` Transfer
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` Transfer
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` other
  - `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` UniswapV2 Sync
  - `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` UniswapV2 Swap
- receipt status 1, index 33

### Back leg: `0x9100ca05f372b21efeed36b675350f1769083bd893d416e015fdf8302bf61fe9`
- block 10248838, position 34, result success, from `0xc3518561f4370c8b826bc6864616991b83327074`, to `0x4df3f167387f93fdc927a6e6d709f166b2ee279b`, value 0.000000 ETH, gas used 89745 at 35.0 gwei, fee 0.003141 ETH
- token transfers (Blockscout, decoded):
  - 255576.563890 UNIUSD (`0x256845e7`): `0x4df3f167387f93fdc927a6e6d709f166b2ee279b` -> `0xbd39b1f24b8960d3d7cd2c5471d0493496888185`
  - 5215.848243 UNIUSD (`0x256845e7`): `0x4df3f167387f93fdc927a6e6d709f166b2ee279b` -> `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea`
  - 2.436503 WETH (`0xc02aaa39`): `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` -> `0x4df3f167387f93fdc927a6e6d709f166b2ee279b`
  - 2.436503 WETH (`0xc02aaa39`): `0x4df3f167387f93fdc927a6e6d709f166b2ee279b` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 2.436503 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x4df3f167387f93fdc927a6e6d709f166b2ee279b` [call]
  - 0.000000 ETH: `0x6cfdf8318f5270b18e95ea6c4958eac34b2614d4` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x6b26568d5f438765a48c0d30ecf1159393e6859d` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x8164685c820733e1662996233891ed29ebd3ac6a` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` Transfer
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` Transfer
  - `0x256845e721c0c46d54e6afbd4fa3b52cb72353ea` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` UniswapV2 Sync
  - `0xbd39b1f24b8960d3d7cd2c5471d0493496888185` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 2.436503 ETH for `0x4df3f167387f93fdc927a6e6d709f166b2ee279b`
- receipt status 1, index 34
