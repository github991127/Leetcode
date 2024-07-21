'''
https://leetcode.cn/problems/all-paths-from-source-to-target/description/
给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。
'''
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.path = [0]

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph: return []

        self.dfs(graph, 0)
        return self.result

    def dfs(self, graph, root: int):
        if root == len(graph) - 1:  # 成功找到一条路径时
            # ***Python的list是mutable类型***
            # ***回溯中必须使用Deep Copy***
            self.result.append(self.path[:])
            return

        for node in graph[root]:  # 遍历节点n的所有后序节点
            self.path.append(node)
            self.dfs(graph, node)
            self.path.pop()  # 回溯


def ACM():
    obj1 = Solution()
    while True:
        try:
            n = int(input())
            graph = []
            for _ in range(n):
                node = list(map(int, input().split(" ")))
                graph.append(node)
            outcome = obj1.allPathsSourceTarget(graph)
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()
    graph = [[1, 2], [3], [3], []]

    obj1 = Solution()
    outcome = obj1.allPathsSourceTarget(graph)
    print(outcome)
