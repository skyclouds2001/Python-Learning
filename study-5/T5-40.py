import random

count1, count2 = 0, 0

for i in range(1000000):
    f = int(random.random() * 2 + 1)
    if f == 1:
        count1 += 1
    else:
        count2 += 1

print("Front : ", count1)
print("Reverse : ", count2)
