class Fan:
    # 定义的三个有关速度的类成员常量
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # 初始化方法，均包含相应的初始化值
    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # 访问器
    def get_speed(self):
        return self.__speed

    def get_on(self):
        return self.__on

    def get_color(self):
        return self.__color

    def get_radius(self):
        return self.__radius

    # 设置器
    def set_speed(self, speed):
        self.__speed = speed

    def set_on(self, on):
        self.__on = on

    def set_color(self, color):
        self.__color = color

    def set_radius(self, radius):
        self.__radius = radius


# 用于格式化输出fan类对象
def fan_print(fan):
    print("speed = ", fan.get_speed(),
          "radius = ", fan.get_radius(),
          "color = ",  fan.get_color(),
          "on = ", fan.get_on())


# 主函数
def main():
    # 创建Fan类对象
    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)
    # 输出测试
    fan_print(fan1)
    fan_print(fan2)


# 调用主函数
main()
