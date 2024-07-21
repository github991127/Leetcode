'''
https://leetcode.cn/problems/ones-and-zeroes/
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
'''
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 排除 Corner Case

        # 创建 dp table
        dp = [[0] * (m + 1) for _ in range(n + 1)]  # 1n行,0m列

        # 初始化 dp 数组

        # 遍历顺序
        for str in strs:
            zero, one = str.count('0'), str.count('1')
            for i in range(n, one - 1, -1):
                for j in range(m, zero - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - one][j - zero])  # 最多有 m个0和n个1 ,因此只要有剩余空间就可以+1物品

        # 返回答案
        # print(dp)
        return dp[-1][-1]


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    obj1 = Solution()
    outcome = obj1.findMaxForm(strs, m, n)
    print(outcome)
