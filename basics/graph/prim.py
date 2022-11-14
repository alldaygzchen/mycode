# compare to dijkstras
# minimumSpanningTree

import heapq
def minimumSpanningTree(edges,n):
    
    res = []
    adj = {}
    for i in range(1,n+1):
        adj[i] = []
    for src,dst,weight in edges:
        adj[src].append([dst,weight]) #the graph is undirected
        adj[dst].append([src,weight]) #the graph is undirected

    minHeap = []
    for neighbor,weight in adj[1]:
        heapq.heappush(minHeap,[weight,1,neighbor])

    visit = set()
    visit.add(1)

    while minHeap:# popping all remaining node and find its neighbor
        weight,src,node = heapq.heappop(minHeap)
        if node in visit:
            continue
        res.append([src,node])
        visit.add(node)
        for neighbor,weight in adj[node]:
            if neighbor not in visit: #not cycle for making a tree
                heapq.heappush(minHeap,[weight,node,neighbor])


    return res
    