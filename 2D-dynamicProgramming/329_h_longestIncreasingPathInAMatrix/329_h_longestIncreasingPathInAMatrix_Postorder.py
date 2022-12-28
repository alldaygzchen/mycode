class Solution:
    def longestIncreasingPath(self, matrix):
        
        self.matrix = matrix
        self.cache = {}
        self.r = len(matrix)
        self.c = len(matrix[0])
        
        res = float("-inf")
        for r in range(self.r):
            for c in range(self.c):
                res = max(res, self.dfs_postorder(r,c,-1))
        return res


    def dfs_postorder(self,r,c,prev):
        
        # base case
        if r<0 or r == self.r or c<0 or c==self.c or self.matrix[r][c]<=prev:
            return 0


        if (r,c) in self.cache:
            return self.cache[(r,c)]
        
        # formula
        res = 1 
        res = max(res,1+self.dfs_postorder(r+1,c,self.matrix[r][c]))
        res = max(res,1+self.dfs_postorder(r-1,c,self.matrix[r][c]))
        res = max(res,1+self.dfs_postorder(r,c+1,self.matrix[r][c]))
        res = max(res,1+self.dfs_postorder(r,c-1,self.matrix[r][c]))
        self.cache[(r,c)] =res 

        return self.cache[(r,c)]