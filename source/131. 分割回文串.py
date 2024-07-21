'''
https://leetcode.cn/problems/palindrome-partitioning/
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        i: int = start
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        self.backtracking(s, start=0)
        return self.result

    def backtracking(self, s, start):
        if start == len(s):
            self.result.append(self.path[:])
        for index in range(start, len(s)):
            if self.is_palindrome(s, start, index):
                self.path.append(s[start:index + 1])
                self.backtracking(s, index + 1)
                self.path.pop()


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.partition("aab")
    print(outcome)
