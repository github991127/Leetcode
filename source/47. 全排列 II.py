'''
https://leetcode.cn/problems/permutations-ii/
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        self.backtracking(nums, used)
        return self.result

    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        map=set()
        for i in range(len(nums)):
            if used[i] or nums[i] in map:
                continue
            used[i] = True
            map.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path.pop()
            used[i] = False


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.permuteUnique([1, 2, 2])
    print(outcome)
