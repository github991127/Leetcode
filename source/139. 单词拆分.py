'''
https://leetcode.cn/problems/climbing-stairs/
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 排除 Corner Case

        # 创建 dp table
        dp = [False] * (len(s) + 1)

        # 初始化 dp 数组
        dp[0] = True

        # 遍历顺序
        for j in range(1, len(s) + 1):
            for i in wordDict:
                l = len(i)
                if j >= l and s[j - l:j] == i:  # s的索引0对应dp的索引1
                    dp[j] = dp[j] or dp[j - l]

        # 返回答案
        return dp[-1]


if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]

    obj1 = Solution()
    outcome = obj1.wordBreak(s, wordDict)
    print(outcome)
