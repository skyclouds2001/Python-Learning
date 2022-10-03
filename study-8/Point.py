import math


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return "(" + self.__x + "," + self.__y + ")"

    def distance(self, p):
        return math.sqrt((self.__x - p.__x) ** 2 + (self.__y - p.__y) ** 2)

    def is_near_by(self, p):
        return self.distance(p) < 5
