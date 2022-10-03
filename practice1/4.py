import math


def main():
    #   读入两个圆的半径和圆心坐标
    x1, y1 = eval(input("Enter the center coordinate of the first round : "))
    r1 = eval(input("Enter the radius of the first round : "))
    x2, y2 = eval(input("Enter the center coordinate of the second round : "))
    r2 = eval(input("Enter the radius of the second round : "))

    #   计算两圆心间距及两半径和与差的绝对值
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    ra = float(r1 + r2)
    ri = float(abs(r1 - r2))

    #   分情况判断两圆的关系
    if d > ra:
        print("外离")
    elif d == ra:
        print("外切")
    elif ra > d > ri:
        print("相交")
    elif d == ri:
        print("内切")
    else:
        print("内含")


main()
