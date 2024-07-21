'''
https://leetcode.cn/problems/symmetric-tree/
给你一个二叉树的根节点 root ， 检查它是否轴对称。
'''
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            level = []
            l = len(queue)
            for _ in range(l):
                cur = queue.popleft()
                if cur == None:
                    level.append(cur)
                    continue
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                else:
                    queue.append(None)
                if cur.right:
                    queue.append(cur.right)
                else:
                    queue.append(None)
            if level != level[::-1]:
                return False
        return True


if __name__ == "__main__":
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)

    obj1 = Solution()
    outcome = obj1.isSymmetric(root)
    print(outcome)
