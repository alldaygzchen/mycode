from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self,times,n,k):
        
        self.visit = set()
        self.result =0
        self.minHeap = [[0,k]]
        self.adjDict = defaultdict(list)

        for s,t,time in times:
            self.adjDict[s].append([time,t])

        while self.minHeap:
            t1,d1 = heapq.heappop(self.minHeap)
            if d1 in self.visit:
                continue
            self.visit.add(d1)
            self.result = t1

            for t2,d2 in self.adjDict[d1]:
                if d2 not in self.visit:
                    heapq.heappush(self.minHeap,[t1+t2,d2])

        if len(self.visit)==n:
            return self.result

        return -1
        