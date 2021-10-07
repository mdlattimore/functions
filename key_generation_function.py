""" Function that generates random bytes of given size and then converts to string """

def generate_key(size):
    import os
    from base64 import b64encode
    byte_string = os.urandom(size)
    key = b64encode(byte_string).decode('utf-8')
    return key

