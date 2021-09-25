def bin_convert(num):
    bin_num = [lett for lett in num][::-1]
    result = []
    for index, digit in enumerate(bin_num):
        x = int(digit) * (2 ** index)
        result.append(x)

    return sum(result)


number = input("Please enter a binary: ")
print(bin_convert(number))