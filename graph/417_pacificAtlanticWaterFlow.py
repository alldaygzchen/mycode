class Solution:
    def pacificAtlantic(self, heights):
        self.heights =heights
        self.rows,self.cols = len(heights), len(heights[0])
        self.pac, self.atl = set(), set()


        for c in range(self.cols):

            self.dfs(0, c, self.pac, heights[0][c])
            self.dfs(self.rows - 1, c, self.atl, heights[self.rows - 1][c])

        for r in range(self.rows):
  
            self.dfs(r, 0, self.pac, heights[r][0])
            self.dfs(r, self.cols - 1, self.atl, heights[r][self.cols - 1])

        res = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.pac and (r, c) in self.atl:
                    res.append([r, c])
        return res

    def dfs(self,r, c, visit, prevHeight): #recursive all self.pac ,self.atl result 
        if (
            (r, c) in visit
            or r < 0
            or c < 0
            or r == self.rows
            or c == self.cols
            or self.heights[r][c] < prevHeight
        ):
            return
        visit.add((r, c))
        self.dfs(r + 1, c, visit, self.heights[r][c])
        self.dfs(r - 1, c, visit, self.heights[r][c])
        self.dfs(r, c + 1, visit, self.heights[r][c])
        self.dfs(r, c - 1, visit, self.heights[r][c])

s =Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(s.pacificAtlantic(heights))


