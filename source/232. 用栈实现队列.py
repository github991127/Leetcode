'''
https://leetcode.cn/problems/implement-queue-using-stacks/
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
'''
from typing import List


class MyQueue:

    def __init__(self):
        # in主要负责push，out主要负责pop
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # 有新元素进来，就往in里面push
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        # 只要in或者out有元素，说明队列不为空
        return not (self.stack_in or self.stack_out)


if __name__ == "__main__":
    queue = MyQueue();

    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
