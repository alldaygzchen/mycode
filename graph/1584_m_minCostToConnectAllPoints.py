from collections import defaultdict
import heapq
class Solution:

    def minCostConnectPoints(self,points):
        self.points =points
        self.adjDict = defaultdict(list)
        self.minHeap =[[0,0]]
        self.visit =set()
        self.res = 0

        for i in range(len(self.points)):
            for j in range(i+1,len(points)):
                x1,y1 = self.points[i]
                x2,y2 = self.points[j]
                dis = abs(x1-x2)+abs(y1-y2)
                self.adjDict[i].append([dis,j])
                self.adjDict[j].append([dis,i])

        # while self.minHeap:
        while len(self.visit) < len(self.points):
            dis,idx =heapq.heappop(self.minHeap)
            if idx in self.visit:
                continue
            self.res +=dis
            self.visit.add(idx)
            for nextdis,nextidx in self.adjDict[idx]:
                if nextidx not in self.visit:
                    heapq.heappush(self.minHeap,[nextdis,nextidx])

        return self.res