# pack_071

Block 12550742. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x488456ec733420ce9221e22a29a791e51be3b8243a648a68a04c8ac7117ab072`
- block 12550742, position 0, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.000000 ETH, gas used 101908 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 2.929267 WETH (`0xc02aaa39`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1`
  - 134840757811.717484 CHINU (`0x910985ff`): `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x4f7556ceaefd0ffaebf6a03f98fe2a73ce36de37` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x307fea7d8a0447ba04680b1a7deb51554b7eef58` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x43d7e568155c243740136864677b7e7f6cdc2178` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x167d571d9b82da272c485812230985b6bed02937` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Transfer
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Sync
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xc04c8405e18249d91d31b7b8ca297d8d7f1cca17ed9ee5c22532f1009f572b27`
- block 12550742, position 1, result success, from `0x8221c2ea04e50c67c5276d5c26e5caeaedb88a1c`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 210694 at 39.0 gwei, fee 0.008217 ETH
- token transfers (Blockscout, decoded):
  - 3270.848557 GET (`0x8a854288`): `0x8221c2ea04e50c67c5276d5c26e5caeaedb88a1c` -> `0x2680a95fc9de215f1034f073185cc1f2a28b4107`
  - 4.995948 WETH (`0xc02aaa39`): `0x2680a95fc9de215f1034f073185cc1f2a28b4107` -> `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1`
  - 197328954554.938263 CHINU (`0x910985ff`): `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` -> `0x8221c2ea04e50c67c5276d5c26e5caeaedb88a1c`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x8a854288a5976036a725879164ca3e91d30c6a1b` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2680a95fc9de215f1034f073185cc1f2a28b4107` UniswapV2 Sync
  - `0x2680a95fc9de215f1034f073185cc1f2a28b4107` UniswapV2 Swap
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Transfer
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Sync
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x10b2f82e64d48ec09647c48cfd25c9313a0c8d3b9fa4ae2e03bd0f8a48f194c4`
- block 12550742, position 2, result success, from `0xa6ae57b1da8238cd149bc718c40578e4620b752c`, to `0x00000000003b3cc22af3ae1eac0440bcee416b40`, value 0.262827 ETH, gas used 247069 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 750000000.000000 CHINU (`0x910985ff`): `0x910985ffa7101bf5801dd2e91555c465efd9aab3` -> `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1`
  - 0.019896 WETH (`0xc02aaa39`): `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.019896 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 249339297.585898 CHINU (`0x910985ff`): `0x910985ffa7101bf5801dd2e91555c465efd9aab3` -> `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1`
  - 0.006632 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.006632 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1`
  - 0.036457 UNI-V2 (`0xe3c7ed83`): `0x0000000000000000000000000000000000000000` -> `0x9d9792819436600b1b11a31138c43088fba0838e`
  - 129465045387.395798 CHINU (`0x910985ff`): `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1`
  - 3.236668 WETH (`0xc02aaa39`): `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40`
- internal ETH transfers (Etherscan):
  - 0.019896 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.019896 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x910985ffa7101bf5801dd2e91555c465efd9aab3` [call]
  - 0.006632 ETH: `0x910985ffa7101bf5801dd2e91555c465efd9aab3` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.006632 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.013264 ETH: `0x910985ffa7101bf5801dd2e91555c465efd9aab3` -> `0x7067f9128c02428dfe4b0164990f670798aa9be7` [call]
  - 0.262827 ETH: `0x00000000003b3cc22af3ae1eac0440bcee416b40` -> `0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c` [call]
  - 0.000000 ETH: `0x3083f1d7811d0674d8b9e5980ca81f1a8890e583` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x803a77142627d5ec3278433104dc15ceb1e5e8a9` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x939a92790aa816ca5370d5a3da630f91c80c34fc` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x71cc0cd7227cb298d0cb82b56e48263e72d1eb1f` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0x9d8d42228c9f203f57682f7ad85d439c113dddda` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
  - 0.000000 ETH: `0xe9132fd8c67498e93b65df6ed85e0ed7189a6da9` -> `0x00000000003b3cc22af3ae1eac0440bcee416b40` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Approval
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Transfer
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Sync
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.019896 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Approval
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Transfer
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.006632 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` Transfer
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Sync
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` other
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` other
  - `0x910985ffa7101bf5801dd2e91555c465efd9aab3` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Sync
  - `0xe3c7ed83438482c7b2c2df48842a5e34d710bfb1` UniswapV2 Swap
- receipt status 1, index 2
