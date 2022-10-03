import random

a = random.randint(0, 99)
b = random.randint(0, 99)

print("What is ", a, '+', b, '?')

ans = eval(input())

if ans == a + b:
    print("Right!")
else:
    print("Wrong!")
    print("The answer of", a, '+', b, "is", a+b)
