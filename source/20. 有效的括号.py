'''
https://leetcode.cn/problems/valid-parentheses/submissions/
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
'''


# 左进栈，右匹配
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False
#         stack = []
#         dic = {'{': '}', '[': ']', '(': ')'}
#         for s_char in s:
#             if s_char in ['(', '[', '{']:
#                 stack.append(s_char)
#             elif len(stack) == 0:
#                 return False
#             elif dic[stack.pop()] != s_char:
#                 return False
#         if stack:
#             return False
#         else:
#             return True

# 右进栈，左匹配
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif len(stack) == 0:
                return False
            elif stack[-1] != item:
                return False
            else:
                stack.pop()
        if stack:
            return False
        else:
            return True


def ACM():
    obj = Solution()
    while True:
        try:
            strS = input()
            x = obj.isValid(strS)
            print(x)
        except:
            break


if __name__ == "__main__":
    obj = Solution()
    strS = ")("
    # stS = "(("
    x = obj.isValid(strS)
    print(x)
    ACM()
