# klogn better than nlogn
import heapq
class Solution:
    def kClosest(self,points,k):
        res =[]
        record =[]
        for x,y in points:
            dist = (x**2)+(y**2)
            record.append([dist,x,y])

        heapq.heapify(record)
        while k:
            dist,x,y=heapq.heappop(record)
            res.append([x,y])
            k-=1
        return res