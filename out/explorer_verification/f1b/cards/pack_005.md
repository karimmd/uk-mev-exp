# pack_005

Block 12284806. Three transactions in block order: front, victim, back. Evidence is what two public explorers return for each hash.

### Front leg: `0x4dcf9e82ffd14ab4fdc25122ebb0237583edb0b867d28d022eeb2f16bc1023c0`
- block 12284806, position 0, result success, from `0x36660b1156a7983da91037c985f6987fe612c273`, to `0x38f2e4e2e33c81998b20989513e124e9d568f365`, value 0.000000 ETH, gas used 131329 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 12.150242 WETH (`0xc02aaa39`): `0x38f2e4e2e33c81998b20989513e124e9d568f365` -> `0x06da0fd433c1a5d7a4faa01111c044910a184553`
  - 29440.140504 USDT (`0xdac17f95`): `0x06da0fd433c1a5d7a4faa01111c044910a184553` -> `0x1812ef69e1753f908229df40d304a5fbdcd52dd3`
  - 365.683852 FORTH (`0x77fba179`): `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` -> `0x38f2e4e2e33c81998b20989513e124e9d568f365`
  - 4.000000 CHI (`0x00000000`): `0x38f2e4e2e33c81998b20989513e124e9d568f365` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.000000 ETH: `0x2042987520a09c5dfe19eb2d4610fd7977a782f0` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xdca8d4c265640e5493350bb4e03b0c3fe010b94c` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0xe9239400d6fb307d4f3e54541b9e1745b0f9fb6f` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x0b085bf2b318a08a0c62a8b8d43add6f54eb8f4e` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Sync
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Swap
  - `0x77fba179c79de5b7653f68b5039af940ada60ce0` Transfer
  - `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` UniswapV2 Sync
  - `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` UniswapV2 Swap
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Transfer
- receipt status 1, index 0

### Victim leg: `0xafb7426811eca4a2de2e430b41544cdbc763148d653c48b38bbd8136a842a084`
- block 12284806, position 1, result success, from `0xfe2e1954c7b28817894cf63eb5f182f917ae24b8`, to `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`, value 0.000000 ETH, gas used 107127 at 700.0 gwei, fee 0.074989 ETH
- token transfers (Blockscout, decoded):
  - 34501.776138 USDT (`0xdac17f95`): `0xfe2e1954c7b28817894cf63eb5f182f917ae24b8` -> `0x1812ef69e1753f908229df40d304a5fbdcd52dd3`
  - 377.248070 FORTH (`0x77fba179`): `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` -> `0xfe2e1954c7b28817894cf63eb5f182f917ae24b8`
- internal ETH transfers (Etherscan):
  - none with value
- events in the receipt (Etherscan), by emitting contract:
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x77fba179c79de5b7653f68b5039af940ada60ce0` Transfer
  - `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` UniswapV2 Sync
  - `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` UniswapV2 Swap
- receipt status 1, index 1

### Back leg: `0xf42ceda950de35e887fdfdf2de446711f0e66abafc7fdc9bcae3b39699fed522`
- block 12284806, position 2, result success, from `0x36660b1156a7983da91037c985f6987fe612c273`, to `0x38f2e4e2e33c81998b20989513e124e9d568f365`, value 0.000000 ETH, gas used 102282 at 0.0 gwei, fee 0.000000 ETH
- token transfers (Blockscout, decoded):
  - 365.683852 FORTH (`0x77fba179`): `0x38f2e4e2e33c81998b20989513e124e9d568f365` -> `0x1812ef69e1753f908229df40d304a5fbdcd52dd3`
  - 33322.389418 USDT (`0xdac17f95`): `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` -> `0x06da0fd433c1a5d7a4faa01111c044910a184553`
  - 13.669706 WETH (`0xc02aaa39`): `0x06da0fd433c1a5d7a4faa01111c044910a184553` -> `0x38f2e4e2e33c81998b20989513e124e9d568f365`
  - 4.000000 CHI (`0x00000000`): `0x38f2e4e2e33c81998b20989513e124e9d568f365` -> `0x0000000000000000000000000000000000000000`
- internal ETH transfers (Etherscan):
  - 0.379866 ETH: `0x38f2e4e2e33c81998b20989513e124e9d568f365` -> `0x04668ec2f57cc15c381b461b9fedab5d451c8f7f` [call]
  - 0.000000 ETH: `0xc699772a1cffc628acabd6a8ec2b653f8a0c8c5a` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x877092fb7c522b441995fb53a5626234cbb5ff95` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x218aed014bf0d903ef503be5b7dc36f33a688596` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
  - 0.000000 ETH: `0x22bae990fba22406d26b9dbe7b82d1bc678b3245` -> `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` [self-destruct]
- events in the receipt (Etherscan), by emitting contract:
  - `0x77fba179c79de5b7653f68b5039af940ada60ce0` Transfer
  - `0xdac17f958d2ee523a2206206994597c13d831ec7` Transfer
  - `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` UniswapV2 Sync
  - `0x1812ef69e1753f908229df40d304a5fbdcd52dd3` UniswapV2 Swap
  - `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2` Transfer
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Sync
  - `0x06da0fd433c1a5d7a4faa01111c044910a184553` UniswapV2 Swap
  - `0x0000000000004946c0e9f43f4dee607b0ef1fa1c` Transfer
- receipt status 1, index 2
