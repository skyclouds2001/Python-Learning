import turtle

x1, y1 = eval(input())
r = eval(input())
x2, y2 = eval(input())

turtle.penup()
turtle.goto(x1, x2 - r)
turtle.pendown()
turtle.circle(r)

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot(5, "red")

turtle.penup()
turtle.goto(x1 - 70, y1 - 20 - r)
turtle.pendown()

d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
if d <= r:
    turtle.write("The point is inside the circle")
else:
    turtle.write("The point is outside the circle")

turtle.hideturtle()

turtle.done()

