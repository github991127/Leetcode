'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
链接：https://leetcode.cn/problems/binary-search
'''
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0  # 当前的累加值

        while right < l:
            cur_sum += nums[right]
            while cur_sum >= s:  # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]

                left += 1
            right += 1

        return min_len if min_len != float('inf') else 0


if __name__ == "__main__":
    obj1 = Solution()
    # x = 5
    x = 17
    # x = 100
    List1 = [1, 2, 3, 8, 9]
    outcome = obj1.minSubArrayLen(x, List1)
    print(outcome)

'''
自解
局限：length应该设置为float('inf')，最后用无穷大判断代替布尔判断
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        sum = nums[right]
        length = len(nums)
        bool = False
        while (right < len(nums)):
            if sum >= target:
                bool = True
                length = min(length, right - left + 1)
                # print(length)
                sum -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    sum += nums[right]
        if bool:
            return length
        else:
            return 0
'''
