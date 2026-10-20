# pack_181

Block 12666022. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x49dfba56527989ec5b520f93ea65fb352617966f656a154ef1f05e1a9c6367eb`
- block 12666022, position 3, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 114824 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.147386 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x6af1becb78701f5919adb6f6932965abe4547763`
  - 31729722858.602436 KELPIE (`0x672d7b33`): `0x6af1becb78701f5919adb6f6932965abe4547763` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x672d7b3333d0f069a28b73a268bc6eaec65f2e1a` Transfer
  - `0x6af1becb78701f5919adb6f6932965abe4547763` UniswapV2 Sync
  - `0x6af1becb78701f5919adb6f6932965abe4547763` UniswapV2 Swap
- receipt status 1, index 3

### Victim leg: `0xde83cd4d9d268bf33316fc5b3c086f599ba032856d81bb4ba46e8dfebb90f26b`
- block 12666022, position 4, result success, from `0xa2e52ff98291862ad6c942e83341827edd560285`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 242100 at 21.0 gwei, fee 0.005084 ETH
- token transfers (Blockscout, decoded):
  - 404698340094.598816 BoomB (`0x82b89e0f`): `0xa2e52ff98291862ad6c942e83341827edd560285` -> `0xbbca2b6b6e8c76ba2d53f8d3cbab00a9e5535fe3`
  - 3.773087 WETH (`0xc02aaa39`): `0xbbca2b6b6e8c76ba2d53f8d3cbab00a9e5535fe3` -> `0x6af1becb78701f5919adb6f6932965abe4547763`
  - 728875405564.260498 KELPIE (`0x672d7b33`): `0x6af1becb78701f5919adb6f6932965abe4547763` -> `0xa2e52ff98291862ad6c942e83341827edd560285`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x82b89e0f9c0695639eb88659d0c306dbc242af96` Transfer
  - `0x82b89e0f9c0695639eb88659d0c306dbc242af96` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xbbca2b6b6e8c76ba2d53f8d3cbab00a9e5535fe3` UniswapV2 Sync
  - `0xbbca2b6b6e8c76ba2d53f8d3cbab00a9e5535fe3` UniswapV2 Swap
  - `0x672d7b3333d0f069a28b73a268bc6eaec65f2e1a` Transfer
  - `0x6af1becb78701f5919adb6f6932965abe4547763` UniswapV2 Sync
  - `0x6af1becb78701f5919adb6f6932965abe4547763` UniswapV2 Swap
- receipt status 1, index 4

### Back leg: `0x7a155e59de0913f7753fdfe559e6c1600de9c39b998b0ac3d3a44d70910843f3`
- block 12666022, position 5, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.023640 ETH, gas used 114070 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 31095611084.421932 KELPIE (`0x672d7b33`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x6af1becb78701f5919adb6f6932965abe4547763`
  - 0.173279 WETH (`0xc02aaa39`): `0x6af1becb78701f5919adb6f6932965abe4547763` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.023640 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xea674fdde714fd979de3edf0f56aa9716b898ec8` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x672d7b3333d0f069a28b73a268bc6eaec65f2e1a` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6af1becb78701f5919adb6f6932965abe4547763` UniswapV2 Sync
  - `0x6af1becb78701f5919adb6f6932965abe4547763` UniswapV2 Swap
- receipt status 1, index 5
