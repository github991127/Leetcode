'''

'''
import random


def generate_until_increase(min_value=1, max_value=13):
    count = 0  # 记录生成的次数
    last_value = -1  # 上一次生成的值，初始化为-1
    while True:
        count += 1
        current_value = random.randint(min_value, max_value)  # 生成一个随机数
        # print(current_value)
        if current_value > last_value:
            last_value = current_value
        else:
            break
    return count


if __name__ == "__main__":
    N = 10000
    # N = 100
    x = 0
    for _ in range(N):
        count = generate_until_increase()
        x += count
    print(x / N)
