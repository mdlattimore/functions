def teletype(text: str, interval: float):
    """ Prints text one letter at a time with 'interval' seconds between letters
    using a 'for loop.'
    Requires import of time module."""
    import time  # remove if you copy/paste function into main program then import time at top of module
    for char in text:
        print(char, end="", flush=True)
        time.sleep(interval)
    print()  # remove if execution should continue on the same line as last line of print


if __name__ == "__main__":
    quote = "Fourscore and seven years ago, our fathers brought forth on this continent a new nation," \
            " conceived in liberty and dedicated to the proposition that all men are created equal."

    teletype(quote, .07)