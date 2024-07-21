'''
输入nums，输出其中子序列["xiao", "mi"]的数量
'''
from typing import List


class Solution:
    def solve(self, nums) -> int:
        target = ["xiao", "mi"]
        i = len(target)
        j = len(nums)
        if j < 6:
            return 0
        dp = [[0] * j for _ in range(i)]

        count = 0
        for indexj in range(3, j):
            if nums[indexj - 3:indexj + 1] == target[0]:
                count += 1
            dp[0][indexj] = count

        for indexi in range(1, i):
            count = 0
            for indexj in range(5, j):
                if nums[indexj - 1:indexj + 1] == target[1]:
                    count += dp[indexi - 1][indexj]
                dp[indexi][indexj] = count
        # print(dp)
        return dp[-1][-1]


def ACM():
    obj1 = Solution()
    while True:
        try:
            nums = input()
            outcome = obj1.solve(nums)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    ACM()

    nums = "I love xiaomi, i often visit mi.com to buy phone"
    obj1 = Solution()
    outcome = obj1.solve(nums)
    print(outcome)
