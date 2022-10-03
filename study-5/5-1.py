import random

n1 = random.randint(0, 9)
n2 = random.randint(0, 9)

if n1 < n2:
    t = n1
    n1 = n2
    n2 = t

n = eval(input("What is the answer of " + str(n1) + " - " + str(n2) + "/ "))
while n != n1 - n2:
    print("Wrong answer. Try again.", "What is the answer of" + str(n1) + " - " + str(n2) + "? ", end="")
    n = eval(input())
print("You got it!")
