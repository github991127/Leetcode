# 0. 常用
import math

# ——————————————————————int列表A，str列表B，str字符串C的转换
A = [1, 2, 3, 4, 5]
B = [str(x) for x in A]  # A-B
print(B)
A = [int(x) for x in B]  # B-A
print(A)

C = "-".join(B)  # B-C
print(C)
B = C.split("-")  # C-B(split默认以任意个空格隔开)
# B=[x for x in C]  # 无间隔
print(B)

A = [int(i) for i in C.split("-")]  # C-A
print(A)
# A = [1, 2, 3, 'a', 'b']
C = "-".join('%s' % i for i in A)  # A-C(A含非数字也可以)
print(C)
# ——————————————————————列表和字符串
# 2维数组创建初始化
i, j = 2, 3
dp = [[0] * j for _ in range(i)]  # [[0, 0, 0], [0, 0, 0]]2行3列
print(dp)

# 索引插入
str = "12345"
list = [1, 2, 3, 4, 5]

str = (str[0:2] + "x" + str[2:len(str)])
list.insert(2, "x")
print(str)
print(list)

# 尾部插入
str = "12345"
list = [1, 2, 3, 4, 5]

str += '6789'
list.append(6)
list.extend((7, 8))
list = list + [9, 10]
print(str)
print(list)

# 删除
str = "12345"
list = [1, 2, 3, 4, 5]

str = str.strip('1')  # 移除字符串头尾字符（默认为空格或换行符）
list.remove(1)  # 移除值
list.pop(1)  # 移除索引,默认-1
print(str)
print(list)

# 查找,计数,翻转
str = "12345"
list = [1, 2, 3, 4, 5]

print(str.find('5'))
print(list.index(5))
print(str.count('5'))
print(list.count(5))
print(str[::-1])
print(list[::-1])

# 替换
str = "12345"
list = [1, 2, 3, 4, 5]

replace = {'1': '11', '2': '22'}
print([replace[i] if i in replace else i for i in str])  # 变成列表
replace = {1: 11, 2: 22}
print([replace[i] if i in replace else i for i in list])
# ——————————————————————集合和字典
# set集合增删
set1 = {1, 2, 3}
set1.add(3)  # 增，有不报错
set1.discard(4)  # 删，无不报错
print(set1)

# dict字典增删查
dict = {'A': 1, 'B': 2, 'C': 3}
dict.update({'A': 0, 'D': 4})  # 增，有不报错,覆盖
print(dict.pop('F', -1))  # 删，无不报错，返回-1
print(dict.setdefault('E', 5))  # 键查值，无不报错,增加后返回
print(dict.get('G', -1))  # 键查值，无不报错,返回-1
print(dict)

# dict字典遍历键值
dict = {'A': 1, 'B': 2, 'C': 3}
for i in dict:  # 遍历键
    print(i)
for i in dict.values():  # 遍历值
    print(i)
for i in dict.items():  # 遍历键值元组
    print(i)
for key, value in dict.items():  # 遍历键值
    print(key, value)
# ——————————————————————基本
# range边界,切片边界
for i in range(2, 5, 1):  # 234
    print(i, end='')
    if i == 4: print()
for i in range(5, 2, -1):  # 543
    print(i, end='')
    if i == 3: print()
nums = [0, 1, 2, 3, 4, 5]
print(nums[2:4])
print(nums[-2:])
print(nums[:-2])

# 除和整除
print(5 / 2, -5 / 2, 5 / -2, -5 / -2)  # 2 -3 -3 2
print(5 // 2, -5 // 2, 5 // -2, -5 // -2)  # 2.5 -2.5 -2.5 2.5

# 最小值列表初始化
n = 9
i = 3
nums = [float('-inf')] * n
nums[i:n] = [float('inf')] * (n - i)
print(nums)
# ——————————————————————语法糖
# 打包解包
x = [1, 2, 3]
a, b, c = x  # 需要和容器元素个数相同
print(a, b)

# 列表推导式
a = [1, 2, 3]
b = [10 + x for x in a]  # [11, 12, 13]
c = [10 + x for x in a if x % 2 != 0]  # [11, 13]
print(b, c)
a2 = [[1, 2, 3], [4, 5, 6]]
b2 = [100 + x for y in a2 for x in y if x % 2 != 0]  # [111, 113, 111, 113]
print(b2)

# 数字分隔符
a = [1_000_000, 2_000]
print(a)

# 自动处理文件流
with open('test.txt', 'r')as f:
    data = f.read()
    print(data)

# float数字比较
a = 0.1
b = 0.2
print(a + b == 0.3)
print(math.isclose(a + b, 0.3))

# format字符串格式化，保留小数点后2位
print("{0}+{1}={2}?".format(1, 2, 3))  # 1+2=3?
print("{:.2f}".format(2 / 3))  # 0.67
print("{:.2%}".format(2 / 3))  # 66.67%
print("{:.2e}".format(2 / 3))  # 6.67e-01

print(" ", end="")  # 输出末尾字符end默认为回车换行符，修改为空
