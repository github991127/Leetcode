# 11. 动规模板
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
    n = 2

    obj = Solution()
    x = obj.climbStairs(n)
    print(x)

    # ACM()
