import random
from typing import IO


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def judge_legal_d(m: list[int], num: int) -> bool:
    flag = True
    for i in range(0, num):
        for j in range(0, num):
            if i != j and gcd(m[i], m[j]) != 1:
                flag = False
                break
    return flag


def create_d_array(n: int) -> list[int]:
    d = [1 for _ in range(0, n)]
    d[0] = random.randint(pow(10, 167), pow(10, 168))
    i = 1
    while i < n:
        d[i] = random.randint(pow(10, 167), pow(10, 168))
        if judge_legal_d(d, i + 1):
            i = i + 1
    d.sort()
    return d


def get_n_and_m(d: list[int], t: int) -> (int, int):
    m, n = 1, 1
    for i in range(0, t):
        n = n * d[i]
    for i in range(len(d) - t + 1, len(d)):
        m = m * d[i]
    return n, m


def get_kk(d: list[int], k: int) -> list[int]:
    kk = [1 for _ in range(0, len(d))]
    for i in range(0, len(d)):
        kk[i] = k % d[i]
    kk = kk[0:len(d)]
    return kk


def get_mod_reverse(a: int, m: int) -> int | None:
    if gcd(a, m) != 1:
        raise Exception("Invalid Error")
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def get_product_m(li: list[int]) -> int:
    res: int = 1
    for i in li:
        res *= i
    return res


def chinese_surplus(k: list[int], d: list[int], t: int) -> int:
    m = d[0:t]
    a = k[0:t]
    M = get_product_m(m)
    Mj = div_result(m)
    Mj_i = [0 for _ in range(0, len(m))]
    for i in range(0, len(m)):
        Mj_i[i] = get_mod_reverse(Mj[i], m[i])
    x = 0
    for i in range(0, len(m)):
        x += Mj[i] * Mj_i[i] * a[i]
    res = x % M
    return res


def div_result(m: list[int]) -> list[int]:
    Mj = [1 for _ in range(0, len(m))]
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if i == j:
                Mj[i] = Mj[i] * 1
            else:
                Mj[i] = Mj[i] * m[j]
    return Mj


def main() -> None:
    n: int = random.randint(1, 6)
    t: int = random.randint(1, n)
    print("n: ", n)
    print("t: ", t)

    file: IO = open("D:\\学习\\3·1信息安全基础与密码学综合实验\\secret1.txt")
    key: int = int(file.readline())
    print("key: ", key)

    d: list[int] = create_d_array(n)
    print("d: ", d)

    N, M = get_n_and_m(d, t)
    print("n: ", N)
    print("m: ", M)

    kk: list[int] = get_kk(d, key)
    print("keys: ", kk)

    res: int = chinese_surplus(kk, d, t)
    print("recovered key with t keys: ", res)

    res: int = chinese_surplus(kk, d, t - 1)
    print("recovered key with t - 1 keys: ", res)


if __name__ == '__main__':
    main()
