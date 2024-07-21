'''
https://leetcode.cn/problems/combination-sum-iv/description/
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
题目数据保证答案符合 32 位整数范围。
'''
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 排除 Corner Case

        # 创建 dp table
        dp = [0] * (target + 1)

        # 初始化 dp 数组
        dp[0] = 1

        # 遍历顺序
        for j in range(1, target + 1):
            for i in nums:
                if j - i >= 0:
                    dp[j] += dp[j - i]

        # 返回答案
        return dp[-1]


if __name__ == "__main__":
    target = 4
    nums = [1, 2, 3]
    obj1 = Solution()
    outcome = obj1.combinationSum4(nums, target)
    print(outcome)
