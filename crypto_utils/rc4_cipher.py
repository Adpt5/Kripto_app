def ksa(key):
    key = [ord(c) for c in key]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, data_len):
    i = j = 0
    keystream = []
    for _ in range(data_len):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream.append(S[(S[i] + S[j]) % 256])
    return keystream

def encrypt(data, key):
    S = ksa(key)
    keystream = prga(S, len(data))
    return bytes([data[i] ^ keystream[i] for i in range(len(data))])

def decrypt(data, key):
    return encrypt(data, key)
