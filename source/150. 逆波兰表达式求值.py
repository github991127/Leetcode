'''
https://leetcode.cn/problems/evaluate-reverse-polish-notation/
给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。
请你计算该表达式。返回一个表示表达式值的整数。
'''
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item in ['+', '-', '*', '/']:
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                if item == '+':
                    stack.append(a + b)
                elif item == '-':
                    stack.append(a - b)
                elif item == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(item))
        return stack[0]


if __name__ == "__main__":
    s1 = Solution()
    # str = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    str = ["0", "3", "/"]
    x = s1.evalRPN(str)
    print(x)
