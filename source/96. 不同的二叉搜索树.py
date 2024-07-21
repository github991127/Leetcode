'''
https://leetcode.cn/problems/unique-binary-search-trees/
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
'''
from typing import List


class Solution:
    def numTrees(self, n: int) -> int:
        # 排除 Corner Case

        # 创建 dp table
        dp = [0] * (n + 1)

        # 初始化 dp 数组
        dp[0] = 1
        dp[1] = 1

        # 遍历顺序
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]

        # 返回答案
        return dp[n]


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.numTrees(3)
    print(outcome)
