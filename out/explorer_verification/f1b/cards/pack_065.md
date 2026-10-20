# pack_065

Block 14001070. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x7769f6db5fae7189d6806696aa88f319d056a9704d4cd29baa7ed557483b4dc0`
- block 14001070, position 1, result success, from `0x1dd71645847ba3a22df1261ad32d66d9a701552d`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 80973 at 209.1 gwei, fee 0.016934 ETH
- token transfers (Blockscout, decoded):
  - 2.299594 WETH (`0xc02aaa39`): `0x4b3d09151ad295623ac9e50967739fd437b0d892` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 2.690160 WETH (`0xc02aaa39`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x06bf054b9aafc075f9be814e1b7f948c6e845596`
  - 2397.679557 NCR (`0xdb5c3c46`): `0x06bf054b9aafc075f9be814e1b7f948c6e845596` -> `0x4b3d09151ad295623ac9e50967739fd437b0d892`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdb5c3c46e28b53a39c255aa39a411dd64e5fed9c` Transfer
  - `0x06bf054b9aafc075f9be814e1b7f948c6e845596` UniswapV2 Sync
  - `0x06bf054b9aafc075f9be814e1b7f948c6e845596` UniswapV2 Swap
  - `0x4b3d09151ad295623ac9e50967739fd437b0d892` UniswapV3 Swap
- receipt status 1, index 1

### Victim leg: `0x25429647a891cfd67df109ca6d18132bba8f5670b40a48d2dc17578763639eac`
- block 14001070, position 2, result success, from `0x45d29b661f9351abb53d3412ffe8852e6708f9d0`, to `0xdef1c0ded9bec7f1a1670819833240f027b25eff`, value 0.000000 ETH, gas used 296998 at 211.0 gwei, fee 0.062667 ETH
- token transfers (Blockscout, decoded):
  - 6.898616 WETH (`0xc02aaa39`): `0x4b3d09151ad295623ac9e50967739fd437b0d892` -> `0xdef1c0ded9bec7f1a1670819833240f027b25eff`
  - 7354.613076 NCR (`0xdb5c3c46`): `0x45d29b661f9351abb53d3412ffe8852e6708f9d0` -> `0x4b3d09151ad295623ac9e50967739fd437b0d892`
  - 26808.745265 USDC (`0xa0b86991`): `0xdd005650ac6805457f4fa6ee1816813ce815e914` -> `0xdef1c0ded9bec7f1a1670819833240f027b25eff`
  - 8645.386924 NCR (`0xdb5c3c46`): `0x45d29b661f9351abb53d3412ffe8852e6708f9d0` -> `0xdd005650ac6805457f4fa6ee1816813ce815e914`
  - 8.188972 WETH (`0xc02aaa39`): `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` -> `0xdef1c0ded9bec7f1a1670819833240f027b25eff`
  - 26808.745265 USDC (`0xa0b86991`): `0xdef1c0ded9bec7f1a1670819833240f027b25eff` -> `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640`
  - 15.087588 WETH (`0xc02aaa39`): `0xdef1c0ded9bec7f1a1670819833240f027b25eff` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 15.087588 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0xdef1c0ded9bec7f1a1670819833240f027b25eff` [call]
  - 15.087588 ETH: `0xdef1c0ded9bec7f1a1670819833240f027b25eff` -> `0x45d29b661f9351abb53d3412ffe8852e6708f9d0` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdb5c3c46e28b53a39c255aa39a411dd64e5fed9c` Transfer
  - `0x4b3d09151ad295623ac9e50967739fd437b0d892` UniswapV3 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xdb5c3c46e28b53a39c255aa39a411dd64e5fed9c` Transfer
  - `0xdd005650ac6805457f4fa6ee1816813ce815e914` UniswapV3 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` UniswapV3 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 15.087588 ETH for `0xdef1c0ded9bec7f1a1670819833240f027b25eff`
- receipt status 1, index 2

### Back leg: `0x4660378aa890ab5e1fcc36dfced6307c96f57c412ae8a06f6c621a8488413552`
- block 14001070, position 3, result success, from `0x1dd71645847ba3a22df1261ad32d66d9a701552d`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.014752 ETH, gas used 80879 at 209.1 gwei, fee 0.016914 ETH
- token transfers (Blockscout, decoded):
  - 2937.873226 NCR (`0xdb5c3c46`): `0x4b3d09151ad295623ac9e50967739fd437b0d892` -> `0x06bf054b9aafc075f9be814e1b7f948c6e845596`
  - 3.197034 WETH (`0xc02aaa39`): `0x06bf054b9aafc075f9be814e1b7f948c6e845596` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 2.744587 WETH (`0xc02aaa39`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x4b3d09151ad295623ac9e50967739fd437b0d892`
- internal ETH transfers (Etherscan):
  - 0.014752 ETH: `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x7f101fe45e6649a6fb8f3f8b43ed03d353f2b90c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xdb5c3c46e28b53a39c255aa39a411dd64e5fed9c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x06bf054b9aafc075f9be814e1b7f948c6e845596` UniswapV2 Sync
  - `0x06bf054b9aafc075f9be814e1b7f948c6e845596` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4b3d09151ad295623ac9e50967739fd437b0d892` UniswapV3 Swap
- receipt status 1, index 3
