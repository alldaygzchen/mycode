class Solution:


    def findRedundantConnection(self, edges):

        # init 
        # two edges has at least three vercitiles
        self.edges = edges
        self.par = [i for i in range(len(edges)+1)]
        self.rank = [0] *(len(edges)+1)

        # for loop edges if union fails return edges otherwise return []
        for n1,n2 in self.edges:
            if not self._union(n1,n2):
                return [n1,n2]
        return [] 

    def _union(self,n1,n2):
        
        p1,p2 = self._find(n1),self._find(n2)

        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2] = p1

        if self.rank[p2]>self.rank[p1]:
            self.par[p1] = p2
        
        else:
            self.par[p1] = p2
            self.rank[p2]+=1

        return True

    def _find(self,n):

        while n!=self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n= self.par[n]
        return  n