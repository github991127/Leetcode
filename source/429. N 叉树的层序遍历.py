'''
https://leetcode.cn/problems/n-ary-tree-level-order-traversal/
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
'''
from typing import List, Optional
from collections import deque


# Definition for a Node.
class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        if child:
                            queue.append(child)
            result.append(level)
        return result


if __name__ == "__main__":
    left = TreeNode(2)
    right = TreeNode(3)
    children = [left, right]
    root = TreeNode(1, children)

    obj1 = Solution()
    outcome = obj1.levelOrder(root)
    print(outcome)
