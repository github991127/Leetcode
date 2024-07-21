'''
https://leetcode.cn/problems/two-sum/
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个集合来存储我们目前看到的数字
        seen = set()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)


if __name__ == "__main__":
    x = 6
    List1 = [1, 2, 3, 5, 8]

    obj1 = Solution()
    outcome = obj1.twoSum(List1, x)
    print(outcome)
