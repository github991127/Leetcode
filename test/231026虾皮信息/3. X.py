'''
将字符串n位之后前移
'''
from typing import List


class Solution:
    def moveSubStr(self, str, n):
        res = []
        for i in range(n - 1, len(str)):
            res.append(str[i])
        for i in range(n - 1):
            res.append(str[i])
        x=''.join(res)
        return x
        # return str[n - 1:len(str)] + str[0:n - 1]

        # return str[n - 1:] + str[:n - 1]


def ACM():
    obj1 = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))
            outcome = obj1.fun()
            print(outcome)
        except:
            break


if __name__ == "__main__":
    # ACM()
    str = "abcdefg"
    n = 3

    obj1 = Solution()
    outcome = obj1.moveSubStr(str, n)
    print(outcome)
