'''
https://leetcode.cn/problems/happy-number/
编写一个算法来判断一个数 n 是不是快乐数。「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
'''
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()  # 不重复集合
        while n not in record:
            record.add(n)
            sum = 0
            n_str = str(n)
            for i in n_str:
                sum += int(i) ** 2
            if sum == 1:
                return True
            else:
                n = sum
        return False


if __name__ == "__main__":
    x = 2

    obj1 = Solution()
    outcome = obj1.isHappy(x)
    print(outcome)
