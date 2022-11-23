from collections import defaultdict
from collections import deque

#not done

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        self.adjDict= defaultdict(list)
        for s,d,p in flights:
            self.adjDict[s].append([d,p])
        
        self.quene = deque()
        self.quene.append((0,src))
        self.step = 0
        self.ans = float('inf')

        while self.quene:
            for i in range(len(self.quene)):
                p,d= self.quene.popleft()

                if d ==dst:
                    self.ans = min(p,self.ans)

                for next_d,next_p in self.adjDict[d]:
                    if p+next_p>self.ans:
                        continue
                    self.quene.append((p+next_p,next_d))

            if self.step>k:
                break
            self.step+=1

        if self.ans == float('inf'):
            return -1
        return self.ans


        