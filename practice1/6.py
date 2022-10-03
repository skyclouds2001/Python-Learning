import math


#   判断数是否为素数方法
def is_prime(x):
    #   小于等于1情况、等于2情况、偶数情况特判
    if x <= 1:
        flag = False
    elif x == 2:
        flag = True
    elif x % 2 == 0:
        flag = False
    #   其他情况判断
    #   只判断是否被奇数整除且到该数的平方根即可
    else:
        flag = True
        for j in range(3, int(math.sqrt(x)), 2):
            if x % j == 0:
                flag = False
                break
    return flag


#   判断数是否为回文数方法
def is_palindrome_number(x):
    s = str(x)
    #   默认为True，若不相符再标记为False
    flag = True
    #   头尾同时比较
    for k in range(len(s)):
        if s[k] != s[len(s) - k - 1]:
            flag = False
    return flag


#   主函数部分
#   定义常量：总题目个数、每行题目个数
TOTAL_NUMBER_OF_INTEGERS = 100
NUMBER_OF_INTEGERS_PER_LINE = 10
#   定义变量：起始从2开始判断、初始化个数为0
i = 2
n = 0

while n < TOTAL_NUMBER_OF_INTEGERS:
    if is_prime(i) and is_palindrome_number(i):
        print(format(i, "10d"), end="")
        n += 1
        #   输出每行个数达到10时换行
        if n % NUMBER_OF_INTEGERS_PER_LINE == 0 and n > 0:
            print()
    i += 1
