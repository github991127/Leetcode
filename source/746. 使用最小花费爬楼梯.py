'''
https://leetcode.cn/problems/min-cost-climbing-stairs/
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。
'''
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 排除 Corner Case

        # 创建 dp table
        l = len(cost)
        dp = [0] * (l + 1)

        # 初始化 dp 数组
        # dp[0] = 0
        # dp[1] = 0

        # 遍历顺序
        for i in range(2, l + 1):
            # 确定递归公式/状态转移公式
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])

        # 返回答案
        return dp[-1]


def ACM():
    obj = Solution()
    while True:
        try:
            cost = list(map(int, input().split(',')))
            x = obj.minCostClimbingStairs(cost)
            print(x)
        except:
            break


if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    obj = Solution()
    x = obj.minCostClimbingStairs(cost)
    print(x)

    ACM()
    # 1, 100, 1, 1, 1, 100, 1, 1, 100, 1
