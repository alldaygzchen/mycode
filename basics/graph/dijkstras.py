# unweighted => bfs
# weighted => dijkstras
# assume no negative weight, thus minheap result is the minumum
# coding similiar as bfs

# Find the shortest path length from src to every other node
# compare to prim

import heapq
def shortestPath(edges,n,src):
    
    adj = {}
    for i in range(1,n+1):
        adj[i] = [] #(dst,weight)

    for s,d,w in edges:
        adj[s].append((d,w))

    shortest = {}
    minHeap = [(0,src)]

    while minHeap:# popping all remaining node and find its neighbor
        
        dis, n1= heapq.heapop(minHeap)
        if n1 in shortest: # skip all not minimum
            continue
        shortest[n1] =dis

        for n2,w2 in adj[n1]:
            if n2 not in shortest: # stop minHeap since finding the minimum
                heapq.heappush(minHeap,(dis+w2,n2))

    return shortest

        
# for example 
#a -> b
#a -> c
#c -> b