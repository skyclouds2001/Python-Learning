from Circle import Circle


def main():
    c = Circle()

    n = 5
    print_area(c, n)

    print("c->R = ", c.radius, "\tn = ", n)


def print_area(c, t):
    print("Radius\t\tArea")
    while t >= 1:
        print(c.radius, "\t\t", c.get_area())
        c.radius += 1
        t -= 1


main()
