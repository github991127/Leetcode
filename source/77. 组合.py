'''
https://leetcode.cn/problems/combinations/
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
'''
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        path = []
        self.backtracking(n, k, 1, path, result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])  # path为浅复制，必须要重新用一个列表path[:]，否则后续path改变，result会随之变化
            return
        # for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
        for i in range(startIndex, n + 1):
            if startIndex + (k - len(path)) > n + 1:  # 优化的地方从for范围中剥离出来写成if
                return
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.combine(4, 3)
    print(outcome)
