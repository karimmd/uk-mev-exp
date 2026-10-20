# pack_007

Block 12034886. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xc3323b5d3e67f23441c2da0c4aa3e23c14f7ae0be108c6b031a8b4a549828aab`
- block 12034886, position 41, result success, from `0xc85ed10b68e4d22b2ec8f2ab94081a8a6f3cd0f9`, to `0xb5917a48a99c1f8c76119a5133fde1169ec11170`, value 0.000000 ETH, gas used 99044 at 135.0 gwei, fee 0.013371 ETH
- token transfers (Blockscout, decoded):
  - 16528.271828 BLANK (`0xaec7e1f5`): `0xb5917a48a99c1f8c76119a5133fde1169ec11170` -> `0x4d4786384eb4e356ea2df195bbe84c89440accf0`
  - 7.886000 WETH (`0xc02aaa39`): `0x4d4786384eb4e356ea2df195bbe84c89440accf0` -> `0xb5917a48a99c1f8c76119a5133fde1169ec11170`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xaec7e1f531bb09115103c53ba76829910ec48966` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4d4786384eb4e356ea2df195bbe84c89440accf0` UniswapV2 Sync
  - `0x4d4786384eb4e356ea2df195bbe84c89440accf0` UniswapV2 Swap
- receipt status 1, index 41

### Victim leg: `0x0d0b21b403ea09ff31cd11c186a0eef50172ba7977d905de264299260c8c62f3`
- block 12034886, position 42, result success, from `0x0c111567d0ffabb6623df1d7ff26d3c2ed880956`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 115731 at 135.0 gwei, fee 0.015624 ETH
- token transfers (Blockscout, decoded):
  - 5289.000000 BLANK (`0xaec7e1f5`): `0x0c111567d0ffabb6623df1d7ff26d3c2ed880956` -> `0x4d4786384eb4e356ea2df195bbe84c89440accf0`
  - 2.443216 WETH (`0xc02aaa39`): `0x4d4786384eb4e356ea2df195bbe84c89440accf0` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 2.443216 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 2.443216 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` [call]
  - 2.443216 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x0c111567d0ffabb6623df1d7ff26d3c2ed880956` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xaec7e1f531bb09115103c53ba76829910ec48966` Transfer
  - `0xaec7e1f531bb09115103c53ba76829910ec48966` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4d4786384eb4e356ea2df195bbe84c89440accf0` UniswapV2 Sync
  - `0x4d4786384eb4e356ea2df195bbe84c89440accf0` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 2.443216 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- receipt status 1, index 42

### Back leg: `0xa4054b1ee101721780ed2db95d8de5f49c84fb305c768447b6cf0c8bd2ad9a77`
- block 12034886, position 43, result success, from `0xc85ed10b68e4d22b2ec8f2ab94081a8a6f3cd0f9`, to `0xb5917a48a99c1f8c76119a5133fde1169ec11170`, value 0.000000 ETH, gas used 91681 at 135.0 gwei, fee 0.012377 ETH
- token transfers (Blockscout, decoded):
  - 7.810223 WETH (`0xc02aaa39`): `0xb5917a48a99c1f8c76119a5133fde1169ec11170` -> `0x4d4786384eb4e356ea2df195bbe84c89440accf0`
  - 16528.271828 BLANK (`0xaec7e1f5`): `0x4d4786384eb4e356ea2df195bbe84c89440accf0` -> `0xb5917a48a99c1f8c76119a5133fde1169ec11170`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xaec7e1f531bb09115103c53ba76829910ec48966` Transfer
  - `0x4d4786384eb4e356ea2df195bbe84c89440accf0` UniswapV2 Sync
  - `0x4d4786384eb4e356ea2df195bbe84c89440accf0` UniswapV2 Swap
- receipt status 1, index 43
