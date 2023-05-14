"""Generates random byte strings of 'n' bytes (user input) and then runs the key generation function on a loop until it generates a collision"""

from base64 import b64encode
import os
import time
import sys
from rich.console import Console

console = Console()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def generate_key(size):
    byte_string = os.urandom(size)
    key = b64encode(byte_string).decode('utf-8')
    return key

clear()
    
print("Enter key_size (in bytes). Keys larger than 6 bytes may take an extraordinarily long time to test.")
key_size = int(input("> "))
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
time = stop - start
print()
print(f"The key was {key}")
print(f"The duplicated key was {final[0]} (these two must match)")
print(f"The duplicated key was first generated at: {keys.index(key)}")
print(f"The key at index position {len(keys)} was a duplicate")
print(f"The duplicate keys were {(len(keys)) - (keys.index(key))} apart")
print(f"You produced {len(keys_set)} unique keys.")
print(f"Time: {time} seconds")
print()
    
# TODO Set up to run n times, store the times and average them.
