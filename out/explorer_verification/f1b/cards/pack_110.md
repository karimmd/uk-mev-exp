# pack_110

Block 13617654. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x1c89a41b4a03fe19f557eef7b897d910f9a078a832f531f3ad9334e7c5426f7a`
- block 13617654, position 0, result success, from `0x07ad46191db28b77525f103b88e57a773252d615`, to `0x55eb58655f8202ff839487886fedba2a1eb7b2d7`, value 0.000000 ETH, gas used 75544 at 169.6 gwei, fee 0.012811 ETH
- token transfers (Blockscout, decoded):
  - 6.720188 WETH (`0xc02aaa39`): `0x55eb58655f8202ff839487886fedba2a1eb7b2d7` -> `0x52127470de72e5ef77ca962d23125cbe096e2d81`
  - 3045916.795251 RACA (`0x12bb8905`): `0x52127470de72e5ef77ca962d23125cbe096e2d81` -> `0x700fc86c46299cf2a8fd86edadae3f57014351b0`
  - 31120.111039 USDT (`0xdac17f95`): `0x700fc86c46299cf2a8fd86edadae3f57014351b0` -> `0x55eb58655f8202ff839487886fedba2a1eb7b2d7`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x12bb890508c125661e03b09ec06e404bc9289040` Transfer
  - `0x52127470de72e5ef77ca962d23125cbe096e2d81` UniswapV2 Sync
  - `0x52127470de72e5ef77ca962d23125cbe096e2d81` UniswapV2 Swap
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x700fc86c46299cf2a8fd86edadae3f57014351b0` UniswapV2 Sync
  - `0x700fc86c46299cf2a8fd86edadae3f57014351b0` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xd89957d217348f593339f7ee4ff605c2abea31166272bba9a27c29a2c798ee7a`
- block 13617654, position 1, result success, from `0x27bc639b0392fa88552dbf6a4a4f81df7dc3a56b`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 106638 at 187.3 gwei, fee 0.019977 ETH
- token transfers (Blockscout, decoded):
  - 30000000.000000 RACA (`0x12bb8905`): `0x27bc639b0392fa88552dbf6a4a4f81df7dc3a56b` -> `0x700fc86c46299cf2a8fd86edadae3f57014351b0`
  - 298338.668700 USDT (`0xdac17f95`): `0x700fc86c46299cf2a8fd86edadae3f57014351b0` -> `0x27bc639b0392fa88552dbf6a4a4f81df7dc3a56b`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x12bb890508c125661e03b09ec06e404bc9289040` Transfer
  - `0x12bb890508c125661e03b09ec06e404bc9289040` Approval
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x700fc86c46299cf2a8fd86edadae3f57014351b0` UniswapV2 Sync
  - `0x700fc86c46299cf2a8fd86edadae3f57014351b0` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x10d702be76ef78c15f5cb031e5a694cefa180fd785c330c1ea53331f3315acaf`
- block 13617654, position 2, result success, from `0x07ad46191db28b77525f103b88e57a773252d615`, to `0x55eb58655f8202ff839487886fedba2a1eb7b2d7`, value 0.000000 ETH, gas used 88839 at 1649.6 gwei, fee 0.146546 ETH
- token transfers (Blockscout, decoded):
  - 31120.111039 USDT (`0xdac17f95`): `0x55eb58655f8202ff839487886fedba2a1eb7b2d7` -> `0x700fc86c46299cf2a8fd86edadae3f57014351b0`
  - 3179751.514862 RACA (`0x12bb8905`): `0x700fc86c46299cf2a8fd86edadae3f57014351b0` -> `0x52127470de72e5ef77ca962d23125cbe096e2d81`
  - 6.970486 WETH (`0xc02aaa39`): `0x52127470de72e5ef77ca962d23125cbe096e2d81` -> `0x55eb58655f8202ff839487886fedba2a1eb7b2d7`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x12bb890508c125661e03b09ec06e404bc9289040` Transfer
  - `0x700fc86c46299cf2a8fd86edadae3f57014351b0` UniswapV2 Sync
  - `0x700fc86c46299cf2a8fd86edadae3f57014351b0` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x52127470de72e5ef77ca962d23125cbe096e2d81` UniswapV2 Sync
  - `0x52127470de72e5ef77ca962d23125cbe096e2d81` UniswapV2 Swap
- receipt status 1, index 2
