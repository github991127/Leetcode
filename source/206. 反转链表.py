# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# https://leetcode.cn/problems/reverse-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


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
    head = s.reverseList(L0)
    readlinklist(head)
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        a=ListNode(-1,head)#多余，应创建空指针a = None
        b1=b=head
        while b:
            a1=a#多余。只需要一个临时变量记录
            b1=b
            a=b
            b=b.next
            b1.next=a1
        head.next=None
        return b1
'''
