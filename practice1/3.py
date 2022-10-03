import math


def main():
    n = eval(input("Enter a number between 0 and 1000 : "))
    #   取出各位数并相加
    ans = n % 10 + n // 10 % 10 + n // 100 % 10 + n // 1000
    print("The sum of every digit is", ans)
    print("The area of", ans, "is", ans * ans * math.pi)


main()
