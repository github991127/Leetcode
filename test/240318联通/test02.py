'''
最大的连续子序列和
'''
from typing import List


class Solution:
    def fun(self, nums):
        result = float("-inf")
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:
                count = 0

        return result


obj = Solution()
while True:
    try:
        nums = list(map(int, input().split(" ")))
        x = obj.fun(nums)
        print(x)
    except:
        break


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))
            x = obj.fun(nums)
            print(x)
        except:
            break


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, 10]
    obj = Solution()
    x = obj.fun(nums)
    print(x)
    ACM()
# 1 2 3 4 5 -1 -2 -3 -4 10
