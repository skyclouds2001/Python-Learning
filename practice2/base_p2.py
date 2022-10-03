import turtle


def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


def write_text(s, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(s)


def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()


def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.circle(r)
