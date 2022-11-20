from collections import defaultdict
class Solution:

    """
    ADJACENT LIST: key:str value: a list with sorting element
    DFS preorder
        # start with jfk
        # may have cycle:pop the list element 
        # base case [check len(tickets)+1 == list(res)]
        # return the list path

    """
    def findItinerary(self, tickets):
        
        # INIT 
        tickets.sort()
        self.tickets =tickets
        self.adjList = defaultdict(list)
        self.res = ["JFK"]

        # CREATE ADJACENT LIST
        for src,dst in self.tickets:
            self.adjList[src].append(dst)

        # DFS PREORDER
        self.dfs_preorder("JFK")
        return self.res

    def dfs_preorder(self,src):

        # base case
        if len(self.tickets)+1 == len(self.res):
            return True
        
        
        # since we need pop, we need the index
        temp = list(self.adjList[src])
        for i,v in enumerate(temp):

            self.adjList[src].pop(i)
            self.res.append(v)
            if self.dfs_preorder(v):
                return True
            
            # the tricky part
            self.adjList[src].insert(i,v)
            self.res.pop()

        return
        