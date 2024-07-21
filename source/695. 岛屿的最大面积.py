'''
https://leetcode.cn/problems/max-area-of-island/description/
岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
岛屿的面积是岛上值为 1 的单元格的数目。
计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
'''
from typing import List
from collections import deque


class SolutionDFS:
    def __init__(self):
        self.count = 0

    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        result = 0

        def dfs(x, y):  # 内方法省去了变量传递
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
                    dfs(i, j)  # 将与其链接的陆地都标记上 true
                    result = max(result, self.count)

        return result


class SolutionBFS:
    def __init__(self):
        self.count = 0

    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        result = 0

        def bfs(i, j):
            q = deque()
            q.append((i, j))  # 加入队列即标记，防止重复加入，append必定伴随visited
            visited[i][j] = True
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
                        self.count += 1

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    self.count = 1
                    bfs(i, j)
                    result = max(result, self.count)
        return result


def ACM():
    obj1 = SolutionDFS()
    while True:
        try:
            n = int(input())
            grid = []
            for _ in range(n):
                grid.append(list(map(int, input().split(" "))))
            outcome = obj1.maxAreaOfIsland(grid)
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

    # obj1 = SolutionDFS()
    # outcome = obj1.maxAreaOfIsland(grid)
    # print(outcome)

    obj2 = SolutionBFS()
    outcome = obj2.maxAreaOfIsland(grid)
    print(outcome)
