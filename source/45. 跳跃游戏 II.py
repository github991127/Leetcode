'''
45. 跳跃游戏 II
https://leetcode.cn/problems/jump-game-ii/
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
'''
from typing import List


class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0

        cur_distance = 0  # 当前覆盖最远距离下标
        result = 0  # 记录走的最大步数
        next_distance = 0  # 下一步覆盖最远距离下标

        for i in range(len(nums)):
            next_distance = max(nums[i] + i, next_distance)  # 更新下一步覆盖最远距离下标
            if i == cur_distance:  # 遇到当前覆盖最远距离下标
                result += 1  # 需要走下一步
                cur_distance = next_distance  # 更新当前覆盖最远距离下标（相当于加油了）
                if next_distance >= len(nums) - 1:  # 当前覆盖最远距离达到数组末尾，不用再做result++操作，直接结束
                    break

        return result


if __name__ == "__main__":
    nums = [1, 3, 2]

    obj1 = Solution()
    outcome = obj1.jump(nums)
    print(outcome)
