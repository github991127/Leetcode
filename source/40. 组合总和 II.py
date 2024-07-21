'''
https://leetcode.cn/problems/combination-sum-ii/
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
            if index > startIndex and candidates[index] == candidates[index - 1]:
                continue
            self.path.append(candidates[index])
            if sum(self.path) > target:
                self.path.pop()
                break
            self.backtracking(candidates, target, index + 1)
            self.path.pop()


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5)
    print(outcome)
