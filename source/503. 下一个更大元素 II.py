'''
https://leetcode.cn/problems/next-greater-element-ii/description/
给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。
'''
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = [0]  # 存放下标0，下标索引数值效率高
        for i in range(1, len(nums) * 2):
            i = i % len(nums)
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums[i] > nums[stack[-1]]:
                    result[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i)
        return result


def ACM():
    obj1 = Solution()
    while True:
        try:
            nums = int(input())
            outcome = obj1.nextGreaterElements(nums)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()
    nums = [1, 3, 2, 4, 0]
    nums = [1, 2, 1]

    obj1 = Solution()
    outcome = obj1.nextGreaterElements(nums)
    print(outcome)
