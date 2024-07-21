# 11. 完全背包
from typing import List


class Solution:
    def function(self, weight, value, bagWeight) -> bool:
        # 排除 Corner Case

        # 创建 dp table

        # 初始化 dp 数组
        dp = [0] * (bagWeight + 1)

        # 遍历顺序:顺序，内层容量
        for i in range(len(weight)):
            for j in range(weight[i], bagWeight + 1):  # 顺序✓;内层容量求组合数，内层物品求排列数
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        # 返回答案
        return dp[bagWeight]


def ACM():
    obj = Solution()
    while True:
        try:
            weight = list(map(int, input().split(" ")))
            value = list(map(int, input().split(" ")))
            bagWeight = int(input())
            x = obj.function(weight, value, bagWeight)
            print(x)
        except:
            break


if __name__ == "__main__":
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4

    obj = Solution()
    x = obj.function(weight, value, bagWeight)
    print(x)

    # ACM()
    # 1 3 4
    # 15 20 30
    # 4
