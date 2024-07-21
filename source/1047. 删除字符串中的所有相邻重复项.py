'''
https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if len(stack) == 0 or stack[-1] != item:
                stack.append(item)
            else:
                stack.pop()
        s = "".join(stack)
        return s


if __name__ == "__main__":
    s1 = Solution()
    str = "abbaca"
    x = s1.removeDuplicates(str)
    print(x)
