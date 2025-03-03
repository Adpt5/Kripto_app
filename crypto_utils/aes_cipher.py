from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(data, key, mode="ECB"):
    key = key.ljust(16, "0").encode()[:16]
    cipher = AES.new(key, AES.MODE_ECB if mode == "ECB" else AES.MODE_CBC if mode == "CBC" else AES.MODE_CTR, nonce=b'0')
    return cipher.encrypt(pad(data.encode() if isinstance(data, str) else data, AES.block_size))

def decrypt(data, key, mode="ECB"):
    key = key.ljust(16, "0").encode()[:16]
    cipher = AES.new(key, AES.MODE_ECB if mode == "ECB" else AES.MODE_CBC if mode == "CBC" else AES.MODE_CTR, nonce=b'0')
    return unpad(cipher.decrypt(data), AES.block_size).decode(errors='ignore')
