# 计数方法
def count(s: str):
    c1 = c2 = c3 = c4 = 0

    # 枚举各字符分别计数即可
    for i in range(len(s)):
        if s[i].isupper():
            c1 += 1
        elif s[i].islower():
            c2 += 1
        elif s[i].isdigit():
            c3 += 1
        else:
            c4 += 1

    # 返回元组
    return c1, c2, c3, c4


# 主方法/测试方法
def main():
    c = count("Get my name @ me in 12345.")
    print("Uppercase:", c[0])
    print("Lowercase:", c[1])
    print("Digit:", c[2])
    print("Other:", c[3])


# 调用主方法
if __name__ == '__main__':
    main()
