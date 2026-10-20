# pack_130

Block 13897758. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe99b6819bc9e8b695a4698f7d0e3ce427bf87d170605c21e73406d32faefab41`
- block 13897758, position 0, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 69221 at 88.1 gwei, fee 0.006098 ETH
- token transfers (Blockscout, decoded):
  - 3.573203 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c`
  - 853131.590290 MX (`0xe0df31d0`): `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe0df31d06d72b2f5231489af0edc422b372f49f1` Transfer
  - `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` UniswapV2 Sync
  - `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x71e277e73eb5414dab6b45700f77702d5ef657b609b24f59e8516b464feb355d`
- block 13897758, position 1, result success, from `0x291d224a23359c7e727a7af1ed5dc64d6b545edc`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.500000 ETH, gas used 108261 at 90.0 gwei, fee 0.009743 ETH
- token transfers (Blockscout, decoded):
  - 0.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 0.500000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c`
  - 111564.026728 MX (`0xe0df31d0`): `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` -> `0x291d224a23359c7e727a7af1ed5dc64d6b545edc`
- internal ETH transfers (Etherscan):
  - 0.500000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.500000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe0df31d06d72b2f5231489af0edc422b372f49f1` Transfer
  - `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` UniswapV2 Sync
  - `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x520ccbd330e201a379c637261800e4ebce905d4d0bc5a10aca33231820a2f9e8`
- block 13897758, position 2, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.018820 ETH, gas used 68257 at 88.1 gwei, fee 0.006013 ETH
- token transfers (Blockscout, decoded):
  - 853131.462888 MX (`0xe0df31d0`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c`
  - 3.609082 WETH (`0xc02aaa39`): `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.018820 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x7f101fe45e6649a6fb8f3f8b43ed03d353f2b90c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xe0df31d06d72b2f5231489af0edc422b372f49f1` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` UniswapV2 Sync
  - `0x1965a114cc3341c0d2ba96a6361790b96ba8c20c` UniswapV2 Swap
- receipt status 1, index 2
