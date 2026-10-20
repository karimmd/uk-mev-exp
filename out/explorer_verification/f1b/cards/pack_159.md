# pack_159

Block 11964486. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x93686a83ff32b064de36b78824d086393c1aa8afc40bfa2075f408783924e140`
- block 11964486, position 59, result success, from `0xc005f9dd90fe94ee5f45ba1d879f88e2d4c2c2f6`, to `0x51acf0af77adcb20de482e1cd678f620baf07e0c`, value 0.000000 ETH, gas used 131391 at 127.0 gwei, fee 0.016687 ETH
- token transfers (Blockscout, decoded):
  - 6.750000 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - 6.750000 WETH (`0xc02aaa39`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x659a9a43b32bea6c113c393930a45c7634a242d5`
  - 17528.180027 EROWAN (`0x07bac358`): `0x659a9a43b32bea6c113c393930a45c7634a242d5` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
- internal ETH transfers (Etherscan):
  - 6.750000 ETH: `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 6.750000 ETH for `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x07bac35846e5ed502aa91adf6a9e7aa210f2dcbe` Transfer
  - `0x659a9a43b32bea6c113c393930a45c7634a242d5` UniswapV2 Sync
  - `0x659a9a43b32bea6c113c393930a45c7634a242d5` UniswapV2 Swap
- receipt status 1, index 59

### Victim leg: `0x9aa4470ac9fbabd9597f3f712ee8125e05a49728d1e3499e37208da667e88141`
- block 11964486, position 60, result success, from `0xe5da1092871a3a5034ae3c3d1d091bc4ea6b5ca9`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 173507 at 127.0 gwei, fee 0.022035 ETH
- token transfers (Blockscout, decoded):
  - 20000.000000 MANA (`0x0f5d2fb2`): `0xe5da1092871a3a5034ae3c3d1d091bc4ea6b5ca9` -> `0x11b1f53204d03e5529f09eb3091939e4fd8c9cf3`
  - 3.679658 WETH (`0xc02aaa39`): `0x11b1f53204d03e5529f09eb3091939e4fd8c9cf3` -> `0x659a9a43b32bea6c113c393930a45c7634a242d5`
  - 9235.837326 EROWAN (`0x07bac358`): `0x659a9a43b32bea6c113c393930a45c7634a242d5` -> `0xe5da1092871a3a5034ae3c3d1d091bc4ea6b5ca9`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x0f5d2fb29fb7d3cfee444a200298f468908cc942` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x11b1f53204d03e5529f09eb3091939e4fd8c9cf3` UniswapV2 Sync
  - `0x11b1f53204d03e5529f09eb3091939e4fd8c9cf3` UniswapV2 Swap
  - `0x07bac35846e5ed502aa91adf6a9e7aa210f2dcbe` Transfer
  - `0x659a9a43b32bea6c113c393930a45c7634a242d5` UniswapV2 Sync
  - `0x659a9a43b32bea6c113c393930a45c7634a242d5` UniswapV2 Swap
- receipt status 1, index 60

### Back leg: `0x328227e4096a34f0c72ec548732990ca7e5f14001e7fd8593744d4b18670a8fc`
- block 11964486, position 61, result success, from `0xc005f9dd90fe94ee5f45ba1d879f88e2d4c2c2f6`, to `0x51acf0af77adcb20de482e1cd678f620baf07e0c`, value 0.000000 ETH, gas used 90663 at 127.0 gwei, fee 0.011514 ETH
- token transfers (Blockscout, decoded):
  - 17528.180027 EROWAN (`0x07bac358`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x659a9a43b32bea6c113c393930a45c7634a242d5`
  - 6.869693 WETH (`0xc02aaa39`): `0x659a9a43b32bea6c113c393930a45c7634a242d5` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
  - 6.869693 WETH (`0xc02aaa39`): `0x51acf0af77adcb20de482e1cd678f620baf07e0c` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 6.869693 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x51acf0af77adcb20de482e1cd678f620baf07e0c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x07bac35846e5ed502aa91adf6a9e7aa210f2dcbe` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x659a9a43b32bea6c113c393930a45c7634a242d5` UniswapV2 Sync
  - `0x659a9a43b32bea6c113c393930a45c7634a242d5` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 6.869693 ETH for `0x51acf0af77adcb20de482e1cd678f620baf07e0c`
- receipt status 1, index 61
