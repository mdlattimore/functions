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


if __name__ == "__main__":

    allowed = {'1', '0'}
    number = input("Please enter a binary: ")

    # input validation
    while True:
        if not set(number).issubset(allowed):
            number = input("Invalid input. Please try again: ")
            continue
        else:
            break

    print(bin_convert(number))