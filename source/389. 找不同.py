'''
给定两个字符串 s 和 t ，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict = {}
        for s1 in s:
            if s1 not in dict:dict[s1] = 0
            dict[s1] += 1
        for t1 in t:
            if t1 not in dict:return t1
            else:dict[t1] -= 1
            if dict[t1] < 0:return t1

obj1=Solution()
s='abcdd'
t='cbadda'
outcome = obj1.findTheDifference(s,t)
print(outcome)
'''
#自解:创建两个字典，比较值大小。改为创建一个字典，通过+1-1判断值的正负
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1 = {}
        dict2 = {}
        for s1 in s:
            if s1 not in dict1:dict1[s1] = 0
            dict1[s1] += 1
        for t1 in t:
            if t1 not in dict2:dict2[t1] = 0
            dict2[t1] += 1
            if t1 not in dict1 or dict2[t1]>dict1[t1]:
                return t1
#官解2异或：两个字符串合起来，多余的字符出现奇数次，偶数次的字符计算后为0
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in s+t:
            res ^= ord(i)
        return chr(res)
    
#ASCII运算，t-s即为多余字符的ASCII
'''