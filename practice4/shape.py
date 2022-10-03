import abc
import math


# 形状基类
class Shape(abc.ABC):
    area = 0
    perimeter = 0

    # 计算面积函数
    @abc.abstractmethod
    def set_area(self):
        pass

    # 计算周长函数
    @abc.abstractmethod
    def set_perimeter(self):
        pass


# 圆类
class Circle(Shape):
    radius = 0

    def __init__(self, radius):
        self.radius = radius
        self.set_perimeter()
        self.set_area()

    def set_area(self):
        self.area = self.radius * self.radius * math.pi

    def set_perimeter(self):
        self.perimeter = self.radius * 2 * math.pi


# 矩形类
class Rectangle(Shape):
    length = 0
    width = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.set_perimeter()
        self.set_area()

    def set_area(self):
        self.area = self.width * self.length

    def set_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)


# 三角形类
class Triangle(Shape):
    a = 0
    b = 0
    c = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.set_perimeter()
        self.set_area()

    def set_area(self):
        p = (self.a + self.b + self.c) / 2
        self.area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def set_perimeter(self):
        self.perimeter = self.a + self.b + self.c


# 主方法
def main():
    c = Circle(2)
    r = Rectangle(2, 3)
    t = Triangle(1, 2, 2)
    print(c.perimeter, c.area)
    print(r.perimeter, r.area)
    print(t.perimeter, t.area)


# 调用主方法
if __name__ == '__main__':
    main()
