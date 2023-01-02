class Solution:
    def maxSubArray(self, nums):
        self.nums =nums 
        self.res = float('-inf')
        self.cache = {}
        self.dfs_postorder(len(nums)-1)
        return self.res
        


    def dfs_postorder(self,idx):
        
        if idx<0:
            return 0
        if idx in self.cache:
            return self.cache[idx]

        curSum = max(self.nums[idx]+self.dfs_postorder(idx-1), self.nums[idx])
        self.res = max(self.res, curSum)
        self.cache[idx] = curSum
        return curSum