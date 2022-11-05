#considering -10**5 <= num <= 10**5


import heapq

class MedianFinder:

    def __init__(self):
        # maxHeap for small numbers
        # minHeap for large numbers
        self.maxHeap, self.minHeap = [],[]
    
    def addNum(self,num):
        heapq.heappush(self.maxHeap,-1*num)

        # make sure statement #1
        if self.maxHeap and self.minHeap and (-1*self.maxHeap[0])>self.minHeap[0]:
            val = -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,val)

        # make sure statement #2
        if len(self.maxHeap)>len(self.minHeap)+1:
            val = -1*heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,val)
        
        # make sure statement #3
        if len(self.minHeap)>len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-1*val)

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return -1*self.maxHeap[0]
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        return (-1*self.maxHeap[0]+self.minHeap[0])/2

        
