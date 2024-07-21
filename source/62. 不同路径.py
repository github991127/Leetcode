'''
https://leetcode.cn/problems/unique-paths-ii/
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
'''
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 排除 Corner Case

        # 创建 dp table
        dp = [1] * n

        # 初始化 dp 数组

        # 遍历顺序
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        # 返回答案
        return dp[-1]


def ACM():
    obj = Solution()
    while True:
        try:
            nums = input().split(' ')
            m = int(nums[0])
            n = int(nums[1])
            x = obj.uniquePaths(m, n)
            print(x)
        except:
            break


if __name__ == "__main__":
    m = 3
    n = 7
    obj = Solution()
    x = obj.uniquePaths(m, n)
    print(x)

    ACM()
