from Circle2D import Circle2D


def main():
    print("Enter x1, y1, radius1: ")
    x1, y1, r1 = eval(input())
    c1 = Circle2D(x1, y1, r1)
    print("Enter x1, y1, radius2: ")
    x2, y2, r2 = eval(input())
    c2 = Circle2D(x2, y2, r2)

    print("Area for c1 is ", c1.get_area())
    print("Perimeter for c1 is ", c1.get_perimeter())
    print("Area for c2 is ", c2.get_area())
    print("Perimeter for c2 is ", c2.get_perimeter())
    print("c1 contains the center of c2? ", c1.contain_point(c2.get_x(), c2.get_y()))
    print("c1 contains c2? ", c1.contain(c2))
    print("c1 overlaps c2? ", c1.overlaps(c2))


main()
