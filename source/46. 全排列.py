'''
https://leetcode.cn/problems/permutations/
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def permute(self, nums):
        used = [False] * len(nums)
        self.backtracking(nums, used)
        return self.result

    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path.pop()
            used[i] = False


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.permute([1, 2, 3])
    print(outcome)
