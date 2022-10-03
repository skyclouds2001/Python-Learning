import random

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)

if n1 < n2:
    t = n1
    n1 = n2
    n2 = t

n = eval(input("What is the answer of " + str(n1) + " - " + str(n2) + " ?\n"))

while True:
    if n == n1 - n2:
        print("Correct!", end="")
        print("The answer of " + str(n1) + " - " + str(n2) + " is " + str(n))
        break
    else:
        print("Wrong!")
        n = eval(input("What is the answer of " + str(n1) + " - " + str(n2) + " ?\n"))
