import math


# 二分法
def isSqrt(n):
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        s = pow(mid, 2)
        if s < n:
            left = mid + 1
        elif s > n:
            right = mid - 1
        else:
            return True
    else:
        return False


# 分解聚合法
def isSqrt(n):
    a = int((math.sqrt(n)))
    return n == a * a


# 除余法
def isSqrt(n):
    i = n
    while i * i > n:
        i = (i + n / i) // 2
    return n == i * i


# 牛顿迭代法
def isSqrt(n):
    i = 1
    while n > 0:
        n -= i
        i += 2
    return n == 0


def solve(nums, a, b, x):
    outcome = -1
    for i in range(a - 1, b):
        if isSqrt(nums[i] * x) == False:
            outcome = nums[i]
            break
    return outcome


if __name__ == "__main__":
    print(solve([1, 6, 24, 12, 3], 1, 3, 4))

    input_num = list(map(int, input().split(" ")))
    length = input_num[0]
    count = input_num[1]
    nums = list(map(int, input().split(" ")))
    for i in range(count):
        try:
            input_index = list(map(int, input().split(" ")))
            outcome = solve(nums, input_index[0], input_index[1], input_index[2])
            print(outcome)
        except:
            break

'''
已知数列和区间，判断数列区间内元素乘以x后是否为平方数，求第一个不满足的元素，若无返回-1
输入
5（数列长度） 3（次数）
1 6 24 12 3
1 3 4（[0,2]元素分别乘以4，是否满足）
3 5 2
4 5 3
输出
6
24
-1
解析
复杂度不能超过n2
'''
