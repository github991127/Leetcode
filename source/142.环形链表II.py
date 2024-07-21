# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# https://leetcode.cn/problems/linked-list-cycle-ii/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        slow = slow2 = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while (slow != slow2):
                    slow = slow.next
                    slow2 = slow2.next
                return slow
        return None


def linklist():
    # linklistname = ['None', 'L5', 'L4', 'L3', 'L2', 'L1', 'L0']
    # linklistval = [1, 4, 5, 1, 2, 3]
    L5 = ListNode(3, None)
    L4 = ListNode(2, L5)
    L3 = ListNode(1, L4)
    L2 = ListNode(5, L3)
    L1 = ListNode(4, L2)
    L0 = ListNode(1, L1)
    L5.next=L2
    return L0


def readlinklist(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    L0 = linklist()
    index = 1
    s = Solution()
    head = s.detectCycle(L0)
    print(head.val)
    # readlinklist(head)
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
