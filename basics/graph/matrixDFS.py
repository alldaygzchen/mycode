# 0 is Free & 1 is Block
class Solution:
    def matrix(self,grid):
        self.grid = grid 
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.count = 0 
        self.helper(0,0,set())
        return self.count

    def helper(self,r,c,visit):

        if min(r,c)<0 or r==self.rows or c==self.cols or (r,c) in visit or self.grid[r][c]==1:
            return 

        if r==self.rows-1 and c==self.cols-1:
            self.count+=1
            return 

        visit.add((r,c))
        self.helper(r+1,c,visit) # prevent visit a
        self.helper(r-1,c,visit) # prevent visit b
        self.helper(r,c+1,visit) # prevent visit c
        self.helper(r,c-1,visit) # prevent visit d
        visit.remove((r,c))

s = Solution()
print(s.matrix([[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
))