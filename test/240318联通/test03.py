'''
第k大的数
'''
from typing import List
import heapq


class Solution:
    def fun(self, nums, k):
        priQue = []
        for n in nums:
            heapq.heappush(priQue, n)
            if len(priQue) > k:
                heapq.heappop(priQue)
        # result = [0] * k
        # for i in range(k - 1, -1, -1):
        #     result[i] = heapq.heappop(priQue)
        # return result[-1]
        return heapq.heappop(priQue)


obj = Solution()
while True:
    try:
        nums = list(map(int, input().split(" ")))
        k = int(input())
        x = obj.fun(nums, k)
        print(x)
    except:
        break


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))
            k = int(input())
            x = obj.fun(nums, k)
            print(x)
        except:
            break


if __name__ == "__main__":
    nums = [2, 7, 8, 3, 5, 6, 1, 4, 9, 10]
    k = 5
    obj = Solution()
    x = obj.fun(nums, k)
    print(x)
    ACM()

# 2 7 8 3 5 6 1 4 9 10
# 5
