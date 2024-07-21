'''
https://leetcode.cn/problems/perfect-squares/description/
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
'''
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        # 排除 Corner Case

        # 创建 dp table
        dp = [float('inf')] * (n + 1)

        # 初始化 dp 数组
        dp[0] = 0

        # 遍历顺序
        for i in range(1, int(n ** 0.5) + 1):
            num = i ** 2
            for j in range(num, n + 1):
                dp[j] = min(dp[j], 1 + dp[j - num])

        # 返回答案
        return dp[-1]


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.numSquares(12)
    print(outcome)
