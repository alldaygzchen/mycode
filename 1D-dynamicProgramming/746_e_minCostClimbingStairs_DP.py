class Solution:
    """
    Cannot use greedy since there may be a step with higher cost
    
    
    """
    def minCostClimbingStairs(self, cost):
        
        if len(cost)<=1:
            return 0

        dp = [0]*(len(cost)+1)
        dp[0]=0
        dp[1]=0


        for i in range(2,len(dp)):
 
            dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])


        
        return dp[len(dp)-1]


s =Solution()
print(s.minCostClimbingStairs([10,15,20]))

