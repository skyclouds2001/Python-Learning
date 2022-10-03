import math
TOTAL_NUMBER = 10

print("Enter 10 numbers:")
list0 = list()

for i in range(TOTAL_NUMBER):
    n = eval(input())
    list0.append(n)

sum0 = 0
sum0_2 = 0

for i in range(TOTAL_NUMBER):
    sum0 += list0[i]
    sum0_2 += list0[i] * list0[i]

mean = sum0 / TOTAL_NUMBER
deviation = math.sqrt(math.fabs((sum0_2 - sum0 * sum0) / (TOTAL_NUMBER - 1)))

print("The mean is", mean)
print("The standard deviation is", deviation)
