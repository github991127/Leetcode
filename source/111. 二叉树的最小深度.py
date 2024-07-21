'''
https://leetcode.cn/problems/minimum-depth-of-binary-tree/
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
'''
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        deep = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if not cur.left and not cur.right:
                    return deep + 1
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            deep += 1
        return deep


if __name__ == "__main__":
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left)

    obj1 = Solution()
    outcome = obj1.minDepth(root)
    print(outcome)
