class Solution:
    """
    postorder  reference: grpah adjacencyListDFS.py
    
    """
    def climbStairs(self, n):

        return self.dfs_postorder(n)


    def dfs_postorder(self,stair):

        if stair==0:
            return 1
        if stair<0:
            return 0

        return self.dfs_postorder(stair-1)+self.dfs_postorder(stair-2) 


s =Solution()
print(s.climbStairs(5))