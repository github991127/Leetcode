'''
https://leetcode.cn/problems/repeated-substring-pattern/
给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
'''
from typing import List


class Solution:
    def getnext(self, needle, next):
        j = 0
        next[0] = 0
        for i in range(1, len(needle)):
            while (j > 0 and needle[i] != needle[j]):
                j = next[j - 1]  # ij不等，对比上一位next对应的下标j
            if (needle[i] == needle[j]):
                j += 1
            next[i] = j
        return

    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False
        next = [0] * len(s)
        self.getnext(s, next)
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        return False


if __name__ == "__main__":
    haystack = "sosossoo"
    # haystack = "sossossos"

    obj1 = Solution()
    outcome = obj1.repeatedSubstringPattern(haystack)
    print(outcome)
