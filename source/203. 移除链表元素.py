'''
https://leetcode.cn/problems/remove-linked-list-elements/
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
'''


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next=head)

        # 遍历列表并删除值为val的节点
        cur = dummy_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_head.next

    def numsToListNode(self, nums):
        dummy = ListNode(None)
        root = dummy
        for i in range(len(nums)):
            node = ListNode(nums[i])
            root.next = node
            root = root.next
        return dummy.next

    def listNodeToNums(self, root):
        nums = []
        while root:
            nums.append(root.val)
            root = root.next
        return nums


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))  # 第一个数为val，后面的数为nums
            val = nums.pop(0)
            root = obj.numsToListNode(nums)

            x = obj.removeElements(root, val)

            nums = obj.listNodeToNums(x)
            print(nums)
        except:
            break


if __name__ == "__main__":
    nums = [1, 0, 0, 1, 1]

    obj = Solution()
    root = obj.numsToListNode(nums)

    val = 1
    x = obj.removeElements(root, val)
    print(x)

    nums = obj.listNodeToNums(x)
    print(nums)

    # ACM()
