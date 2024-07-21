'''
https://leetcode.cn/problems/climbing-stairs/
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 排除 Corner Case
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        # 创建 dp table
        dp = [1] * n

        # 初始化 dp 数组
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                dp[j:n] = [0] * (n - j)
                break

                # 遍历顺序
        for i in range(1, m):
            for j in range(0, n):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j != 0:
                    dp[j] += dp[j - 1]

        # 返回答案
        return dp[-1]


def ACM():
    obj = Solution()
    while True:
        try:
            m = int(input())
            obstacleGrid = []
            for i in range(m):
                digits = list(map(int, input().split(' ')))
                obstacleGrid.append(digits)
            x = obj.uniquePathsWithObstacles(obstacleGrid)
            print(x)
        except:
            break


if __name__ == "__main__":
    # obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    obstacleGrid = [[0, 1], [0, 0]]
    # obstacleGrid = [[1, 0], [0, 0]]
    obj = Solution()
    x = obj.uniquePathsWithObstacles(obstacleGrid)
    print(x)

    ACM()
