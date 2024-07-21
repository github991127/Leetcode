'''
写一个 RecentCounter 类来计算特定时间范围内最近的请求。
请你实现 RecentCounter 类：
RecentCounter() 初始化计数器，请求数为 0 。
int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
保证 每次对 ping 的调用都使用比之前更大的 t 值。
'''
from collections import deque#队列包
class RecentCounter:
    def __init__(self):
        self.queue=deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0]<t-3000:self.queue.popleft()#一次可能弹出多个元素，需要while
        return len(self.queue)

obj = RecentCounter()
a = obj.ping(1)
a = obj.ping(3000)
a = obj.ping(3001)
a = obj.ping(3002)
print(a)
