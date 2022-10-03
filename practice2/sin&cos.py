import math
import turtle

import base_p2


# 返回sin函数的函数值
def fs(x):
    return 50 * math.sin(2 * math.pi * (x / 100))


# 返回cos函数的函数值
def fc(x):
    return 50 * math.cos(2 * math.pi * (x / 100))


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

    # 修改画笔颜色为blue
    turtle.color("blue")
    # 绘制sin函数图线
    turtle.penup()
    turtle.goto(-275, fs(-275))
    turtle.pendown()
    for i in range(-275, 276):
        turtle.goto(i, fs(i))

    # 修改画笔颜色为red
    turtle.color("red")
    # 绘制cos函数图线
    turtle.penup()
    turtle.goto(-275, fc(-275))
    turtle.pendown()
    for i in range(-275, 276):
        turtle.goto(i, fc(i))

    # 重置画笔颜色为black
    turtle.color("black")
    # 写文字2π与-2π
    base_p2.write_text("2\u03c0", 100, 0)
    base_p2.write_text("-2\u03c0", -100, 0)

    # 完成绘画
    turtle.done()


# 调用主函数
main()
