# pack_040

Block 12463798. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xd6be48c341b862c930ffac8066ceb52c1d67c72f6dd8437720947e1696094f0f`
- block 12463798, position 0, result success, from `0xeeaa58c690453b64c58191de8835fe26ea44e3a2`, to `0x575c3a99429352eda66661fc3857b9f83f58a73f`, value 0.000000 ETH, gas used 147987 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 17.977618 WETH (`0xc02aaa39`): `0x575c3a99429352eda66661fc3857b9f83f58a73f` -> `0xa7ad4ce6c21d9e875f1067cd377256326b483002`
  - 19776282967751.539062 SANSHU (`0xc73c167e`): `0xa7ad4ce6c21d9e875f1067cd377256326b483002` -> `0x575c3a99429352eda66661fc3857b9f83f58a73f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc73c167e7a4ba109e4052f70d5466d0c312a344d` Transfer
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Sync
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xa96aeaab1ebeccd4b27062276b872b0b98c1100f7a407849e05fe13fe280ef58`
- block 12463798, position 1, result success, from `0xc8f0a3328cc4a32ae419c55328940bdf699fb15d`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 160723 at 92.0 gwei, fee 0.014787 ETH
- token transfers (Blockscout, decoded):
  - 6.000000 LEASH (`0x27c70cd1`): `0xc8f0a3328cc4a32ae419c55328940bdf699fb15d` -> `0x874376be8231dad99aabf9ef0767b3cc054c60ee`
  - 6.497970 WETH (`0xc02aaa39`): `0x874376be8231dad99aabf9ef0767b3cc054c60ee` -> `0xa7ad4ce6c21d9e875f1067cd377256326b483002`
  - 6308639445003.263672 SANSHU (`0xc73c167e`): `0xa7ad4ce6c21d9e875f1067cd377256326b483002` -> `0xc8f0a3328cc4a32ae419c55328940bdf699fb15d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x27c70cd1946795b66be9d954418546998b546634` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x874376be8231dad99aabf9ef0767b3cc054c60ee` UniswapV2 Sync
  - `0x874376be8231dad99aabf9ef0767b3cc054c60ee` UniswapV2 Swap
  - `0xc73c167e7a4ba109e4052f70d5466d0c312a344d` Transfer
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Sync
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x076dbb139a296b9152543d736397596f7b9d191ec3527fdf915dab04eb61f122`
- block 12463798, position 2, result success, from `0xeeaa58c690453b64c58191de8835fe26ea44e3a2`, to `0x575c3a99429352eda66661fc3857b9f83f58a73f`, value 0.000000 ETH, gas used 120340 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 19380860481406.402344 SANSHU (`0xc73c167e`): `0x575c3a99429352eda66661fc3857b9f83f58a73f` -> `0xa7ad4ce6c21d9e875f1067cd377256326b483002`
  - 18.308539 WETH (`0xc02aaa39`): `0xa7ad4ce6c21d9e875f1067cd377256326b483002` -> `0x575c3a99429352eda66661fc3857b9f83f58a73f`
  - 0.231386 WETH (`0xc02aaa39`): `0x575c3a99429352eda66661fc3857b9f83f58a73f` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.231386 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x575c3a99429352eda66661fc3857b9f83f58a73f` [call]
  - 0.231386 ETH: `0x575c3a99429352eda66661fc3857b9f83f58a73f` -> `0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc73c167e7a4ba109e4052f70d5466d0c312a344d` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Sync
  - `0xa7ad4ce6c21d9e875f1067cd377256326b483002` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.231386 ETH for `0x575c3a99429352eda66661fc3857b9f83f58a73f`
- receipt status 1, index 2
