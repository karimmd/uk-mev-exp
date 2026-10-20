# pack_068

Block 12188710. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x5ac07171cda021c57547156c5a5a2facf9a13322680b90701a3ff61cfe54bc60`
- block 12188710, position 148, result success, from `0x1db88c476f4548cc37c2d0f8d1d24a76282a1ac9`, to `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`, value 0.000000 ETH, gas used 329379 at 169.7 gwei, fee 0.055879 ETH
- token transfers (Blockscout, decoded):
  - 1.979486 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - 1.979486 WETH (`0xc02aaa39`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0xe632ded5195e945a31f56d674aab0c0c9e7e812c`
  - 1137.082427 UBI (`0xdd1ad9a2`): `0xe632ded5195e945a31f56d674aab0c0c9e7e812c` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - 1137.082427 UBI (`0xdd1ad9a2`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0xea7952fac7ff6e997d895c1566599b86b91444c0`
  - 4181.202643 DAI (`0x6b175474`): `0xea7952fac7ff6e997d895c1566599b86b91444c0` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - 4181.202643 DAI (`0x6b175474`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0x9b208194acc0a8ccb2a8dcafeacfbb7dcc093f81`
  - 2.007097 WETH (`0xc02aaa39`): `0x9b208194acc0a8ccb2a8dcafeacfbb7dcc093f81` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - 2.007097 WETH (`0xc02aaa39`): `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 1.979486 ETH: `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 2.007097 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 1.979486 ETH for `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdd1ad9a21ce722c151a836373babe42c868ce9a4` Transfer
  - `0xe632ded5195e945a31f56d674aab0c0c9e7e812c` UniswapV2 Sync
  - `0xe632ded5195e945a31f56d674aab0c0c9e7e812c` UniswapV2 Swap
  - `0xdd1ad9a21ce722c151a836373babe42c868ce9a4` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xea7952fac7ff6e997d895c1566599b86b91444c0` UniswapV2 Sync
  - `0xea7952fac7ff6e997d895c1566599b86b91444c0` UniswapV2 Swap
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Approval
  - `0x9b208194acc0a8ccb2a8dcafeacfbb7dcc093f81` other
  - `0x9b208194acc0a8ccb2a8dcafeacfbb7dcc093f81` other
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 2.007097 ETH for `0x860bd2dba9cd475a61e6d1b45e16c365f6d78f66`
- receipt status 1, index 148

### Victim leg: `0xe2415b149c832c857681aceb99c3d9e97000ed9c12be9ef45e8dcea04c222fc1`
- block 12188710, position 185, result success, from `0x23e492a7dfda07befa65223a15efdeafc27c813e`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 217728 at 152.9 gwei, fee 0.033291 ETH
- token transfers (Blockscout, decoded):
  - 20642.147012 SAR (`0xbd4a8581`): `0x23e492a7dfda07befa65223a15efdeafc27c813e` -> `0x4896938404e0af7b694076329013bf5973c01a93`
  - 0.604427 WETH (`0xc02aaa39`): `0x4896938404e0af7b694076329013bf5973c01a93` -> `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11`
  - 1270.775235 DAI (`0x6b175474`): `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` -> `0xea7952fac7ff6e997d895c1566599b86b91444c0`
  - 332.469785 UBI (`0xdd1ad9a2`): `0xea7952fac7ff6e997d895c1566599b86b91444c0` -> `0x23e492a7dfda07befa65223a15efdeafc27c813e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xbd4a858139b155219e2c8d10135003fdef720b6b` Transfer
  - `0xbd4a858139b155219e2c8d10135003fdef720b6b` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4896938404e0af7b694076329013bf5973c01a93` UniswapV2 Sync
  - `0x4896938404e0af7b694076329013bf5973c01a93` UniswapV2 Swap
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Sync
  - `0xa478c2975ab1ea89e8196811f51a7b7ade33eb11` UniswapV2 Swap
  - `0xdd1ad9a21ce722c151a836373babe42c868ce9a4` Transfer
  - `0xea7952fac7ff6e997d895c1566599b86b91444c0` UniswapV2 Sync
  - `0xea7952fac7ff6e997d895c1566599b86b91444c0` UniswapV2 Swap
- receipt status 1, index 185

### Back leg: `0x4f7c0567bbbd84f67a6dac8b432d138676b0096e15cc9ac50a578111b7bcdf2f`
- block 12188710, position 186, result success, from `0x0000000090a491597198dfda1cad7c7db3c70fd0`, to `0x0000000000005117dd3a72e64a705198753fdd54`, value 0.000000 ETH, gas used 370158 at 152.9 gwei, fee 0.056597 ETH
- token transfers (Blockscout, decoded):
  - 1358.613073 UBI (`0xdd1ad9a2`): `0xe632ded5195e945a31f56d674aab0c0c9e7e812c` -> `0x0000000000005117dd3a72e64a705198753fdd54`
  - 1358.613073 UBI (`0xdd1ad9a2`): `0x0000000000005117dd3a72e64a705198753fdd54` -> `0xea7952fac7ff6e997d895c1566599b86b91444c0`
  - 5046.390574 DAI (`0x6b175474`): `0xea7952fac7ff6e997d895c1566599b86b91444c0` -> `0x0000000000005117dd3a72e64a705198753fdd54`
  - 5046.390574 DAI (`0x6b175474`): `0x0000000000005117dd3a72e64a705198753fdd54` -> `0x9b208194acc0a8ccb2a8dcafeacfbb7dcc093f81`
  - 2.372662 WETH (`0xc02aaa39`): `0x9b208194acc0a8ccb2a8dcafeacfbb7dcc093f81` -> `0x0000000000005117dd3a72e64a705198753fdd54`
  - 2.297013 WETH (`0xc02aaa39`): `0x0000000000005117dd3a72e64a705198753fdd54` -> `0xe632ded5195e945a31f56d674aab0c0c9e7e812c`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x0000000000005117dd3a72e64a705198753fdd54` other
  - `0x0000000000005117dd3a72e64a705198753fdd54` other
  - `0x0000000000005117dd3a72e64a705198753fdd54` other
  - `0x0000000000005117dd3a72e64a705198753fdd54` other
  - `0xdd1ad9a21ce722c151a836373babe42c868ce9a4` Transfer
  - `0xdd1ad9a21ce722c151a836373babe42c868ce9a4` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xea7952fac7ff6e997d895c1566599b86b91444c0` UniswapV2 Sync
  - `0xea7952fac7ff6e997d895c1566599b86b91444c0` UniswapV2 Swap
  - `0x9b208194acc0a8ccb2a8dcafeacfbb7dcc093f81` other
  - `0x9b208194acc0a8ccb2a8dcafeacfbb7dcc093f81` other
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xe632ded5195e945a31f56d674aab0c0c9e7e812c` UniswapV2 Sync
  - `0xe632ded5195e945a31f56d674aab0c0c9e7e812c` UniswapV2 Swap
- receipt status 1, index 186
