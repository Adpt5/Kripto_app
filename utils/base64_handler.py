import base64

def to_base64(data):
    return base64.b64encode(data).decode()

def from_base64(data):
    return base64.b64decode(data.encode())
