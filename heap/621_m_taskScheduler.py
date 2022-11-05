from collections import Counter
from collections import deque
import heapq



class Solution:
    def leastInterval(self, tasks, n: int) -> int:

        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #[number, idleTime]

        while maxHeap or q:
            time+=1
            if maxHeap:
                number = abs(heapq.heappop(maxHeap))-1
                if number:
                    q.append([number,time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0]*-1)
        return time


# tasks = ["A","A","A","B","B","B"]
# n = 2
# count = Counter(tasks)
# # print(count)
# # print(count.values())
# maxHeap = [-cnt for cnt in count.values()]
# heapq.heapify(maxHeap)


