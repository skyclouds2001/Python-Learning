def main():
    try:
        i = 20
        j = 5
        k = i // j
        print(k)
    except ZeroDivisionError as e:
        print(e)
    else:
        print(i + j)


if __name__ == '__main__':
    main()


class My:
    def __init__(self):
        self.__a = 1

    @classmethod
    def f(cls):
        print(cls().__a)

    @staticmethod
    def g():
        print("static")


# m = My()
# print(m)
