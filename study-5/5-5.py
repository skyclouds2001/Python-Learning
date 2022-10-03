n = eval(input("Enter an integer (the input ends if it is 0): "))
ns = 0

while n != 0:
    ns += n
    n = eval(input("Enter an integer (the input ends if it is 0): "))

print("The sum is ", ns)
