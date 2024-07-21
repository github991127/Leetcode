'''
https://leetcode.cn/problems/restore-ip-addresses/
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
'''
from typing import List


class Solution:
    def __init__(self):
        self.path = ""
        self.result = []

    def is_ip(self, s: str, start: int, end: int) -> bool:
        if s[start] == "0" and end - start != 1:
            return False
        elif int(s[start:end]) > 255:
            return False
        else:
            return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        self.backtracking(s, start=0, deep=0)
        return self.result

    def backtracking(self, s, start, deep):
        if deep == 4:
            if start == len(s):
                self.result.append(self.path.strip("."))
            return
        for index in range(start, min(start + 3, len(s))):  # 最多分3个数字
            if self.is_ip(s, start, index + 1):
                var = self.path
                self.path = self.path + "." + s[start:index + 1]
                self.backtracking(s, index + 1, deep + 1)
                self.path = var


if __name__ == "__main__":
    obj1 = Solution()
    outcome = obj1.restoreIpAddresses("101023")
    print(outcome)
