# pack_060

Block 13443766. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0xfce780d8b5b9996ac34fd2ab0ad4b3b7cbfc7f0179cafb2ca95493bed755ba7b`
- block 13443766, position 6, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.000000 ETH, gas used 84034 at 750.0 gwei, fee 0.063025 ETH
- token transfers (Blockscout, decoded):
  - 13.817921 aKLIMA (`0x6b4d5e9e`): `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 4.890465 WETH (`0xc02aaa39`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x2fa7361d7e3b812375604681eb155a97b4d65e9e`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0x6b4d5e9ec2acea23d4110f4803da99e25443c5df` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` UniswapV3 Swap
- receipt status 1, index 6

### Victim leg: `0x34bd9302fccad2b00241c2e7abbb7416e5683a5a660a2ffdf6508321a969ec6e`
- block 13443766, position 8, result success, from `0x0f402f993fc698e5854d4f6848422b25ab7955ee`, to `0x881d40237659c251811cec9c364ef91dc08d300c`, value 4.500000 ETH, gas used 317846 at 185.6 gwei, fee 0.058995 ETH
- token transfers (Blockscout, decoded):
  - 4.460625 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x0000000000000000000000000000000000000000`
  - 11.712597 aKLIMA (`0x6b4d5e9e`): `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - 4.460625 WETH (`0xc02aaa39`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x2fa7361d7e3b812375604681eb155a97b4d65e9e`
  - 11.712597 aKLIMA (`0x6b4d5e9e`): `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631`
  - 11.712597 aKLIMA (`0x6b4d5e9e`): `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x0f402f993fc698e5854d4f6848422b25ab7955ee`
- internal ETH transfers (Etherscan):
  - 4.500000 ETH: `0x881d40237659c251811cec9c364ef91dc08d300c` -> `0x74de5d4fcbf63e00296fd95d33236b9794016631` [call]
  - 4.460625 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11111112542d85b3ef69ae05771c2dccff4faa26` [call]
  - 4.460625 ETH: `0x11111112542d85b3ef69ae05771c2dccff4faa26` -> `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` [call]
  - 4.460625 ETH: `0x27239549dd40e1d60f5b80b0c4196923745b1fd2` -> `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` [call]
  - 0.039375 ETH: `0x74de5d4fcbf63e00296fd95d33236b9794016631` -> `0x11ededebf63bef0ea2d2d071bdf88f71543ec6fb` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` WETH Deposit 4.460625 ETH for `0x27239549dd40e1d60f5b80b0c4196923745b1fd2`
  - `0x6b4d5e9ec2acea23d4110f4803da99e25443c5df` Transfer
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` UniswapV3 Swap
  - `0x6b4d5e9ec2acea23d4110f4803da99e25443c5df` Transfer
  - `0x11111112542d85b3ef69ae05771c2dccff4faa26` other
  - `0x6b4d5e9ec2acea23d4110f4803da99e25443c5df` Transfer
  - `0x881d40237659c251811cec9c364ef91dc08d300c` other
- receipt status 1, index 8

### Back leg: `0xa9926df2afd2d9c1a00ac8578f7fce5464fcd7b282186b26afb632cbac93fe8b`
- block 13443766, position 9, result success, from `0x0000000000c521824eaff97eac7b73b084ef9306`, to `0x499dd900f800fd0a2ed300006000a57f00fa009b`, value 0.190440 ETH, gas used 151230 at 750.0 gwei, fee 0.113422 ETH
- token transfers (Blockscout, decoded):
  - 5.202896 WETH (`0xc02aaa39`): `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` -> `0x499dd900f800fd0a2ed300006000a57f00fa009b`
  - 13.817921 aKLIMA (`0x6b4d5e9e`): `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x2fa7361d7e3b812375604681eb155a97b4d65e9e`
- internal ETH transfers (Etherscan):
  - 0.190440 ETH: `0x499dd900f800fd0a2ed300006000a57f00fa009b` -> `0x3ecef08d0e2dad803847e052249bb4f8bff2d5bb` [call]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x6b4d5e9ec2acea23d4110f4803da99e25443c5df` Transfer
  - `0x2fa7361d7e3b812375604681eb155a97b4d65e9e` UniswapV3 Swap
- receipt status 1, index 9
