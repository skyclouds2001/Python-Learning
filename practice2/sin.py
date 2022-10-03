import math
import turtle

import base_p2


# 返回sin函数的函数值
def f(x):
    return 50 * math.sin(2 * math.pi * (x / 100))


# 主函数
def main():
    # 调整画笔速度及隐藏画笔
    turtle.speed(10)
    turtle.hideturtle()

    # 绘制x轴，先画主轴后画箭头
    base_p2.draw_line(-300, 0, 300, 0)
    base_p2.draw_line(290, 10, 300, 0)
    base_p2.draw_line(290, -10, 300, 0)

    # 绘制y轴，先画主轴后画箭头
    base_p2.draw_line(0, -100, 0, 100)
    base_p2.draw_line(10, 90, 0, 100)
    base_p2.draw_line(-10, 90, 0, 100)

    # 绘制sin函数图线
    turtle.penup()
    turtle.goto(-275, f(-275))
    turtle.pendown()
    for i in range(-275, 275):
        turtle.goto(i, f(i))

    # 写文字2π与-2π
    base_p2.write_text("2\u03c0", 100, 0)
    base_p2.write_text("-2\u03c0", -100, 0)

    # 完成绘画
    turtle.done()


# 调用主函数
main()
