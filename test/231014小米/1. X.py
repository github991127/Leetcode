'''
输入nums, m, n，输出3*3矩阵中包含xiaomi的子矩阵数
'''
from typing import List


class Solution:

    def solve(self, nums, m, n) -> int:
        count = 0
        for i in range(0, m - 3 + 1):
            for j in range(0, n - 3 + 1):
                xiaomi = {'x': 0, 'i': 0, 'a': 0, 'o': 0, 'm': 0}
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if nums[x][y] in xiaomi:
                            xiaomi[nums[x][y]] += 1
                if xiaomi['x'] >= 1 and xiaomi['i'] >= 2 and xiaomi['a'] >= 1 and xiaomi['o'] >= 1 and xiaomi['m'] >= 1:
                    count += 1
        return count


def ACM():
    obj1 = Solution()
    while True:
        try:
            m, n = map(int, input().split(' '))
            nums = []
            for _ in range(m):
                x = input()
                list = []
                for num in x:
                    list.append(num)
                nums.append(list)
            outcome = obj1.solve(nums, m, n)
            print(outcome)
            return
        except:
            break


if __name__ == "__main__":
    ACM()
    nums = [
        ['x', 'i', 'a', 'q'],
        ['o', 'i', 'm', 'e'],
        ['x', 'a', 'i', 'c'],
        ['c', 'a', 'd', 'f']
    ]
    # m, n = 4, 4
    # obj1 = Solution()
    # outcome = obj1.solve(nums, m, n)
    # print(outcome)
