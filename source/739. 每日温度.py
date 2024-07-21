'''
https://leetcode.cn/problems/daily-temperatures/description/
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 result ，其中 result[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
'''
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [0]  # 存放下标0，下标索引数值效率高
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return result


def ACM():
    obj1 = Solution()
    while True:
        try:
            nums = int(input())
            outcome = obj1.dailyTemperatures(nums)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()

    nums = [1, 3, 2, 4, 0]

    obj1 = Solution()
    outcome = obj1.dailyTemperatures(nums)
    print(outcome)
