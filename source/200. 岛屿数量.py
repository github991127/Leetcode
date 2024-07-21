'''
https://leetcode.cn/problems/number-of-islands/description/
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
'''
from typing import List
from collections import deque


class SolutionDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
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
                if not visited[nextx][nexty] and grid[nextx][nexty] == '1':  # 没有访问过的同时是陆地的
                    visited[nextx][nexty] = True
                    dfs(nextx, nexty)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    visited[i][j] = True
                    result += 1  # 遇到没访问过的陆地，+1
                    dfs(i, j)  # 将与其链接的陆地都标记上 true

        return result


class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
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
                    if not visited[next_i][next_j] and grid[next_i][next_j] == '1':
                        q.append((next_i, next_j))
                        visited[next_i][next_j] = True

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    result += 1
                    bfs(i, j)
        return result


def ACM():
    obj1 = Solution()
    while True:
        try:
            n = int(input())
            grid = []
            for _ in range(n):
                grid.append(input().split(" "))
            outcome = obj1.numIslands(grid)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    obj1 = SolutionDFS()
    outcome = obj1.numIslands(grid)
    print(outcome)

    obj2 = SolutionBFS()
    outcome = obj2.numIslands(grid)
    print(outcome)
