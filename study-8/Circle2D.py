import math


class Circle2D:
    def __init__(self, x=0.0, y=0.0, r=0):
        self.__x = x
        self.__y = y
        self.__radius = r

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_r(self, r):
        self.__radius = r

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_r(self):
        return self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def contain_point(self, x, y):
        return (self.__x - x) ** 2 + (self.__y - y) ** 2 <= self.__radius ** 2

    def contain(self, c):
        return math.sqrt((self.__x - c.get_x()) ** 2 + (self.__y - c.get_y()) ** 2) < (self.__radius - c.get_r())

    def overlaps(self, c):
        return (self.__radius - c.get_r()) ** 2 \
               <= (self.__x - c.get_x()) ** 2 + (self.__y - c.get_y()) ** 2 \
               <= (self.__radius + c.get_r()) ** 2

    def __contains__(self, item):
        return math.sqrt((self.__x - item.get_x()) ** 2 + (self.__y - item.get_y()) ** 2) \
               < (self.__radius - item.get_r())

    def __cmp__(self, other):
        if self.__radius == other.get_r():
            return 0
        elif self.__radius > other.get_r():
            return 1
        elif self.__radius < other.get_r():
            return -1

    def __lt__(self, other):
        return self.__radius < other.get_r()

    def __le__(self, other):
        return self.__radius <= other.get_r()

    def __eq__(self, other):
        return self.__radius == other.get_r()

    def __ne__(self, other):
        return self.__radius != other.get_r()

    def __gt__(self, other):
        return self.__radius > other.get_r()

    def __ge__(self, other):
        return self.__radius >= other.get_r()
