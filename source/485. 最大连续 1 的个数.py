# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0

        maxCount = max(maxCount, count)  # ●考虑数组结尾为1
        return maxCount


obj1 = Solution()
list = [1, 1, 0, 1, 1, 1]
a = obj1.findMaxConsecutiveOnes(list)
print(a)
'''
自解
#部分错解，未考虑分支走不到更新语句
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        total=0
        a=0
        for i in nums:
            if i==0:
                a=max(a,total)
                total=0
            else:
                total+=1
        return a#错误，未考虑else分支造成的total大于a情况（未更新），循环完后应该再进行一次max(a,total)
'''
