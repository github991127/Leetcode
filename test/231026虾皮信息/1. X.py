'''

'''
from typing import List


class Solution:
    def fun(self) -> int:
        return 0


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

    obj1 = Solution()
    outcome = obj1.fun()
    print(outcome)
