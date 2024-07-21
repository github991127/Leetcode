# 09. 回溯模板
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtracking(n, k, 1)
        return self.result

    def backtracking(self, n, k, startIndex):
        if len(self.path) == k:
            self.result.append(self.path[:])  # path为浅复制，必须要重新用一个列表path[:]，否则后续path改变，result会随之变化
            return
        # for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
        for i in range(startIndex, n + 1):
            if startIndex + (k - len(self.path)) > n + 1:  # 优化的地方从for范围中剥离出来写成if
                return
            self.path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1)
            self.path.pop()  # 回溯，撤销处理的节点


def ACM():
    obj = Solution()
    while True:
        try:
            n, k = list(map(int, input().split(" ")))
            x = obj.combine(n, k)
            print(x)
        except:
            break


if __name__ == "__main__":
    n = 4
    k = 3

    obj = Solution()
    x = obj.combine(n, k)
    print(x)

    # ACM()
