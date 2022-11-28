from collections import deque


class Solution:
    def monotoneDeque(self,arrayList):
        myQuene= deque()
        result  = []
        prev_collect =[]
        loops = len(arrayList)+1
        idx=0

        while idx!=loops:

            while (myQuene and idx==len(arrayList)) or (myQuene and myQuene[-1]!=arrayList[idx]):
                prev = myQuene.popleft()
                prev_collect.append(prev)

            if len(prev_collect)>0:
                result.append(prev_collect)
                prev_collect =[]

            if idx!=len(arrayList):
                myQuene.append(arrayList[idx])

            idx+=1
        


        return result

test1 = ['a','a','a','a','a','b','b','b','b','c','c','c','d','d','e','e','f','f']
test2 = ['a','a','a','a','a','b','b','b','b','c','c','c','d','d','e','e','f']
s =Solution()
print(s.monotoneDeque(test1))
print(s.monotoneDeque(test2))