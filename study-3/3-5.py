import turtle

turtle.pensize(3)
turtle.speed(10)

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40)

turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps=3)

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps=4)

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps=5)

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40, steps=6)

turtle.pensize(1)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.dot(30, "red")

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.dot(20, "blue")

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.dot(10, "green")

turtle.done()
