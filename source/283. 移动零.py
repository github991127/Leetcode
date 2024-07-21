# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
from typing import List
#官解1:第一次遍历数非0数量，记录位置。第二次将位置后位全置0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = j = 0
        while i < n:
            if nums[i] != 0:
                nums[j]= nums[i]
                j += 1
            i+=1
        for k in range(j,n):#range左闭右开
            nums[k]=0
obj1=Solution()
List=[1,3,0,0,4,0]
obj1.moveZeroes(List)
print(List)
'''
官解2：判断非0交换，使得使得左指针前全为非0，右指针后全为0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:#右指针判断非0，交换
                nums[left], nums[right] = nums[right], nums[left]
                left += 1#换后，左指针+1
            right += 1
'''
'''
自解
局限：没有将解法抽象到通用部分，增加了不必要初始化
循环逻辑理解混乱，乱加嵌套，不善用if，使得数组边界多次判断
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        left=0
        while (nums[left] and left<n-1): a += 1
        right=left
        while (right<nums.__len__()-1):
            while (nums[right] == 0 and right<nums.__len__()-1):right+=1
            nums[left],nums[right]=nums[right],nums[left]
            left=left+1
'''