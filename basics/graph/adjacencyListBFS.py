# Shortest path from node to the target
#     o
#     o
#     o
#    o o
#   o o
#  .. None

# from collections import deque
# class Solution:

#     def __init__(self,edges):

#         self.adjList = {}
#         for src, dst in edges:
#             if src not in self.adjList:
#                 self.adjList[src] = []
#             if dst not in self.adjList:
#                 self.adjList[dst] = []
#             self.adjList[src].append(dst)

#     def bfs(self,node,target):

#         length = 0
#         quene = deque()
#         quene.append(node)
#         visit = set()
#         visit.add(node)

#         while quene:
#             for i in range(len(quene)):
#                 curr = quene.popleft()
#                 if curr == target:
#                     return length
#                 for neighbor in self.adjList[curr]:
#                     if neighbor not in visit:
#                         visit.add(neighbor)
#                         quene.append(neighbor)

#             length+=1
#         return length

# edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
# s = Solution(edges)
# print(s.bfs("A","E"))

# https://stackoverflow.com/questions/69471667/two-implementation-methods-of-bfs-for-finding-the-shortest-path-which-one-is-th
from collections import deque
class Solution:

    def __init__(self,edges):

        self.adjList = {}
        for src, dst in edges:
            if src not in self.adjList:
                self.adjList[src] = []
            if dst not in self.adjList:
                self.adjList[dst] = []
            self.adjList[src].append(dst)
   #ab,abc,abe,abce
    def bfs(self,node,target):

        quene = deque()
        quene.append([node])
        visit = set()
        visit.add(node)

        while quene:
            for i in range(len(quene)):
                path = quene.popleft()
                curr = path[-1]
                if curr == target:
                    return path
                for neighbor in self.adjList.get(curr,[]):
                    if neighbor not in visit:
                        new_path=path[:]
                        new_path.append(neighbor)

                        quene.append(new_path)

        return []

edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
s = Solution(edges)
print(s.bfs("A","E"))