# pack_015

Block 12478758. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x8b3ed4a7836167050647a61b7ab4a05ddff1ddb275c915a80fdff660e9d387f5`
- block 12478758, position 0, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 95700 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 1.610000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x428bc363a7d743425863d6e5699683a69cacedc8`
  - 27800140841094.363281 JINU (`0x439dd02b`): `0x428bc363a7d743425863d6e5699683a69cacedc8` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xa0916cd2be200cc95b5b46f36d95889291c1bbe1` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0xa1a9ae88c9c042d7cb480103199679938170bd23` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x439dd02bfd144a5d6a5967895358e0d25d5ab784` Transfer
  - `0x428bc363a7d743425863d6e5699683a69cacedc8` UniswapV2 Sync
  - `0x428bc363a7d743425863d6e5699683a69cacedc8` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xd56674ad9cd66aabfd61889449fea84058ae85963e7f940b2e96ffa4d4a52689`
- block 12478758, position 1, result success, from `0x6e19cbe0122b3a4fe15967fe8f4559e94d1d59e7`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 178438 at 180.0 gwei, fee 0.032119 ETH
- token transfers (Blockscout, decoded):
  - 18920.638587 USDT (`0xdac17f95`): `0x6e19cbe0122b3a4fe15967fe8f4559e94d1d59e7` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 7.603724 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x428bc363a7d743425863d6e5699683a69cacedc8`
  - 120348693055582.265625 JINU (`0x439dd02b`): `0x428bc363a7d743425863d6e5699683a69cacedc8` -> `0x6e19cbe0122b3a4fe15967fe8f4559e94d1d59e7`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x439dd02bfd144a5d6a5967895358e0d25d5ab784` Transfer
  - `0x428bc363a7d743425863d6e5699683a69cacedc8` UniswapV2 Sync
  - `0x428bc363a7d743425863d6e5699683a69cacedc8` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x2a63ae4b65837c9f4b4ab7829308c03ada21fc35650554361c9273be063ad0ea`
- block 12478758, position 2, result success, from `0x4f69c5b694d5a14a0a595703175c478ec6b2a2fe`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.134622 ETH, gas used 110369 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 27244961757070.652344 JINU (`0x439dd02b`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x428bc363a7d743425863d6e5699683a69cacedc8`
  - 1.772641 WETH (`0xc02aaa39`): `0x428bc363a7d743425863d6e5699683a69cacedc8` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.134622 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xd224ca0c819e8e97ba0136b3b95ceff503b79f53` [call]
  - 0.000000 ETH: `0x453a901ed13916a722698e2ba9a260dbfb176f80` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
  - 0.000000 ETH: `0x654f93d1902643e75143904246244b8a7ed416e2` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x439dd02bfd144a5d6a5967895358e0d25d5ab784` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x428bc363a7d743425863d6e5699683a69cacedc8` UniswapV2 Sync
  - `0x428bc363a7d743425863d6e5699683a69cacedc8` UniswapV2 Swap
- receipt status 1, index 2
