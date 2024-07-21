'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
'''

#官解：基于快速排序的快速选择法
import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, nums, left, right, index):
        partitionIndex = self.partition(nums, left, right)
        if partitionIndex == index:#partitionIndex（pivot的索引）即已确定的第k大的数。否则只用查找左子序列或右子序列
            return nums[partitionIndex]
        elif partitionIndex > index:
            return self.quickSelect(nums, left, partitionIndex - 1, index)
        else:
            return self.quickSelect(nums, partitionIndex + 1, right, index)

    def partition(self, nums, left, right):
        pivot = random.randint(left, right)  # 随机选择pivot，属于[left, right]，避免最坏情况
        nums[pivot], nums[left] = nums[left], nums[pivot]  # 交换pivot到最左边，方便与数组所有元素比较
        index = left + 1
        # 除了left外，每个数和left比较，小的靠左，大的靠右，然后将left放到中间
        for i in range(index, right + 1):
            if nums[i] < nums[left]:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        # swap index-1 and left
        nums[left], nums[index - 1] = nums[index - 1], nums[left]# 和比left小的所有数的最靠右的数交换，因此交换后left左边全比left小
        return index - 1

obj1=Solution()
List=[5,5,3,4]
k=2
outcome = obj1.findKthLargest(List,k)
print(outcome)
'''
#自解：创建最小堆
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums)>k: heapq.heappop(nums)
        return heapq.heappop(nums)
'''
