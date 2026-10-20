# pack_133

Block 13297950. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x6ecefc11eb168398bcd124919eb12b36f377c278457a92063af7eda359a57aee`
- block 13297950, position 0, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 220636 at 32.6 gwei, fee 0.007195 ETH
- token transfers (Blockscout, decoded):
  - 5317.136449 CFG (`0xc221b7e6`): `0x6127cc12b45b7a765d6509e191d23ca97badd8d1` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 2.421606 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x6127cc12b45b7a765d6509e191d23ca97badd8d1`
  - 6412.918549 USDC (`0xa0b86991`): `0x7270233ccae676e776a659affc35219e6fcfbb10` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 5317.136449 CFG (`0xc221b7e6`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x7270233ccae676e776a659affc35219e6fcfbb10`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc221b7e65ffc80de234bbb6667abdd46593d34f0` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6127cc12b45b7a765d6509e191d23ca97badd8d1` UniswapV3 Swap
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc221b7e65ffc80de234bbb6667abdd46593d34f0` Transfer
  - `0x7270233ccae676e776a659affc35219e6fcfbb10` UniswapV3 Swap
- receipt status 1, index 0

### Victim leg: `0x3049ce3224488e5e420a66f511255d47a1c36c078b6017623a676d63bc843933`
- block 13297950, position 1, result success, from `0xcf1ba0985f328b894ca55697c0fc2a39058a5b8a`, to `0xe592427a0aece92de3edee1f18e0157c05861564`, value 0.000000 ETH, gas used 143198 at 34.1 gwei, fee 0.004885 ETH
- token transfers (Blockscout, decoded):
  - 31278.829560 USDC (`0xa0b86991`): `0x7270233ccae676e776a659affc35219e6fcfbb10` -> `0xcf1ba0985f328b894ca55697c0fc2a39058a5b8a`
  - 26312.253155 CFG (`0xc221b7e6`): `0xcf1ba0985f328b894ca55697c0fc2a39058a5b8a` -> `0x7270233ccae676e776a659affc35219e6fcfbb10`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0xc221b7e65ffc80de234bbb6667abdd46593d34f0` Transfer
  - `0x7270233ccae676e776a659affc35219e6fcfbb10` UniswapV3 Swap
- receipt status 1, index 1

### Back leg: `0x1337ea52b13d2866ad01a3977bb03b64054d56df6ac7a2c281ebb77c21ab0d21`
- block 13297950, position 2, result success, from `0x4f80b2cd1f550f81581c15f690bdd623f3824c86`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 213705 at 80.6 gwei, fee 0.017227 ETH
- token transfers (Blockscout, decoded):
  - 5416.720108 CFG (`0xc221b7e6`): `0x7270233ccae676e776a659affc35219e6fcfbb10` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 6412.918549 USDC (`0xa0b86991`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x7270233ccae676e776a659affc35219e6fcfbb10`
  - 2.448867 WETH (`0xc02aaa39`): `0x6127cc12b45b7a765d6509e191d23ca97badd8d1` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
  - 5416.720108 CFG (`0xc221b7e6`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x6127cc12b45b7a765d6509e191d23ca97badd8d1`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc221b7e65ffc80de234bbb6667abdd46593d34f0` Transfer
  - `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` Transfer
  - `0x7270233ccae676e776a659affc35219e6fcfbb10` UniswapV3 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc221b7e65ffc80de234bbb6667abdd46593d34f0` Transfer
  - `0x6127cc12b45b7a765d6509e191d23ca97badd8d1` UniswapV3 Swap
- receipt status 1, index 2
