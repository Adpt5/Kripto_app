def encrypt(data, key):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data.encode() if isinstance(data, str) else data)])

def decrypt(data, key):
    return encrypt(data, key).decode(errors='ignore')
