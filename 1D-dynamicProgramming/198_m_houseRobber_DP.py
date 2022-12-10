class Solution:
    """
    dp = [] #max profit
  
    """

    def rob(self, nums):
        dp = [0]*(len(nums)+1)
        dp[0]=0
        dp[1] = nums[0]

        for i in range(2,len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1],dp[i-1])

        # for i in range(1,len(nums)):
        #     dp[i+1] = max(dp[i-1]+nums[i],dp[i])

        return dp[len(nums)]




    # def rob(self, nums):

    #     if len(nums)==1:
    #         return nums[0]

    #     if len(nums)==2:
    #         return max(nums[0],nums[1])

    #     dp = [0]*len(nums)
    #     dp[0] = nums[0]
    #     dp[1] = max(nums[0], nums[1])

    #     for i in range(2,len(nums)):
    #         dp[i] = max(dp[i-2]+nums[i],dp[i-1])

    #     return dp[len(nums)-1]

s =Solution()
print(s.rob([2,1,1,2]))


    #     3
    #   1   2
    # -1  0 0 1