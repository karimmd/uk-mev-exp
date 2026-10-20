# pack_046

Block 12326958. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x525e9673fad03837eea17006d978a89eb9ca7258d31acd581d38f310fd1fd6b2`
- block 12326958, position 0, result success, from `0x74b892425a206eb23905a5f5c322e4386460312d`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.000000 ETH, gas used 109758 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 3.070000 WETH (`0xc02aaa39`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xc9993ec8646f50cd5e239e845e525d2abb2a6809`
  - 8435305387.897448 CyberE (`0xcf87223c`): `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcf87223c945fa6aac0e9997e8569864b4f47e8f7` Transfer
  - `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` UniswapV2 Sync
  - `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0xa3978495382590508ab3cf1dc34b4505522a3ef8bcf4fbfe30b89dcff87804fd`
- block 12326958, position 1, result success, from `0xefa15ef206eb1948b0a2382b5d06ea6697e417ba`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 172586 at 90.9 gwei, fee 0.015688 ETH
- token transfers (Blockscout, decoded):
  - 82783.674069 FVT (`0x45080a65`): `0xefa15ef206eb1948b0a2382b5d06ea6697e417ba` -> `0x75001b3ffe0f77864c7dc64c55e1e22b205e4a07`
  - 1.376457 WETH (`0xc02aaa39`): `0x75001b3ffe0f77864c7dc64c55e1e22b205e4a07` -> `0xc9993ec8646f50cd5e239e845e525d2abb2a6809`
  - 2838740060.501284 CyberE (`0xcf87223c`): `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` -> `0xefa15ef206eb1948b0a2382b5d06ea6697e417ba`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x45080a6531d671ddff20db42f93792a489685e32` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x75001b3ffe0f77864c7dc64c55e1e22b205e4a07` UniswapV2 Sync
  - `0x75001b3ffe0f77864c7dc64c55e1e22b205e4a07` UniswapV2 Swap
  - `0xcf87223c945fa6aac0e9997e8569864b4f47e8f7` Transfer
  - `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` UniswapV2 Sync
  - `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x96ad933c5610d45ff052c1b51482f937018eede2fce51bdeeae6ef920dde7c17`
- block 12326958, position 2, result success, from `0x74b892425a206eb23905a5f5c322e4386460312d`, to `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`, value 0.075047 ETH, gas used 101614 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 7851495599.659150 CyberE (`0xcf87223c`): `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0xc9993ec8646f50cd5e239e845e525d2abb2a6809`
  - 3.148914 WETH (`0xc02aaa39`): `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` -> `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d`
- internal ETH transfers (Etherscan):
  - 0.075047 ETH: `0x1d6e8bac6ea3730825bde4b005ed7b2b39a2932d` -> `0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xcf87223c945fa6aac0e9997e8569864b4f47e8f7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` UniswapV2 Sync
  - `0xc9993ec8646f50cd5e239e845e525d2abb2a6809` UniswapV2 Swap
- receipt status 1, index 2
