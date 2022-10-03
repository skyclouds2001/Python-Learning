n = eval(input("Enter a number : "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i, j)

print("The total number of all combinations is", int(n * (n - 1) / 2))
