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



