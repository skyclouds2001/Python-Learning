import turtle

x1, y1 = eval(input("point 1:"))
x2, y2 = eval(input("point 2:"))
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
print(distance)

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p1")
turtle.goto(x2, y2)
turtle.write("p2")

turtle.penup()
turtle.goto((x1+x2)/2, (y1+y2)/2)
turtle.pendown()
turtle.write(distance)

turtle.done()
