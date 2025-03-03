from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt(data, key, mode="ECB"):
    key = key.ljust(8, "0").encode()[:8]
    cipher = DES.new(key, DES.MODE_ECB if mode == "ECB" else DES.MODE_CBC if mode == "CBC" else DES.MODE_CTR, nonce=b'0')
    return cipher.encrypt(pad(data.encode() if isinstance(data, str) else data, DES.block_size))

def decrypt(data, key, mode="ECB"):
    key = key.ljust(8, "0").encode()[:8]
    cipher = DES.new(key, DES.MODE_ECB if mode == "ECB" else DES.MODE_CBC if mode == "CBC" else DES.MODE_CTR, nonce=b'0')
    return unpad(cipher.decrypt(data), DES.block_size).decode(errors='ignore')
