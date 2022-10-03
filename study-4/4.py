import random
import time

# : == != < > <= >=

print(bool(2), bool(1), bool(0))

i = 1
while i <= 5:
    print(format(random.random(), ".2f"))
    i += 1

for i in range(1, 11):
    print(format(i ** i, "-10d"))

print(time.time())

n1 = True
n2 = False
for i in range(20):
    print(n1 if random.randint(0, 9) % 2 == 0 else n2, " ", end="")
