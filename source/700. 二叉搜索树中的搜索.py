'''
https://leetcode.cn/problems/search-in-a-binary-search-tree/
给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None


if __name__ == "__main__":
    left = TreeNode(1)
    right = TreeNode(5)
    root = TreeNode(3, left, right)  # 二叉搜索树（BST）左小右大

    obj1 = Solution()
    outcome = obj1.searchBST(root, 5)
    print(outcome)
