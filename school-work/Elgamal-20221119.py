import gmpy2
import Crypto.Util.number as crypto


# 生成密钥
def generate_key(bits: int) -> tuple[tuple[int, int, int], int]:
    p = crypto.getStrongPrime(bits)
    q = (p - 1) // 2
    g = crypto.getRandomRange(2, p - 1)
    while pow(g, q, p) == 1 and pow(g, 2, p) == 1:
        g = crypto.getRandomRange(2, p - 1)
    a = crypto.getRandomRange(1, q - 1)
    ga = pow(g, a, p)
    return (p, g, ga), a


# 加密
def encrypt(m: int, pub: tuple[int, int, int]) -> tuple[int, int]:
    p, g, ga = pub
    k = crypto.getRandomRange(1, p - 2)
    c1 = pow(g, k, p)
    c2 = (m * pow(ga, k, p)) % p
    return c1, c2


# 解密
def decrypt(c: tuple[int, int], pub: tuple[int, int, int], pri: int) -> int:
    p, g, ga = pub
    c1, c2 = c
    a = pri
    s = pow(c1, a, p)
    m = (c2 * gmpy2.invert(s, p)) % p
    return m


def main() -> None:
    public_key, private_key = generate_key(1024)
    print("Public Key:")
    print(f"  p = {public_key[0]}")
    print(f"  g = {public_key[1]}")
    print(f"  g^a = {public_key[2]}")
    print("Private Key:")
    print(f"  x = {private_key}")
    print()

    file = open("D:\\学习\\3·1信息安全基础与密码学综合实验\\secret0(2).txt")
    message = int(file.readline())
    file.flush()
    file.close()
    print(f"Message: {message}")

    secret = encrypt(message, public_key)
    print("Encrypt:")
    print(f"  c1 = {secret[0]}")
    print(f"  c2 = {secret[1]}")

    recover_message = decrypt(secret, public_key, private_key)
    print("Decrypt:")
    print(f"  mes = {recover_message}")


if __name__ == '__main__':
    main()
