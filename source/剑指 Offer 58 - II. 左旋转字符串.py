'''
https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

'''
from typing import List


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)

        s[0:n] = list(reversed(s[0:n]))
        s[n:] = list(reversed(s[n:]))
        s.reverse()

        s = "".join(s)
        return s


if __name__ == "__main__":
    x = 5
    s = "thesky"

    obj1 = Solution()
    outcome = obj1.reverseLeftWords(s, x)
    print(outcome)
