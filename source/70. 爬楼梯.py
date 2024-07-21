'''
https://leetcode.cn/problems/climbing-stairs/
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        # 排除 Corner Case
        if n == 1:
            return 1

        # 创建 dp table
        dp = [0] * (n + 1)

        # 初始化 dp 数组
        dp[1] = 1
        dp[2] = 2

        # 遍历顺序
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # 返回答案
        return dp[n]


def ACM():
    obj = Solution()
    while True:
        try:
            n = int(input())
            x = obj.climbStairs(n)
            print(x)
        except:
            break


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.climbStairs(5)
    print(outcome)

    ACM()
