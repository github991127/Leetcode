'''
将字符串中的每个大写字母替换成最近的偏爱字符，替换同时发生只进行一次
    # 12 4
    # Z G B A
    # ZQWEGRTBYAAI
    # 结果ZZZGGGBBBAAA
'''


# class Solution:
#     def fun(self, n, m, loveList, strS):
#         x = ''
#         l = len(strS)
#         for i in range(l):
#             if strS[i] in loveList:
#                 x += strS[i]
#                 continue
#             else:
#                 left = right = i
#                 while True:
#                     left -= 1
#                     if left > -1 and strS[left] in loveList:
#                         x += strS[left]
#                         break
#                     right += 1
#                     if right < l and strS[right] in loveList:
#                         x += strS[right]
#                         break
#                     # if left<0 and right>l-1:
#                     #     break
#         return x


# class Solution:
#     def fun(self, n, m, loveList, strS):
#         x = ''
#         l = len(strS)
#         res=[0]*26
#         for a in loveList:
#             res[ord(a)-ord('A')]+=1
#         for i in range(l):
#             if res[ord(strS[i])-ord('A')]:
#                 x += strS[i]
#                 continue
#             else:
#                 left = right = i
#                 while True:
#                     left -= 1
#                     if left > -1 and res[ord(strS[left])-ord('A')]:
#                         x += strS[left]
#                         break
#                     right += 1
#                     if right < l and res[ord(strS[right])-ord('A')]:
#                         x += strS[right]
#                         break
#                     # if left<0 and right>l-1:
#                     #     break
#         return x

class Solution:
    def fun(self, n, m, loveList, strS):
        loveRecord = []
        temp = ''
        l = len(strS)
        res = [0] * 26
        for a in loveList:
            res[ord(a) - ord('A')] += 1
        for i in range(l):
            if res[ord(strS[i]) - ord('A')]:
                if strS[i] != temp:
                    temp = strS[i]
                    loveRecord.append(i)
        # print(loveRecord)
        strNew = []
        for s in strS:
            strNew.append(s)
        print(strNew)
        for i in range(len(loveRecord) - 1):
            left = loveRecord[i]
            right = loveRecord[i + 1]
            for j in range(left + 1, (left + right) // 2 + 1):
                strNew[j] = strNew[loveRecord[i]]
            for k in range((left + right) // 2 + 1, right):
                strNew[k] = strNew[loveRecord[i + 1]]
        for j in range(loveRecord[-1], len(strS)):
            strNew[j] = strNew[loveRecord[-1]]
        strS = ''.join(strNew)
        return strS


def ACM():
    obj = Solution()
    while True:
        try:
            nums = input().split(" ")
            n = int(nums.pop(0))
            m = int(nums.pop(0))
            loveList = input().split(" ")
            strS = input()
            x = obj.fun(n, m, loveList, strS)
            print(x)
        except:
            break


if __name__ == "__main__":
    obj = Solution()
    n = 12
    m = 4
    loveList = ['Z', 'G', 'B', 'A']
    strS = "ZQWEGRTBYAAI"
    x = obj.fun(n, m, loveList, strS)
    print(x)
    ACM()
    # 12 4
    # Z G B A
    # ZQWEGRTBYAAI
