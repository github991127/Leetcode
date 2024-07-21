'''
#283题变式
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
https://leetcode.cn/problems/remove-element/
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = j = 0
        while i < n:
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


obj1 = Solution()
List = [1, 3, 0, 0, 4, 0]
val = 0
len = obj1.removeElement(List, val)
print(List[0:len])
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
