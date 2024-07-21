'''
输入非负整数数组nums和加1次数k，给nums中任意个数分配加1次数共计k次，使得数组乘积最大，输出乘积
'''


class Solution:
    def maximumProduct(self, nums, k: int) -> int:
        nums.sort()
        l = len(nums)
        for _ in range(k):
            i = 0
            nums[0] += 1
            for j in range(i + 1, l):
                if nums[j] >= nums[i]:
                    nums[j - 1], nums[i] = nums[i], nums[j - 1]
                    break
                if j == l - 1:
                    nums[j], nums[i] = nums[i], nums[j]
        # print(nums)
        x = 1
        for i in nums:
            x = (x * i) % (1e9 + 7)
        x = int(x)
        return x


# def ACM():
#     obj = Solution()
#     while True:
#         try:
#             nums = list(map(int, input().split(" ")))
#             x = obj.fun()
#             print(x)
#         except:
#             break

if __name__ == "__main__":
    nums = [6, 3, 3, 3]
    k = 3
    obj = Solution()
    x = obj.maximumProduct(nums, k)
    print(x)
    # ACM()
