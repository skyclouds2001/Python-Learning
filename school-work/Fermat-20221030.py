import math
import random


def quick_mod(a, k, m):
    v = 1
    while k > 0:
        if (k & 1) == 1:
            v *= a
            v %= m
        a *= a
        a %= m
        k >>= 1
    return v


def main():
    m = int(input())
    k = int(input())
    i = 1

    flag = True

    while i <= k:
        a = random.randint(2, m - 2)

        g = math.gcd(a, m)
        if g == 1:
            f = quick_mod(a, m - 1, m)

            if f != 1:
                flag = False
                break
        else:
            flag = False
            break

        i += 1

    if flag:
        print('该数以', 1 - 1 / (2 ** k), '概率下是素数', end='')
    else:
        print('该数是合数', end='')


if __name__ == '__main__':
    main()
