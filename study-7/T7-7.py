from LinearEquation import LinearEquation


def main():
    a, b, c, d, e, f = eval(input("Input a, b, c, d, e, f:\n"))
    le = LinearEquation(a, b, c, d, e, f)
    if le.is_solvable():
        print("X = ", le.get_x(), "\t", "Y = ", le.get_y())
    else:
        print("No solution!")


main()
