def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def check_number(ma: int, mb: int) -> bool:
    return gcd(ma, mb) == 1


def get_product_m(m1: int, m2: int, m3: int) -> int:
    return m1 * m2 * m3


def get_division_m(mi: int, m: int) -> int:
    return m // mi


def get_inverse_m(a: int, m: int) -> int:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def main() -> None:
    file = open("D:\\学习\\3·1信息安全基础与密码学综合实验\\4 (2).txt")
    lines = file.readlines()

    a1: int = int(lines[0].strip())
    a2: int = int(lines[1].strip())
    a3: int = int(lines[2].strip())
    m1: int = int(lines[3].strip())
    m2: int = int(lines[4].strip())
    m3: int = int(lines[5].strip())
    a: [int, int, int] = [a1, a2, a3]

    if check_number(m1, m2) and check_number(m3, m2) and check_number(m1, m3):
        m = get_product_m(m1, m2, m3)
        mm1, mm2, mm3 = get_division_m(m1, m), get_division_m(m2, m), get_division_m(m3, m)
        mi1, mi2, mi3 = get_inverse_m(mm1, m1), get_inverse_m(mm2, m3), get_inverse_m(mm3, m3)
        x = 1
        for i in range(3):
            x += mm1 * mi1 * a[i]
            x %= m
        print("Answer: ", x)
    else:
        print("Unable to calculate!")

    file.close()


if __name__ == '__main__':
    main()
