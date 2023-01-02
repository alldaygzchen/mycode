class Solution:
    def isMatch(self, s: str, p: str):
        
        self.s = s
        self.p = p 
        self.cache = {}
        return self.dfs_postorder(0,0)

    def dfs_postorder(self,i,j):
        
        # base case
        if (i,j) in self.cache:
            return self.cache[(i,j)]
        
        if i>=len(self.s) and j>= len(self.p):
            self.cache[(i,j)] = True
            return self.cache[(i,j)]

        if j>=len(self.p):
            self.cache[(i,j)] = False
            return self.cache[(i,j)]
        

        # formula
        match = i<len(self.s) and (self.s[i] == self.p[j] or self.p[j]==".")
        if (j+1)<len(self.p) and self.p[j+1]=="*":
            # don't use the star(skip) or use the star
            self.cache[(i,j)] = self.dfs_postorder(i,j+2) or (match and self.dfs_postorder(i+1,j))
            return self.cache[(i,j)] 

        if match:
            self.cache[(i,j)] = self.dfs_postorder(i+1,j+1)
            return self.cache[(i,j)] 

        self.cache[(i,j)] = False
        return self.cache[(i,j)] 