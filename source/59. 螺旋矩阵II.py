'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
https://leetcode.cn/problems/spiral-matrix-ii/
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        loop = 0
        fig = 1
        a = [[0] * n for _ in range(n)]
        while (loop < n / 2):
            i = j = loop
            while (j < n - 1 - loop):
                a[i][j] = fig
                fig += 1
                j += 1
            while (i < n - 1 - loop):
                a[i][j] = fig
                fig += 1
                i += 1
            while (j > 0 + loop):
                a[i][j] = fig
                fig += 1
                j -= 1
            while (i > 0 + loop):
                a[i][j] = fig
                fig += 1
                i -= 1
            loop += 1
        if n % 2 == 1:
            a[loop - 1][loop - 1] = n ** 2
        return a


if __name__ == "__main__":
    obj1 = Solution()
    n = 5
    outcome = obj1.generateMatrix(n)
    for row in outcome:
        print(row)
