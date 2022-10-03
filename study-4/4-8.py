n = eval(input())

if n % 2 == 0 and n % 3 == 0:
    print("2 and 3 !")

if n % 2 == 0 or n % 3 == 0:
    print("2 or 3 !")

if (n % 2 == 0 or n % 3 == 0) and n % 2 != n % 3:
    print("2 xor 3 !")
