'''
https://leetcode.cn/problems/number-of-enclaves/description/
给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
'''
from typing import List
from collections import deque


class SolutionDFS:
    def __init__(self):
        self.count = 0
        self.flag = True

    def numEnclaves(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        result = 0

        def dfs(x, y):  # 内方法省去了变量传递
            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                self.flag = False
            for d in dirs:  # dfs从任意一方向（四方向之一）一直递归
                nextx = x + d[0]
                nexty = y + d[1]
                if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:  # 越界了，直接跳过
                    continue
                if not visited[nextx][nexty] and grid[nextx][nexty] == 1:  # 没有访问过的同时是陆地的
                    visited[nextx][nexty] = True
                    self.count += 1
                    dfs(nextx, nexty)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    self.count = 1  # 遇到没访问过的陆地，+1
                    self.flag = True
                    dfs(i, j)  # 将与其链接的陆地都标记上 true
                    if self.flag:
                        result += self.count

        return result


class SolutionBFS:
    def __init__(self):
        self.count = 0
        self.flag = 0

    def numEnclaves(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        result = 0

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
                    if not visited[next_i][next_j] and grid[next_i][next_j] == 1:
                        q.append((next_i, next_j))
                        visited[next_i][next_j] = True
                        if next_i == 0 or next_i == m - 1 or next_j == 0 or next_j == n - 1:
                            self.flag = False
                        self.count += 1

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    self.count = 1
                    self.flag = True
                    bfs(i, j)
                    if self.flag:
                        result += self.count
        return result


def ACM():
    obj1 = SolutionDFS()
    while True:
        try:
            n = int(input())
            grid = []
            for _ in range(n):
                grid.append(list(map(int, input().split(" "))))
            outcome = obj1.numEnclaves(grid)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]

    obj1 = SolutionDFS()
    outcome = obj1.numEnclaves(grid)
    print(outcome)

    obj2 = SolutionBFS()
    outcome = obj2.numEnclaves(grid)
    print(outcome)
