from Circle import Circle


def main():
    circle1 = Circle()
    print(circle1.radius, " ", format(circle1.get_area(), ".4f"))

    circle2 = Circle(5)
    print(circle2.radius, " ", format(circle2.get_area(), ".3f"))

    circle3 = Circle(25)
    print(circle3.radius, " ", format(circle3.get_area(), ".3f"))

    circle4 = Circle(100)
    print(circle4.radius, " ", format(circle4.get_area(), ".3f"))


main()