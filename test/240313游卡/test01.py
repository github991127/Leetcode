'''
输入整数num，输出和为num的三个连续的奇数或偶数，不存在返回空列表
'''


class Solution:
    def sumOfThree(self, num: int):
        x = num % 3
        if x == 0:
            y = int(num / 3)
            # y = num / 3
            return [y - 2, y, y + 2]
        else:
            return []


#
#
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
    obj = Solution()
    x = obj.sumOfThree(15)
    print(x)
    # ACM()
