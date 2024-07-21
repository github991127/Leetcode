'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            rightBoder = -1
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                elif middle == len(nums) - 1 or nums[middle + 1] != target:  # 相等，然后判断当前边界外是否仍相等
                    return middle
                else:  # 若不相等，说明右边界还在右侧，情况同nums[middle] < target
                    left = middle + 1
            return rightBoder

        def getLeftBorder(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            leftBoder = -1
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                elif middle == 0 or nums[middle - 1] != target:
                    return middle
                else:
                    right = middle - 1
            return leftBoder

        leftBoder = getLeftBorder(nums, target)
        rightBoder = getRightBorder(nums, target)
        return [leftBoder, rightBoder]


if __name__ == "__main__":
    obj1 = Solution()
    x = 3
    # x = 8
    List1 = [1, 3, 3, 5, 7]
    outcome = obj1.searchRange(List1, x)
    print(outcome)
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            rightBoder = -2
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                else:  # 寻找右边界，nums[middle] == target的时候更新left
                    left = middle + 1
                    rightBoder = left  # ???

            return rightBoder

        def getLeftBorder(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            leftBoder = -2
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] >= target:  # 寻找左边界，nums[middle] == target的时候更新right
                    right = middle - 1
                    leftBoder = right
                else:
                    left = middle + 1
            return leftBoder

        leftBoder = getLeftBorder(nums, target)
        rightBoder = getRightBorder(nums, target)
        print(leftBoder, rightBoder)
        # 情况一
        if leftBoder == -2 or rightBoder == -2: return [-1, -1]
        # 情况三
        if rightBoder - leftBoder > 1: return [leftBoder + 1, rightBoder - 1]
        # 情况二
        return [-1, -1]
'''
