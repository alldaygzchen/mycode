# objective: O(mn) return all cells with min distance

# init
# find all gate(value=0) position
# define quene
# conduct bfs
# return the rooms


from collections import deque

class Solution:
    def wallsAndGates(self,rooms):
        self.rooms = rooms
        self.rows = len(rooms)
        self.cols = len(rooms[0])
        self.dist = 0
        self.visit =set()
        self.quene = deque()

        for r in range(self.rows):
            for c in range(self.cols):
                if self.rooms[r][c]==0:
                    self.quene.append((r,c))
                    self.visit.add((r,c))

        while self.quene:
            for i in range(len(self.quene)):
                r,c = self.quene.popleft()
                self.rooms[r][c]=self.dist
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr,dc in directions:
                    new_r,new_c= r+dr,c+dc
                    if (min(new_r,new_c)<0 or 
                        new_r==self.rows or 
                        new_c==self.cols or 
                        (new_r,new_c) in self.visit or 
                        self.rooms[r][c]==-1
                    ):
                            continue

                    self.visit.add((r,c))
                    self.quene.append((r,c))
            self.dist+=1
        return self.rooms





        