from Complex import Complex


def main():
    a, b = eval(input("Enter the first complex number: "))
    c, d = eval(input("Enter the second complex number: "))
    n1 = Complex(a, b)
    n2 = Complex(c, d)
    print("(", str(n1), ") + (", str(n2), ") = (", str(n1 + n2), ")")
    print("(", str(n1), ") - (", str(n2), ") = (", str(n1 - n2), ")")
    print("(", str(n1), ") * (", str(n2), ") = (", str(n1 * n2), ")")
    print("(", str(n1), ") / (", str(n2), ") = (", str(n1 / n2), ")")
    print("| ", str(n1), " | = ", str(abs(n1)))


main()
