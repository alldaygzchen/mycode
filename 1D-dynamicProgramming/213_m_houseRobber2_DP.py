class Solution:

    """
    dp = [] # max profit 
    """
    def rob(self, nums):

        if len(nums)!=1:
            m1 = self.helper(nums[:-1])
            m2 = self.helper(nums[1:])
            return max(m1,m2)
        return nums[0]

    def helper(self, nums):
        if len(nums)==1:
            return nums[0]

        if len(nums)==2:
            return max(nums[0],nums[1])

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],max(dp[0:i-1])+nums[i])

        return dp[len(nums)-1]

s =Solution()
print(s.rob([2,3,2]))
print(s.rob([1,2,3,1]))
print(s.rob([1,2,3]))