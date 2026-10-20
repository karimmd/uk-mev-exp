# pack_182

Block 13173870. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xe19ac1a2664bcbac3c861969a4eaf4b4424a8ce5380cd7d05a8f07fec35a06ca`
- block 13173870, position 0, result success, from `0xba02a83d3fead87c1bfdc15f1c07db53888305a3`, to `0x00000081c57cbc967248bea482c417207e84cffb`, value 0.000000 ETH, gas used 258604 at 99.6 gwei, fee 0.025749 ETH
- token transfers (Blockscout, decoded):
  - 1.352746 WBTC (`0x2260fac5`): `0x4585fe77225b41b697c938b018e2ac67ac5a20c0` -> `0xcd7989894bc033581532d2cd88da5db0a4b12859`
  - 17.788800 WETH (`0xc02aaa39`): `0x00000081c57cbc967248bea482c417207e84cffb` -> `0x4585fe77225b41b697c938b018e2ac67ac5a20c0`
  - 2871.878644 BADGER (`0x3472a5a7`): `0xcd7989894bc033581532d2cd88da5db0a4b12859` -> `0x00000081c57cbc967248bea482c417207e84cffb`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x4585fe77225b41b697c938b018e2ac67ac5a20c0` UniswapV3 Swap
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0xcd7989894bc033581532d2cd88da5db0a4b12859` UniswapV2 Sync
  - `0xcd7989894bc033581532d2cd88da5db0a4b12859` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x5b9804a5e8d9bda17c2e2484d983c825e77ac1d875952f4d8bf9cfb6ba77d196`
- block 13173870, position 1, result success, from `0xfb902be6accb767b78f5906ca8f7a27b113bd44f`, to `0x11111112542d85b3ef69ae05771c2dccff4faa26`, value 0.000000 ETH, gas used 623425 at 102.0 gwei, fee 0.063560 ETH
- token transfers (Blockscout, decoded):
  - 540000.000000 USDT (`0xdac17f95`): `0xfb902be6accb767b78f5906ca8f7a27b113bd44f` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 540000.000000 USDT (`0xdac17f95`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xd51a44d3fae010294c616388b506acda1bfaae46`
  - 10.436120 WBTC (`0x2260fac5`): `0xd51a44d3fae010294c616388b506acda1bfaae46` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 3.965725 WBTC (`0x2260fac5`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xcd7989894bc033581532d2cd88da5db0a4b12859`
  - 8035.592031 BADGER (`0x3472a5a7`): `0xcd7989894bc033581532d2cd88da5db0a4b12859` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 6.470394 WBTC (`0x2260fac5`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x110492b31c59716ac47337e616804e3e3adc0b4a`
  - 13414.240365 BADGER (`0x3472a5a7`): `0x110492b31c59716ac47337e616804e3e3adc0b4a` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 21449.832396 BADGER (`0x3472a5a7`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xfb902be6accb767b78f5906ca8f7a27b113bd44f`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Approval
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xd51a44d3fae010294c616388b506acda1bfaae46` other
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0xcd7989894bc033581532d2cd88da5db0a4b12859` UniswapV2 Sync
  - `0xcd7989894bc033581532d2cd88da5db0a4b12859` UniswapV2 Swap
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0x110492b31c59716ac47337e616804e3e3adc0b4a` UniswapV2 Sync
  - `0x110492b31c59716ac47337e616804e3e3adc0b4a` UniswapV2 Swap
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
- receipt status 1, index 1

### Back leg: `0x305dfa299c065510fab15f48c315118f8d93c33462468d39bb49023a5fa56ca2`
- block 13173870, position 2, result success, from `0xba02a83d3fead87c1bfdc15f1c07db53888305a3`, to `0x00000081c57cbc967248bea482c417207e84cffb`, value 0.923261 ETH, gas used 215894 at 99.6 gwei, fee 0.021496 ETH
- token transfers (Blockscout, decoded):
  - 2871.878644 BADGER (`0x3472a5a7`): `0x00000081c57cbc967248bea482c417207e84cffb` -> `0xcd7989894bc033581532d2cd88da5db0a4b12859`
  - 1.440461 WBTC (`0x2260fac5`): `0xcd7989894bc033581532d2cd88da5db0a4b12859` -> `0x00000081c57cbc967248bea482c417207e84cffb`
  - 18.922931 WETH (`0xc02aaa39`): `0x4585fe77225b41b697c938b018e2ac67ac5a20c0` -> `0x00000081c57cbc967248bea482c417207e84cffb`
  - 1.440461 WBTC (`0x2260fac5`): `0x00000081c57cbc967248bea482c417207e84cffb` -> `0x4585fe77225b41b697c938b018e2ac67ac5a20c0`
- internal ETH transfers (Etherscan):
  - 0.923261 ETH: `0x00000081c57cbc967248bea482c417207e84cffb` -> `0xea674fdde714fd979de3edf0f56aa9716b898ec8` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xcd7989894bc033581532d2cd88da5db0a4b12859` UniswapV2 Sync
  - `0xcd7989894bc033581532d2cd88da5db0a4b12859` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x4585fe77225b41b697c938b018e2ac67ac5a20c0` UniswapV3 Swap
- receipt status 1, index 2
