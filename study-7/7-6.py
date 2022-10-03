import math


class Circle:
    def __init__(self, radius=1):
        self.__radius = radius

    def get_perimeter(self):
        return math.pi * 2 * self.__radius

    def get_area(self):
        return math.pi * self.__radius * self.__radius

    def get_radius(self):               # 获取器-访问器
        return self.__radius

    def set_radius(self, radius):       # 设置器-修改器
        self.__radius = radius
