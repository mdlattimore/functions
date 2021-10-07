from base64 import b64encode
import os
import datetime


def generate_key(size):
    byte_string = os.urandom(size)
    key = b64encode(byte_string).decode('utf-8')  # Convert byte class instance to utf-8 encoded string
    return key


result = generate_key(32)

with open(f'key_{datetime.datetime.now()}.txt', 'w') as file:
    file.write(result)

print(result)
print(datetime.datetime.now())


