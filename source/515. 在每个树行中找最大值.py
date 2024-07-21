'''
https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
'''
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            maxnode = float('-inf')
            for _ in range(len(queue)):
                cur = queue.popleft()
                maxnode = max(maxnode, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(maxnode)
        return result


if __name__ == "__main__":
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)

    obj1 = Solution()
    outcome = obj1.largestValues(root)
    print(outcome)
