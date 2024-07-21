'''
https://leetcode.cn/problems/jump-game/
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
'''
from typing import List


class Solution:
    # def __init__(self):
    #     self.path = []
    #     self.result = []

    def canJump(self, nums: List[int]) -> bool:
        maxd = 0
        for index in range(len(nums)):
            if index > maxd:
                return False
            maxd = max(maxd, index + nums[index])
            if maxd >= len(nums) - 1:
                break
        return True


if __name__ == "__main__":
    nums = [2, 3, 1, 0, 1]

    obj1 = Solution()
    outcome = obj1.canJump(nums)
    print(outcome)
