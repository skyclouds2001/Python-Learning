import math
import turtle

#   设置窗口大小:500*500
turtle.screensize(500, 500)

#   设置画笔速度、颜色、画笔大小
turtle.speed(10)
turtle.color("red")
turtle.pensize(2)

#   将画笔移动至起始点：最上方的尖角处
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()

#   画第一条边前调整画笔角度
turtle.setheading(288)

#   画第一至五条边
for i in range(5):
    #   边的长度为200 * math.cos(18)
    turtle.forward(200 * math.cos(18))
    #   每次向原画笔方向右侧旋转144度
    turtle.right(144)

#   隐藏画笔，完成绘画
turtle.hideturtle()
turtle.done()
