class Solution:
    def numIslands(self, grid):

        self.grid = grid 
        self.visit = set()
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.result = 0
        
        for r in range(self.rows):
            for c in range(self.cols):

                if self.grid[r][c] == "1" and (r,c) not in self.visit:
                    self.result+=1
                    self.dfs(r,c)

        return self.result

    def dfs(self,r,c): # self.visit
        if (r not in range(self.rows) or c not in range(self.cols) or self.grid[r][c]=="0" or (r,c) in self.visit):
            return 

        self.visit.add((r,c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr,dc in directions:
            self.dfs(r+dr,c+dc)

