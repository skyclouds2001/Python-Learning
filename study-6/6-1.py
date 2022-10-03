def imax(n1, n2):
    if n1 > n2:
        n = n1
    else:
        n = n2
    return n


def main():
    n1 = eval(input("Enter the first number : "))
    n2 = eval(input("Enter the second number : "))
    print("the biggest number of", n1, "and", n2, "is", imax(n1, n2))
    print("the biggest number of", n1, "and", n2, "is", imax(n2=12, n1=21))


main()
