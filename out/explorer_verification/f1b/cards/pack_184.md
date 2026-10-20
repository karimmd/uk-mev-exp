# pack_184

Block 13720878. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x45c371862eda463a575de6430c9d8a77a75044a722b09c2392b8cf07c600bd4a`
- block 13720878, position 0, result success, from `0xb7ab1de5b259a880c4bb5451bdbe6f80f3798538`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 112316 at 76.6 gwei, fee 0.008607 ETH
- token transfers (Blockscout, decoded):
  - 42.944214 WBTC (`0x2260fac5`): `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 524.854919 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed` UniswapV3 Swap
- receipt status 1, index 0

### Victim leg: `0xb938e8dd563ff13c7dba873f289a0113c21471eb52fe93d8320c71b962dca1e5`
- block 13720878, position 1, result success, from `0x58c0a5f11469ea49ad1bf0ad0d25a5cae582dd0a`, to `0xdef1c0ded9bec7f1a1670819833240f027b25eff`, value 5180.000000 ETH, gas used 1044691 at 108.0 gwei, fee 0.112827 ETH
- token transfers (Blockscout, decoded):
  - 5180.000000 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0x0000000000000000000000000000000000000000`
  - 4.844669 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0x2fa96250cf4eafe165ed7cd3f05e32a99e271566`
  - 0.398375 WBTC (`0x2260fac5`): `0x2fa96250cf4eafe165ed7cd3f05e32a99e271566` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 206.196186 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0x1d22397edfc4edf622d692050635bfc1febf1404`
  - 16.877275 WBTC (`0x2260fac5`): `0x1d22397edfc4edf622d692050635bfc1febf1404` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 258.659200 WBTC (`0x2260fac5`): `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 3224.617992 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed`
  - 921.919822 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xd51a44d3fae010294c616388b506acda1bfaae46`
  - 75.293982 WBTC (`0x2260fac5`): `0xd51a44d3fae010294c616388b506acda1bfaae46` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 292.440864 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xceff51756c56ceffca006cd410b03ffc46dd3a58`
  - 23.820541 WBTC (`0x2260fac5`): `0xceff51756c56ceffca006cd410b03ffc46dd3a58` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 292.440864 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xba12222222228d8ba445958a75a0704d566bf2c8`
  - 23.850676 WBTC (`0x2260fac5`): `0xba12222222228d8ba445958a75a0704d566bf2c8` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 237.539603 WETH (`0xc02aaa39`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xbb2b8038a1640196fbe3e38816f3e67cba72d940`
  - 19.269518 WBTC (`0x2260fac5`): `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - 418.169567 WBTC (`0x2260fac5`): `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0x58c0a5f11469ea49ad1bf0ad0d25a5cae582dd0a`
- internal ETH transfers (Etherscan):
  - 5180.000000 ETH: `0xdef1c0ded9bec7f1a1670819833240f027b25eff` -> `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` [call]
  - 5180.000000 ETH: `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 5180.000000 ETH for `0x22f9dcf4647084d6c31b2765f6910cd85c178c18`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xdef1c0ded9bec7f1a1670819833240f027b25eff` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xdef1c0ded9bec7f1a1670819833240f027b25eff` other
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed` UniswapV3 Swap
  - `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xd51a44d3fae010294c616388b506acda1bfaae46` other
  - `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xceff51756c56ceffca006cd410b03ffc46dd3a58` UniswapV2 Sync
  - `0xceff51756c56ceffca006cd410b03ffc46dd3a58` UniswapV2 Swap
  - `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` other
  - `0xba12222222228d8ba445958a75a0704d566bf2c8` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` other
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` UniswapV2 Sync
  - `0xbb2b8038a1640196fbe3e38816f3e67cba72d940` UniswapV2 Swap
  - `0x22f9dcf4647084d6c31b2765f6910cd85c178c18` other
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xdef1c0ded9bec7f1a1670819833240f027b25eff` other
- receipt status 1, index 1

### Back leg: `0x7148a464defd215536189b083a5b0229663303c71c10d1c680e7707f99e3f33f`
- block 13720878, position 2, result success, from `0xb7ab1de5b259a880c4bb5451bdbe6f80f3798538`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 13.666852 ETH, gas used 115747 at 76.6 gwei, fee 0.008870 ETH
- token transfers (Blockscout, decoded):
  - 539.602972 WETH (`0xc02aaa39`): `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 42.944214 WBTC (`0x2260fac5`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed`
- internal ETH transfers (Etherscan):
  - 13.666852 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x1ad91ee08f21be3de0ba2ba6918e714da6b45836` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xcbcdf9626bc03e24f779434178a73a0b4bad62ed` UniswapV3 Swap
- receipt status 1, index 2
