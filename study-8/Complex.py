import math


class Complex:
    def __init__(self, a, b):
        self.__real_part = a
        self.__imaginary_part = b

    def get_real_part(self):
        return self.__real_part

    def get_imaginary_part(self):
        return self.__imaginary_part

    def __add__(self, other):
        rp = self.__real_part + other[0]
        ip = self.__imaginary_part + other[1]
        return Complex(rp, ip)

    def __sub__(self, other):
        rp = self.__real_part - other[0]
        ip = self.__imaginary_part - other[1]
        return Complex(rp, ip)

    def __mul__(self, other):
        rp = self.__real_part * other[0] - self.__imaginary_part * other[1]
        ip = self.__imaginary_part * other[0] + self.__real_part * other[1]
        return Complex(rp, ip)

    def __truediv__(self, other):
        rp = (self.__real_part * other[0] + self.__imaginary_part * other[1]) / (other[0] ** 2 + other[1] ** 2)
        ip = (self.__imaginary_part * other[0] + self.__real_part * other[1]) / (other[0] ** 2 + other[1] ** 2)
        return Complex(rp, ip)

    def __abs__(self):
        return math.sqrt(self.__real_part ** 2 + self.__imaginary_part ** 2)

    def __str__(self):
        if self.__real_part == 0 and self.__imaginary_part == 0:
            return "0"
        elif self.__real_part == 0:
            return str(self.__imaginary_part) + "i"
        elif self.__imaginary_part == 0:
            return str(self.__real_part)
        elif self.__imaginary_part == 1:
            return str(self.__real_part) + " + i"
        elif self.__imaginary_part == -1:
            return str(self.__real_part) + " - i"
        elif self.__imaginary_part > 0:
            return str(self.__real_part) + " + " + str(self.__imaginary_part) + "i"
        elif self.__imaginary_part < 0:
            return str(self.__real_part) + " - " + str(self.__imaginary_part) + "i"

    def __getitem__(self, index):
        if index == 0:
            return self.__real_part
        else:
            return self.__imaginary_part
