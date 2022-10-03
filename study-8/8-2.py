def char_hex_to_decimal(x):
    if '0' <= x <= '9':
        return int(x)
    elif 'a' <= x <= 'f':
        return ord(x) - ord('a') + 10
    elif 'A' <= x <= 'F':
        return ord(x) - ord('A') + 10


def string_hex_to_decimal(x):
    ans = 0
    for i in range(len(x)):
        ans = ans * 16 + char_hex_to_decimal(x[i])
    return ans


def main():
    s = input("Enter a hex number : ")
    print(string_hex_to_decimal(s))


main()
