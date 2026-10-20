# pack_076

Block 13649334. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x2735ee5e6d44bb68754153ba536dfe7d968180f173825e6f7e8d5130317fbbff`
- block 13649334, position 11, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 204511 at 111.0 gwei, fee 0.022693 ETH
- token transfers (Blockscout, decoded):
  - 68.406470 WETH (`0xc02aaa39`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x97524f602706cdb64f9dfa71909ace06e98200b6`
  - 3268.593723 BADGER (`0x3472a5a7`): `0x97524f602706cdb64f9dfa71909ace06e98200b6` -> `0x110492b31c59716ac47337e616804e3e3adc0b4a`
  - 1.565618 WBTC (`0x2260fac5`): `0x110492b31c59716ac47337e616804e3e3adc0b4a` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0x97524f602706cdb64f9dfa71909ace06e98200b6` UniswapV2 Sync
  - `0x97524f602706cdb64f9dfa71909ace06e98200b6` UniswapV2 Swap
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x110492b31c59716ac47337e616804e3e3adc0b4a` UniswapV2 Sync
  - `0x110492b31c59716ac47337e616804e3e3adc0b4a` UniswapV2 Swap
- receipt status 1, index 11

### Victim leg: `0x11eba4870709770c0629023c4f0d388cf250510ba7eb935acf0c280618d37c8d`
- block 13649334, position 12, result success, from `0x3e6099d8e6225d83c2deaa7d530503d55b2673c0`, to `0x1111111254fb6c44bac0bed2854e76f90643097d`, value 0.000000 ETH, gas used 644999 at 140.0 gwei, fee 0.090300 ETH
- token transfers (Blockscout, decoded):
  - 6000.000000 BADGER (`0x3472a5a7`): `0x3e6099d8e6225d83c2deaa7d530503d55b2673c0` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4`
  - 1320.000000 BADGER (`0x3472a5a7`): `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0xcd7989894bc033581532d2cd88da5db0a4b12859`
  - 0.628799 WBTC (`0x2260fac5`): `0xcd7989894bc033581532d2cd88da5db0a4b12859` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4`
  - 4680.000000 BADGER (`0x3472a5a7`): `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0x110492b31c59716ac47337e616804e3e3adc0b4a`
  - 2.207271 WBTC (`0x2260fac5`): `0x110492b31c59716ac47337e616804e3e3adc0b4a` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4`
  - 166472.358514 DAI (`0x6b175474`): `0x0000006daea1723962647b7e189d311d757fb793` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4`
  - 2.836070 WBTC (`0x2260fac5`): `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0x0000006daea1723962647b7e189d311d757fb793`
  - 166472.358514 DAI (`0x6b175474`): `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c`
  - 215.837426 OHM (`0x38351818`): `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` -> `0x220bda5c8994804ac96ebe4df184d25e5c2196d4`
  - 215.837426 OHM (`0x38351818`): `0x220bda5c8994804ac96ebe4df184d25e5c2196d4` -> `0x1111111254fb6c44bac0bed2854e76f90643097d`
  - 215.837426 OHM (`0x38351818`): `0x1111111254fb6c44bac0bed2854e76f90643097d` -> `0x3e6099d8e6225d83c2deaa7d530503d55b2673c0`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0xcd7989894bc033581532d2cd88da5db0a4b12859` UniswapV2 Sync
  - `0xcd7989894bc033581532d2cd88da5db0a4b12859` UniswapV2 Swap
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x110492b31c59716ac47337e616804e3e3adc0b4a` UniswapV2 Sync
  - `0x110492b31c59716ac47337e616804e3e3adc0b4a` UniswapV2 Swap
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Approval
  - `0x080bf510fcbf18b91105470639e9561022937712` other
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x6b175474e89094c44da98b954eedeac495271d0f` Transfer
  - `0x383518188c0c6d7730d91b2c03a03c837814a899` Transfer
  - `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` UniswapV2 Sync
  - `0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c` UniswapV2 Swap
  - `0x383518188c0c6d7730d91b2c03a03c837814a899` Transfer
  - `0x383518188c0c6d7730d91b2c03a03c837814a899` Transfer
- receipt status 1, index 12

### Back leg: `0x0d5c8f7819ef194c1cca66f753e7c94c8f6011f83560feb4de3e8e81a8c75067`
- block 13649334, position 13, result success, from `0x50efbf12580138bc263c95757826df4e24eb81c9`, to `0x000000000035b5e5ad9019092c665357240f594e`, value 0.000000 ETH, gas used 138949 at 614.5 gwei, fee 0.085382 ETH
- token transfers (Blockscout, decoded):
  - 1.565618 WBTC (`0x2260fac5`): `0x000000000035b5e5ad9019092c665357240f594e` -> `0x110492b31c59716ac47337e616804e3e3adc0b4a`
  - 3308.469323 BADGER (`0x3472a5a7`): `0x110492b31c59716ac47337e616804e3e3adc0b4a` -> `0x97524f602706cdb64f9dfa71909ace06e98200b6`
  - 68.533215 WETH (`0xc02aaa39`): `0x97524f602706cdb64f9dfa71909ace06e98200b6` -> `0x000000000035b5e5ad9019092c665357240f594e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599` Transfer
  - `0x3472a5a71965499acd81997a54bba8d852c6e53d` Transfer
  - `0x110492b31c59716ac47337e616804e3e3adc0b4a` UniswapV2 Sync
  - `0x110492b31c59716ac47337e616804e3e3adc0b4a` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x97524f602706cdb64f9dfa71909ace06e98200b6` UniswapV2 Sync
  - `0x97524f602706cdb64f9dfa71909ace06e98200b6` UniswapV2 Swap
- receipt status 1, index 13
