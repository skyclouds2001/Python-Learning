import hashlib
import math
import random
from typing import Any, Type

"""
  SM2 默认参数
  素数p
  8542D69E 4C044F18 E8B92435 BF6FF7DE 45728391 5C45517D 722EDB8B 08F1DFC3
  系数a
  787968B4 FA32C3FD 2417842E 73BBFEFF 2F3C848B 6831D7E0 EC65228B 3937E498
  系数b
  63E4C6D3 B23B0C84 9CF84241 484BFE48 F61D59A5 B16BA06E 6E12D1DA 27C5249A
  基点G=(xG,yG)，其阶记为n
* 坐标xG
  421DEBD6 1B62EAB6 746434EB C3CC315E 32220B3B ADD50BDC 4C4E6C14 7FEDD43D
* 坐标yG
  0680512B CBB42C07 D47349D2 153B70C4 E5D7FDFC BFA36EA1 A85841B9 E46E09A2
* 阶n
  8542D69E 4C044F18 E8B92435 BF6FF7DD 29772063 0485628D 5AE74EE7 C32E79B7
* 余因子h
  1
"""

ec_p = 0x8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3
ec_a = 0x787968B4FA32C3FD2417842E73BBFEFF2F3C848B6831D7E0EC65228B3937E498
ec_b = 0x63E4C6D3B23B0C849CF84241484BFE48F61D59A5B16BA06E6E12D1DA27C5249A
ec_G = (0x421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D, 0x0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2)
ec_xG = ec_G[0]
ec_yG = ec_G[1]
ec_n = 0x8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7
ec_h = 1
Hv = 256


"""
  常量
"""

EC_INFINITY_POINT = None


"""
  工具方法
"""

def miller_rabin(p: int) -> bool:
    """
    整除法判定数p是否为素数
    :param p: 需判定的数
    :return: 判定结果
    """
    if p == 1: return False
    if p == 2: return True
    if p % 2 == 0: return False
    m, k = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = random.randint(2, p - 1)
    x = pow(a, m, p)
    if x == 1 or x == p - 1:
        return True
    while k > 1:
        x = pow(x, 2, p)
        if x == 1:
            return False
        if x == p - 1:
            return True
        k = k - 1
    return False


def is_prime(p: int, r: int = 40) -> bool:
    """
    Miller-Rabin测试素数算法
    :param p: 需测试的素数
    :param r: 测试精度（默认为40）
    :return: 判定结果
    """
    for i in range(r):
        if not miller_rabin(p):
            return False
    return True


def randint_gen(start: int, end: int) -> int:
    """
    生成给定范围内的随机数
    :param start: 起始范围
    :param end: 终止范围
    :return: 生成的随机数
    """
    return random.randint(start, end)


def int_to_bytes(x: int, k: int) -> bytes:
    """
    转换整数为字节串
    :param x: 非负整数
    :param k: 字节串的目标长度 (其中k满足2^(8k) > x)
    :return: 长度为k的字节串M
    """
    M = b""
    for _shift in range(k):
        M = bytes([(x >> (8 * _shift)) & 0xFF]) + M
    return M


def bytes_to_int(m: bytes) -> int:
    """
    转换字节串为整数
    :param m: 长度为k的字节串m
    :return: 整数x
    """
    x = 0
    k = len(m)
    m = list(reversed(m))
    for shift in range(k):
        x += m[shift] << (shift * 8)
    return x


def bits_to_bytes(s: str) -> bytes:
    """
    转换比特串为字节串
    :param s: 长度为m的比特串s
    :return: 长度为k的字节串M（k = ⌈m/8⌉）
    """
    m = len(s)
    k = math.ceil(m / 8)
    s = s.rjust(k * 8, "0")
    M = b""
    for shift in range(k):
        M = bytes([int(s[-(shift * 8 + 8):][:8], 2)]) + M
    return M


def bytes_to_bits(m: bytes) -> str:
    """
    转换比特串为字节串
    :param m: 长度为k的字节串M
    :return: 长度为m的比特串s（m = 8k）
    """
    s = ""
    k = len(m)
    m = list(reversed(m))
    for idx in range(k):
        s = (bin(m[idx])[2:]).rjust(8, "0") + s
    return s


def bits_xor(x: str, y: str) -> str:
    """
    两比特串异或方法
    :param x: 比特串x
    :param y: 比特串y
    :return: 异或后的新比特串
    """
    m_len = max(len(x), len(y))
    x.ljust(m_len, "0")
    y.ljust(m_len, "0")
    return "".join([str(int(x[i]) ^ int(y[i])) for i in range(m_len)])


def negate_mod(x: int) -> int:
    """
    取反取模
    :param x: 原数
    :return: 新数
    """
    return (-x) % ec_p


def add_mod(x: int, y: int) -> int:
    """
    相加取模
    :param x: 原数x
    :param y: 原数y
    :return: 新数
    """
    return (x + y) % ec_p


def sub_mod(x: int, y: int) -> int:
    """
    相减取模
    :param x: 原数x
    :param y: 原数y
    :return: 新数
    """
    return (x - y) % ec_p


def mul_mod(x: int, y: int) -> int:
    """
    相乘取模
    :param x: 原数x
    :param y: 原数y
    :return: 新数
    """
    return (x * y) % ec_p


def inv_mod(x: int) -> int:
    """
    指数模逆取模
    :param x: 原数x
    :return: 新数
    """
    return pow(x, ec_p - 2, ec_p)


def bits_hash_256(data: str) -> str:
    """
    生成比特串的哈希值
    :param data: 需计算的比特串
    :return: 比特串的哈希值
    """
    sm3 = hashlib.new("sm3")
    sm3.update(bits_to_bytes(data))
    return bytes_to_bits(sm3.digest())


def domain_elem_to_bytes(a: int, l: int = 0) -> bytes:
    """
    将域中元素转换为给定长度的字节串
    :param a: 域中元素
    :param l: 给定的长度
    :return: 字节串
    """
    q = ec_p
    if not is_prime(q) or not isinstance(a, int) or q <= 2 or a < 0 or a > q - 1:
        raise ValueError
    l = math.ceil(math.log2(q) / 8) if not l else l
    return int_to_bytes(a, l)


def bytes_to_domain_elem(s: bytes) -> int:
    """
    字节串转换为域中元素
    :param s: 字节串
    :return: 域中元素
    """
    q = ec_p
    if not is_prime(q) or q <= 2:
        raise ValueError
    a = bytes_to_int(s)
    if a < 0 or a > q - 1:
        raise ValueError
    return a


def domain_elem_to_int(a: int) -> int:
    """
    将域中元素转换为整数
    :param a: 域中元素
    :return: 整数
    """
    q = ec_p
    if not is_prime(q) or not isinstance(a, int) or q <= 2:
        raise ValueError
    return a


"""
类型 - 点
"""
Point: Type[tuple] = tuple[int, int]


def is_point(p: Any) -> bool:
    """
    判定值是否为点
    :param p: 任意值
    :return: 判定结果
    """
    return isinstance(p, tuple) and len(p) == 2


def point_to_bytes(p: Point) -> bytes:
    """
    点转换为字节串
    :param p: 椭圆曲线上的非零点
    :return: 字节串S（长度为2l+1）
    """
    q = ec_p

    if not is_point(p):
        raise ValueError
    l = math.ceil(math.log2(q) / 8)

    xP = p[0]
    yP = p[1]
    X1 = domain_elem_to_bytes(xP, l)
    Y1 = domain_elem_to_bytes(yP, l)
    PC = b"\x04"
    return PC + X1 + Y1


def bytes_to_point(s: bytes) -> Point:
    """
    字节串转换为点
    :param s: 字节串S
    :return: 椭圆曲线上的非零点P
    """
    q = ec_p
    a, b = ec_a, ec_b

    if len(s) <= 1:
        raise ValueError
    l = math.ceil(math.log2(q) / 8)

    PC = s[0]
    X1 = s[1 : 1 + l]
    Y1 = s[1 + l : 1 + 2 * l]
    xp = bytes_to_int(X1)

    # 校验PC值
    if PC != 0x4:
        raise ValueError
    # 返回前校验点是否满足椭圆曲线方程
    yp = bytes_to_int(Y1)
    if pow(yp, 2) % q != (pow(xp, 3) + a * xp + b) % q:
        raise ValueError
    return xp, yp


def calc_lambda_in_add(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    非互逆不同点相加
    :param x1: 点1横坐标
    :param y1: 点1纵坐标
    :param x2: 点2横坐标
    :param y2: 点1纵坐标
    :return: 计算结果
    """
    a = sub_mod(y2, y1)
    b = sub_mod(x2, x1)
    b_inv = inv_mod(b)
    return mul_mod(a, b_inv)


def calc_lambda_in_mul(x1: int, y1: int) -> int:
    """
    倍点运算
    :param x1: 点横坐标
    :param y1: 点纵坐标
    :return: 计算结果
    """
    a = mul_mod(x1, x1)
    a = mul_mod(3, a) + ec_a
    b = mul_mod(2, y1)
    b_inv = inv_mod(b)
    return mul_mod(a, b_inv)


def point_add(p1, p2):
    """
    域内点相加
    :param p1: 点A
    :param p2: 点B
    :return: 计算结果
    """
    # 处理无穷远点
    if p1 == EC_INFINITY_POINT:
        return p2
    elif p2 == EC_INFINITY_POINT:
        return p1

    if not is_point(p1) and is_point(p2):
        raise ValueError

    x1, y1 = p1
    x2, y2 = p2

    # 检查P1, P2是否互逆
    if x1 == x2:
        # 互逆
        if negate_mod(y1) == y2:
            return EC_INFINITY_POINT
        # 倍点运算
        else:
            _lambda = calc_lambda_in_mul(x1, y1)
    else:
        # 非互逆不同点相加
        _lambda = calc_lambda_in_add(x1, y1, x2, y2)

    x3 = mul_mod(_lambda, _lambda)
    x3 = sub_mod(x3, x1)
    x3 = sub_mod(x3, x2)
    y3 = sub_mod(x1, x3)
    y3 = mul_mod(_lambda, y3)
    y3 = sub_mod(y3, y1)
    return x3, y3


def k_times_point(p: Point, k: int) -> tuple[int, int]:
    """
    计算点的k倍点
    :param p: 原点
    :param k: k系数
    :return: 现点
    """
    if p == EC_INFINITY_POINT:
        return p
    if not is_point(p):
        raise ValueError

    # 二进制展开法
    k = list(reversed(bin(k)[2:]))
    Q = EC_INFINITY_POINT
    for j in range(len(k) - 1, -1, -1):
        Q = point_add(Q, Q)
        if k[j] == "1":
            Q = point_add(Q, p)
    return Q


"""
  核心方法
"""

def gen_keys() -> tuple[Point, int]:
    """
    获取密钥对
    :return: (公钥p, 私钥d)
    """
    # 计算d倍点 - 获取随机数d ∈ [1, n - 1]
    d = randint_gen(1, ec_n - 2)
    p = k_times_point(ec_G, d)
    return p, d


def kdf(z: str, k_len: int) -> str:
    """
    密钥派生函数 KDF
    :param z: 比特串
    :param k_len: 要获得的密钥数据的比特长度（小于(2^32-1)）
    :return: 密钥数据比特串
    """
    ct = 0x00000001
    v = Hv
    Ha = {}

    for i in range(1, math.ceil(k_len / v) + 1):
        # 计算Hai = Hv(Z||ct)
        Ha[i] = bits_hash_256(z + bin(ct)[2:].rjust(32, "0"))
        # ++ct
        ct += 1

    # 判断是否需要取前k_len - (v * math.ceil(k_len / v))比特
    if k_len % v != 0:
        Ha[math.ceil(k_len / v)] = Ha[math.ceil(k_len / v)][:k_len - v * math.ceil(k_len / v)]
    K = ""

    # 拼接并返回
    for i in range(1, math.ceil(k_len / v) + 1):
        K += Ha[i]
    return K


def encrypt(message: bytes, public_key: Point) -> bytes:
    """
    加密主要方法
    :param message: 待加密信息
    :param public_key: 公钥
    :return: 加密后信息
    """
    # 预处理
    M = bytes_to_bits(message)
    k_len = len(M)
    pb = public_key # 公钥
    n = ec_n
    G = ec_G
    h = ec_h

    while True:
        # 取随机数k ∈ [1, n - 1]
        k = randint_gen(1, n)

        # 计算G的K倍点为C1，并转化为比特串
        C1 = bytes_to_bits(point_to_bytes(k_times_point(G, k)))

        # S = [h]PB，若S是无穷远点，则报错
        S = k_times_point(pb, h)
        if S == EC_INFINITY_POINT:
            raise ValueError

        # 计算椭圆曲线点[k]PB = (x2, y2)，并将x2与y2存为比特串
        x2, y2 = k_times_point(pb, k)
        x2 = bytes_to_bits(domain_elem_to_bytes(x2))
        y2 = bytes_to_bits(domain_elem_to_bytes(y2))

        # 计算t = KDF(x2 || y2, k_len)，若t为全0比特串，则返回第一步
        t = kdf(x2 + y2, k_len)
        if t.find("1") != -1:
            break

    # 计算 C2 = M ⊕ t
    C2 = bits_xor(M, t)

    # 计算 C3 = Hash(x2 || M || y2)
    C3 = bits_hash_256(x2 + M + y2)

    # 密文 C = C1 || C2 || C3
    C = C1 + C2 + C3

    # 打印输出结果
    print(f"    M: {bits_to_bytes(M).hex()}")
    print(f"    k: {hex(k)}")
    print(f"    C1: {bits_to_bytes(C1).hex()}")
    print(f"    S: ({bits_to_bytes(x2).hex()}, {bits_to_bytes(y2).hex()})")
    print(f"    t: {bits_to_bytes(t).hex()}")
    print(f"    C2: {bits_to_bytes(C2).hex()}")
    print(f"    C3: {bits_to_bytes(C3).hex()}")

    return bits_to_bytes(C)


def decrypt(secret: bytes, private_key: int) -> bytes:
    """
    解密主要方法
    :param secret: 待解密信息
    :param private_key: 私钥
    :return: 解密后信息
    """
    # 预处理
    C = bytes_to_bits(secret)
    dB = private_key # 私钥
    p = ec_p
    h = ec_h

    # 计算C1, C2, C3的长度
    C1_len = 8 * (2 * math.ceil(math.log2(p) / 8) + 1)
    C3_len = Hv
    C2_len = len(C) - C1_len - C3_len
    k_len = C2_len

    # 从C中取出比特串C1，并转换为椭圆曲线上的点，同时检查点的合法性
    C1 = bytes_to_point(bits_to_bytes(C[ : C1_len]))

    # 计算椭圆曲线点S = [h]C1，并校验S不为无穷远点，否则报错并退出
    S = k_times_point(C1, h)
    if S == EC_INFINITY_POINT:
        raise ValueError

    # 计算[dB]C1 = (x2, y2)
    x2, y2 = k_times_point(C1, dB)
    x2 = bytes_to_bits(domain_elem_to_bytes(x2))
    y2 = bytes_to_bits(domain_elem_to_bytes(y2))

    # 计算t = KDF(x2 || y2, k_len)，若t为全0比特串
    t = kdf(x2 + y2, k_len)
    if t.find("1") == -1:
        raise ValueError

    # 从C中取出比特串C2，计算M′ = C2 ⊕ t
    C2 = C[C1_len : C1_len + k_len]
    M = bits_xor(C2, t)

    # 计算u = Hash(x2 || M′ || y2)，从C中取出比特串C3，若u ≠ C3，则报错并退出
    u = bits_hash_256(x2 + M + y2)
    C3 = C[C1_len + k_len : ]
    if u != C3:
        raise ValueError

    print(f"    S: ({bits_to_bytes(x2).hex()}, {bits_to_bytes(y2).hex()})")
    print(f"    t: {bits_to_bytes(t).hex()}")
    print(f"    u: {bits_to_bytes(u).hex()}")

    return bits_to_bytes(M)


"""
  主方法
"""

def main() -> None:
    """
    主方法
    """
    print(" 椭圆曲线方程 y^2 = x^3 + ax + b")
    print(f"    参数 p: {hex(ec_p)}")
    print(f"    参数 a: {hex(ec_a)}")
    print(f"    参数 b: {hex(ec_b)}")
    print(f"    基点 G = (xG, yG)")
    print(f"    坐标 xG: {hex(ec_xG)}")
    print(f"    坐标 yG: {hex(ec_yG)}")
    print(f"    阶 n: {hex(ec_n)}")
    print(f"    余因子 h: {hex(ec_h)}")
    print()

    # 生成密钥对
    print("生成密钥对：")
    public_key, private_key = gen_keys()
    print(f"    公钥 P: ({hex(public_key[0])}, {hex(public_key[1])})")
    print(f"    私钥 d: {hex(private_key)}")
    print()

    # 读取待加密信息
    with open("msg.txt", "rb") as f:
        raw_message: bytes = f.read()

    # 加密
    print("加密：")
    secret: bytes = encrypt(raw_message, public_key)
    print(f"    密文: {secret.hex()}")
    print()

    # 解密
    print("解密：")
    decrypt_message: bytes = decrypt(secret, private_key)
    print(f"    明文: {decrypt_message.hex()}")
    print(f"    明文字节串: {decrypt_message.decode('utf-8').strip()}")
    print()

    # 校验
    print("校验：")
    if raw_message == decrypt_message:
        print("    一致！")
    else:
        print("    不一致！")
    print()

if __name__ == "__main__":
    main()
