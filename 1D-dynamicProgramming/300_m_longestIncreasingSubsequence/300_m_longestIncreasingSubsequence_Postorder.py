class Solution:
    def lengthOfLIS(self, nums):
        
        self.nums = nums
        # {i:1 for i in range(self.nums)}
        self.dp = {len(nums)-1:1}
        for idx in range(len(nums)):
            self.dfs_postorder(idx)
        
        res = float('-inf')
        for v in self.dp.values():
            res = max(res,v)
        return res


    def dfs_postorder(self,idx):
        
        if idx in self.dp:
            return self.dp[idx]

        res = 1

        for j in range(idx+1,len(self.nums)):
            if self.nums[idx]<self.nums[j]:
                res = max(res,1+self.dfs_postorder(j))

        self.dp[idx]=res
        return res


s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) #[2, 2, 4, 3, 3, 2, 1, 1]