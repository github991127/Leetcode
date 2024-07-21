'''
https://leetcode.cn/problems/combination-sum-iii/
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
只使用数字1到9
每个数字 最多使用一次
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
'''
from typing import List

N = 10


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n or n > 60:
            return []
        result = []
        path = []
        self.backtracking(n, k, 1, path, result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            if sum(path) == n:
                result.append(path[:])
            return
        for i in range(startIndex, min(N, n - sum(path) + 1)):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.combinationSum3(3, 20)
    print(outcome)
