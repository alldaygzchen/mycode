class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self,node):
        self.oldToNew = {}
        if node:
            self.dfs(node)
        else:
            None

    def dfs(self,node):#create a deep copy node #postorder

        if node in self.oldToNew: # already has a copy
            return self.oldToNew[node]

        copy = Node(node.val)
        self.oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(self.dfs(nei))

        return copy


#   A
# B  C  D
#A E



        