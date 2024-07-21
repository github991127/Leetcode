'''
https://leetcode.cn/problems/invert-binary-tree/
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        d = deque()
        d.append(root)
        while d:
            node = d.popleft()
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
            node.left, node.right = node.right, node.left
        return root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)

    obj1 = Solution()
    outcome = obj1.invertTree(root)
    print(outcome)
