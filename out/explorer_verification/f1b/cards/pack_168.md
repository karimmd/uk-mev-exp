# pack_168

Block 13432062. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x6223b9d0c98b4c541889d6dba0ce2a83c24b3a4091805ad1f19711997265b4db`
- block 13432062, position 0, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 107431 at 64.3 gwei, fee 0.006912 ETH
- token transfers (Blockscout, decoded):
  - 0.290722 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xc352e35a7e5364e53073b4670d5f622438774a41`
  - 116252572492237.484375 FIRU (`0xe276056f`): `0xc352e35a7e5364e53073b4670d5f622438774a41` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe276056f924e15beac26f7b10b6d2805f9c64bb5` Transfer
  - `0xc352e35a7e5364e53073b4670d5f622438774a41` UniswapV2 Sync
  - `0xc352e35a7e5364e53073b4670d5f622438774a41` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x8a09346f53c6d1d83cd62f5f474dc8bc2b93832ea7e7388e99e69caeb764f853`
- block 13432062, position 1, result success, from `0xadde00b8a6957f79a1ad63c9364bdd6f7b8e4ef4`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 169796 at 74.8 gwei, fee 0.012701 ETH
- token transfers (Blockscout, decoded):
  - 160000000.000000 SHIB (`0x95ad61b0`): `0xadde00b8a6957f79a1ad63c9364bdd6f7b8e4ef4` -> `0x811beed0119b4afce20d2583eb608c6f7af1954f`
  - 1.054715 WETH (`0xc02aaa39`): `0x811beed0119b4afce20d2583eb608c6f7af1954f` -> `0xc352e35a7e5364e53073b4670d5f622438774a41`
  - 376811586173134.312500 FIRU (`0xe276056f`): `0xc352e35a7e5364e53073b4670d5f622438774a41` -> `0xadde00b8a6957f79a1ad63c9364bdd6f7b8e4ef4`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Transfer
  - `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x811beed0119b4afce20d2583eb608c6f7af1954f` UniswapV2 Sync
  - `0x811beed0119b4afce20d2583eb608c6f7af1954f` UniswapV2 Swap
  - `0xe276056f924e15beac26f7b10b6d2805f9c64bb5` Transfer
  - `0xc352e35a7e5364e53073b4670d5f622438774a41` UniswapV2 Sync
  - `0xc352e35a7e5364e53073b4670d5f622438774a41` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x9187e17ca4a677653b59b7b0676f1562c225b547c8e933c0ab417337c88043b3`
- block 13432062, position 2, result success, from `0x26ce7c1976c5eec83ea6ac22d83cb341b08850af`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 99240 at 314.4 gwei, fee 0.031205 ETH
- token transfers (Blockscout, decoded):
  - 113938882152028.328125 FIRU (`0xe276056f`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xc352e35a7e5364e53073b4670d5f622438774a41`
  - 0.330432 WETH (`0xc02aaa39`): `0xc352e35a7e5364e53073b4670d5f622438774a41` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xe276056f924e15beac26f7b10b6d2805f9c64bb5` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc352e35a7e5364e53073b4670d5f622438774a41` UniswapV2 Sync
  - `0xc352e35a7e5364e53073b4670d5f622438774a41` UniswapV2 Swap
- receipt status 1, index 2
