from Rational import Rational


s = Rational(1, 2) + Rational(1, 3)
for i in range(3, 10):
    s = s + Rational(i, i + 1)
print(float(s))
