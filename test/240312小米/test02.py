'''

'''
class Solution:
    def fun(self):
        return 0


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))
            x = obj.fun()
            print(x)
        except:
            break


if __name__ == "__main__":
    obj = Solution()
    x = obj.fun()
    print(x)
    # ACM()
