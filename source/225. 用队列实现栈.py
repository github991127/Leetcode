'''
https://leetcode.cn/problems/implement-stack-using-queues/
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
'''
from typing import List


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.pop(0))
        return self.stack.pop(0)

    def top(self) -> int:
        x = self.pop()
        if x:
            self.stack.append(x)
            return x
        else:
            return

    def empty(self) -> bool:
        return not self.stack


if __name__ == "__main__":
    x = 3
    stack = MyStack()
    stack.push(x)
    param_2 = stack.pop()
    param_3 = stack.top()
    param_4 = stack.empty()
    print(param_2)
    print(param_3)
    print(param_4)
