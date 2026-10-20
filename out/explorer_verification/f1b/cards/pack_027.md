# pack_027

Block 12504630. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x2ce97ecb3c6d0b09479484f129163a825d72bf5424340493dac6d448285b0e7e`
- block 12504630, position 15, result success, from `0xc29115b68fb48bfcba8a42b5140f60cb25595b99`, to `0xa1fac94eabbc27715a022a96009babfb4a49fb5d`, value 0.000000 ETH, gas used 151563 at 100.0 gwei, fee 0.015156 ETH
- token transfers (Blockscout, decoded):
  - 1.555025 WETH (`0xc02aaa39`): `0xa1fac94eabbc27715a022a96009babfb4a49fb5d` -> `0xfac2c7bc156c2c764ea21def2262ec2131100ab1`
  - 8663724207.610018 RAKUC (`0x714599f7`): `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` -> `0xa1fac94eabbc27715a022a96009babfb4a49fb5d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x714599f7604144a3fe1737c440a70fc0fd6503ea` Transfer
  - `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` UniswapV2 Sync
  - `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` UniswapV2 Swap
- receipt status 1, index 15

### Victim leg: `0x132a5d4184e02c4dab3976cce2be1c5cc38c3b7400763b100d51e0e6bf234a46`
- block 12504630, position 159, result success, from `0x7d26d3bd8e5eee24697ecdf4f7b41c2ca2f92f30`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 199616 at 60.0 gwei, fee 0.011977 ETH
- token transfers (Blockscout, decoded):
  - 1000.000000 USDT (`0xdac17f95`): `0x7d26d3bd8e5eee24697ecdf4f7b41c2ca2f92f30` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 0.388568 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0xfac2c7bc156c2c764ea21def2262ec2131100ab1`
  - 1717348423.891124 RAKUC (`0x714599f7`): `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` -> `0x7d26d3bd8e5eee24697ecdf4f7b41c2ca2f92f30`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x714599f7604144a3fe1737c440a70fc0fd6503ea` Transfer
  - `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` UniswapV2 Sync
  - `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` UniswapV2 Swap
- receipt status 1, index 159

### Back leg: `0x0f682df30b03d590c6d82cfea147514958c90da1d34a04bd273e1bdaabd4134c`
- block 12504630, position 160, result success, from `0xc29115b68fb48bfcba8a42b5140f60cb25595b99`, to `0xa1fac94eabbc27715a022a96009babfb4a49fb5d`, value 0.000000 ETH, gas used 249823 at 60.0 gwei, fee 0.014989 ETH
- token transfers (Blockscout, decoded):
  - 243869446.250602 RAKUC (`0x714599f7`): `0x714599f7604144a3fe1737c440a70fc0fd6503ea` -> `0xfac2c7bc156c2c764ea21def2262ec2131100ab1`
  - 0.054243 WETH (`0xc02aaa39`): `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.054243 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 8493019317.091521 RAKUC (`0x714599f7`): `0xa1fac94eabbc27715a022a96009babfb4a49fb5d` -> `0xfac2c7bc156c2c764ea21def2262ec2131100ab1`
  - 1.717745 WETH (`0xc02aaa39`): `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` -> `0xa1fac94eabbc27715a022a96009babfb4a49fb5d`
- internal ETH transfers (Etherscan):
  - 0.054243 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 0.054243 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x714599f7604144a3fe1737c440a70fc0fd6503ea` [call]
  - 0.054243 ETH: `0x714599f7604144a3fe1737c440a70fc0fd6503ea` -> `0x3b266905425d6fe88a845898009fccd353e9481b` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x714599f7604144a3fe1737c440a70fc0fd6503ea` Approval
  - `0x714599f7604144a3fe1737c440a70fc0fd6503ea` Transfer
  - `0x714599f7604144a3fe1737c440a70fc0fd6503ea` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` UniswapV2 Sync
  - `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 0.054243 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0x714599f7604144a3fe1737c440a70fc0fd6503ea` Transfer
  - `0x714599f7604144a3fe1737c440a70fc0fd6503ea` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` UniswapV2 Sync
  - `0xfac2c7bc156c2c764ea21def2262ec2131100ab1` UniswapV2 Swap
- receipt status 1, index 160
