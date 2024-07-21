# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# https://leetcode.cn/problems/design-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index + 1 > self.size or index < 0:  # index从0开始
            return -1
        node = self.dummy_head
        for i in range(index + 1):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.dummy_head.next)
        self.dummy_head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = self.dummy_head
        while node.next:
            node = node.next
        node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index < 0:
            self.addAtHead(val)
        else:
            node = self.dummy_head
            for i in range(index):
                node = node.next
            newnode = ListNode(val, node.next)
            self.node.next = newnode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > -1 and index < self.size:
            node = self.dummy_head
            for i in range(index):
                node = node.next
            node.next = node.next.next
            self.size -= 1


if __name__ == "__main__":
    index = val = 3

    obj = MyLinkedList()
    param_1 = obj.get(index)
    obj.addAtHead(val)
    obj.addAtTail(val)
    obj.addAtIndex(index, val)
    obj.deleteAtIndex(index)

'''
#官解：无头结点，先判断出第一个不删除的结点，若为空返回，不为空正式开始遍历判断next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            # 让自head起第一个值不为val的节点作为头节点
            # 退出while循环时，有两种情况
            # 1 head为空(即链表左右节点值均为val，则进入if并return
            # 2 找到了第一个值不为val的节点(是真正的头节点)，那么之后就开始对该节点之后的非头节点的元素进行遍历处理
            head = head.next
        if head is None:
            return head
        node = head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head
'''
