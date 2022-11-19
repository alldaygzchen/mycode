# lintcode
# n: vertices

#create a union class with find and union method
class UnionFind:
    def __init__(self,n):

        self.par = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}

    # find method is used to find its parent

    def find(self,node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]

        return node

    # union method returns True or False
    def union(self,n1,n2):
        p1,p2 = self.find(n1), self.find(n2)

        if p1==p2:
            return False
        if self.par[p1]>self.par[p2]:
            self.par[p2] =p1
        elif self.par[p2]>self.par[p1]:
            self.par[p1] =p2
        else:
            self.par[p1] =p2
            self.rank[p2]+=1

        return True



class Solution:
    def countComponents(self,n,edges):

        # res has at most n components
        self.res = n
        # create an instance of union class 
        unionfind = UnionFind(n)
        # loop all edges
        for e1,e2 in edges:
            # if union method is True => n-1
            if unionfind.union(e1,e2):
                self.res-=1
            # else same
        # return res 
        return self.res


