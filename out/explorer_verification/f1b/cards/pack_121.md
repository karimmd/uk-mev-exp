# pack_121

Block 11828614. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x1e7e390df71f4e795e0200c5cdf1708d28aac0b026e5ed792aebd5254e84f5e4`
- block 11828614, position 100, result success, from `0xb6b7cc8c20a25d886f3feff988d15d267f71ac7c`, to `0x7b78eb388fe213037b0f558a4a5935fe27b1e481`, value 0.000000 ETH, gas used 149024 at 204.0 gwei, fee 0.030408 ETH
- token transfers (Blockscout, decoded):
  - 3.760000 WETH (`0xc02aaa39`): `0x7b78eb388fe213037b0f558a4a5935fe27b1e481` -> `0x0000000000000000000000000000000000000000`
  - 3.760000 WETH (`0xc02aaa39`): `0x7b78eb388fe213037b0f558a4a5935fe27b1e481` -> `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8`
  - 1943.610652 LYXE (`0xa8b91968`): `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` -> `0x7b78eb388fe213037b0f558a4a5935fe27b1e481`
- internal ETH transfers (Etherscan):
  - 3.760000 ETH: `0x7b78eb388fe213037b0f558a4a5935fe27b1e481` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 3.760000 ETH for `0x7b78eb388fe213037b0f558a4a5935fe27b1e481`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa8b919680258d369114910511cc87595aec0be6d` other
  - `0xa8b919680258d369114910511cc87595aec0be6d` Transfer
  - `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` UniswapV2 Sync
  - `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` UniswapV2 Swap
- receipt status 1, index 100

### Victim leg: `0xee1f741d6078a324017825d6332cb0c5637d5bb2a2680eb60e59e2a7897653f7`
- block 11828614, position 101, result success, from `0x3e626731961734d28e393fd35ea99848546c5656`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 166949 at 204.0 gwei, fee 0.034066 ETH
- token transfers (Blockscout, decoded):
  - 7977.759460 USDT (`0xdac17f95`): `0x3e626731961734d28e393fd35ea99848546c5656` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 4.455359 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8`
  - 2230.501394 LYXE (`0xa8b91968`): `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` -> `0x3e626731961734d28e393fd35ea99848546c5656`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0xa8b919680258d369114910511cc87595aec0be6d` other
  - `0xa8b919680258d369114910511cc87595aec0be6d` Transfer
  - `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` UniswapV2 Sync
  - `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` UniswapV2 Swap
- receipt status 1, index 101

### Back leg: `0xbd1c1f33f1b896caf46553113b9a1624cec3e15614ee4e2b28dfd58fe48b0f20`
- block 11828614, position 102, result success, from `0xb6b7cc8c20a25d886f3feff988d15d267f71ac7c`, to `0x7b78eb388fe213037b0f558a4a5935fe27b1e481`, value 0.000000 ETH, gas used 128138 at 204.0 gwei, fee 0.026146 ETH
- token transfers (Blockscout, decoded):
  - 1943.610652 LYXE (`0xa8b91968`): `0x7b78eb388fe213037b0f558a4a5935fe27b1e481` -> `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8`
  - 3.867903 WETH (`0xc02aaa39`): `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` -> `0x7b78eb388fe213037b0f558a4a5935fe27b1e481`
  - 3.867903 WETH (`0xc02aaa39`): `0x7b78eb388fe213037b0f558a4a5935fe27b1e481` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 3.867903 ETH: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` -> `0x7b78eb388fe213037b0f558a4a5935fe27b1e481` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xa8b919680258d369114910511cc87595aec0be6d` other
  - `0xa8b919680258d369114910511cc87595aec0be6d` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` UniswapV2 Sync
  - `0xd583d0824ed78767e0e35b9bf7a636c81c665aa8` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Withdrawal 3.867903 ETH for `0x7b78eb388fe213037b0f558a4a5935fe27b1e481`
- receipt status 1, index 102
