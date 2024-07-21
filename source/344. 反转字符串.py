'''
https://leetcode.cn/problems/reverse-string/
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

'''
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while (left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(' ')))
            x = obj.reverseString(nums)
            print(nums)
        except:
            break


if __name__ == "__main__":
    nums = [1, 2, 3, 5, 8]

    obj = Solution()
    x = obj.reverseString(nums)
    print(nums)
    ACM()
