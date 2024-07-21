'''
输入可重复的0-9数组digits，输出所有合法的排列三位数
'''

from typing import List


class Solution:

    def findMyNumbers(self, digits: List[int]) -> List[int]:
        # def findMyNumbers(self, digits):
        digits.sort()
        self.backtracking(digits, [False] * len(digits))
        return self.result

    def __init__(self):
        self.path = []
        self.result = []
        self.temp = 0

    def backtracking(self, digits, used):
        if len(self.path) == 3:
            # if self.path[-1] % 2 == 1 and self.path[0] != 0:
            if self.path[-1] % 2 == 1:
                x = 100 * self.path[0] + 10 * self.path[1] + self.path[2]
                self.result.append(x)
            return
        for i in range(len(digits)):
            if (i > 0 and digits[i] == digits[i - 1] and not used[i - 1]) or used[i]:
                continue
            if (i == 0 and len(self.path) == 0):
                continue
            used[i] = True
            self.path.append(digits[i])
            self.backtracking(digits, used)
            self.path.pop()
            used[i] = False


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
    # digits = [1, 3, 4, 4]
    digits = [1, 3, 4, 4, 0]
    obj = Solution()
    x = obj.findMyNumbers(digits)
    print(x)
    # ACM()
