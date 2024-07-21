'''
最大路径
'''

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
            if Tree[i]: # 当前节点不为0
                if 2 * i + 1 < len(Tree):  # 左孩子
                    Tree[i].left = Tree[2 * i + 1]
                if 2 * i + 2 < len(Tree):  # 右孩子
                    Tree[i].right = Tree[2 * i + 2]

        return root

    # 二叉树-数组（层序遍历）
    def BinarytreeToNums(self, root: Optional[TreeNode], nonenode='null') -> List[int]:
        if not root:
            return []
        nums = [root.val]

        queue = deque([root])#队列遍历节点
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

        for i in range(len(nums)-1,-1,-1):#移除尾部空节点
            if nums[i]==nonenode:
                nums.pop(i)
            else:
                break

        return nums

    def fun(self,root: Optional[TreeNode], nonenode='null')->List[int]:


        return []



def ACM():
    obj1 = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))

            obj1 = Solution()
            root = obj1.NumsToBinarytree(nums)

            nums = obj1.BinarytreeToNums(root)
            print(nums)

        except:
            break


if __name__ == "__main__":
    # ACM()
    nums = [1, 2, 3, 4, 'null', 'null', 1]

    obj1 = Solution()
    root = obj1.NumsToBinarytree(nums)

    nums = obj1.BinarytreeToNums(root)
    print(nums)
