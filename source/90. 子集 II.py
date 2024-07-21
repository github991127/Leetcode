'''
https://leetcode.cn/problems/subsets-ii/
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, startIndex=0)
        return self.result

    def backtracking(self, nums, startIndex):
        self.result.append(self.path[:])
        for index in range(startIndex, len(nums)):
            if index != startIndex and nums[index] == nums[index - 1]:
                continue
            self.path.append(nums[index])
            self.backtracking(nums, index + 1)
            self.path.pop()


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.subsetsWithDup([2, 2, 1, 2])
    print(outcome)
