import random

n = random.randint(0, 100)

print("Guess a number between 0 and 100")

a = eval(input("Enter your guess: "))

while True:
    if a == n:
        print("Yes, the number is ", n)
        break
    elif a < n:
        print("You guess is low")
    else:
        print("You guess is high")
    a = eval(input("Enter your guess: "))
