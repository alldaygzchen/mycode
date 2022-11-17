
# init
# find all rotted oranges
# define quene,time,fresh
# add rotted oranges in quene, record fresh number 
# run bfs 
# if fresh => -1 otherwise time
# prevent visit to the same orange twice duplicate


# from collections import deque
# class Solution:
#     def orangesRotting(self, grid):

#         self.grid = grid
#         self.rows = len(grid)
#         self.cols = len(grid[0])
#         self.quene = deque()
#         self.visit = set()
#         self.fresh = 0
#         self.time =0
        
#         # time:0
#         for r in range(self.rows):
#             for c in range(self.cols):
#                 if self.grid[r][c] == 2:
#                     self.quene.append((r,c))
#                     self.visit.add((r,c))
#                 if self.grid[r][c] == 1:
#                     self.fresh +=1

#         while self.quene and self.fresh>0:
#             for i in range(len(self.quene)):
#                 r,c = self.quene.popleft()
#                 directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#                 for dr,dc in directions:
#                     new_r,new_c= r+dr,c+dc
#                     if (
#                         new_r in range(self.rows) and 
#                         new_c in range(self.cols) and 
#                         self.grid[new_r][new_c] !=0 and 
#                         (new_r,new_c) not in self.visit
#                     ):
#                         self.quene.append((new_r,new_c))
#                         self.visit.add((new_r,new_c))
#                         self.fresh-=1


#             self.time+=1

#         if self.fresh:
#             return -1
#         return self.time


from collections import deque
class Solution:
    def orangesRotting(self, grid):

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.quene = deque()
        self.fresh = 0
        self.time =0
        
        # time:0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 2:
                    self.quene.append((r,c))
                if self.grid[r][c] == 1:
                    self.fresh +=1
        # time:n
        while self.quene and self.fresh>0:
            for i in range(len(self.quene)):
                r,c = self.quene.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr,dc in directions:
                    new_r,new_c= r+dr,c+dc
                    if (
                        new_r in range(self.rows) and 
                        new_c in range(self.cols) and 
                        self.grid[new_r][new_c] ==1
                    ):
                        self.quene.append((new_r,new_c))
                        self.grid[new_r][new_c]=2
                        self.fresh-=1


            self.time+=1

        if self.fresh:
            return -1
        return self.time
