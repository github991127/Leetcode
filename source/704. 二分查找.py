'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
链接：https://leetcode.cn/problems/binary-search
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)  # 左闭右开
        while (left < right):
            # mid = (left + right) // 2
            mid = left + (right - left) // 2  # 防止溢出
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    obj1 = Solution()

    nums = [1, 2, 3, 5, 8]
    target = 5
    print(obj1.search(nums, target))

    while True:
        try:
            nums = list(map(int, input().split(" ")))
            target = nums.pop(0)
            print(obj1.search(nums, target))
        except:
            break
