'''
https://leetcode.cn/problems/integer-break/
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
返回 你可以获得的最大乘积 。
'''
from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        # 排除 Corner Case
        if n <= 3:
            return n - 1

        # 创建 dp table
        dp = [1] * (n + 1)

        # 初始化 dp 数组
        dp[2] = 2
        dp[3] = 3

        # 遍历顺序
        for i in range(4, n + 1):
            maxX = 0
            for j in range(2, i // 2 + 1):
                maxX = max(j * dp[i - j], maxX)
            dp[i] = maxX

        # 返回答案
        return dp[-1]


def ACM():
    obj = Solution()
    while True:
        try:
            n = int(input())
            x = obj.integerBreak(n)
            print(x)
        except:
            break


if __name__ == "__main__":
    n = 10
    obj = Solution()
    x = obj.integerBreak(n)
    print(x)

    ACM()
