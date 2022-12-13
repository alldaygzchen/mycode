class Solution:
    """
    Cannot use greedy since there may be a step with higher cost
    
    
    """
    def minCostClimbingStairs(self, cost):
        self.cost =cost
        self.dp = [-1]*(len(cost)+1)
        return self.dfs_inorder(len(cost))

    def dfs_inorder(self,idx):

        # base case
        if idx in [0,1]:
            self.dp[idx]=0
            return self.dp[idx]
        if idx<0:
            return 
        if self.dp[idx]!=-1:
            return self.dp[idx]


        #formula
        if idx-2<0:
            self.dp[idx] = self.dfs_inorder(idx-1)+self.cost[idx-1]
            return self.dp[idx]
        
        self.dp[idx] = min(self.dfs_inorder(idx-1)+self.cost[idx-1],self.dfs_inorder(idx-2)+self.cost[idx-2])
        return self.dp[idx]



s =Solution()
print(s.minCostClimbingStairs([10,15,20]))