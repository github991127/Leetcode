# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# https://leetcode.cn/problems/swap-nodes-in-pairs/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        cur = dummy_head
        while cur.next != None and cur.next.next != None:
            temp1 = cur.next
            cur.next = cur.next.next
            temp2 = cur.next.next
            cur.next.next = temp1
            temp1.next = temp2
            cur = temp1
        return dummy_head.next


def linklist():
    # linklistname = ['None', 'L5', 'L4', 'L3', 'L2', 'L1', 'L0']
    # linklistval = [1, 4, 5, 1, 2, 3]
    L5 = ListNode(3, None)
    L4 = ListNode(2, L5)
    L3 = ListNode(1, L4)
    L2 = ListNode(5, L3)
    L1 = ListNode(4, L2)
    L0 = ListNode(1, L1)
    return L0


def readlinklist(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    L0 = linklist()
    val = 0
    s = Solution()
    head = s.swapPairs(L0)
    readlinklist(head)
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = head
        cur = head.next
        if cur:
            head = cur
        while cur:
            temp = cur.next
            cur.next = pre
            pre.next = temp
            if temp == None: break
            pre = temp
            cur = temp.next  # 错误，第二组交换后，第一组的指针没有指向第二组的首节点
        return head
'''
