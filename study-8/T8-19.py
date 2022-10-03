from Rectangle2D import Rectangle2D


def main():
    x1, y1, width1, height1 = eval(input("Enter x1, y1, width1, height1: "))
    r1 = Rectangle2D(x1, y1, width1, height1)
    x2, y2, width2, height2 = eval(input("Enter x2, y2, width2, height2: "))
    r2 = Rectangle2D(x2, y2, width2, height2)
    print("Area for r1 is", r1.get_area())
    print("Perimeter for r1 is", r1.get_perimeter())
    print("Area for r1 is", r2.get_area())
    print("Perimeter for r1 is", r2.get_perimeter())
    print("r1 contains the center of r2?", r1.contains_point(r2.get_x(), r2.get_y()))
    print("r1 contains r2?", r1.contain(r2))
    print("r1 overlaps r2?", r1.overlaps(r2))


main()
