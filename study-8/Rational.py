class Rational:
    def __init__(self, numerator, denominator):
        divisor = gcd(numerator, denominator)
        self.__numerator = (1 if denominator > 0 else -1) * int(numerator / divisor)
        self.__denominator = int(abs(denominator) / divisor)

    def __add__(self, second_rational):
        n = self.__numerator * second_rational[1] + self.__denominator * second_rational[0]
        d = self.__denominator * second_rational[1]
        return Rational(n, d)

    def __sub__(self, second_rational):
        n = self.__numerator * second_rational[1] - self.__denominator * second_rational[0]
        d = self.__denominator * second_rational[1]
        return Rational(n, d)

    def __mul__(self, second_rational):
        n = self.__numerator * second_rational[0]
        d = self.__denominator * second_rational[1]
        return Rational(n, d)

    def __truediv__(self, second_rational):
        n = self.__numerator * second_rational[1]
        d = self.__denominator * second_rational[0]
        return Rational(n, d)

    def __float__(self):
        return self.__numerator / self.__denominator

    def __int__(self):
        return int(self.__float__())

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)

    def __lt__(self, second_rational):
        return self.__cmp__(second_rational) < 0

    def __le__(self, second_rational):
        return self.__cmp__(second_rational) <= 0

    def __gt__(self, second_rational):
        return self.__cmp__(second_rational) > 0

    def __ge__(self, second_rational):
        return self.__cmp__(second_rational) >= 0

    def __cmp__(self, second_rational):
        temp = self.__sub__(second_rational)
        if temp[0] > 0:
            return 1
        elif temp[0] < 0:
            return -1
        else:
            return 0

    def __getitem__(self, index):
        if index == 0:
            return self.__numerator
        else:
            return self.__denominator


def gcd(n, d):
    n1 = abs(n)
    n2 = abs(d)
    gcd_ = 1

    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd_ = k
        k += 1

    return gcd_
