import math


#   形状基类
class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)

    #   访问器方法
    def get_color(self):
        return self.__color

    def is_filled(self):
        return self.__filled

    #   设置器方法
    def set_color(self, color):
        self.__color = color

    def set_filled(self, filled):
        self.__filled = filled


#   三角形类
class Triangle(GeometricObject):
    #   初始化方法
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, color="green", filled=True):
        if side1 <= 0 or side2 <= 0 or side3 <= 0 or \
                side1 + side2 < side3 or side3 + side2 < side1 or side1 + side3 < side2:
            raise TriangleError

        super().__init__(color, filled)

        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    #   计算面积周长方法
    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def get_area(self):
        p = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(p * (p - self.__side1) * (p - self.__side2) * (p - self.__side3))

    #   重写字符串化方法
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + \
               " side2 = " + str(self.__side2) + \
               " side3 = " + str(self.__side3)

    #   访问器方法
    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    #   设置器方法
    def set_side1(self, side1):
        self.__side1 = side1

    def set_side2(self, side2):
        self.__side2 = side2

    def set_side3(self, side3):
        self.__side3 = side3


#   三角形异常类
class TriangleError(RuntimeError):
    __side1: float
    __side2: float
    __side3: float

    #   初始化方法
    def __init__(self):
        super().__init__()

    #   访问器方法
    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    #   设置器方法
    def set_side1(self, side1):
        self.__side1 = side1

    def set_side2(self, side2):
        self.__side2 = side2

    def set_side3(self, side3):
        self.__side3 = side3


def main():
    # 提示输入并读取
    print("Enter the three sides of the triangle: ")
    side1, side2, side3 = eval(input())
    print("Enter the color of the triangle: ")
    color = input()
    print("Enter the number if is filled of the triangle: ")
    filled = eval(input())

    # 尝试创建Triangle类
    try:
        tri = Triangle(side1, side2, side3, color, filled == 1)
    except TriangleError as e:
        print(e)
        return

    # 打印输出
    print("The area of the triangle: {:.2f}".format(tri.get_area()))
    print("The perimeter of the triangle: ", tri.get_perimeter())
    print("The color of the triangle: ", tri.get_color())
    print("The fill of the triangle: ", tri.is_filled())


if __name__ == '__main__':
    main()
