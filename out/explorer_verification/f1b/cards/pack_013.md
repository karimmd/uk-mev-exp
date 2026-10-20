# pack_013

Block 12554438. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x0d1d6c660a30406003d553e4069a95dc6e250ff94937d63c739ea224a8c0293c`
- block 12554438, position 8, result success, from `0x86254cb5a96c161e503d3255d67fdddec056fefe`, to `0xc65433d2a598c323e04fd143566b08609af008dc`, value 0.000000 ETH, gas used 75185 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.440000 WETH (`0xc02aaa39`): `0xc65433d2a598c323e04fd143566b08609af008dc` -> `0xd329d43715aa7b13f6d8aab5746fd824e7b643de`
  - 146.279741 COLLAR (`0x4cde0dd7`): `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` -> `0xc65433d2a598c323e04fd143566b08609af008dc`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x44430c194d9b6a62250397b6f8ebac80340a7a69` -> `0xc65433d2a598c323e04fd143566b08609af008dc` [self-destruct]
  - 0.000000 ETH: `0xf25bec03c0cb53932b9368f3a79f45cd41690286` -> `0xc65433d2a598c323e04fd143566b08609af008dc` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4cde0dd772eafe365728e6434e55e2c975df5f0f` Transfer
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Sync
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Swap
- receipt status 1, index 8

### Victim leg: `0x81dd011ac5653610dfa00ca6d045bdd850d681c5e5da705065fec55f6e01bb7b`
- block 12554438, position 9, result success, from `0x2e139cfea562cbdfdaf14c1c4b89106cb9218bd4`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.435935 ETH, gas used 108485 at 17.0 gwei, fee 0.001844 ETH
- token transfers (Blockscout, decoded):
  - 0.435935 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.435935 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xd329d43715aa7b13f6d8aab5746fd824e7b643de`
  - 138.174367 COLLAR (`0x4cde0dd7`): `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` -> `0x2e139cfea562cbdfdaf14c1c4b89106cb9218bd4`
- internal ETH transfers (Etherscan):
  - 0.435935 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.435935 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4cde0dd772eafe365728e6434e55e2c975df5f0f` Transfer
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Sync
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Swap
- receipt status 1, index 9

### Back leg: `0xae6aab99bd0bde5394748bfbcb6ee1c5edc27ec73de6bdd0f0b57385eaa62f1c`
- block 12554438, position 10, result success, from `0x86254cb5a96c161e503d3255d67fdddec056fefe`, to `0xc65433d2a598c323e04fd143566b08609af008dc`, value 0.018185 ETH, gas used 62728 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 146.279741 COLLAR (`0x4cde0dd7`): `0xc65433d2a598c323e04fd143566b08609af008dc` -> `0xd329d43715aa7b13f6d8aab5746fd824e7b643de`
  - 0.458185 WETH (`0xc02aaa39`): `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` -> `0xc65433d2a598c323e04fd143566b08609af008dc`
- internal ETH transfers (Etherscan):
  - 0.001819 ETH: `0xc65433d2a598c323e04fd143566b08609af008dc` -> `0x99c85bb64564d9ef9a99621301f22c9993cb89e3` [call]
  - 0.000000 ETH: `0x4ac866b4022bf0d6c0f21408dc32f86b335bfbd2` -> `0xc65433d2a598c323e04fd143566b08609af008dc` [self-destruct]
  - 0.000000 ETH: `0x1ef0b4c7eaace7694ae20ccde764646dcfb6d06b` -> `0xc65433d2a598c323e04fd143566b08609af008dc` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x4cde0dd772eafe365728e6434e55e2c975df5f0f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Sync
  - `0xd329d43715aa7b13f6d8aab5746fd824e7b643de` UniswapV2 Swap
- receipt status 1, index 10
