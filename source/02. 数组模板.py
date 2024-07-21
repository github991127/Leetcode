# 02. 数组模板
from typing import List


class Solution:
    def function(self, nums: List[int], target: int) -> int:
        # while (left < right):  # 有序数组-二分法
        # while i < n:  # 二重遍历-快慢指针
        # while i < n:  # 二重遍历-滑动窗口
        # float('-inf')  # 更新最大值-初始化最小值
        # range(0, 9)  # 循环不变量-左开右闭
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
