import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 3)
print(minHeap)



H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)