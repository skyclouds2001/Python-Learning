# Person类
class Person:
    def __init__(self, name: str, phone: str, email: str, work: str):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__work = work

    def __str__(self):
        return "name: " + self.__name + "  phone: " + self.__phone +\
               "  e-mail: " + self.__email + "  work: " + self.__work


# 主方法
def main():
    d = {}

    # 循环处理指令
    while True:
        print("Please press 0 to exit,")
        print("press 1 to add,")
        print("press 2 to delete.")
        print("press 3 to search.")
        print("press 4 to print ALL.")
        choice = eval(input())

        # 根据指令执行对应操作：
        # 退出程序
        if choice == 0:
            break

        # 添加信息
        elif choice == 1:
            name = input("Please input the name: ")
            phone = input("Please input the phone: ")
            email = input("Please input the email: ")
            work = input("Please input the working place: ")
            p = Person(name, phone, email, work)
            d[name] = p

        # 删除信息
        elif choice == 2:
            name = input("Please input the name of the person to delete: ")
            del d[name]

        # 搜索信息
        elif choice == 3:
            name = input("Please input the name: ")
            print(d.get(name))

        # 打印全部信息
        elif choice == 4:
            for p in d.values():
                print(p)

        # 其他指令
        else:
            print("Unfair order!")
            print("Please check your input.")

        print()


# 调用主方法
if __name__ == '__main__':
    main()
