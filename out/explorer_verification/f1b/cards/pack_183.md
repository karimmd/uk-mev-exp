# pack_183

Block 12210358. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x5453c1217d060be9e8ac09649b241808bd64140afaa766b41635ad4997bd769b`
- block 12210358, position 0, result success, from `0xb38a9f021a3bf6bebcb7b7c4f4df3064b9143098`, to `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16`, value 0.000000 ETH, gas used 173332 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 99.999966 WETH (`0xc02aaa39`): `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16` -> `0x06da0fd433c1a5d7a4faa01111c044910a184553`
  - 215885.226414 USDT (`0xdac17f95`): `0x06da0fd433c1a5d7a4faa01111c044910a184553` -> `0x43747d31fc178d626047c5b4346a251418167a1a`
  - 712300.691802 NBNG (`0x9275e838`): `0x43747d31fc178d626047c5b4346a251418167a1a` -> `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Sync
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Swap
  - `0x9275e8386a5bdda160c0e621e9a6067b8fd88ea2` Transfer
  - `0x43747d31fc178d626047c5b4346a251418167a1a` UniswapV2 Sync
  - `0x43747d31fc178d626047c5b4346a251418167a1a` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x48ae178b37885aef783202075aeb7c4c3cc2547aa64c8823b5297a98e08f3443`
- block 12210358, position 1, result success, from `0x252e2e0e4cc5bd7391acb47634fb6bb382d08586`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 96426 at 82.8 gwei, fee 0.007979 ETH
- token transfers (Blockscout, decoded):
  - 42000.000000 USDT (`0xdac17f95`): `0x252e2e0e4cc5bd7391acb47634fb6bb382d08586` -> `0x43747d31fc178d626047c5b4346a251418167a1a`
  - 129315.553122 NBNG (`0x9275e838`): `0x43747d31fc178d626047c5b4346a251418167a1a` -> `0x252e2e0e4cc5bd7391acb47634fb6bb382d08586`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x9275e8386a5bdda160c0e621e9a6067b8fd88ea2` Transfer
  - `0x43747d31fc178d626047c5b4346a251418167a1a` UniswapV2 Sync
  - `0x43747d31fc178d626047c5b4346a251418167a1a` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x00cee8119c4aa7a6fe4536570335a70c37a7b48e000363637062715136e6a4d4`
- block 12210358, position 2, result success, from `0xb38a9f021a3bf6bebcb7b7c4f4df3064b9143098`, to `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16`, value 0.000000 ETH, gas used 126769 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 712300.691802 NBNG (`0x9275e838`): `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16` -> `0x43747d31fc178d626047c5b4346a251418167a1a`
  - 219274.501520 USDT (`0xdac17f95`): `0x43747d31fc178d626047c5b4346a251418167a1a` -> `0x06da0fd433c1a5d7a4faa01111c044910a184553`
  - 100.959853 WETH (`0xc02aaa39`): `0x06da0fd433c1a5d7a4faa01111c044910a184553` -> `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16`
- internal ETH transfers (Etherscan):
  - 0.479944 ETH: `0xf73d5d4962e08c1d572f56e2f3e2728a77507e16` -> `0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x9275e8386a5bdda160c0e621e9a6067b8fd88ea2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x43747d31fc178d626047c5b4346a251418167a1a` UniswapV2 Sync
  - `0x43747d31fc178d626047c5b4346a251418167a1a` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Sync
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Swap
- receipt status 1, index 2
