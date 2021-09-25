def dec_convert(number):
    """Returns binary representation of positive base 10 integer as a
    string without the 0b prefix used by Python to designate a binary
    number. No input validation is baked into the function. Input validation
    should be handled within calling script. For an example, see code below
    if __name__ == '__main__' in this script"""

    return str(bin(number)[2:])


if __name__ == "__main__":

    # input validation
    while True:
        try:
            num = int(input("Please enter a base 10 number: "))
        except ValueError:
            print("Invalid input.")
            continue
        break

    print(dec_convert(num))
