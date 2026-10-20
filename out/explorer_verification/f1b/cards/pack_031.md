# pack_031

Block 11936414. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x30b2a853fea1c5becba449daa8c796f245acefe9c896b21640ca4517d5cc4bfc`
- block 11936414, position 29, result success, from `0x3dbe3107bdd0178f91dc3e882154ad8a9eca52a5`, to `0x78a55b9b3bbeffb36a43d9905f654d2769dc55e8`, value 0.000000 ETH, gas used 195059 at 134.2 gwei, fee 0.026177 ETH
- token transfers (Blockscout, decoded):
  - 0.084784 SOCKS (`0x23b60867`): `0x22d8432cc7aa4f8712a655fc4cdfb1baec29fca9` -> `0x78a55b9b3bbeffb36a43d9905f654d2769dc55e8`
  - 0.084784 SOCKS (`0x23b60867`): `0x78a55b9b3bbeffb36a43d9905f654d2769dc55e8` -> `0x0dacb47e00aed6abade32c7b398e029393e0d848`
  - 4.561977 WETH (`0xc02aaa39`): `0x0dacb47e00aed6abade32c7b398e029393e0d848` -> `0x78a55b9b3bbeffb36a43d9905f654d2769dc55e8`
  - 4.561977 WETH (`0xc02aaa39`): `0x78a55b9b3bbeffb36a43d9905f654d2769dc55e8` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 4.508070 ETH: `0x78a55b9b3bbeffb36a43d9905f654d2769dc55e8` -> `0x22d8432cc7aa4f8712a655fc4cdfb1baec29fca9` [call]
  - 4.561977 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x78a55b9b3bbeffb36a43d9905f654d2769dc55e8` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x23b608675a2b2fb1890d3abbd85c5775c51691d5` Transfer
  - `0x22d8432cc7aa4f8712a655fc4cdfb1baec29fca9` other
  - `0x23b608675a2b2fb1890d3abbd85c5775c51691d5` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0dacb47e00aed6abade32c7b398e029393e0d848` UniswapV2 Sync
  - `0x0dacb47e00aed6abade32c7b398e029393e0d848` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 4.561977 ETH for `0x78a55b9b3bbeffb36a43d9905f654d2769dc55e8`
- receipt status 1, index 29

### Victim leg: `0x379a3eaac17a7f0923d580d152054f3b54edc67ddd3462db1104a92261bbf4ac`
- block 11936414, position 52, result success, from `0x5b4eb01c4a876277fd3410245707c55211239970`, to `0x111111125434b319222cdbf8c261674adb56f3ae`, value 0.000000 ETH, gas used 217639 at 122.0 gwei, fee 0.026552 ETH
- token transfers (Blockscout, decoded):
  - 1300.000000 UNI (`0x1f9840a8`): `0x5b4eb01c4a876277fd3410245707c55211239970` -> `0xd3d2e2692501a5c9ca623199d38826e513033a17`
  - 21.062814 WETH (`0xc02aaa39`): `0xd3d2e2692501a5c9ca623199d38826e513033a17` -> `0x0dacb47e00aed6abade32c7b398e029393e0d848`
  - 0.381729 SOCKS (`0x23b60867`): `0x0dacb47e00aed6abade32c7b398e029393e0d848` -> `0xe069cb01d06ba617bcdf789bf2ff0d5e5ca20c71`
  - 0.381729 SOCKS (`0x23b60867`): `0xe069cb01d06ba617bcdf789bf2ff0d5e5ca20c71` -> `0x5b4eb01c4a876277fd3410245707c55211239970`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x1f9840a85d5af5bf1d1762f925bdaddc4201f984` Approval
  - `0x1f9840a85d5af5bf1d1762f925bdaddc4201f984` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd3d2e2692501a5c9ca623199d38826e513033a17` UniswapV2 Sync
  - `0xd3d2e2692501a5c9ca623199d38826e513033a17` UniswapV2 Swap
  - `0x23b608675a2b2fb1890d3abbd85c5775c51691d5` Transfer
  - `0x0dacb47e00aed6abade32c7b398e029393e0d848` UniswapV2 Sync
  - `0x0dacb47e00aed6abade32c7b398e029393e0d848` UniswapV2 Swap
  - `0x23b608675a2b2fb1890d3abbd85c5775c51691d5` Transfer
  - `0x111111125434b319222cdbf8c261674adb56f3ae` other
- receipt status 1, index 52

### Back leg: `0x8c3deaaa15ee80c45d897f4e06eeb6a5146a90b874e8a17a2e5a680133954eb6`
- block 11936414, position 53, result success, from `0xe47c990171cfe8cb8c81f5f6179d8521f7b809fd`, to `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`, value 0.000000 ETH, gas used 155636 at 122.0 gwei, fee 0.018988 ETH
- token transfers (Blockscout, decoded):
  - 0.151093 SOCKS (`0x23b60867`): `0x22d8432cc7aa4f8712a655fc4cdfb1baec29fca9` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - 0.151093 SOCKS (`0x23b60867`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0x0dacb47e00aed6abade32c7b398e029393e0d848`
  - 8.410940 WETH (`0xc02aaa39`): `0x0dacb47e00aed6abade32c7b398e029393e0d848` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - 8.410940 WETH (`0xc02aaa39`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 8.181578 ETH: `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0x22d8432cc7aa4f8712a655fc4cdfb1baec29fca9` [call]
  - 8.410940 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x23b608675a2b2fb1890d3abbd85c5775c51691d5` Transfer
  - `0x22d8432cc7aa4f8712a655fc4cdfb1baec29fca9` other
  - `0x23b608675a2b2fb1890d3abbd85c5775c51691d5` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0dacb47e00aed6abade32c7b398e029393e0d848` UniswapV2 Sync
  - `0x0dacb47e00aed6abade32c7b398e029393e0d848` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 8.410940 ETH for `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
- receipt status 1, index 53
