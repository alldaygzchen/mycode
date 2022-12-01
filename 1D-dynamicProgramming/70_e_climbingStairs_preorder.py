class Solution:
    """
    preorder
    
    """
    def climbStairs(self, n):

        self.n = n
        self.count =0
        self.dfs_preorder(0)
        return self.count

    def dfs_preorder(self,stair):

        if stair == self.n:
            self.count+=1
            return 
        if stair>self.n:
            return



        self.dfs_preorder(stair+1)
        self.dfs_preorder(stair+2)

s =Solution()
print(s.climbStairs(5))