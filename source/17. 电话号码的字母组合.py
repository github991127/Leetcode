'''
https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
from typing import List


class Solution:
    def __init__(self):
        self.letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.path = ""
        self.result = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        for d in digits:
            if int(d) not in range(2, 10):
                return "error"
        self.backtracking(0, digits)
        return self.result

    def backtracking(self, index, digits):
        if index == len(digits):
            self.result.append(self.path)  # path添加到result后，后续path变化不影响result
            return
        else:
            letterStr = self.letterMap[int(digits[index])]
        for letter in letterStr:
            self.path += letter
            self.backtracking(index + 1, digits)
            self.path = self.path[:-1]


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.letterCombinations("23")
    print(outcome)
