# only work for directed, acyclical graph 
# first way: change graph order
# second way: postorder


class Solution:

    def __init__(self,edges,n):

        self.adj = {}
        self.n =n 
        for i in range(1,n+1):
            self.adj[i] = []
        for src,dst in edges:
            self.adj[src].append(dst)


    def topologicalSort(self):
        self.topSort = []
        self.visit = set()
        for i in range(1,self.n+1):
            self.dfs(i)
        self.topSort.reverse()
        return self.topSort


    def dfs(self,src):
        if src in self.visit:
            return
        self.visit.add(src)
        # print(src)

        for neighbor in self.adj[src]:
            self.dfs(neighbor)
        self.topSort.append(src)
        
edges = [[6,3],[6,1],[5,1],[5,2],[3,4],[4,2]]
s= Solution(edges,6)
print(s.topologicalSort()) #6,5,3,4,2,1


# def topologicalSort(edges, n):
#     adj = {}
#     for i in range(1, n + 1):
#         adj[i] = []
#     for src, dst in edges:
#         adj[src].append(dst)

#     topSort = []
#     visit = set()
#     for i in range(1, n + 1):
#         dfs(i, adj, visit, topSort)
#     topSort.reverse()
#     return topSort

# def dfs(src, adj, visit, topSort):
#     if src in visit:
#         return
#     visit.add(src)
    
#     for neighbor in adj[src]:
#         dfs(neighbor, adj, visit, topSort)
#     topSort.append(src)

# edges = [[6,3],[6,1],[5,1],[5,2],[3,4],[4,2]]
# print(topologicalSort(edges,6)) #6,5,3,4,2,1