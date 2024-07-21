# 05. 字符串模板
from typing import List


class Solution:
    def function(self, nums: List[int], target: int) -> int:
        nums = nums[::-1]  # 双重翻转-整体和局部
        return 0

    # KMP
    def getNext(self, next, s):
        j = -1
        next[0] = j
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j + 1]:
                j = next[j]
            if s[i] == s[j + 1]:
                j += 1
            next[i] = j

    def strStr(self, haystack: str, needle: str) -> int:  # KMP
        if not needle:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j + 1]:
                j = next[j]
            if haystack[i] == needle[j + 1]:
                j += 1
            if j == len(needle) - 1:
                return i - j
        return -1


def ACM():
    obj = Solution()
    while True:
        try:
            haystack, needle = input().split(' ')
            x = obj.strStr(haystack, needle)
            print(x)
        except:
            break


if __name__ == "__main__":
    haystack = "abbabbabc"
    needle = "abbabc"
    obj = Solution()
    x = obj.strStr(haystack, needle)
    print(x)

    # ACM()
    # abbabbabc abbabc
