'''
给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。
返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
'''
#官解https://leetcode.cn/problems/top-k-frequent-words/solution/by-sunguodong-3tov/
from typing import List
from collections import Counter
from collections import deque
import heapq

class Pair:
    def __init__(self, word: str, count: int):
        self.word = word
        self.count = count
    def __lt__(self, pair) -> bool:#重写<方法
        return self.count < pair.count or self.count == pair.count and self.word > pair.word#'a'<'b',因此字母排序要取反

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)#计数字典
        occur = [Pair(word, count) for word, count in counter.items()]#Pair组成的列表

        heap = [occur[i] for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(occur)):
            heapq.heappushpop(heap, occur[i])#先push再pop，保证堆元素数量不变
        ans = deque()
        for _ in range(k):
            ans.appendleft(heapq.heappop(heap).word)#如果先用deque()储存结果，则每次可以仅用O(1)O(1)的时间进行左插入。kk次出堆完成后再将其转换为list
        return list(ans)

obj1=Solution()
List=['ax','ax','an','bar']
var=2
outcome = obj1.topKFrequent(List,var)
print(outcome)
