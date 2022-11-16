class Solution:
    def maxAreaOfIsland(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visit = set()
        self.res = 0
        
        
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c]==1 and (r,c) not in self.visit:
                    self.res = max(self.res,self.dfs_postorder(r,c))

        return self.res


    def dfs_postorder(self,r,c):

        if (r not in range(self.rows) or c not in range(self.cols) or self.grid[r][c]==0 or (r,c) in self.visit):
            return 0 

        self.visit.add((r,c))

        return 1+self.dfs_postorder(r,c+1)+self.dfs_postorder(r,c-1)+self.dfs_postorder(r+1,c)+self.dfs_postorder(r-1,c)


        



