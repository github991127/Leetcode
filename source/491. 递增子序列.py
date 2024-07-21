'''
https://leetcode.cn/problems/non-decreasing-subsequences/
给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.N = 201

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.result

    # # 哈希表去重
    # def backtracking(self, nums, startIndex):
    #     if len(self.path) > 1:
    #         self.result.append(self.path[:])
    #     map = [0] * self.N
    #     for index in range(startIndex, len(nums)):
    #         if map[nums[index] + 100] == 1:
    #             continue
    #         if self.path == [] or nums[index] >= self.path[-1]:
    #             map[nums[index] + 100] = 1
    #             self.path.append(nums[index])
    #             self.backtracking(nums, index + 1)
    #             self.path.pop()

    # # set去重
    def backtracking(self, nums, startIndex):
        if len(self.path) > 1:
            self.result.append(self.path[:])
        numset = set()
        for index in range(startIndex, len(nums)):
            if nums[index] in numset:
                continue
            if self.path == [] or nums[index] >= self.path[-1]:
                numset.add(nums[index])
                self.path.append(nums[index])
                self.backtracking(nums, index + 1)
                self.path.pop()


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.findSubsequences([4, 6, 7, 7])
    print(outcome)
