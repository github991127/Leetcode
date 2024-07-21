'''
https://leetcode.cn/problems/ti-huan-kong-ge-lcof/
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
'''
from typing import List


class Solution:
    def replaceSpace(self, s: str) -> str:
        counter = s.count(' ')

        res = list(s)
        # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
        res.extend([' '] * counter * 2)

        # 原始字符串的末尾，拓展后的末尾
        left, right = len(s) - 1, len(res) - 1

        while left >= 0:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                # [right - 2, right), 左闭右开
                res[right - 2: right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)


if __name__ == "__main__":
    s = 'a bc ABC'

    obj1 = Solution()
    outcome = obj1.replaceSpace(s)
    print(outcome)
