'''
https://leetcode.cn/problems/reverse-words-in-a-string/
给你一个字符串 s ，请你反转字符串中 单词 的顺序。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
'''
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        # 删除前后空白
        s = s.strip()
        # 反转整个字符串
        s = s[::-1]
        # 将字符串拆分为单词，并反转每个单词
        List = []
        for word in s.split():
            List.append(word[::-1])
        s = ' '.join(List)
        return s


if __name__ == "__main__":
    s = "the sky is blue"

    obj1 = Solution()
    outcome = obj1.reverseWords(s)
    print(outcome)
