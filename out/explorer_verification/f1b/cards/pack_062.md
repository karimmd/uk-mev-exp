# pack_062

Block 14078334. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xc878005961e8a58db49750c2159f51d5f308ef4c16ee9674736d346d6d8c4cff`
- block 14078334, position 8, result success, from `0x1845d06fe03c445dfd6ca0d66073cf931caf7d51`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 87117 at 124.4 gwei, fee 0.010840 ETH
- token transfers (Blockscout, decoded):
  - 3202.841186 BRD (`0x558ec315`): `0x5c1e3f0979513f1111995da718780bd24e73cda3` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 0.406118 WETH (`0xc02aaa39`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 984.403744 USDT (`0xdac17f95`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x5c1e3f0979513f1111995da718780bd24e73cda3`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x558ec3152e2eb2174905cd19aea4e34a23de9ad6` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x5c1e3f0979513f1111995da718780bd24e73cda3` UniswapV3 Swap
- receipt status 1, index 8

### Victim leg: `0x3226aa9d72afc3924921f803c2ff2e477f298c4c433b16d077759b06d9dc5384`
- block 14078334, position 10, result success, from `0xa8bbee00c54cfc449de526e2caeec94146ae3195`, to `0xe66b31678d6c16e9ebf358268a790b763c133750`, value 0.000000 ETH, gas used 431269 at 142.0 gwei, fee 0.061240 ETH
- token transfers (Blockscout, decoded):
  - 1251.738526 NCT (`0x9e46a38f`): `0xa8bbee00c54cfc449de526e2caeec94146ae3195` -> `0x382ffce2287252f930e1c8dc9328dac5bf282ba1`
  - 123922.114047 NCT (`0x9e46a38f`): `0xa8bbee00c54cfc449de526e2caeec94146ae3195` -> `0xe66b31678d6c16e9ebf358268a790b763c133750`
  - 2.548226 WETH (`0xc02aaa39`): `0x05aaa0053fa5c28e8c558d4c648cc129bea45018` -> `0xdef1c0ded9bec7f1a1670819833240f027b25eff`
  - 123922.114047 NCT (`0x9e46a38f`): `0xe66b31678d6c16e9ebf358268a790b763c133750` -> `0x05aaa0053fa5c28e8c558d4c648cc129bea45018`
  - 6207.663290 USDT (`0xdac17f95`): `0x11b815efb8f581194ae79006d24e0d814b7697f6` -> `0xdef1c0ded9bec7f1a1670819833240f027b25eff`
  - 2.548226 WETH (`0xc02aaa39`): `0xdef1c0ded9bec7f1a1670819833240f027b25eff` -> `0x11b815efb8f581194ae79006d24e0d814b7697f6`
  - 18082.976814 BRD (`0x558ec315`): `0x5c1e3f0979513f1111995da718780bd24e73cda3` -> `0xe66b31678d6c16e9ebf358268a790b763c133750`
  - 6207.663290 USDT (`0xdac17f95`): `0xdef1c0ded9bec7f1a1670819833240f027b25eff` -> `0x5c1e3f0979513f1111995da718780bd24e73cda3`
  - 18082.976814 BRD (`0x558ec315`): `0xe66b31678d6c16e9ebf358268a790b763c133750` -> `0xa8bbee00c54cfc449de526e2caeec94146ae3195`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x9e46a38f5daabe8683e10793b06749eef7d733d1` Transfer
  - `0x9e46a38f5daabe8683e10793b06749eef7d733d1` Transfer
  - `0x9e46a38f5daabe8683e10793b06749eef7d733d1` Approval
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x9e46a38f5daabe8683e10793b06749eef7d733d1` Transfer
  - `0x05aaa0053fa5c28e8c558d4c648cc129bea45018` UniswapV3 Swap
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x11b815efb8f581194ae79006d24e0d814b7697f6` UniswapV3 Swap
  - `0x558ec3152e2eb2174905cd19aea4e34a23de9ad6` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x5c1e3f0979513f1111995da718780bd24e73cda3` UniswapV3 Swap
  - `0x558ec3152e2eb2174905cd19aea4e34a23de9ad6` Transfer
- receipt status 1, index 10

### Back leg: `0x558d4d680def39a9d42a1c54e3cefbb7f6fb1925b9f258edc98ce4b269ecf328`
- block 14078334, position 11, result success, from `0x1845d06fe03c445dfd6ca0d66073cf931caf7d51`, to `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`, value 0.000000 ETH, gas used 130770 at 150.8 gwei, fee 0.019717 ETH
- token transfers (Blockscout, decoded):
  - 1164.369741 USDT (`0xdac17f95`): `0x5c1e3f0979513f1111995da718780bd24e73cda3` -> `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852`
  - 0.477484 WETH (`0xc02aaa39`): `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` -> `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f`
  - 3202.841186 BRD (`0x558ec315`): `0x7cf09d7a9a74f746edcb06949b9d64bcd9d1604f` -> `0x5c1e3f0979513f1111995da718780bd24e73cda3`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Sync
  - `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` UniswapV2 Swap
  - `0x558ec3152e2eb2174905cd19aea4e34a23de9ad6` Transfer
  - `0x5c1e3f0979513f1111995da718780bd24e73cda3` UniswapV3 Swap
- receipt status 1, index 11
