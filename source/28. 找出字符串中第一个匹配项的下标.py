'''
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
'''
from typing import List


class Solution:
    def findNext(self, needle:str, next: List[int]):
        next[0] = j = -1
        for i in range(1, len(next)):
            while needle[j + 1] != needle[i] and j >= 0:
                j = next[j]
            if needle[j + 1] == needle[i]:
                j += 1
            next[i] = j
        return

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return -1
        next = [0] * len(needle)
        self.findNext(needle, next)
        j = -1

        for i in range(len(haystack)):
            while needle[j + 1] != haystack[i] and j >= 0:
                j = next[j]
            if needle[j + 1] == haystack[i]:
                j += 1
            if j == len(needle) - 1:
                return i - j

        return -1

if __name__ == '__main__':
    haystack = "abbabbabc"
    needle = "abbabc"

    obj1 = Solution()
    outcome = obj1.strStr(haystack,needle)
    print(outcome)
