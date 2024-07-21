'''
https://leetcode.cn/problems/intersection-of-two-arrays/
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
'''
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1

        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)

        return list(res)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 5, 5]
    nums2 = [2, 2, 2, 5, 3]

    obj1 = Solution()
    outcome = obj1.intersection(nums1, nums2)
    print(outcome)
