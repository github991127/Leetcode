'''
https://leetcode.cn/problems/last-stone-weight-ii/
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
'''
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 排除 Corner Case

        # 创建 dp table
        s = sum(stones)
        bagstones = s // 2
        dp = [0] * (bagstones + 1)

        # 初始化 dp 数组
        for j in range(stones[0], bagstones + 1):
            dp[j] = stones[0]

        # 遍历顺序
        for i in range(1, len(stones)):
            for j in range(bagstones, stones[i] - 1, -1):
                dp[j] = max(dp[j],
                            stones[i] + dp[j - stones[i]])

        # 返回答案
        left = dp[-1]
        right = s - left
        return right - left


if __name__ == "__main__":
    stones = [31, 26, 33, 21, 40]

    obj1 = Solution()
    outcome = obj1.lastStoneWeightII(stones)
    print(outcome)
