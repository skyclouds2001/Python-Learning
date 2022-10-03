import random

a = int(random.random() * 13) + 1
b = int(random.random() * 4) + 1

s1 = "!"
s2 = "!"

if 2 <= a <= 10:
    s1 = str(a)
elif a == 1:
    s1 = "Ace"
elif a == 11:
    s1 = "Jack"
elif a == 12:
    s1 = "Queen"
elif a == 13:
    s1 = "King"

if b == 1:
    s2 = "Club"
elif b == 2:
    s2 = "Spade"
elif b == 3:
    s2 = "Heart"
elif b == 4:
    s2 = "Diamond"

print("The card you picked is the ", s1, "of", s2)
