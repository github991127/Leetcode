'''
https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/
给定一个二叉树：
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。
初始状态下，所有 next 指针都被设置为 NULL 。
'''
from typing import List,Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([root])
        while queue:
            l = len(queue)
            for i in range(l):
                cur = queue.popleft()
                if i == l - 1:
                    cur.next = None
                else:
                    cur.next = queue[0]
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

        
if __name__ == "__main__":
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)

    obj1 = Solution()
    outcome = obj1.connect(root)
    print(outcome)