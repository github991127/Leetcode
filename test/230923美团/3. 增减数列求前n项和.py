def solve(n):
    outcome = 0
    sum = 0
    k = 1
    while n > sum:
        sum += k
        outcome += sum
        k += 1
    for i in range(sum - n + 1):
        outcome -= i
    return outcome % (10 ** 9 + 7)


if __name__ == "__main__":
    # print(solve(4))

    while True:
        try:
            n = int(input())
            print(solve(n))

        except:
            break
'''
已知增减数列每次从k减到1，k自增后重新递减。1，2，1，3，2，1，4，3，2，1……求前n项和
输入
4
输出
7
解析
1，2，1，3和为7
'''
