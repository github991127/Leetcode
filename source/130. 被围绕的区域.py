'''
https://leetcode.cn/problems/surrounded-regions/description/
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
'''
from typing import List
from collections import deque


class SolutionDFS:
    def __init__(self):
        self.node = []
        self.flag = True

    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(x, y):  # 内方法省去了变量传递
            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                self.flag = False
            for d in dirs:  # dfs从任意一方向（四方向之一）一直递归
                nextx = x + d[0]
                nexty = y + d[1]
                if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:  # 越界了，直接跳过
                    continue
                if not visited[nextx][nexty] and board[nextx][nexty] == "O":  # 没有访问过的同时是陆地的
                    visited[nextx][nexty] = True
                    self.node.append((nextx, nexty))
                    dfs(nextx, nexty)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == "O":
                    visited[i][j] = True
                    self.flag = True
                    self.node.clear()
                    self.node.append((i, j))
                    dfs(i, j)  # 将与其链接的陆地都标记上 true
                    if self.flag:
                        for node in self.node:
                            board[node[0]][node[1]] = "X"


class SolutionBFS:
    def __init__(self):
        self.node = []
        self.flag = True

    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def bfs(i, j):
            q = deque()
            q.append((i, j))  # 加入队列即标记，防止重复加入，append必定伴随visited
            visited[i][j] = True
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                self.flag = False
            while q:  # bfs从任意一节点（队尾）一直发散，入队出队
                x, y = q.popleft()
                for d in dirs:
                    next_i = x + d[0]
                    next_j = y + d[1]
                    if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
                        continue
                    if not visited[next_i][next_j] and board[next_i][next_j] == "O":
                        q.append((next_i, next_j))
                        self.node.append((next_i, next_j))
                        visited[next_i][next_j] = True
                        if next_i == 0 or next_i == m - 1 or next_j == 0 or next_j == n - 1:
                            self.flag = False

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == "O":
                    self.flag = True
                    self.node.clear()
                    self.node.append((i, j))
                    bfs(i, j)
                    if self.flag:
                        for node in self.node:
                            board[node[0]][node[1]] = "X"


def ACM():
    obj1 = SolutionDFS()
    while True:
        try:
            n = int(input())
            board = []
            for _ in range(n):
                board.append(list(map(int, input().split(" "))))
            outcome = obj1.solve(board)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]

    obj1 = SolutionDFS()
    obj1.solve(board)
    print(board)

    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]

    obj2 = SolutionBFS()
    obj2.solve(board)
    print(board)
