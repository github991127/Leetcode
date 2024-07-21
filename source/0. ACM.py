class Solution:
    def addSum(self, nums, minus):
        sum = 0
        for n in nums:
            sum += n
        if minus == 0 or minus == '-':
            sum = -sum
        return sum


# 无限输入
obj = Solution()
while True:
    try:
        # nums = input().split(" ") # str字符串list
        nums = list(map(int, input().split(" ")))  # map()通过函数对列表元素分别处理，返回map类型，再转换为list
        minus = nums.pop(0)
        x = obj.addSum(nums, minus)
        print(x)
    except:
        break
'''
# n次输入
obj = Solution()
n = int(input())
for _ in range(n):
    try:
        nums = list(map(int, input().split(" ")))
        minus = nums.pop(0)
        x = obj.addSum(nums, minus)
        print(x)
    except:
        break

# 无限输入2
import sys
obj = Solution()
for line in sys.stdin:
    nums = list(map(int, line.split(" ")))
    minus = nums.pop(0)
    x = obj.addSum(nums, minus)
    print(x)
'''
