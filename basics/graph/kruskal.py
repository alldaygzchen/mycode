# union find: find whether has a path already in the graph
# minimumSpanningTree

import heapq

class UnionFind:

    def __init__(self,n):
        self.par = {}
        self.rank = {}
        for i in range(1,n+1):
            self.par[i]=i
            self.rank[i] = 0

    def find(self,n):

        while n!=self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n= self.par[n]
        return n

    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1]>self.rank[p2]:
            self.par[p2] =p1
        elif self.rank[p1]<self.rank[p2]:
            self.par[p1] =p2
        else:
            self.par[p1] = p2
            self.rank[p2]+=1
        return True

def minimumSpanningTree(edges,n):
    minHeap = []
    mst = []
    for n1,n2,weight in edges:
        heapq.heappush(minHeap,[weight,n1,n2]) # push all, its different than prim and dijkstras

    unionFind = UnionFind(n)
    while len(mst)<n-1:
        weight,n1,n2 = heapq.heappop(minHeap)
        if not unionFind.union(n1,n2):#duplicate path
            continue
        mst.append([n1,n2])

    return mst
