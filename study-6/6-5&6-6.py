from GCDFuction import gcd


def main():
    n1 = eval(input("Enter the first number : "))
    n2 = eval(input("Enter the second number : "))
    print("the biggest number of", n1, "and", n2, "is", gcd(n1, n2))


main()
