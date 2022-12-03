class Solution:
    """
    dp = [] #max profit
  
    """
    def rob(self, nums):

        if len(nums)==1:
            return nums[0]

        if len(nums)==2:
            return min(nums[0],nums[1])

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2,len(nums)):
            dp[i] = max(max(dp[0:i-1])+nums[i],dp[i-1])

        print(dp)

        return dp[len(nums)-1]

s =Solution()
print(s.rob([2,1,1,2]))
