import random


def main():
    # 打开文件
    file = open("Salary.txt", "w+")
    position = ("assistant", "associate", "full")

    for i in range(1, 1001):
        # 生成姓氏
        file.write("FirstName" + str(i) + " ")
        file.write("LastName" + str(i) + " ")

        # 生成职位
        t = random.randint(0, 2)
        file.write(position[t] + " ")

        # 根据职位生成对应的工资
        if t == 0:
            file.write("{:.2f}".format(random.random() * 30000 + 50000))
        elif t == 1:
            file.write("{:.2f}".format(random.random() * 50000 + 60000))
        elif t == 2:
            file.write("{:.2f}".format(random.random() * 55000 + 75000))

        # 换行
        file.write("\n")

    file.close()


if __name__ == '__main__':
    main()
