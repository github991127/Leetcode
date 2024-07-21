'''
https://leetcode.cn/problems/binary-tree-preorder-traversal/
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
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
    def preorderTraversal0(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right

    # 迭代前序
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 根结点为空则返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 左孩子后入栈
            if node.left:
                stack.append(node.left)
        return result

    # 迭代中序
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]

    # 迭代后序
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        result.reverse()
        return result

    # 根据数组构建二叉树
    def NumsToBinarytree(self, nums: [], nonenode='null') -> TreeNode:
        if not nums:
            return None
        # 用于存放构建好的节点
        root = TreeNode(-1)
        Tree = []
        # 将数组元素全部转化为树节点
        for i in range(len(nums)):
            if nums[i] != nonenode:
                node = TreeNode(nums[i])
            else:
                node = None
            Tree.append(node)
            if i == 0:
                root = node
        # 直接判断2*i+2<len(Tree)会漏掉2*i+1=len(Tree)-1的情况
        for i in range(len(Tree)):
            if Tree[i] and 2 * i + 1 < len(Tree):
                Tree[i].left = Tree[2 * i + 1]
                if 2 * i + 2 < len(Tree):
                    Tree[i].right = Tree[2 * i + 2]
        return root

    def BinarytreeToNums(self, root: Optional[TreeNode], nonenode='null') -> List[int]:
        if not root:
            return None
        nums = [root.val]
        queue = deque([root])
        while queue:
            l = len(queue)
            for _ in range(l):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    nums.append(cur.left.val)
                else:
                    nums.append(nonenode)
                if cur.right:
                    queue.append(cur.right)
                    nums.append(cur.right.val)
                else:
                    nums.append(nonenode)
        return nums


if __name__ == "__main__":
    test_tree = [0, 1, 2, 'null', 'null', 1, 1]

    obj1 = Solution()
    root = obj1.NumsToBinarytree(test_tree)

    # outcome = obj1.preorderTraversal0(root)
    # outcome = obj1.postorderTraversal(root)
    # outcome = obj1.inorderTraversal(root)
    outcome = obj1.preorderTraversal(root)
    print(outcome)

    nums = obj1.BinarytreeToNums(root)
    print(nums)
