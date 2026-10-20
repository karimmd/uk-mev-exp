# pack_175

Block 13569694. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x8783b53adfd52d2c59ac0467fce910dc562889d352a1984e0ef349d0d07b2edf`
- block 13569694, position 0, result success, from `0x7b34d49fabeeb86d785db00cbe5b730b2afbf2ea`, to `0x000000005736775feb0c8568e7dee77222a26880`, value 0.000000 ETH, gas used 41346 at 81.4 gwei, fee 0.003365 ETH
- token transfers (Blockscout, decoded):
  - 1.753999 WETH (`0xc02aaa39`): `0x000000005736775feb0c8568e7dee77222a26880` -> `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae`
  - 13933.463034 XTM (`0xcd1faff6`): `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` -> `0x000000005736775feb0c8568e7dee77222a26880`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcd1faff6e578fa5cac469d2418c95671ba1a62fe` Transfer
  - `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` UniswapV2 Sync
  - `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` UniswapV2 Swap
- receipt status 1, index 0

### Victim leg: `0x0dd80d912f04ac79a6e1236a388389f9a23b163ac899d2caca496a1eb742bb2b`
- block 13569694, position 1, result success, from `0x8e6594d31ac86cd3d2481d09cf59a275c94ae4d6`, to `0x881d40237659c251811cec9c364ef91dc08d300c`, value 0.000000 ETH, gas used 448283 at 103.6 gwei, fee 0.046437 ETH
- token transfers (Blockscout, decoded):
  - 60000.279626 BMI (`0x725c263e`): `0x8e6594d31ac86cd3d2481d09cf59a275c94ae4d6` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 59475.277179 BMI (`0x725c263e`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 23790.110872 BMI (`0x725c263e`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x53813285cc60b13fcd2105c6472a47af01f8ac84`
  - 1.704036 WETH (`0xc02aaa39`): `0x53813285cc60b13fcd2105c6472a47af01f8ac84` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 35685.166307 BMI (`0x725c263e`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xa9bd7eef0c7affbdbdae92105712e9ff8b06ed49`
  - 2.556804 WETH (`0xc02aaa39`): `0xa9bd7eef0c7affbdbdae92105712e9ff8b06ed49` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 4.260840 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae`
  - 32126.311146 XTM (`0xcd1faff6`): `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 32126.311146 XTM (`0xcd1faff6`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 525.002447 BMI (`0x725c263e`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11ededebf63bef0ea2d2d071bdf88f71543ec6fb`
  - 32126.311146 XTM (`0xcd1faff6`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x8e6594d31ac86cd3d2481d09cf59a275c94ae4d6`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x725c263e32c72ddc3a19bea12c5a0479a81ee688` Transfer
  - `0x725c263e32c72ddc3a19bea12c5a0479a81ee688` Approval
  - `0x725c263e32c72ddc3a19bea12c5a0479a81ee688` Transfer
  - `0x725c263e32c72ddc3a19bea12c5a0479a81ee688` Approval
  - `0x725c263e32c72ddc3a19bea12c5a0479a81ee688` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x53813285cc60b13fcd2105c6472a47af01f8ac84` UniswapV2 Sync
  - `0x53813285cc60b13fcd2105c6472a47af01f8ac84` UniswapV2 Swap
  - `0x725c263e32c72ddc3a19bea12c5a0479a81ee688` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xa9bd7eef0c7affbdbdae92105712e9ff8b06ed49` UniswapV2 Sync
  - `0xa9bd7eef0c7affbdbdae92105712e9ff8b06ed49` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xcd1faff6e578fa5cac469d2418c95671ba1a62fe` Transfer
  - `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` UniswapV2 Sync
  - `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` UniswapV2 Swap
  - `0xcd1faff6e578fa5cac469d2418c95671ba1a62fe` Transfer
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
  - `0x725c263e32c72ddc3a19bea12c5a0479a81ee688` Transfer
  - `0xcd1faff6e578fa5cac469d2418c95671ba1a62fe` Transfer
  - `0x881d40237659c251811cec9c364ef91dc08d300c` other
- receipt status 1, index 1

### Back leg: `0x7fcc2bd0b50d93dd06e092d9b34fdc9b96b6075f08020cbfeae5645c0addecf6`
- block 13569694, position 2, result success, from `0x7b34d49fabeeb86d785db00cbe5b730b2afbf2ea`, to `0x000000005736775feb0c8568e7dee77222a26880`, value 0.000000 ETH, gas used 34951 at 1452.2 gwei, fee 0.050754 ETH
- token transfers (Blockscout, decoded):
  - 13933.463034 XTM (`0xcd1faff6`): `0x000000005736775feb0c8568e7dee77222a26880` -> `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae`
  - 1.875399 WETH (`0xc02aaa39`): `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` -> `0x000000005736775feb0c8568e7dee77222a26880`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xcd1faff6e578fa5cac469d2418c95671ba1a62fe` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` UniswapV2 Sync
  - `0xc34da1ab0f93dfed30729951dafcfb9ce3e2a9ae` UniswapV2 Swap
- receipt status 1, index 2
