class Solution:
    def numDistinct(self, s, t):
        self.s = s 
        self.t = t
        self.cache = {}

        return self.dfs_postorder(0,0) 

    def dfs_postorder(self,i,j):
        
        # base case
        if j == len(self.t):
            return 1

        if i == len(self.s):
            return 0

        if (i,j) in self.cache:
            return self.cache[(i,j)] 

        # formula 
        if self.s[i] == self.t[j]:
            self.cache[(i,j)] = self.dfs_postorder(i+1,j+1) + self.dfs_postorder(i+1,j)
        else:
            self.cache[(i,j)] = self.dfs_postorder(i+1,j)

        return self.cache[(i,j)]