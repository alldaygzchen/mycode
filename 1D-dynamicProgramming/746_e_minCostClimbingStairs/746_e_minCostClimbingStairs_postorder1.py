class Solution:
    """
    Cannot use greedy since there may be a step with higher cost
    
    
    """
    def minCostClimbingStairs(self, cost):
        self.cost =cost
        self.dp = [-1]*(len(cost)+1)
        self.dfs_inorder(0)
        return min(self.dp[0],self.dp[1])

    def dfs_inorder(self,idx):

        # base case
        if idx == len(self.cost):
            self.dp[idx]=0
            return self.dp[idx]
        if idx>len(self.cost):
            return 
        if self.dp[idx]!=-1:
            return self.dp[idx]


        #formula
        if idx+2>len(self.cost):
            self.dp[idx] = self.dfs_inorder(idx+1)+self.cost[idx]
            return self.dp[idx]
        
        self.dp[idx] = min(self.dfs_inorder(idx+1)+self.cost[idx],self.dfs_inorder(idx+2)+self.cost[idx])
        return self.dp[idx]
        
s =Solution()
print(s.minCostClimbingStairs([10,15,20]))