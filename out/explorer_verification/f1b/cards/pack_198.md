# pack_198

Block 14367414. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xb45473576236ef3ef85f58c952700c24dedfa177b9235236f38b316c3838aed7`
- block 14367414, position 0, result success, from `0x5aa17fc7f2950eca85376c3a8cb1509e8e4b39df`, to `0x01ff6318440f7d5553a82294d78262d5f5084eff`, value 0.000000 ETH, gas used 90211 at 23.7 gwei, fee 0.002134 ETH
- token transfers (Blockscout, decoded):
  - 3.475330 WETH (`0xc02aaa39`): `0x01ff6318440f7d5553a82294d78262d5f5084eff` -> `0x635b58600509acfe70e0bd4c4935c08182774e58`
  - 79355.203674 STACK (`0x56a86d64`): `0x635b58600509acfe70e0bd4c4935c08182774e58` -> `0x01ff6318440f7d5553a82294d78262d5f5084eff`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x56a86d648c435dc707c8405b78e2ae8eb4e60ba4` Transfer
  - `0x635b58600509acfe70e0bd4c4935c08182774e58` UniswapV2 Sync
  - `0x635b58600509acfe70e0bd4c4935c08182774e58` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x07fceb0482b237f3944db39a827c0a42a1c7b4190c83d95f8a48d01d30b2418f`
- block 14367414, position 1, result success, from `0x0bda046968c97347c6154f59013f059ca88bb03a`, to `0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45`, value 0.000000 ETH, gas used 187034 at 34.8 gwei, fee 0.006515 ETH
- token transfers (Blockscout, decoded):
  - 5850.081928 USDT (`0xdac17f95`): `0x0bda046968c97347c6154f59013f059ca88bb03a` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 2.278654 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x635b58600509acfe70e0bd4c4935c08182774e58`
  - 50000.000002 STACK (`0x56a86d64`): `0x635b58600509acfe70e0bd4c4935c08182774e58` -> `0x0bda046968c97347c6154f59013f059ca88bb03a`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x56a86d648c435dc707c8405b78e2ae8eb4e60ba4` Transfer
  - `0x635b58600509acfe70e0bd4c4935c08182774e58` UniswapV2 Sync
  - `0x635b58600509acfe70e0bd4c4935c08182774e58` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0x12e8cd0bab7b414ec4d4a38362a67a8db5a97a29af94cb4f588f46e8027d4605`
- block 14367414, position 2, result success, from `0x5aa17fc7f2950eca85376c3a8cb1509e8e4b39df`, to `0x01ff6318440f7d5553a82294d78262d5f5084eff`, value 0.000000 ETH, gas used 80511 at 1050.4 gwei, fee 0.084571 ETH
- token transfers (Blockscout, decoded):
  - 79355.203674 STACK (`0x56a86d64`): `0x01ff6318440f7d5553a82294d78262d5f5084eff` -> `0x635b58600509acfe70e0bd4c4935c08182774e58`
  - 3.562954 WETH (`0xc02aaa39`): `0x635b58600509acfe70e0bd4c4935c08182774e58` -> `0x01ff6318440f7d5553a82294d78262d5f5084eff`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x56a86d648c435dc707c8405b78e2ae8eb4e60ba4` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x635b58600509acfe70e0bd4c4935c08182774e58` UniswapV2 Sync
  - `0x635b58600509acfe70e0bd4c4935c08182774e58` UniswapV2 Swap
- receipt status 1, index 2
