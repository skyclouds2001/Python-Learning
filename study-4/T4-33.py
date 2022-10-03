t = eval(input("Enter a decimal value (0 to 15) : "))
if 10 <= t <= 15:
    a = chr(t - 10 + ord('A'))
else:
    a = str(t)
print("The hex value is", a)
