'''
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
https://leetcode.cn/problems/squares-of-a-sorted-array/
'''
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = n = len(nums) - 1
        nums_new = [float('-inf')] * len(nums)  # 需要提前定义列表，存放结果，float('inf')指无穷大；float('-inf')指无穷小
        # print(nums_new)
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                nums_new[n] = nums[left] ** 2
                left += 1
            else:
                nums_new[n] = nums[right] ** 2
                right -= 1
            n -= 1
        return nums_new

if __name__ == "__main__":
    obj1 = Solution()
    List = [-2, -1, 0, 3, 5]
    nums_new = obj1.sortedSquares(List)
    print(nums_new)

'''
官解2
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
'''
