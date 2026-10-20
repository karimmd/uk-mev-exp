# pack_074

Block 12018078. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xecfa084dcfea8018ae27c8d29beee64dd5825e15840fe7dfca91cdfecaa422a7`
- block 12018078, position 14, result success, from `0x520db7c2161aa43fb7eb1bd87c40a084de2c5008`, to `0x00000000000064c443ef440577c26525a3c34a30`, value 0.000000 ETH, gas used 80513 at 225.7 gwei, fee 0.018174 ETH
- token transfers (Blockscout, decoded):
  - 930.701366 B20 (`0xc4de189a`): `0x00000000000064c443ef440577c26525a3c34a30` -> `0xe6f51e892046cb5b437e0033d990b527ea4367c8`
  - 14.841519 WETH (`0xc02aaa39`): `0xe6f51e892046cb5b437e0033d990b527ea4367c8` -> `0x00000000000064c443ef440577c26525a3c34a30`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc4de189abf94c57f396bd4c52ab13b954febefd8` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe6f51e892046cb5b437e0033d990b527ea4367c8` UniswapV2 Sync
  - `0xe6f51e892046cb5b437e0033d990b527ea4367c8` UniswapV2 Swap
- receipt status 1, index 14

### Victim leg: `0x68909ca3bb224101a450006645f50e1fd64931cc6cb6782b43616267541ce588`
- block 12018078, position 73, result success, from `0x228e402a8eeedd5d1062287bfb1fa0c87df6f69c`, to `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`, value 0.000000 ETH, gas used 237349 at 207.8 gwei, fee 0.049322 ETH
- token transfers (Blockscout, decoded):
  - 0.840656 WETH (`0xc02aaa39`): `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0x0000000000000000000000000000000000000000`
  - 0.840656 WETH (`0xc02aaa39`): `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0xe6f51e892046cb5b437e0033d990b527ea4367c8`
  - 52.746257 B20 (`0xc4de189a`): `0xe6f51e892046cb5b437e0033d990b527ea4367c8` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`
  - 52.018617 B20 (`0xc4de189a`): `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0x6f1a5cdf95a81c9c5fbf825c4a09b5ad94c47318`
  - 0.890753 WETH (`0xc02aaa39`): `0x6f1a5cdf95a81c9c5fbf825c4a09b5ad94c47318` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`
  - 0.890753 WETH (`0xc02aaa39`): `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.840656 ETH: `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.890753 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` [call]
  - 0.000000 ETH: `0x80ad88348041b2ef0882d6c58d0afb1ba826bb4a` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` [self-destruct]
  - 0.000000 ETH: `0x91e20a361189e64272fac2862352dfdba2dfc6da` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` [self-destruct]
  - 0.000000 ETH: `0xba694e8f56e3b4e608bbe23a9a049cb47ccd9cb1` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` [self-destruct]
  - 0.000000 ETH: `0x6ff10e73fb703da64e7f6c766bf5c026772be720` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` [self-destruct]
  - 0.000000 ETH: `0xcd81d9c2c18270de612e82174df3a95da223d225` -> `0x0000000000007f150bd6f54c40a34d7c3d5e9f56` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.840656 ETH for `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc4de189abf94c57f396bd4c52ab13b954febefd8` Transfer
  - `0xe6f51e892046cb5b437e0033d990b527ea4367c8` UniswapV2 Sync
  - `0xe6f51e892046cb5b437e0033d990b527ea4367c8` UniswapV2 Swap
  - `0x6f1a5cdf95a81c9c5fbf825c4a09b5ad94c47318` other
  - `0x6f1a5cdf95a81c9c5fbf825c4a09b5ad94c47318` other
  - `0xc4de189abf94c57f396bd4c52ab13b954febefd8` Transfer
  - `0xc4de189abf94c57f396bd4c52ab13b954febefd8` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.890753 ETH for `0x0000000000007f150bd6f54c40a34d7c3d5e9f56`
- receipt status 1, index 73

### Back leg: `0x182fffe60b25bf0459a8e47ba0671c0cc673e31d8ec85b5a51236f69351bab19`
- block 12018078, position 189, result success, from `0x520db7c2161aa43fb7eb1bd87c40a084de2c5008`, to `0x00000000000064c443ef440577c26525a3c34a30`, value 0.000000 ETH, gas used 89227 at 180.0 gwei, fee 0.016061 ETH
- token transfers (Blockscout, decoded):
  - 14.400110 WETH (`0xc02aaa39`): `0x00000000000064c443ef440577c26525a3c34a30` -> `0xe6f51e892046cb5b437e0033d990b527ea4367c8`
  - 930.701366 B20 (`0xc4de189a`): `0xe6f51e892046cb5b437e0033d990b527ea4367c8` -> `0x00000000000064c443ef440577c26525a3c34a30`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc4de189abf94c57f396bd4c52ab13b954febefd8` Transfer
  - `0xe6f51e892046cb5b437e0033d990b527ea4367c8` UniswapV2 Sync
  - `0xe6f51e892046cb5b437e0033d990b527ea4367c8` UniswapV2 Swap
- receipt status 1, index 189
