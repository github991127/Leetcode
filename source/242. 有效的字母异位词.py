'''
https://leetcode.cn/problems/valid-anagram/
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
'''
from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True

def ACM():
    obj = Solution()
    while True:
        try:
            s,t=input().split(' ')
            x = obj.isAnagram(s, t)
            print(x)
        except:
            break
        
    
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    obj = Solution()
    x = obj.isAnagram(s,t)
    print(x)
    ACM()
