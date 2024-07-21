'''
https://leetcode.cn/problems/coin-change/description/
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。
'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 排除 Corner Case

        # 创建 dp table
        dp = [float('inf')] * (amount + 1)

        # 初始化 dp 数组
        dp[0] = 0

        # 遍历顺序
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = min(dp[j], 1 + dp[j - i])

        # 返回答案
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]


if __name__ == "__main__":
    coins = [1, 2, 5]
    # coins = [3, 5]
    amount = 7

    obj1 = Solution()
    outcome = obj1.coinChange(coins, amount)
    print(outcome)
