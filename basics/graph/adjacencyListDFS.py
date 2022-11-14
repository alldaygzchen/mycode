from collections import deque
# count path
# GraphNode used for adjacency list (Another way to represent)
# class GraphNode:
#     def __init__(self, val):
#         self.val = val
#         self.neighbors = []# pointing to next node


#    A
#  B  C  D  E
#F   G 

#count path (postorder)
# class Solution:

#     def __init__(self,edges):

#         self.adjList = {}
#         for src, dst in edges:
#             if src not in self.adjList:
#                 self.adjList[src] = []
#             if dst not in self.adjList:
#                 self.adjList[dst] = []
#             self.adjList[src].append(dst)


#     def dfs(self,node,target,visit):
#         if node in visit:
#             return  0
#         if node ==target:
#             return 1
#         count = 0 # the key point
#         visit.add(node)
        
#         for neighbor in  self.adjList[node]:
#             count+=self.dfs(neighbor,target,visit)
#         visit.remove(node) #e.g. remove B

#         return count
# edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
# s = Solution(edges)
# print(s.dfs("A","E",set()))


class Solution:#(preorder)

    def __init__(self,edges):

        self.adjList = {}
        for src, dst in edges:
            if src not in self.adjList:
                self.adjList[src] = []
            if dst not in self.adjList:
                self.adjList[dst] = []
            self.adjList[src].append(dst)


    def countPath(self,node,target):

        self.target = target
        self.count = 0
        self.dfs("A",set(),[])

        return self.count


    def dfs(self,node,visit,path):


        if node in visit:
            return

        path.append(node)
        
        if node ==self.target:
            self.count+=1
            # print('##',self.record)
            return

        visit.add(node)

        
        for neighbor in  self.adjList[node]:
            self.dfs(neighbor,visit,path[:])
        visit.remove(node) #e.g. remove B
        path.pop()




edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
s = Solution(edges)
print(s.countPath("A","E"))

        
# class Solution:

#     def __init__(self,edges):

#         self.adjList = {}
#         for src, dst in edges:
#             if src not in self.adjList:
#                 self.adjList[src] = []
#             if dst not in self.adjList:
#                 self.adjList[dst] = []
#             self.adjList[src].append(dst)


#     def recordPath(self,node,target):

#         self.target = target
#         self.record = []
#         self.dfs("A",set(),[])

#         return self.record


#     def dfs(self,node,visit,path):


#         if node in visit:
#             return

#         path.append(node)
        
#         if node ==self.target:
#             self.record.append(path)
#             # print('##',self.record)
#             return

#         visit.add(node)

        
#         for neighbor in  self.adjList[node]:
#             self.dfs(neighbor,visit,path[:])
#         visit.remove(node) #e.g. remove B
#         path.pop()




# edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
# s = Solution(edges)
# print(s.recordPath("A","E"))

