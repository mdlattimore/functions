# A Collection of Useful(ish) Functions and Code Snippets
This is a collection of functions I created when first learning Python, 
simply as an exercise to test my understanding of the underlying skills. 
They are basically useless but still fun little exercises.

## Binary to Decimal Converter
```python
def bin_convert(num):
    """Convert binary input to base 10 representation. No input validation
    is baked into the function. Input validation should be handled within
    calling script. For an example, see code below if __name__ == '__main__'
    in this script"""

    bin_num = [char for char in num][::-1]
    result = []
    for index, digit in enumerate(bin_num):
        x = int(digit) * (2 ** index)
        result.append(x)

    return sum(result)
```

## Decimal to Binary Converter
```python
def dec_convert(number):
    """Returns binary representation of positive base 10 integer as a
    string without the 0b prefix used by Python to designate a binary
    number. No input validation is baked into the function. Input validation
    should be handled within calling script. For an example, see code below
    if __name__ == '__main__' in this script"""

    return str(bin(number)[2:])
```

## Random Key Generation
```python
""" Function that generates random bytes of given size and then converts to string """

def generate_key(size):
    import os
    from base64 import b64encode
    byte_string = os.urandom(size)
    key = b64encode(byte_string).decode('utf-8')
    return key
```

## Center a tkinter root or toplevel window on screen
```python
def center_screen(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    return "%dx%d+%d+%d" % (width, height, x, y)
```

## Math Functions  
- ### Circle Area
  ```python
  def area_circle(r: float):
    """Computes the area of a circle with radius 'r'. Uses literal value of pi rather than math.pi to avoid necessity of importing math module"""
    area = 3.141592653589793115997963468544185161590576171875 * (r ** 2)
    return area
    ```
- ### Rectangle Area
  ```python
  def area_rectangle(length: float, width: float):
    """Computes the area of rectangle given length and width"""
    area = length * width
    return area
    ```
- ### Triangle Area
  ```python
  def area_triangle(base: float, height: float):
    """Computes the area of a triangle given base and height"""
    area = (base / 2) * height
    return area
    ```
- ### Cube Volume
  ```python
  def volume_cube(length: float, width: float, height: float):
    """Calculates volume of cube"""
    volume = length * width * height
    return volume
    ```
- ### Sphere Volume
  ```python
  def volume_sphere(radius: float):
    """Calculates volume of sphere with radius 'r' """
    volume = (4 / 3) * (3.141592653589793115997963468544185161590576171875 * (radius ** 3))
    return volume
    ```
- ### Triangle Hypotenuse
  ```python
  def hypotenuse_triangle(a: float, b: float):
    """Calculates length of the hypotenuse of a right triangle"""
    c = ((a ** 2) + (b ** 2)) ** (1/2)
    return c
    ```

## String Functions
- ### Teletype Function
  ```python
  def teletype(text: str, interval: float = .07):
    """ Prints text one letter at a time with 'interval' seconds between letters
    using a 'for loop.'
    Requires import of time module.
    The function executes a print function, so do not pair with 'print' when calling in main program"""
    import time  # remove if you copy/paste function into main program then import time at top of module
    for char in text:
        print(char, end="", flush=True)
        time.sleep(interval)
    print()  # remove if execution should continue on the same line as last line of print
    ```
- ### Reverse Text
  ```python
  def reverse_type(text: str):
    """Returns provided text in reverse"""
    return text[::-1]
    ```
- ### Scramble Text
  ```python
  def scramble_text(text: str):
    """Scrambles given text and returns scrambled string. If function is copy/pasted into main program,
    remove import random function."""
    import random  # remove if you copy/paste function into main program
    # then import at top of module
    length = len(text)
    scrambled_string = random.sample(text, k=length)
    scrambled_text = ""
    for char in scrambled_string:
        scrambled_text += char
    return scrambled_text
    ```
- ### Remove Vowels
  ```python
  def remove_vowels(text: str):
    """Removes vowels from text and returns vowel-less string"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_text = ""
    for letter in text:
        if letter not in vowels:
            new_text += letter
        else:
            continue
    return new_text
    ```
- ### Letter Skip
  ```python
  def letter_skip(text: str, interval: int):
    """Returns string comprised of every nth letter of given text"""
    listed_text = list(text[::interval])
    new_text = ""
    for char in listed_text:
        new_text += char
    return new_text
    ```
- ### Remove Punctuation
  ```python
  def strip_punct(text: str):
    """Strips punctuation from string. Useful for word frequency analysis. Requires import of string module"""
    from string import whitespace
    text = text.replace("\n", " ")
    # Uncomment following line to count each part of a hyphenated word as a separate word. Otherwise, a hypenated word is considered a single word
    # text = text.replace("-", " ")
    processed_text = ""
    for char in text:
        if char.isalnum() or char in whitespace:
            processed_text += char   
    return processed_text
    ```
- ### Word Count Script
  ```python
  from pprint import pprint
  from collections import Counter

  def strip_punct(text: str):
    """Strips punctuation from string. Useful for word frequency analysis. Requires import of string module"""
    from string import whitespace, punctuation
    text = text.replace("\n", " ")
    # Uncomment following line to count each part of a hyphenated word as a separate word. Otherwise, a hypenated word is considered a single word
    # text = text.replace("-", " ")
    processed_text = ""
    for char in text:
        if char.isalnum() or char in whitespace:
            processed_text += char   
    return processed_text

  def word_count(text):
    scrubbed_text = strip_punct(text)
    word_list = scrubbed_text.split()
    word_set = set(word_list)

    word_count = Counter(word_list)
    return word_count, len(word_list)


  if __name__ == '__main__':

    text = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

    Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

    But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""

    counts = word_count(text)
    count_list = []
    for word, count in counts.items():
        count_list.append((word, count))    
    sorted_list = sorted(count_list, key = lambda x: x[-1], reverse=True)
    for n in sorted_list:
        print(f"{n[0]}: {n[1]}")
    ```

## Random Key Tester Script
```python
"""Generates random byte strings of 'n' bytes (user input) and then runs the key generation function on a loop until it generates a collision"""

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

    
print("Enter key_size (in bytes). Keys larger than 8 bytes may take an extraordinarily long time to test.")
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

```

