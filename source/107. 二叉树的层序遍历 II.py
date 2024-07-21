'''
https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
'''
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归前序
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = deque()
        d.append(root)
        result = []
        while d:
            level = []
            for _ in range(len(d)):
                node = d.popleft()
                level.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            result.append(level)
        result.reverse()
        return result


if __name__ == "__main__":
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)

    obj1 = Solution()
    outcome = obj1.levelOrderBottom(root)
    print(outcome)
