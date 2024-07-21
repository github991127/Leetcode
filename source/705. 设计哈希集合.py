'''
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
实现 MyHashSet 类：
void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
'''
#建立40000个桶，每个桶存放0-31，按照二进制位数表示0-31中哈希列表为0或1
class MyHashSet:
    def __init__(self): # 初始化
        self.bs = [0]*40000

    def add(self, key: int) -> None:
        self.updateVal(key,1)

    def remove(self, key: int) -> None:
        self.updateVal(key,2)

    def contains(self, key: int) -> bool:
        return self.updateVal(key,3)

    def updateVal(self,key,flag) -> bool: # flag = 1 添加, 2 删除 ,3 是否存在
        bucket = key // 32
        loc = key % 32
        if flag == 1:
            self.bs[bucket] = (self.bs[bucket] | (1 << loc))
            print(self.bs[bucket])
        elif flag == 2:
            self.bs[bucket] = (self.bs[bucket] & ~(1 << loc))
            print(self.bs[bucket])
        elif flag == 3:
            u = (self.bs[bucket] >> loc) & 1
            return u == 1

obj = MyHashSet()
#1进入哈希列表，第一个桶第2位赋值1：bs[bucket]=10b
obj.add(31)
#2进入哈希列表，第一个桶第3位赋值1：bs[bucket]=110b
obj.add(32)
obj.remove(2)
param_3 = obj.contains(1)
print(param_3)
