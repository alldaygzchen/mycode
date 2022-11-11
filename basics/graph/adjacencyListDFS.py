from collections import deque

# GraphNode used for adjacency list (Another way to represent)
# class GraphNode:
#     def __init__(self, val):
#         self.val = val
#         self.neighbors = []# pointing to next node


#    A
#  B  C  D  E
#F   G 

#count path
class Solution:

    def __init__(self,edges):

        self.adjList = {}
        for src, dst in edges:
            if src not in self.adjList:
                self.adjList[src] = []
            if dst not in self.adjList:
                self.adjList[dst] = []
            self.adjList[src].append(dst)


    def dfs(self,node,target,visit):
        if node in visit:
            return  0
        if node ==target:
            return 1
        count = 0
        visit.add(node)
        
        for neighbor in  self.adjList[node]:
            count+=self.dfs(neighbor,target,visit)
        visit.remove(node) #e.g. remove B

        return count
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
s = Solution(edges)
print(s.dfs("A","E",set()))

        

