'''
https://leetcode.cn/problems/3sum/
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
你返回所有和为 0 且不重复的三元组。
'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tuple_list = []
        if nums[0] > 0:
            return tuple_list

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            # i去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    tuple_list.append((nums[i], nums[left], nums[right]))

                    # left去重
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1

                    # right去重
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1

        return tuple_list


if __name__ == "__main__":
    List1 = [-4, -1, -1, 0, 1, 2]
    List1 = [-2, 0, 0, 2, 2]
    List1 = [-1, -1, -1, 2, 2]
    obj1 = Solution()
    outcome = obj1.threeSum(List1)
    print(outcome)
