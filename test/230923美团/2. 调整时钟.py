def solve(time_now, x):
    time_now = list(map(int, time_now.split(":")))
    hour = time_now[0]
    minute = time_now[1]
    list_x = x.split(" ")
    fix = list_x[0]
    fix_time = int(list_x[1])

    if fix == '+':
        minute += fix_time
    elif fix == '-':
        minute -= fix_time

    if minute < 0:
        temp = 1 + (-minute // 60)
        hour -= temp
        minute = temp * 60 + minute
    elif minute >= 60:
        hour += minute // 60
        minute = minute % 60

    if hour < 0:
        temp = 1 + (-hour // 24)
        hour = temp * 24 + hour
    elif hour >= 24:
        hour = hour % 24

    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)

    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)

    return hour + ":" + minute


if __name__ == "__main__":
    time_now = "00:00"
    time_now = solve(time_now, "- 1441")
    print(time_now)  # 23:59
    time_now = solve(time_now, "+ 61")
    print(time_now)  # 01:00

    time_now = input()
    n = int(input())
    for i in range(n):
        try:
            x = input()
            time_now = solve(time_now, x)
        except:
            break
    print(time_now)
'''
已知24时制时间00:00，调整次数，调整分钟数+ x或- x，求调整后的时间
输入
00:00
2（调整次数）
+ 2
- 5
输出
00:02
23:57
解析
时满24要进位，分满60要进位
'''
