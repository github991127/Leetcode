#给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for num in nums:
            if dict.get(num):return True#dict.get(num)判断键存在
            else:dict[num]=1
        return False

obj1=Solution()
List=[1,2,3,2]
outcome = obj1.containsDuplicate(List)
print(outcome)

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=[]
        for num in nums:
            if num in a:return True#耗时过长
            else:a.append(num)
        return False
'''