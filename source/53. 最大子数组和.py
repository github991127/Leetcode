'''
https://leetcode.cn/problems/maximum-subarray/
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        num_sum = 0
        for num in nums:
            num_sum += num
            if num_sum > result:
                result = num_sum
            if num_sum < 0:
                num_sum = 0
        return result


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 6
    nums = [-2, -1, -3]  # -1
    obj1 = Solution()
    outcome = obj1.maxSubArray(nums)
    print(outcome)
