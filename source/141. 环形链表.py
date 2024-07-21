'''
给你一个链表的头节点 head ，判断链表中是否有环。
'''
from typing import Optional
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:return False
        slow=fast=head
        while(fast.next and fast.next.next):#先检测and语句1，若通过再检测and语句2，语句2不会非法
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
        
obj1=Solution()
List=[1,2,3,2]
Node3=ListNode(List[3])
Node2=ListNode(List[2],Node3)
Node1=ListNode(List[1],Node2)
Node0=ListNode(List[0],Node1)
#Node3.next=Node0

outcome = obj1.hasCycle(Node0)
print(outcome)