# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
# https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        fastA = slowA = ListNode(0,headA)
        fastB = slowB = ListNode(0,headB)
        iA=jB=0
        while fastA:
            fastA=fastA.next
            iA+=1
        while fastB:
            fastB=fastB.next
            jB+=1
        if iA>jB:
            for i in range(iA-jB):
                slowA=slowA.next
        else:
            for i in range(jB-iA):
                slowB=slowB.next

        while slowA and slowB:
            if slowA.next==slowB.next:
                return slowA.next
            slowA=slowA.next
            slowB=slowB.next
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
    return L0


def readlinklist(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    L0 = linklist()
    index = 1
    s = Solution()
    head = s.getIntersectionNode(L0, L0)
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
