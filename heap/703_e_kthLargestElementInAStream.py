#https://www.tutorialspoint.com/heap-queue-or-heapq-in-python
import heapq

class KthLargest:

    def __init__(self, k, nums):

        self.minHeap = nums #since it is a stream maxheap heappop is not suitable
        self.k = k

        heapq.heapify(self.minHeap) # turn to a heap
        while len(self.minHeap)>k: #to be length=k
            heapq.heappop(self.minHeap) #remain heap
        

    def add(self, val):
        heapq.heappush(self.minHeap,val) #remain heap

        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap) #remain heap

        return self.minHeap[0]
