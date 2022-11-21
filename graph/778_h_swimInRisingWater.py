import heapq
class Solution:

    """

        # init
        # modified kruskal algo
            (self.visit to record visited node)
        # return time
        
    
    """


    def swimInWater(self, grid):
        self.grid =grid
        self.rows =len(grid)
        self.cols =len(grid[0])
        self.visit =set()
        self.visit.add((0,0))
        self.res =0
        self.minHeap = [[self.grid[0][0],0,0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while self.minHeap:
            v,r,c = heapq.heappop(self.minHeap)
            if r ==self.rows-1 and c==self.cols-1:
                self.res =v
                return self.res
            for dr,dc in directions:
                new_dr,new_dc = r+dr,c+dc
                if (min(new_dr,new_dc)<0 or 
                    new_dr==self.rows or 
                    new_dc==self.cols or 
                    (new_dr,new_dc) in self.visit):
                    continue
                # will not be visited again
                self.visit.add((new_dr,new_dc))
                heapq.heappush(self.minHeap,[max(v,self.grid[new_dr][new_dc]),new_dr,new_dc])
            