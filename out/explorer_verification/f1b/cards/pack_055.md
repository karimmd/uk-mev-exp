# pack_055

Block 12436782. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x70fdb63a8b1cbf14f69572c37c595dc47062dfe022d6ccbc7107a518c8612f93`
- block 12436782, position 11, result success, from `0xd2e0f41e091f0e98a0672f441fb4ff995277686d`, to `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336`, value 0.000000 ETH, gas used 134940 at 200.0 gwei, fee 0.026988 ETH
- token transfers (Blockscout, decoded):
  - 15.070000 WETH (`0xc02aaa39`): `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336` -> `0x0000000000000000000000000000000000000000`
  - 15.070000 WETH (`0xc02aaa39`): `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336` -> `0x9314941c11d6dee1d7bf93113eb74d4718949f3b`
  - 15339352770520.662109 $HOKK (`0xc40af1e4`): `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` -> `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336`
- internal ETH transfers (Etherscan):
  - 15.070000 ETH: `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 15.070000 ETH for `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc40af1e4fecfa05ce6bab79dcd8b373d2e436c4e` Transfer
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Sync
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Swap
- receipt status 1, index 11

### Victim leg: `0x461d293e2f29ed8e5cbd728fb9ae8fee9039f377e1842a826c4a9c1f054a0710`
- block 12436782, position 12, result success, from `0x9f3090f8388e0f7fe6de710e2d945fdf1edfe451`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 162198 at 200.0 gwei, fee 0.032440 ETH
- token transfers (Blockscout, decoded):
  - 67901.416122 USDT (`0xdac17f95`): `0x9f3090f8388e0f7fe6de710e2d945fdf1edfe451` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 16.776100 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x9314941c11d6dee1d7bf93113eb74d4718949f3b`
  - 16218218186482.306641 $HOKK (`0xc40af1e4`): `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` -> `0x9f3090f8388e0f7fe6de710e2d945fdf1edfe451`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0xc40af1e4fecfa05ce6bab79dcd8b373d2e436c4e` Transfer
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Sync
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Swap
- receipt status 1, index 12

### Back leg: `0x911ac8d66e3bd7cf576e2bfcba073ac6f393b379badb650f7607e4b1b25b6d6c`
- block 12436782, position 13, result success, from `0xd2e0f41e091f0e98a0672f441fb4ff995277686d`, to `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336`, value 0.000000 ETH, gas used 119545 at 200.0 gwei, fee 0.023909 ETH
- token transfers (Blockscout, decoded):
  - 15032662530120.707031 $HOKK (`0xc40af1e4`): `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336` -> `0x9314941c11d6dee1d7bf93113eb74d4718949f3b`
  - 15.188385 WETH (`0xc02aaa39`): `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` -> `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336`
  - 15.188385 WETH (`0xc02aaa39`): `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 15.188385 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc40af1e4fecfa05ce6bab79dcd8b373d2e436c4e` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Sync
  - `0x9314941c11d6dee1d7bf93113eb74d4718949f3b` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 15.188385 ETH for `0xda1faeb056a2f568b138ca0ad9ad8a51915ba336`
- receipt status 1, index 13
