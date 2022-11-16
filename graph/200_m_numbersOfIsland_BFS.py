from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        self.grid = grid 
        self.visit = set()
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.result = 0 

        for r in range(self.rows):
            for c in range(self.cols):

                if self.grid[r][c] == "1" and (r,c) not in self.visit:
                    self.result+=1
                    self.bfs(r,c)

        return self.result

    def bfs(self,r,c): # self.visit
        
        q = deque()
        self.visit.add((r,c))
        q.append((r,c))

        while q:
            row,col = q.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr,dc in directions:
                r,c = row+dr,col+dc
                if (r in range(self.rows) and  c in range(self.cols) and self.grid[r][c]=="1" and (r,c) not in self.visit):
                    q.append((r,c))
                    self.visit.add((r,c))

