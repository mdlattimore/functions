def teletype(text: str, interval: float):
    """ Prints text one letter at a time with 'interval' seconds between letters
    using a 'for loop.'
    Requires import of time module.
    The function executes a print function, so do not pair with 'print' when calling in main program"""
    import time  # remove if you copy/paste function into main program then import time at top of module
    for char in text:
        print(char, end="", flush=True)
        time.sleep(interval)
    print()  # remove if execution should continue on the same line as last line of print


def reverse_type(text: str):
    """Returns provided text in reverse"""
    return text[::-1]


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


def letter_skip(text: str, interval: int):
    """Returns string comprised of every nth letter of given text"""
    listed_text = list(text[::interval])
    new_text = ""
    for char in listed_text:
        new_text += char
    return new_text

def strip_punct(text: str):
    """Strips punctuation from string. Useful for word frequency analysis. Requires import of string module"""
    from string import whitespace
    processed_text = ""
    for char in text:
        char.replace("-", " ")
        if char.isalnum() or char in whitespace:
            processed_text += char   
    return processed_text


if __name__ == "__main__":
    with open('romeo_and_juliet.txt', mode="r") as file:
        text = file.read()
        
    processed = (strip_punct(text))
    print(len(processed.split()))
    set_list = {word.casefold() for word in processed.split()}
    print(len(set_list))
    