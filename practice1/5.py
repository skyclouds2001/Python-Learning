import random
import time

#   定义常量——题目个数
NUMBER_OF_PROBLEMS = 50
#   定义记录正确题目个数的变量
numberOfCorrectAnswers = 0

#   开始计时
startTime = time.time()

for i in range(NUMBER_OF_PROBLEMS):
    #   产生题目
    a = int(random.random() * 90 + 10)
    b = int(random.random() * 90 + 10)

    #   输出题目与读入答案
    print(i + 1, ": What is the answer of ", a, "-", b, "?")
    ans = eval(input())

    #   判断是否为正确答案，正确则计数+1
    #   输出判断结果
    if ans == a - b:
        numberOfCorrectAnswers += 1
        print("Correct\n")
    else:
        print("Wrong\n")

#   结束计时并计算答题时间
endTime = time.time()
totalTime = int(endTime - startTime)

#   输出正确答题数量及答题时间
print("The number of correct answers is", numberOfCorrectAnswers)
print("The total time is", totalTime, "seconds")
