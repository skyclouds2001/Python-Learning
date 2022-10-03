# 封装列表list实现的栈
# 列表中下标0处为栈顶，下标最大处为栈底
import logging


class Stack:
    def __init__(self):
        self.list0 = []
        self.number: int = 0

#   返回栈内元素个数
    def len(self):
        return self.number

#   返回栈顶元素
    def top(self):
        return self.list0[self.number - 1]

#   向栈中压入元素
    def push(self, x):
        self.list0.append(x)
        self.number += 1

    #   从栈中弹出元素
    def pop(self):
        t = self.list0[self.number - 1]
        del self.list0[self.number - 1]
        self.number -= 1
        return t

#   判断栈是否为空
    def is_empty(self):
        return self.number == 0


class UnExceptedCommandError(Exception):
    pass


#   主函数/测试stack类
def main():
    s = Stack()
    while True:
        try:
            # 根据输入指令分别调用对应的栈类方法
            c = eval(input("Please press the choice: "))
            # 结束测试
            if c == 0:
                break
            # 弹入
            elif c == 1:
                x = eval(input("Please input the number: "))
                s.push(x)
            # 弹出
            elif c == 2:
                print(s.pop())
            # 返回栈顶元素
            elif c == 3:
                print(s.top())
            # 返回栈元素个数
            elif c == 4:
                print(s.len())
            # 返回栈是否为空
            elif c == 5:
                print(s.is_empty())
            # 其他指令，抛出异常
            else:
                raise UnExceptedCommandError
        # 捕获异常
        except IndexError as e:
            logging.exception(e)
        except UnExceptedCommandError as e:
            logging.exception(e)


# 调用主函数
if __name__ == '__main__':
    main()
