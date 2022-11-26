class Solution:
    """
    From the topLeft to the bottomRight
    only move down or move right
    from the point(r,c) how many ways can we go to the bottom right
    save space we dont have a grid. Instead we have two list
    """
    def countPathBottomup(self,rows,cols):
        
        prevRow = [0]*cols

        for r in range(rows-1,-1,-1):
            curRow = [0]*cols
            curRow[cols-1] =1
            for c in range(cols-2,-1,-1):
                curRow[c] = curRow[c+1] +prevRow[c]
            prevRow = curRow
        return prevRow[0]

        

s = Solution()
print(s.ccountPathBottomup(4,4))