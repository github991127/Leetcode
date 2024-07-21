'''
https://leetcode.cn/problems/4sum-ii/
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict = {}
        count = 0
        for num1 in nums1:
            for num2 in nums2:
                dict[num1 + num2] = dict.get(num1 + num2, 0) + 1
        for num3 in nums3:
            for num4 in nums4:
                count += dict.get(0 - num3 - num4, 0)
        return count

if __name__ == "__main__":
    x = 5
    List1 = [1, 2, 3, 5, 8]
    List2 = [-1, 2, 3, 5, 8]
    List3 = [1, -2, 3, 5, 8]
    List4 = [1, 2, -3, 5, 8]

    obj1 = Solution()
    outcome = obj1.fourSumCount(List1, List2, List3, List4)
    print(outcome)
