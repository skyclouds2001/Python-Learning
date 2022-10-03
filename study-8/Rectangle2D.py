class Rectangle2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_x(self, width):
        self.__width = width

    def set_x(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __cmp__(self, other):
        if self.get_area() == other.get_area():
            return 0
        if self.get_area() < other.get_area():
            return -1
        if self.get_area() > other.get_area():
            return 1

    def contains_point(self, x, y):
        return self.__x - self.__width / 2 < x < self.__x + self.__width and \
               self.__y - self.__height / 2 < y < self.__y + self.__height

    def contain(self, other):
        return self.__x - self.__width / 2 < other.__x - other.__width / 2 and\
               self.__y - self.__height / 2 < other.__y - other.__height / 2 and \
               self.__x + self.__width / 2 > other.__x + other.__width / 2 and \
               self.__y + self.__height / 2 > other.__y + other.__height / 2

    def overlaps(self, other):
        return self.__x - self.__width / 2 < other.__x - other.__width / 2 < self.__x + self.__width / 2 or \
               self.__y - self.__height / 2 < other.__y - other.__height / 2 < self.__y - self.__height / 2 or \
               self.__x - self.__width / 2 < other.__x + other.__width / 2 < self.__x + self.__width / 2 or \
               self.__y - self.__height / 2 < other.__y + other.__height / 2 < self.__y - self.__height / 2

    def __contains__(self, other):
        return self.__x - self.__width / 2 > other.__x - other.__width / 2 and \
               self.__y - self.__height / 2 > other.__y - other.__height / 2 and \
               self.__x + self.__width / 2 < other.__x + other.__width / 2 and \
               self.__y + self.__height / 2 < other.__y + other.__height / 2
