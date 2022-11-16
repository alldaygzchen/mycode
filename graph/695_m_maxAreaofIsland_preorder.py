class Solution:
    def maxAreaOfIsland(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visit = set()
        self.count = 0
        self.res = 0
        
        
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c]==1 and (r,c) not in self.visit:
                    self.dfs_preorder(r,c)
                    print(self.count)
                    self.res = max(self.res,self.count)
                    self.count = 0

        return self.res


    def dfs_preorder(self,r,c):

        if (r not in range(self.rows) or c not in range(self.cols) or self.grid[r][c]==0 or (r,c) in self.visit):
            return 

        self.visit.add((r,c))
        self.count+=1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr,dc in directions:
            self.dfs_preorder(r+dr,c+dc)


        



