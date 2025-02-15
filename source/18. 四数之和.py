'''
https://leetcode.cn/problems/4sum/
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:  # 剪枝（可省）
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 去重
                continue
            for j in range(i + 1, n):
                if nums[i] + nums[j] > target and target > 0:  # 剪枝（可省）
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:  # 去重
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return result


if __name__ == "__main__":
    x = 0
    List1 = [-4, -1, -1, -1, 0, 1, 2, 2]
    # List1 = [-2, 0, 0, 2, 2]
    obj1 = Solution()
    outcome = obj1.fourSum(List1, x)
    print(outcome)
