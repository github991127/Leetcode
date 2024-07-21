'''
https://leetcode.cn/problems/assign-cookies/
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

'''
from typing import List


class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        if not s or s[-1] < g[0]:
            return 0
        index = 0
        for i in range(len(s)):
            if index < len(g) and g[index] <= s[i]:
                index += 1
            if index == len(g):
                break
        return index


if __name__ == "__main__":
    obj1 = Solution()
    g = [2]
    s = [1, 2, 3]
    outcome = obj1.findContentChildren(g, s)
    print(outcome)
