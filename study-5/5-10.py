import random

TOTAL_NUMBER = 1000000
count = 0

for i in range(TOTAL_NUMBER):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x * x + y * y <= 1:
        count += 1
pi = 4 * count / TOTAL_NUMBER
print("PI is ", pi)
