class Solution:
    """
    From the topLeft to the bottomRight
    only move down or move right
    from the point(r,c) how many ways can we go to the bottom right
    """
    def countPathPostorder(self,r,c,rows,cols,cache):
        

        #base case 
        if r==rows or c==cols:
            return 0
        if cache[r][c]>0:
            return cache[r][c]
        if r==rows-1 and c==cols-1:
            cache[r][c]=1
            return cache[r][c]

        # record our record
        cache[r][c]=self.countPathPostorder(r+1,c,rows,cols,cache) +self.countPathPostorder(r,c+1,rows,cols,cache)
        return cache[r][c]

s = Solution()
print(s.countPathPostorder(0,0,4,4,[[0]*4 for i in range(4)]))