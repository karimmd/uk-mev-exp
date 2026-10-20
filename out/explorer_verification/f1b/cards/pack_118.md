# pack_118

Block 10829726. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xa209c2a85d3852d0bf2076efacebf5c78453229325d4c7ee3955219e74dd49f9`
- block 10829726, position 33, result success, from `0x30b8235f492265a734347c0bf36e2ffcad887be2`, to `0x3f499fe484a61af03b01ea5c81eab14f67c11a5a`, value 0.000000 ETH, gas used 89230 at 103.2 gwei, fee 0.009211 ETH
- token transfers (Blockscout, decoded):
  - 15.850500 WETH (`0xc02aaa39`): `0x3f499fe484a61af03b01ea5c81eab14f67c11a5a` -> `0xba65016890709dbc9491ca7bf5de395b8441dc8b`
  - 305222.891823 RSR (`0x8762db10`): `0xba65016890709dbc9491ca7bf5de395b8441dc8b` -> `0x3f499fe484a61af03b01ea5c81eab14f67c11a5a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x8762db106b2c2a0bccb3a80d1ed41273552616e8` Transfer
  - `0xba65016890709dbc9491ca7bf5de395b8441dc8b` UniswapV2 Sync
  - `0xba65016890709dbc9491ca7bf5de395b8441dc8b` UniswapV2 Swap
- receipt status 1, index 33

### Victim leg: `0xe6cf20d6cfe37492e4d5d7340514b3769baf33f3fcc6d0b5607b3f01e0188b72`
- block 10829726, position 98, result success, from `0x208b82b04449cd51803fae4b1561450ba13d9510`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 153457 at 93.0 gwei, fee 0.014272 ETH
- token transfers (Blockscout, decoded):
  - 9874.000000 SWAP (`0xcc4304a3`): `0x208b82b04449cd51803fae4b1561450ba13d9510` -> `0xd90a1ba0cbaaaabfdc6c814cdf1611306a26e1f8`
  - 20.812213 WETH (`0xc02aaa39`): `0xd90a1ba0cbaaaabfdc6c814cdf1611306a26e1f8` -> `0xba65016890709dbc9491ca7bf5de395b8441dc8b`
  - 391695.230546 RSR (`0x8762db10`): `0xba65016890709dbc9491ca7bf5de395b8441dc8b` -> `0x208b82b04449cd51803fae4b1561450ba13d9510`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xcc4304a31d09258b0029ea7fe63d032f52e44efe` Transfer
  - `0xcc4304a31d09258b0029ea7fe63d032f52e44efe` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd90a1ba0cbaaaabfdc6c814cdf1611306a26e1f8` UniswapV2 Sync
  - `0xd90a1ba0cbaaaabfdc6c814cdf1611306a26e1f8` UniswapV2 Swap
  - `0x8762db106b2c2a0bccb3a80d1ed41273552616e8` Transfer
  - `0xba65016890709dbc9491ca7bf5de395b8441dc8b` UniswapV2 Sync
  - `0xba65016890709dbc9491ca7bf5de395b8441dc8b` UniswapV2 Swap
- receipt status 1, index 98

### Back leg: `0x3930608e923a5fbfd26aece0691aebe12b268b4db7ca2d7289217406ac611c68`
- block 10829726, position 100, result success, from `0xd11b92824332f966fd7ce0ed79cb70136c5858f7`, to `0x3f499fe484a61af03b01ea5c81eab14f67c11a5a`, value 0.000000 ETH, gas used 88042 at 93.0 gwei, fee 0.008188 ETH
- token transfers (Blockscout, decoded):
  - 305222.891823 RSR (`0x8762db10`): `0x3f499fe484a61af03b01ea5c81eab14f67c11a5a` -> `0xba65016890709dbc9491ca7bf5de395b8441dc8b`
  - 16.167372 WETH (`0xc02aaa39`): `0xba65016890709dbc9491ca7bf5de395b8441dc8b` -> `0x3f499fe484a61af03b01ea5c81eab14f67c11a5a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x8762db106b2c2a0bccb3a80d1ed41273552616e8` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xba65016890709dbc9491ca7bf5de395b8441dc8b` UniswapV2 Sync
  - `0xba65016890709dbc9491ca7bf5de395b8441dc8b` UniswapV2 Swap
- receipt status 1, index 100
