import random

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)

if n1 < n2:
    t = n1
    n1 = n2
    n2 = t

n = eval(input("What is the answer of " + str(n1) + " - " + str(n2) + ":\t"))

if n == n1 - n2:
    print("Correct!", end="")
else:
    print("Wrong!")
    print("The answer is ", n1 - n2, end="")
