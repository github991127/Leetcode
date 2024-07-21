'''
https://leetcode.cn/problems/partition-equal-subset-sum/description/
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
'''
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 排除 Corner Case
        s = sum(nums)
        if s % 2 != 0:
            return False

        # 创建 dp table
        bagnums = s // 2
        dp = [0] * (bagnums + 1)

        # 初始化 dp 数组
        for j in range(nums[0], bagnums + 1):
            dp[j] = nums[0]

        # 遍历顺序
        for i in range(1, len(nums)):  # 内层容量，内层背包均正确
            # for j in range(nums[i], bagnums + 1): # 容量顺序遍历，错误
            for j in range(bagnums, nums[i] - 1, -1):  # 容量逆序遍历
                dp[j] = max(dp[j], nums[i] + dp[j - nums[i]])
            if dp[-1] == bagnums:
                return True

        # 返回答案
        return False


if __name__ == "__main__":
    nums = [1, 3, 2, 4]
    nums = [1, 2, 5]

    obj1 = Solution()
    outcome = obj1.canPartition(nums)
    print(outcome)
