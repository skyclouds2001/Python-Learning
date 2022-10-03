def my_format(n, w):
    s = str(n)
    l = len(s)
    if l < w:
        for i in range(w - l):
            s = "0" + s
    return s


def main():
    s = eval(input("Enter the integer : "))
    w = eval(input("Enter the width : "))
    print(my_format(s, w))


main()
