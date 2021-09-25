import os
import time


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def countdown(x):
    countdown_time = range(x, 0, -1)
    clear()
    for number in countdown_time:
        print("\n" * ((size[1] - 6) // 2))
        print((" " * (size[0] // 2)), number, end="", flush=True)
        time.sleep(1)
        clear()
    print("\n" * ((size[1]-4) // 2))
    print((" " * (size[0] // 2)),end="", flush=True)
    print("""DONE""")
    input()
    clear()


size = os.get_terminal_size()

countdown(10)
