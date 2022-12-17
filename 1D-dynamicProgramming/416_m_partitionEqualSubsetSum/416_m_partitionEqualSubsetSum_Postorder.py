class Solution:
    def canPartition(self, nums):
        self.nums =nums


        if len(nums) ==0:
            return False

        if sum(self.nums)%2:
            return False
        else:
            self.target = sum(nums)//2
            self.dp = [[None for x in range(self.target+1)] for y in range(len(nums)+1)]
    
        return self.dfs_postorder(self.target,0)
    
    def dfs_postorder(self,sum,idx):

        # whether it can be partition in sum=11 and index=0
        
        # base case
        if sum == 0:
            self.dp[idx][sum] = True
            return self.dp[idx][sum]
        
        if (idx>=len(self.nums)):
            self.dp[idx][sum] = False
            return self.dp[idx][sum]

        if self.dp[idx][sum] !=None:
            return self.dp[idx][sum]

        # formula
        if (self.nums[idx]<=sum):
            if self.dfs_postorder(sum-self.nums[idx],idx+1):
                self.dp[idx][sum] = True
                return self.dp[idx][sum]
        self.dp[idx][sum] = self.dfs_postorder(sum,idx+1)
        return self.dp[idx][sum]

s = Solution()
print(s.canPartition([1,5,11,5]))