from crypto import HDPrivateKey, HDKey
import sys
count = int(sys.argv[1])
mnemonic = " ".join(sys.argv[2:])
master_key = HDPrivateKey.master_key_from_mnemonic(mnemonic)
root_keys = HDKey.from_path(master_key,"m/44'/60'/0'")
acct_priv_key = root_keys[-1]
for i in range(count):
    keys = HDKey.from_path(acct_priv_key,'{change}/{index}'.format(change=0, index=i))
    private_key = keys[-1]
    public_key = private_key.public_key
    print("Index %s:" % i)
    print("  Private key (hex, compressed): " + private_key._key.to_hex())
    print("  Address: " + private_key.public_key.address())