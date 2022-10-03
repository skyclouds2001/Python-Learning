x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1 and p2:\n"))
k = float(x1 - x0) / float(y1 - y0)
yy = y0 + k * (x2 - x0)

if yy < y2:
    print("p2 is on the left side of the line from p0 to p1")
elif yy > y2:
    print("p2 is on the right side of the line from p0 to p1")
else:
    print("p2 is on the same line from p0 to p1")
