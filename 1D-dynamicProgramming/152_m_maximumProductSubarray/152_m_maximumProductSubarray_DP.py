class Solution:
    def maxProduct(self, nums):
        
        dp = [None]*(len(nums)+1)
        dp[0] =(1,1)  #(curMin, curMax)
        res =max(nums)

        for i in range(1,len(dp)):

            if nums[i-1]==0:
                res = max(res,0)
                dp[i]=(1,1)

            prevMin, prevMax = dp[i-1]
            curMin = min(prevMin*nums[i-1],prevMax*nums[i-1],nums[i-1])
            curMax = max(prevMin*nums[i-1],prevMax*nums[i-1],nums[i-1])
            res = max(res,curMax)
            dp[i] = (curMin,curMax)
        return res

s =Solution()
print(s.maxProduct([2,3,-2,4]))
print(s.maxProduct([-2,0,-1]))
print(s.maxProduct([0,2]))

