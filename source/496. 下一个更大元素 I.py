'''
https://leetcode.cn/problems/next-greater-element-i/description/
nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
'''
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        stack = [0]  # 存放下标0，下标索引数值效率高
        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        result[index] = nums2[i]
                    stack.pop()
                stack.append(i)
        return result


def ACM():
    obj1 = Solution()
    while True:
        try:
            nums = int(input())
            outcome = obj1.nextGreaterElement(nums)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()
    nums1 = [1, 2, 3]
    nums2 = [1, 3, 2, 4, 0]

    obj1 = Solution()
    outcome = obj1.nextGreaterElement(nums1, nums2)
    print(outcome)
