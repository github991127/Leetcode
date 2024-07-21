'''
https://leetcode.cn/problems/subsets/
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, startIndex=0)
        return self.result

    def backtracking(self, nums, startIndex):
        self.result.append(self.path[:])
        for index in range(startIndex, len(nums)):
            self.path.append(nums[index])
            self.backtracking(nums, index + 1)
            self.path.pop()


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.subsets([1, 2, 3])
    print(outcome)
