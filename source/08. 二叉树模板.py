# 08. 二叉树模板
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 数组-二叉树
    def NumsToBinarytree(self, nums: [], nonenode='null') -> TreeNode:
        if not nums:
            return None
        root = TreeNode()
        Tree = []

        # 将数组元素全部转化为树节点，首元素为root
        for i in range(len(nums)):
            if nums[i] != nonenode:
                node = TreeNode(nums[i])
            else:
                node = None
            Tree.append(node)
            if i == 0:
                root = node

        for i in range(len(Tree)):
            if Tree[i]:  # 当前节点不为None
                if 2 * i + 1 < len(Tree):  # 左孩子
                    Tree[i].left = Tree[2 * i + 1]
                if 2 * i + 2 < len(Tree):  # 右孩子
                    Tree[i].right = Tree[2 * i + 2]

        return root

    # 二叉树-数组（层序遍历）
    def BinarytreeToNums(self, root: TreeNode, nonenode='null') -> List[int]:
        if not root:
            return []
        nums = [root.val]

        queue = deque([root])  # 队列遍历节点
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

        for i in range(len(nums) - 1, -1, -1):  # 移除尾部空节点
            if nums[i] == nonenode:
                nums.pop(i)
            else:
                break

        return nums

    # 前序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 递归法，三种方法相同
        # left = self.preorderTraversal(root.left)
        # right = self.preorderTraversal(root.right)
        # return [root.val] + left + right

        stack = [root]  # 栈遍历节点
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:  # 右孩子先入栈
                stack.append(node.right)
            if node.left:  # 左孩子后入栈
                stack.append(node.left)
        return result

    # 中序遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []  # 不能提前将root结点加入stack中
        result = []
        cur = root

        while cur or stack:
            if cur:  # 先迭代访问最底层的左子树结点
                stack.append(cur)
                cur = cur.left
            else:  # 到达后处理栈顶结点
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right
        return result

    # 后序遍历(前序翻转)
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:  # 左孩子先入栈
                stack.append(node.left)
            if node.right:  # 右孩子后入栈
                stack.append(node.right)

        return result[::-1]  # 中右左-左右中


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))

            obj = Solution()
            root = obj.NumsToBinarytree(nums)

            nums = obj.BinarytreeToNums(root)
            print(nums)

        except:
            break


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 'null', 'null', 7, 8]

    obj = Solution()
    root = obj.NumsToBinarytree(nums)

    nums = obj.BinarytreeToNums(root)
    print(nums)

    print(obj.preorderTraversal(root))
    print(obj.inorderTraversal(root))
    print(obj.postorderTraversal(root))

    # ACM()
