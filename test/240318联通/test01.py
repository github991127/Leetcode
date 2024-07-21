'''
整数各位乘积
'''


class Solution:
    def fun(self, num: int):
        s = 1
        while num:
            s = num % 10 * s
            num = num // 10
        return s


def ACM():
    obj = Solution()
    while True:
        try:
            nums = int(input())
            x = obj.fun(nums)
            print(x)
        except:
            break


if __name__ == "__main__":
    obj = Solution()
    x = obj.fun(23)
    print(x)
    ACM()
