y, m, d = eval(input("Please input the year, month, day : "))
q = d
if m == 1 or m == 2:
    m += 12
    y -= 1
j = (y / 100) // 1
k = y % 100

h = (q + 26 * (m + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7

if h == 0:
    print("Saturday")
elif h == 1:
    print("Sunday")
elif h == 2:
    print("Monday")
elif h == 3:
    print("Tuesday")
elif h == 4:
    print("Wednesday")
elif h == 5:
    print("Thursday")
elif h == 6:
    print("Friday")
