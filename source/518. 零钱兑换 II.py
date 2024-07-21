'''
https://leetcode.cn/problems/coin-change-ii/description/
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
假设每一种面额的硬币有无限个。
题目数据保证结果符合 32 位带符号整数。
'''
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 排除 Corner Case

        # 创建 dp table
        dp = [0] * (amount + 1)

        # 初始化 dp 数组
        dp[0] = 1

        # 遍历顺序
        for i in coins:  # 本题求组合：内层容量；若求排列：内存物品
            for j in range(i, amount + 1):  # 完全背包放入多次，顺序遍历
                dp[j] += dp[j - i]

        # 返回答案
        return dp[-1]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    obj1 = Solution()
    outcome = obj1.change(amount, coins)
    print(outcome)
