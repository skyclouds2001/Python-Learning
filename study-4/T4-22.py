x, y = eval(input("Enter a point : "))
if x * x + y * y <= 100:
    print("Point (", format(float(x), ".1f"), format(float(y), ".1f"), ") is in the circle")
else:
    print("Point (", format(float(x), ".1f"), format(float(y), ".1f"), ") is not in the circle")
