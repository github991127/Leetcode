'''
https://leetcode.cn/problems/combination-sum/
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为 target 的不同组合数少于 150 个。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        self.backtracking(candidates, target, 0)
        return self.result

    def backtracking(self, candidates, target, startIndex):
        if sum(self.path) == target:
            self.result.append(self.path[:])
            return

        for index in range(startIndex, len(candidates)):
            self.path.append(candidates[index])
            if sum(self.path) > target:
                self.path.pop()
                break
            self.backtracking(candidates, target, index)
            self.path.pop()


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.combinationSum([2, 5, 3], 8)
    print(outcome)
