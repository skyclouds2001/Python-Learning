from QuadraticEquation import QuadraticEquation


def main():
    a, b, c = eval(input("Enter the a, b, c : "))
    q = QuadraticEquation(a, b, c)
    if q.get_discriminant() < 0:
        print("无解")
    elif q.get_discriminant() == 0:
        print("x1 = x2 = ", q.get_root1())
    else:
        print("x1 = ", q.get_root1(), "\tx2 = ", q.get_root2())


main()
