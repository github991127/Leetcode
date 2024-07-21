def solve(n, nums):
    max = nums[0]
    min = nums[0]
    count = 0
    for i in range(1, n):
        if nums[i] > max:
            count += 1
            max = nums[i]
        elif nums[i] < min:
            count += 1
            min = nums[i]
    return count


if __name__ == "__main__":
    # print(solve(5, [3,2,1,4,5]))

    while True:
        try:
            n = int(input())
            nums = list(map(int, input().split(" ")))
            print(solve(n, nums))

        except:
            break

'''
已知成绩list，从第二项开始判断是否大于所有历史成绩或小于所有历史成绩，求符合条件成绩的数量
输入
5
3 2 1 4 5
输出
4
解析
2，1，4，5均符合
'''
