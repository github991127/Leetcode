# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy_head = ListNode(0, head)
        slow = fast = dummy_head
        for i in range(n):
            fast = fast.next
            if fast == None: return dummy_head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
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
    index = 1
    s = Solution()
    head = s.removeNthFromEnd(L0, index)
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
