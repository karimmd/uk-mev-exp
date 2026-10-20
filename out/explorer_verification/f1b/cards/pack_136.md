# pack_136

Block 10582094. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xb775b2404fd32c1402615146ca54f8c1a3ff4f6fe264ac780b99b1e5157848f0`
- block 10582094, position 4, result success, from `0x5c2bc88f19674fbf71bcede54f88e6b05ede40d7`, to `0x1dc09af6aeabfe733eac67d11e06f27d1d2ee567`, value 0.000000 ETH, gas used 156417 at 99.0 gwei, fee 0.015485 ETH
- token transfers (Blockscout, decoded):
  - 1.579578 WETH (`0xc02aaa39`): `0x1dc09af6aeabfe733eac67d11e06f27d1d2ee567` -> `0xb9f7046f985a906ee3f48f738a44bbcd22bee727`
  - 83959.177451 MNET (`0x31a2bcf6`): `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` -> `0x1dc09af6aeabfe733eac67d11e06f27d1d2ee567`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0xa6e514da6294b177da2573f4b5003ed7cb1b691d` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0xe9ab4a2961413b8edc080531a8a0fb5c114bb76c` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x1d06060ce02d18586fa94aacf8866d7eca644490` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x8b1f8ea13d2c177495005bcdaecab82c12c47e40` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
  - 0.000000 ETH: `0x426146f78cfe9f8346fbbfa6655e39a2145a7a46` -> `0x0000000000b3f879cb30fe243b4dfee438691c04` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x31a2bcf633d16dee21e3377c8e62070ef553b051` Transfer
  - `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` UniswapV2 Sync
  - `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` UniswapV2 Swap
- receipt status 1, index 4

### Victim leg: `0x932017dd4440a38c917dc355175e6a92b5738bf2055ad3a2d13102916035cfd0`
- block 10582094, position 7, result success, from `0x5269389a29a28c3173db02907c8ad0b009da3425`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 2.000000 ETH, gas used 99197 at 90.0 gwei, fee 0.008928 ETH
- token transfers (Blockscout, decoded):
  - 2.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
  - 2.000000 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xb9f7046f985a906ee3f48f738a44bbcd22bee727`
  - 100592.993118 MNET (`0x31a2bcf6`): `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` -> `0x5269389a29a28c3173db02907c8ad0b009da3425`
- internal ETH transfers (Etherscan):
  - 2.000000 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 2.000000 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x31a2bcf633d16dee21e3377c8e62070ef553b051` Transfer
  - `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` UniswapV2 Sync
  - `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` UniswapV2 Swap
- receipt status 1, index 7

### Back leg: `0x07eafc1d55dafd32edda3dc486d8f8e9b9c13026201a678a904dfff39d42eb75`
- block 10582094, position 8, result success, from `0x69a895686ab085d703071d6c6ffb49a40ff3efb4`, to `0x1dc09af6aeabfe733eac67d11e06f27d1d2ee567`, value 0.000000 ETH, gas used 71313 at 90.0 gwei, fee 0.006418 ETH
- token transfers (Blockscout, decoded):
  - 83959.177451 MNET (`0x31a2bcf6`): `0x1dc09af6aeabfe733eac67d11e06f27d1d2ee567` -> `0xb9f7046f985a906ee3f48f738a44bbcd22bee727`
  - 1.667829 WETH (`0xc02aaa39`): `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` -> `0x1dc09af6aeabfe733eac67d11e06f27d1d2ee567`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x31a2bcf633d16dee21e3377c8e62070ef553b051` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` UniswapV2 Sync
  - `0xb9f7046f985a906ee3f48f738a44bbcd22bee727` UniswapV2 Swap
- receipt status 1, index 8
