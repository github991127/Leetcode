'''
https://leetcode.cn/problems/trapping-rain-water/description/
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftheight, rightheight = [0] * len(height), [0] * len(height)

        leftheight[0] = height[0]  # 记录两侧，防止比较时超出下标
        for i in range(1, len(height)):  # 索引以左最高峰
            leftheight[i] = max(leftheight[i - 1], height[i])

        rightheight[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):  # 索引以右最高峰
            rightheight[i] = max(rightheight[i + 1], height[i])

        result = 0
        for i in range(0, len(height)):  # 索引两侧最低峰-脚下
            summ = min(leftheight[i], rightheight[i]) - height[i]
            result += summ
        print(leftheight, rightheight)
        return result

    def trap2(self, height: List[int]) -> int:
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while len(stack) != 0 and height[i] > height[stack[-1]]:
                    cur = stack.pop()
                    if len(stack) != 0:
                        h = min(height[i], height[stack[-1]]) - height[cur]
                        width = i - stack[-1] - 1
                        result += h * width
                stack.append(i)
        return result


def ACM():
    obj1 = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))
            target = nums.pop(0)
            outcome = obj1.trap(nums)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()

    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    nums = [2, 1, 0, 1, 3]

    obj1 = Solution()
    outcome = obj1.trap2(nums)
    print(outcome)
