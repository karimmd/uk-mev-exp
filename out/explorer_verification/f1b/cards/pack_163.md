# pack_163

Block 12904766. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x2dc66b3a487525cd3927825b312e3f1a854dfeafe38c782f2d933861d0db213f`
- block 12904766, position 3, result success, from `0x30b8235f492265a734347c0bf36e2ffcad887be2`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 56360 at 0.0 gwei, fee 0.000002 ETH
- token transfers (Blockscout, decoded):
  - 0.246800 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x020e6d0e80d08567ecb14f942fa326748407a845`
  - 166.047434 UNQT (`0xa80f2c8f`): `0x020e6d0e80d08567ecb14f942fa326748407a845` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xb10ac5a3334249ebe5b113a750cc2c49a1e5dc74` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x1058f5be38764fb1e108d9b70dbec5cb101ad675` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa80f2c8f61c56546001f5fc2eb8d6e4e72c45d4c` Transfer
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Sync
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0x198bc9b88e8d0a2ddc3a8f0975a16f96db37c45ef1378c4cd78409b17cdb1deb`
- block 12904766, position 4, result success, from `0x7ad7087a708f24f782d897e1652d2abc15290a11`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 141340 at 20.9 gwei, fee 0.002954 ETH
- token transfers (Blockscout, decoded):
  - 1074.015811 USDT (`0xdac17f95`): `0x7ad7087a708f24f782d897e1652d2abc15290a11` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 0.478071 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x020e6d0e80d08567ecb14f942fa326748407a845`
  - 292.064161 UNQT (`0xa80f2c8f`): `0x020e6d0e80d08567ecb14f942fa326748407a845` -> `0x7ad7087a708f24f782d897e1652d2abc15290a11`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0xa80f2c8f61c56546001f5fc2eb8d6e4e72c45d4c` Transfer
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Sync
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0xf18236921dd9da0b0091c253d690b2ecf47cce0af972440eae1d95e7f7b5c439`
- block 12904766, position 5, result success, from `0x30b8235f492265a734347c0bf36e2ffcad887be2`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 48532 at 591.4 gwei, fee 0.028701 ETH
- token transfers (Blockscout, decoded):
  - 166.047434 UNQT (`0xa80f2c8f`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x020e6d0e80d08567ecb14f942fa326748407a845`
  - 0.277501 WETH (`0xc02aaa39`): `0x020e6d0e80d08567ecb14f942fa326748407a845` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xfd8f0f9207d1625ab891f10ede6927428cc8ed8f` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x5c3b8dd7b1d13f5b56f545bdab3207eb062d6931` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xa80f2c8f61c56546001f5fc2eb8d6e4e72c45d4c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Sync
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Swap
- receipt status 1, index 5
