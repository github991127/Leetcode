# 04. 哈希表模板
from typing import List


class Solution:
    def function(self, nums: List[int], target: int) -> int:
        # res = [0] * 26  # 统计有限个数-数组
        # res[ord(i) - ord("a")] += 1

        # res = set()  # 统计无限个数-集合
        # res.add(i)

        # res = {}  # 统计无限个数-字典
        # res[i] = res.get([i], 0) + 1

        # 获取int每位数字
        # n = 31010
        # res = []
        # while n:
        #     n, r = divmod(n, 10)
        #     res.append(r)
        # res.reverse()

        # 不求索引-可排序
        # while left < right and nums[left] == nums[left + 1]:  # 3数4数求和-abcd分别去重

        return 0


def ACM():
    obj = Solution()
    while True:
        try:
            nums = list(map(int, input().split(" ")))
            target = nums.pop(0)
            x = obj.function(nums, target)
            print(x)
        except:
            break


if __name__ == "__main__":
    nums = [1, 2, 3, 5, 8]
    target = 5

    obj = Solution()
    x = obj.function(nums, target)
    print(x)

    # ACM()
