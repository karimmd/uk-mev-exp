# pack_167

Block 12694446. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x25794640453b3cfa0e17935288edd0cccc9d2427e41ec128f39a895f5b3286c6`
- block 12694446, position 3, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 69986 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.407100 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xc491405d542a393d8d202a72f0fb076447e61891`
  - 108071.189623 WHACKD (`0xcf833572`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
  - 12007.909958 WHACKD (`0xcf833572`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x04cccd30330bed99bc29e85f3e3bb748973cf1ac` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x54889cbb36dd3a3d94215a7c341a3c94406d8705` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Sync
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0xc060ad5ad13d58c05da4675c1103d55a78d578e6017abf91aba0e2e9a4204ad7`
- block 12694446, position 4, result success, from `0xbe23cbb62064b8b1550ae5ada59c39d45b1e2081`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 160841 at 10.0 gwei, fee 0.001608 ETH
- token transfers (Blockscout, decoded):
  - 3.712726 XOR (`0x40fd7225`): `0xbe23cbb62064b8b1550ae5ada59c39d45b1e2081` -> `0x01962144d41415cca072900fe87bbe2992a99f10`
  - 0.336872 WETH (`0xc02aaa39`): `0x01962144d41415cca072900fe87bbe2992a99f10` -> `0xc491405d542a393d8d202a72f0fb076447e61891`
  - 63900.000000 WHACKD (`0xcf833572`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0xbe23cbb62064b8b1550ae5ada59c39d45b1e2081`
  - 7100.000000 WHACKD (`0xcf833572`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x40fd72257597aa14c7231a7b1aaa29fce868f677` Transfer
  - `0x40fd72257597aa14c7231a7b1aaa29fce868f677` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x01962144d41415cca072900fe87bbe2992a99f10` UniswapV2 Sync
  - `0x01962144d41415cca072900fe87bbe2992a99f10` UniswapV2 Swap
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Sync
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0xd08f8de6b4e5cec7e6527370acc5a741d23c9ddfde614b0796afb838576c07cc`
- block 12694446, position 5, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.029122 ETH, gas used 75991 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 97264.070661 WHACKD (`0xcf833572`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xc491405d542a393d8d202a72f0fb076447e61891`
  - 10807.118962 WHACKD (`0xcf833572`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x0000000000000000000000000000000000000000`
  - 0.438214 WETH (`0xc02aaa39`): `0xc491405d542a393d8d202a72f0fb076447e61891` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.029122 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x04668ec2f57cc15c381b461b9fedab5d451c8f7f` [call]
  - 0.000000 ETH: `0xb20f4490176a1b3f7b02206cd944a8b7e60ddeea` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x7c85b2bbab2a371f22628a14215dc9e5969e4aa7` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xcf8335727b776d190f9d15a54e6b9b9348439eee` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Sync
  - `0xc491405d542a393d8d202a72f0fb076447e61891` UniswapV2 Swap
- receipt status 1, index 5
