'''
https://leetcode.cn/problems/target-sum/description/
给你一个非负整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
'''
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 排除 Corner Case
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0  # 此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0  # 此时没有方案
        A = (target + total_sum) // 2  # 目标和，即背包容量

        # 创建 dp table
        dp = [0] * (A + 1)  # 创建动态规划数组，初始化为0
        # 初始化 dp 数组
        dp[0] = 1  # 当目标和为0时，只有一种方案，即什么都不选

        # 遍历顺序
        for num in nums:
            for j in range(A, num - 1, -1):  # 装当前物品时，如果物品已经大于容量，那组合数肯定不会增加，所以到num就不用往回退了（回退反而导致负数容量计算错误）
                dp[j] += dp[j - num]

        # 返回答案
        return dp[A]


if __name__ == "__main__":
    nums = [1, 2, 3, 4]  # 2
    # nums = [0, 0, 0, 0]  # 16
    target = 0
    obj1 = Solution()
    outcome = obj1.findTargetSumWays(nums, target)
    print(outcome)
