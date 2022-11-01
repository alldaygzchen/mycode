import heapq
class Solution:
    def lastStoneWeight(self, stones):
        #maxHeap=>minHeap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            if first>second:
                heapq.heappush(stones,second-first)

        #may have at least one stone
        stones.append(0)
        return abs(stones[0])


