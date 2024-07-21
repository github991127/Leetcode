# 03. 链表模板
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def function(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(next=head)  # 创建虚拟头部节点以简化删除过程

        cur = dummy_head
        while cur.next:  # 遍历链表
            cur = cur.next

        temp = cur.next  # 要改变cur->next的指向之前，请用temp保存
        slow = fast = cur  # 快慢指针：需要固定间距N，fast和slow先达到间距N再同时移动。快慢指针可分析比例列方程

        return dummy_head.next

    def NumsToListNode(self, nums):
        dummy = ListNode(None)
        root = dummy
        for i in range(len(nums)):
            node = ListNode(nums[i])
            root.next = node
            root = root.next
        return dummy.next

    def ListNodeToNums(self, root):
        nums = []
        while root:
            nums.append(root.val)
            root = root.next
        return nums


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))
            val = nums.pop(0)

            obj = Solution()
            root = obj.NumsToListNode(nums)

            x = obj.function(root, val)
            # print(x)

            nums = obj.ListNodeToNums(x)
            print(nums)
        except:
            break


if __name__ == "__main__":
    nums = [1, 0, 0, 1, 1]
    val = 1

    obj = Solution()
    root = obj.NumsToListNode(nums)

    x = obj.function(root, val)
    print(x)

    nums = obj.ListNodeToNums(x)
    print(nums)

    # ACM()
