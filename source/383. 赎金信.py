'''
https://leetcode.cn/problems/ransom-note/
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
'''
from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        dict = {}
        for m in magazine:
            dict[m] = dict.get(m, 0) + 1
        for r in ransomNote:
            dict[r] = dict.get(r, 0) - 1
            if dict[r] < 0:
                return False
        return True


if __name__ == "__main__":
    ransomNote = 'abbcde'
    magazine = 'abcdefgb'
    obj1 = Solution()
    outcome = obj1.canConstruct(ransomNote, magazine)
    print(outcome)
