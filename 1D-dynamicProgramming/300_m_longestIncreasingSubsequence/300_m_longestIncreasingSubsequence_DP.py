class Solution:
    def lengthOfLIS(self, nums):

        dp = {}
        dp[len(nums)-1] = 1

        for i in range(len(nums) - 2, -1, -1):
            res =1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    res = max(res,1+dp[j])
            dp[i] =res
        return max([v for v in dp.values()])



s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) #[2, 2, 4, 3, 3, 2, 1, 1]