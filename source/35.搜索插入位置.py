'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
链接：https://leetcode.cn/problems/search-insert-position
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while (left < right):
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return right


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(' ')))
            target = nums.pop(0)
            x = obj.searchInsert(nums, target)
            print(x)
        except:
            break


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 5, 8]
    target = 5
    x = obj.searchInsert(nums, target)
    print(x)
    ACM()
