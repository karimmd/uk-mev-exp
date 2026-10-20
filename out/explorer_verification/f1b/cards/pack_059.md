# pack_059

Block 12869566. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x1156cdc481811d12649b9fc6e02699b2971c630d505fa1b2ee0b17a880e4a14d`
- block 12869566, position 1, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x000000000027d2efc283613d0c3e24a8b430c4d8`, value 0.000000 ETH, gas used 68294 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 0.483237 WETH (`0xc02aaa39`): `0x000000000027d2efc283613d0c3e24a8b430c4d8` -> `0x020e6d0e80d08567ecb14f942fa326748407a845`
  - 530.133065 UNQT (`0xa80f2c8f`): `0x020e6d0e80d08567ecb14f942fa326748407a845` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x445b8cef1b21c09ace8b9a9e3f540b297e43cbda` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
  - 0.000000 ETH: `0x535ea6ce36c8be463c4bee63d32558368b69723a` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa80f2c8f61c56546001f5fc2eb8d6e4e72c45d4c` Transfer
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Sync
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Swap
- receipt status 1, index 1

### Victim leg: `0xbabce1bb5cc7c4dac507d3c8bd53510bd9d90abc11459fe712461491a45f34b2`
- block 12869566, position 2, result success, from `0x5eae117b6fbd12536ab46c8c974b6cf07f1911b5`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.001061 ETH, gas used 99890 at 10.0 gwei, fee 0.000999 ETH
- token transfers (Blockscout, decoded):
  - 0.001057 WETH (`0xc02aaa39`): `0x0000000000000000000000000000000000000000` -> `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - 0.001057 WETH (`0xc02aaa39`): `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x020e6d0e80d08567ecb14f942fa326748407a845`
  - 1.000000 UNQT (`0xa80f2c8f`): `0x020e6d0e80d08567ecb14f942fa326748407a845` -> `0x5eae117b6fbd12536ab46c8c974b6cf07f1911b5`
- internal ETH transfers (Etherscan):
  - 0.001057 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.000004 ETH: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d` -> `0x5eae117b6fbd12536ab46c8c974b6cf07f1911b5` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 0.001057 ETH for `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa80f2c8f61c56546001f5fc2eb8d6e4e72c45d4c` Transfer
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Sync
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Swap
- receipt status 1, index 2

### Back leg: `0xacb0e2498c8fd2e33d50116374b65abf56c03070aebc8934f0a790b80058a52a`
- block 12869566, position 4, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x000000000027d2efc283613d0c3e24a8b430c4d8`, value 0.021037 ETH, gas used 67787 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 530.133065 UNQT (`0xa80f2c8f`): `0x000000000027d2efc283613d0c3e24a8b430c4d8` -> `0x020e6d0e80d08567ecb14f942fa326748407a845`
  - 0.513110 WETH (`0xc02aaa39`): `0x020e6d0e80d08567ecb14f942fa326748407a845` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8`
- internal ETH transfers (Etherscan):
  - 0.021037 ETH: `0x000000000027d2efc283613d0c3e24a8b430c4d8` -> `0xea674fdde714fd979de3edf0f56aa9716b898ec8` [call]
  - 0.000000 ETH: `0x816e01c2d1763f5015f8760a7a644cbec41ee44b` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
  - 0.000000 ETH: `0x04f579e3c13e58c0faf7ad45c1515ac5bfd30852` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
  - 0.000000 ETH: `0xce0d229976212a8acfc987108c9aa5fd5df6df24` -> `0x000000000027d2efc283613d0c3e24a8b430c4d8` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xa80f2c8f61c56546001f5fc2eb8d6e4e72c45d4c` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Sync
  - `0x020e6d0e80d08567ecb14f942fa326748407a845` UniswapV2 Swap
- receipt status 1, index 4
