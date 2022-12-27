from Crypto.Util.number import getStrongPrime, getRandomRange
import gmpy2
import base64
import uuid

class Crypto:
    def __init__(self):
        self.shift_key = [1, 5, 14, 5, 7, 16, 24, 3, 17]
        self.move_key = 3
        self.elgamal_key = Crypto.elgamal_generate_key(1024)

    @staticmethod
    def get_random_str(length: int = 5):
        return str(uuid.uuid4()).replace("-", "")[0: length]

    @staticmethod
    def shift_encrypt(message: str, key: list[int]) -> str:
        m = message
        k = key
        l = len(k)
        s = ""

        for i, c in enumerate(m):
            s += chr(ord(c) + k[i % l] - i % l // 2)

        return s

    @staticmethod
    def shift_decrypt(secret: str, key: list[int]) -> str:
        s = secret
        k = key
        l = len(k)
        m = ""

        for i, c in enumerate(s):
            m += chr(ord(c) - k[i % l] + i % l // 2)

        return m

    @staticmethod
    def move_encrypt(message: str, key: int) -> str:
        m = message
        k = key
        l = len(m)
        s = ""

        for i in range(l // k):
            s = m[i * k: (i + 1) * k] + s

        s = s + m[l // k * k:]

        return s

    @staticmethod
    def move_decrypt(secret: str, key: int) -> str:
        s = secret
        k = key
        l = len(s)
        m = ""

        for i in range(l // k):
            m = s[i * k: (i + 1) * k] + m

        m = m + s[l // k * k:]

        return m

    @staticmethod
    def elgamal_generate_key(bits: int) -> tuple[tuple[int, int, int], int]:
        p = getStrongPrime(bits)
        q = (p - 1) // 2
        g = getRandomRange(2, p - 1)
        while pow(g, q, p) == 1 and pow(g, 2, p) == 1:
            g = getRandomRange(2, p - 1)
        a = getRandomRange(1, q - 1)
        ga = pow(g, a, p)
        return (p, g, ga), a

    @staticmethod
    def elgamal_encrypt(m: int, pub: tuple[int, int, int]) -> tuple[int, int]:
        p, g, ga = pub
        k = getRandomRange(1, p - 2)
        c1 = pow(g, k, p)
        c2 = (m * pow(ga, k, p)) % p
        return c1, c2

    @staticmethod
    def elgamal_decrypt(c: tuple[int, int], pub: tuple[int, int, int], pri: int) -> int:
        p, g, ga = pub
        c1, c2 = c
        a = pri
        s = pow(c1, a, p)
        m = (c2 * gmpy2.invert(s, p)) % p
        return m

    @classmethod
    def encrypt(cls, message: str) -> str:
        m = message
        crypt = Crypto()

        m = base64.b64encode(m.encode()).decode()
        m = cls.get_random_str() + m + cls.get_random_str()
        m = crypt.shift_encrypt(m, crypt.shift_key)
        m = crypt.move_encrypt(m, crypt.move_key)

        return m

    @classmethod
    def decrypt(cls, secret: str) -> str:
        s = secret
        crypt = Crypto()

        s = crypt.move_decrypt(s, crypt.move_key)
        s = crypt.shift_decrypt(s, crypt.shift_key)
        s = s[5: len(s) - 5]
        s = base64.b64decode(s.encode()).decode()

        return s


def main() -> None:
    raw_message = 'We are the world, we are the children. We are the ones who make a brighter day.'

    print("加密前信息：", raw_message)

    secret = Crypto.encrypt(raw_message)

    print("加密后秘密：", secret)

    recover_message = Crypto.decrypt(secret)

    print("解密后信息：", recover_message)


if __name__ == '__main__':
    main()
