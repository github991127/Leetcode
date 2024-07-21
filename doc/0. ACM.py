# https://www.bilibili.com/read/cv15996133/
# https://blog.csdn.net/weixin_42327752/article/details/124381258

def get_input():
    """获取输入数据"""

    ## 2.1 input()函数接收输入和字符串分割
    some_string = input()
    # input()接收输入的一个字符串，如果是多行输入，那么调用一次input()只会读取一行数据
    # 如果最后一行之后再调用input()，则抛出EOFError，表明到达文档末尾EndOfFile
    # input()接收的数据是一个字符串，且不包含该行数据最后的换行符
    # 读取一个数字时
    a_number = int(input())  # 需要手动转型成需要的数据类型
    # 假设逐行或者一次性输入以下数据行
    input_string = '''
    1 2 3
    4 5 6
    7 8 9
    '''
    get_string = input()  # 得到值为“1 2 3”的字符串
    get_string = input()  # 得到值为“4 5 6”的字符串
    get_string = input()  # 得到值为“7 8 9”的字符串
    # 循环形式读取
    for _ in range(3):
        get_string = input()
    # 读取之后，我们要预处理字符串，比如对于“1 2 3”
    get_string = '1 2 3'
    parts_of_string = get_string.split()  # 将get_string按空格分割得到一个列表['1','2','3']
    get_string = '1,2,3'
    parts_of_string = get_string.split(',')  # split()默认分隔符为空格，如果不是，需要自己指定
    get_string = '  1 2 3  '
    parts_of_string = get_string.strip().split()  # strip()可以去掉字符串两端的空格，但实际笔试不常用
    get_string = '1 2 3'
    a_string, b_string, c_string = get_string.split()  # 如果知道输入的数据个数，可以直接赋值
    a_int = int(a_string)  # 如果输入需要作为数字处理，需要转型
    a_float = float(a_string)

    ## 2.2 字符串转型
    # 将输入批量转成数字
    ### 2.2.1 法1：列表生成式
    list1 = [i + 1 for i in range(1, 5)]  # [2, 3, 4, 5]
    # 等价于
    list1 = []
    for i in range(1, 5):
        list1.append(i + 1)
    list2 = [i + 1 for i in range(1, 5) if i % 2 == 0]  # [3, 5]
    # 等价于
    list2 = []
    for i in range(1, 5):
        if i % 2 == 0:
            list2.append(i + 1)

    # 以输入“1 2 3”为例，使用列表生成式获取列表
    get_string = '1 2 3'
    parts_of_string = get_string.split()
    list_of_int = [int(i) for i in parts_of_string]  # [1, 2, 3]
    # 或者
    a, b, c = [int(i) for i in parts_of_string]
    # 合并成一句话
    list_of_int = [int(i) for i in input().split()]

    ### 2.2.2 法2：map()函数并行计算
    # map(函数名, 列表或者迭代器)是一个并行处理列表元素的函数
    # 以输入“1 2 3”为例
    parts_of_string = ['1', '2', '3']
    iterator_of_int = map(int, parts_of_string)
    # 结果等价于
    iterator_of_int = iter(int(i) for i in parts_of_string)
    # map()的返回值是一个迭代器，可以直接对指定个数的变量赋值，或者用于循环
    a, b, c = map(int, parts_of_string)
    for i in map(int, parts_of_string):  # 在笔试中不常见
        pass
    # 但不能直接对列表赋值，必须转型成列表
    list_of_int = list(map(int, parts_of_string))
    # 合并成一句话
    list_of_int = list(map(int, input().split()))

    ### 2.2.3 如果输入的是一个序列化的表示列表的字符串
    get_string = '[1,2,3]'
    # 可以直接去掉串左右两边的括号并分割，灵活处理
    list_of_int = [int(i) for i in input()[1:-1].split(',')]
    # 对于更复杂的情况，如多重列表或者字典，推荐用eval()函数反序列化
    get_string = '[1,2,3]'
    list_of_int = eval(get_string)
    get_string = '{1:0,2:1,3:2}'
    dict_of_int = eval(get_string)
    get_string = '1+2*3'
    result_of_int = eval(get_string)
    # eval()函数非常强大，详细使用建议单独学习

    return result_of_int


def output(data):
    """输出"""

    ## 2.3 输出格式
    # 如果每个用例只输出一个数字，直接print
    print(data)
    # 如果每个用例输出有限个数的变量，要求以空格隔开
    result_a, result_b, result_c = 1, 2, 3
    print(result_a, result_b, result_c)  # 输出1 2 3

    ## 2.4 join()函数连接字符串列表
    list_of_string = ['1', '2', '3']
    joint_mark = ''  # 如果需要将字符串列表连成一个字符串
    joint_string = joint_mark.join(list_of_string)  # 得到“123”
    joint_mark = ' '  # 不仅要连接字符串，中间还要以空格隔开
    joint_string = joint_mark.join(list_of_string)  # 得到“1 2 3”
    joint_mark = ','  # 别的形式可以灵活调整
    joint_string = '[' + joint_mark.join(list_of_string) + ']'  # 得到“[1,2,3]”
    # 对于每个用例输出一个列表的情况，可以先把结果列表转成字符串列表，再用join()函数连接成字符串输出
    # 例如输出一个整数列表[1, 20, 300, 4000]，只输出数字并用空格隔开
    data = [1, 20, 300, 4000]
    print(' '.join([str(i) for i in data]))  # 输出1 20 300 4000


while True:
    try:
        data = get_input()  # 获取输入数据，可以是输入一个数或者字符串，也可以是更复杂的形式
        result = solve(data)  # 用你的算法解题得出需要的答案
        output(result)  # 按题目要求输出结果
    except EOFError:  # 如果try块中发生了EndOfFile错误，就执行break退出循环
        break  # 关于EOFError在下文讲解

## 1.2 情况2：多行输入，指定用例的个数
n, m, p, q = get_input()  # 假设有n个用例
for _ in range(n):  # 如果要对用例计数，则for i in range(n)
    data = get_input()
    # 可能题目会有更多参数，灵活地使用嵌套循环
    # for j in range(m):
    #     for s in range(p):
    #         for t in range(q):
    result = solve(data)
    output(result)

## 1.3 情况3：多行输入，指定某个条件退出
while True:
    data = get_input()
    if judge(data):  # 如果输入满足退出条件，退出循环
        break
    result = solve(data)
    output(result)
