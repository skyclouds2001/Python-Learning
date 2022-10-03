def main():
    # 打开文件
    file = open("Salary.txt", "r")
    pay_sum1, pay_sum2, pay_sum3 = 0.0, 0.0, 0.0
    count1, count2, count3 = 0.0, 0.0, 0.0

    # 循环处理直至读至文件末尾
    while True:
        # 读取数据
        first_name = read(file).strip()
        last_name = read(file).strip()
        pos = read(file).strip()
        pay = read(file).strip()

        # 判断职位分别对人数工资计数
        if pos == "assistant":
            pay_sum1 += float(pay)
            count1 += 1
        if pos == "associate":
            pay_sum2 += float(pay)
            count2 += 1
        if pos == "full":
            pay_sum3 += float(pay)
            count3 += 1

        # 判断是否到达文件末尾
        if pay == '' and pos == '':
            break

    # 计算总体工资及总人数
    total_pay_sum = pay_sum1 + pay_sum2 + pay_sum3
    count_sum = count1 + count2 + count3

    # 计算总平均工资和各职位平均工资
    total_pay_aver = total_pay_sum / count_sum
    pay_aver1 = pay_sum1 / count1
    pay_aver2 = pay_sum2 / count2
    pay_aver3 = pay_sum3 / count3

    # 输出结果
    print("Sum of assistant: {:d} ".format(int(pay_sum1)))
    print("Sum of associate: {:d} ".format(int(pay_sum2)))
    print("Sum of full: {:d} ".format(int(pay_sum3)))
    print("Sum of all: {:d} ".format(int(total_pay_sum)))
    print("Average of assistant: {:.2f} ".format(pay_aver1))
    print("Average of associate: {:.2f} ".format(pay_aver2))
    print("Average of full: {:.2f} ".format(pay_aver3))
    print("Average of all: {:.2f} ".format(total_pay_aver))

    file.close()


# 读取数据方法
def read(file):
    s = ""
    while True:
        t = file.read(1)
        if t.isalnum():
            s += t
        else:
            break
    return s


if __name__ == '__main__':
    main()
