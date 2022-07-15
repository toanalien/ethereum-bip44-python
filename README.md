Ethereum BIP44 Python
================================

*Code adapted from two1 library for bitcoin by 21 Inc. (https://github.com/21dotco/two1-python/tree/master/two1)

### Requirements
Python packages:  
`pip install -r requirements.txt`

Imports:  
`from crypto import HDPrivateKey, HDPublicKey, HDKey`

### BIP32 Master Keys Creation:
```
master_key, mnemonic = HDPrivateKey.master_key_from_entropy()
print('BIP32 Wallet Generated.')  
print('Mnemonic Secret: ' + mnemonic)
```

### Accounts creation
Creation of multiple accounts under master key derived from seed phrase.
Compatible with [Metamask](https://metamask.io). You can just restore your wallet 
with seed phrase and get access to all the accounts under master key via Metamask.

use in bash

```bash
$ docker run -it toanalien/ethereum-bip44-python python main.py 100 seedphrase
# example
# $ docker run -it toanalien/ethereum-bip44-python python main.py 100 there aeroplane curve vent formation doge possible product distinct under spirit lamp
# Index 0:
#   Private key (hex, compressed): e2f2d3db59f6583f2c551c73193f6cf6653fb19cb78da3746fbcf1de0a1a9a1e
#   Address: 0x3868633c3bd0c7ae01ef4429b1dab76e84e3c5d4
# Index 1:
#   Private key (hex, compressed): 12430803f99b8a6afc6708358ca44da530dc197c78de2ac769602ab910a1ee59
#   Address: 0x0a3c2f06d5303c198d0ce10d9c0b5ef0df91701a
# Index 2:
#   Private key (hex, compressed): 41849182a0e6b3fca86f3aa0957c096b894c7bc85fc66c26e405cd1f25d049ee
#   Address: 0x0f6a4013cd782104ba38a32bdba9a3e64a237dc3
# Index 3:
#   Private key (hex, compressed): fa9003dbf5530de337e492017b8f70f6f22f79b9f916ea51119e3e89eebfdd5d
#   Address: 0xf6bcc3e1ea8d349192c687bd2d7e4586a23fe1d3
```

import to python

```python
from crypto import HDPrivateKey, HDKey
master_key = HDPrivateKey.master_key_from_mnemonic('laundry snap patient survey sleep strategy finger bone real west arch protect')
root_keys = HDKey.from_path(master_key,"m/44'/60'/0'")
acct_priv_key = root_keys[-1]
for i in range(10):
    keys = HDKey.from_path(acct_priv_key,'{change}/{index}'.format(change=0, index=i))
    private_key = keys[-1]
    public_key = private_key.public_key
    print("Index %s:" % i)
    print("  Private key (hex, compressed): " + private_key._key.to_hex())
    print("  Address: " + private_key.public_key.address())
```

### Get Account XPUB
```
master_key = HDPrivateKey.master_key_from_mnemonic('laundry snap patient survey sleep strategy finger bone real west arch protect')
root_keys = HDKey.from_path(master_key,"m/44'/60'/0'")
acct_priv_key = root_keys[-1]
acct_pub_key = acct_priv_key.public_key
print('Account Master Public Key (Hex): ' + acct_pub_key.to_hex())
print('XPUB format: ' + acct_pub_key.to_b58check())
```

### Get Address from XPUB
```
acct_pub_key = HDKey.from_b58check('xpub6DKMR7KpgCJbiN4TdzcqcB1Nk84D9bsYUBhbk43EjRqH4RTjz7UgGLZxcQ4JdHBSHDmTUDLApMwYHRQCbbMCPQEtcbVofZEQjFazpGPT1nW')
keys = HDKey.from_path(acct_pub_key,'{change}/{index}'.format(change=0, index=0))
address = keys[-1].address()
print('Account address: ' + address)
```
### Get 64 Character Private Key from XPRIV
```
print(Private key (hex): " + private_key._key.to_hex())

```





