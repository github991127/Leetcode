'''
https://leetcode.cn/problems/n-queens/
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

'''
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.chessboard = []

    def solveNQueens(self, n: int) -> List[List[str]]:

        self.chessboard = ['.' * n for _ in range(n)]  # 初始化棋盘
        self.backtracking(n, row=0)  # 回溯求解
        return self.result

    def backtracking(self, n, row) -> None:
        if row == n:
            self.result.append(self.chessboard[:])  # 棋盘填满，将当前解加入结果集
            return

        for col in range(n):
            if self.isValid(row, col):
                self.chessboard[row] = self.chessboard[row][:col] + 'Q' + self.chessboard[row][col + 1:]  # 放置皇后
                self.backtracking(n, row + 1)  # 递归到下一行
                self.chessboard[row] = self.chessboard[row][:col] + '.' + self.chessboard[row][col + 1:]  # 回溯，撤销当前位置的皇后

    def isValid(self, row, col) -> bool:
        # 检查列
        for i in range(row):
            if self.chessboard[i][col] == 'Q':
                return False  # 当前列已经存在皇后，不合法

        # 检查 45 度角是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.chessboard[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(self.chessboard):
            if self.chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1

        return True  # 当前位置合法


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.solveNQueens(4)
    print(outcome)
