# pack_075

Block 11933950. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x5d22e51e91911abac17500ff8ccac0aa3c9a233a62ff19976ac545dbf37709cc`
- block 11933950, position 110, result success, from `0x1734db5e1ab68173a1225138a32439dbaad4c56d`, to `0x111111125434b319222cdbf8c261674adb56f3ae`, value 0.000000 ETH, gas used 190499 at 235.0 gwei, fee 0.044767 ETH
- token transfers (Blockscout, decoded):
  - 20.907221 WETH (`0xc02aaa39`): `0x7f941cdae3c01906e42f8325af0693a848f81072` -> `0x0000000000000000000000000000000000000000`
  - 20.907221 WETH (`0xc02aaa39`): `0x7f941cdae3c01906e42f8325af0693a848f81072` -> `0x092e793afe54366601eb7ef7e63b6abb93edb485`
  - 19974.459044 MINT (`0x0cdf9acd`): `0x092e793afe54366601eb7ef7e63b6abb93edb485` -> `0x7f941cdae3c01906e42f8325af0693a848f81072`
- internal ETH transfers (Etherscan):
  - 20.907221 ETH: `0x7f941cdae3c01906e42f8325af0693a848f81072` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000000 ETH: `0x9c976e415af311283e32376e5bc5d6539007577a` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x2b619323d73fcf370bb68e32fb25a1b645240e12` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0xcf06ca5d19dfab90a792bc84d501e9f916fd8d83` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x87103f8039fa0e70eff473b9f9414b587aa25a0c` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 20.907221 ETH for `0x7f941cdae3c01906e42f8325af0693a848f81072`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0cdf9acd87e940837ff21bb40c9fd55f68bba059` Transfer
  - `0x092e793afe54366601eb7ef7e63b6abb93edb485` UniswapV2 Sync
  - `0x092e793afe54366601eb7ef7e63b6abb93edb485` UniswapV2 Swap
  - `0x111111125434b319222cdbf8c261674adb56f3ae` other
- receipt status 1, index 110

### Victim leg: `0x1830a9dd4d1029f67662bafa40e301cc25f1bd44691f29946da223f49192bbe4`
- block 11933950, position 114, result success, from `0x418ddde9b5a0a949e3cdbc827124cb418079d4f3`, to `0xe34820500dcd2a2c3c4ce2c1cac561e30ede0dc7`, value 0.000000 ETH, gas used 136800 at 231.0 gwei, fee 0.031601 ETH
- token transfers (Blockscout, decoded):
  - 3.429240 WETH (`0xc02aaa39`): `0xe34820500dcd2a2c3c4ce2c1cac561e30ede0dc7` -> `0x092e793afe54366601eb7ef7e63b6abb93edb485`
  - 3084.804133 MINT (`0x0cdf9acd`): `0x092e793afe54366601eb7ef7e63b6abb93edb485` -> `0xe34820500dcd2a2c3c4ce2c1cac561e30ede0dc7`
  - 3.000000 CHI (`0x00000000`): `0xe34820500dcd2a2c3c4ce2c1cac561e30ede0dc7` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x570446ac46b53c7c284ffec9dd1b2dc378abe519` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x02baca876940f48673d49b9dfcecd5d8d41ccd9a` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xf4da102f2d8019318775c8308449a52aed738eb2` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0cdf9acd87e940837ff21bb40c9fd55f68bba059` Transfer
  - `0x092e793afe54366601eb7ef7e63b6abb93edb485` UniswapV2 Sync
  - `0x092e793afe54366601eb7ef7e63b6abb93edb485` UniswapV2 Swap
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Transfer
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Approval
- receipt status 1, index 114

### Back leg: `0x3cdf2bbc99e853ec75194a4d73799e71d90eb27a8e68a9ec1ee27a5f1fe6a9f5`
- block 11933950, position 152, result success, from `0x1a3080a71b7d43ae629d45e72195b57267fea3e5`, to `0x111111125434b319222cdbf8c261674adb56f3ae`, value 0.000000 ETH, gas used 170533 at 222.0 gwei, fee 0.037858 ETH
- token transfers (Blockscout, decoded):
  - 19341.831531 MINT (`0x0cdf9acd`): `0x7f941cdae3c01906e42f8325af0693a848f81072` -> `0x092e793afe54366601eb7ef7e63b6abb93edb485`
  - 21.464093 WETH (`0xc02aaa39`): `0x092e793afe54366601eb7ef7e63b6abb93edb485` -> `0x7f941cdae3c01906e42f8325af0693a848f81072`
  - 21.464093 WETH (`0xc02aaa39`): `0x7f941cdae3c01906e42f8325af0693a848f81072` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 21.464093 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7f941cdae3c01906e42f8325af0693a848f81072` [call]
  - 0.000000 ETH: `0x8a14af2ff8da213860c59b6908b982415dfde741` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0xfa4b55a2b4b3dc82b3c9576de8abe711a7848bf4` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0xe0b222ea6c404da438ed3a86196c3a5b07d8afae` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x0cdf9acd87e940837ff21bb40c9fd55f68bba059` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x092e793afe54366601eb7ef7e63b6abb93edb485` UniswapV2 Sync
  - `0x092e793afe54366601eb7ef7e63b6abb93edb485` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 21.464093 ETH for `0x7f941cdae3c01906e42f8325af0693a848f81072`
  - `0x111111125434b319222cdbf8c261674adb56f3ae` other
- receipt status 1, index 152
