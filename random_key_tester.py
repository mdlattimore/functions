from base64 import b64encode
import os
import time
import sys
from rich.console import Console

console = Console()


def generate_key(size):
    byte_string = os.urandom(size)
    key = b64encode(byte_string).decode('utf-8')
    return key

    
key_size = 6
final = []
keys = []
keys_set = set()
print()
with console.status("Working ... \n"):
    print()
    start = time.perf_counter()
    while True:
        key = generate_key(key_size)
        keys.append(key)
        keys_set.add(key)
        if len(keys) != len(keys_set):  # compare lengths of list and set and break
            # to determine when duplicate occurs. Once duplicate occurs, list and set
            # no longer of equal length since set does not allow duplicate values
            final.append(key)
            break
        #if keys.count(key) > 1: THIS IS A VERY SLOW METHOD
            #final.append(key)
            #break
        else:
            continue
    stop = time.perf_counter()

#print(keys) USE ONLY FOR TESTING
print()
print(f"The {len(keys)} st/nd/th key was a duplicate")
print(f"You produced {len(keys_set)} unique keys.")
print(f"The duplicated key was {final[0]}")
print(f"Time: {stop - start} seconds")
print()
    

