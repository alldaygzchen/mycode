# Find the length of the shortest path from the top left of the grid to the bottom right

from collections import deque

class Solution:


    def bfs(self,grid):

        rows = len(grid)
        cols = len(grid[0])
        quene = deque()
        quene.append((0,0))
        visit = set()
        visit.add((0,0))

        length = 0

        while quene:
            for i in range(len(quene)):
                r,c = quene.popleft()
                if r == rows-1 and c == rows-1:
                    return length

                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                
                for dr,dc in neighbors:
                    if (r+dr<0 or c+dc<0 or r+dr == rows or c+dc ==cols or (r+dr,c+dc) in visit or grid[r+dr][c+dc]==1):#visited or added
                        continue
                    quene.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))#added

            length +=1

        return length



grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
s=Solution()
print(s.bfs(grid))