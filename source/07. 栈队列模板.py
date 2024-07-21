# 07. 栈队列模板
from typing import List
from collections import deque
import heapq


class MyQueue:  # 单调队列（从大到小）
    def __init__(self):
        self.queue = deque()

    def pop(self, value):  # 出队指定队尾值
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value):  # 清空队尾小元素并入队
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):  # 出队队首值
        return self.queue[0]


class Solution:
    def function(self, nums: List[int], k: int) -> List[int]:
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        pri_que = []  # 小顶堆，弹小留大。若要实现弹大留小，将数据取负数后push到堆中，pop的时候再取负数即可
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))  # 元组按靠前元素freq排序
            if len(pri_que) > k:  # 保证堆最大为K，保留前k大的
                heapq.heappop(pri_que)

        # 从大到小输出前K个，因为小顶堆先弹小，所以倒序来输出
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))
            target = nums.pop(0)
            x = obj.function(nums, target)
            print(x)
        except:
            break


if __name__ == "__main__":
    nums = [3, 3, 5, 5, 1]
    target = 2

    obj = Solution()
    x = obj.function(nums, target)
    print(x)

    # ACM()
